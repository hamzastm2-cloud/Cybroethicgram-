#!/usr/bin/env python3
# Cybroethicgram V8.1 safe patcher for Termux
import shutil, sys, re
from pathlib import Path
from datetime import datetime
root = Path.home() / "cybroethicgram"
main_path, ai_path = root / "main.py", root / "ai_fallback.py"
if not main_path.is_file() or not ai_path.is_file():
    print("ERROR: V8 files not found. No changes made."); sys.exit(1)
main = main_path.read_text(encoding="utf-8")
ai = ai_path.read_text(encoding="utf-8")
if "ai.ask(" not in main or "STYLE_GUIDANCE" not in ai:
    print("ERROR: Expected V8 Gemini files. No changes made."); sys.exit(2)
ai = ai.replace('"systemInstruction": {"parts": [{"text": SYSTEM + " " + STYLE_GUIDANCE[STYLE]}]},',
    '"systemInstruction": {"parts": [{"text": SYSTEM + " CURRENT ANSWER STYLE: " + STYLE + ". " + STYLE_GUIDANCE[STYLE] + " Follow this length strictly; do not repeat the question."}]},')
ai = ai.replace('"generationConfig": {"maxOutputTokens": 1100, "temperature": 0.7}',
    '"generationConfig": {"maxOutputTokens": 180 if STYLE == "brief" else (500 if STYLE == "normal" else 1100), "temperature": 0.5}')
# Gemini-first route fixes local knowledge taking priority over the style-aware AI.
old = """        else:
            hit = pl.find(text)
            if hit:
                show(hit["text"])
                if hit["files"]:
                    last_files = hit["files"]
            else:
                reply = pk.answer(text)
                if reply:
                    show(reply)
                else:
                    save_unknown(text)
                    ans = ai.ask(text)
                    if ans:
                        show(ans)
                    else:
                        show(pk.HELP_TEXT)
                        print("Tip: type \'ai help\' for smart answers.")
"""
new = """        else:
            # V8.1 Gemini-first: style applies to ordinary questions.
            ans = ai.ask(text)
            if ans and not ans.startswith("Gemini is not configured."):
                show(ans)
            else:
                hit = pl.find(text)
                if hit:
                    show(hit["text"])
                    if hit["files"]:
                        last_files = hit["files"]
                else:
                    reply = pk.answer(text)
                    if reply:
                        show(reply)
                    else:
                        save_unknown(text)
                        show(ans or pk.HELP_TEXT)
"""
if old in main:
    main = main.replace(old, new, 1)
elif "V8.1 Gemini-first" not in main:
    print("SAFE STOP: routing pattern differs from saved V8 template. No changes."); sys.exit(3)
try:
    compile(main, str(main_path), "exec"); compile(ai, str(ai_path), "exec")
except SyntaxError as e:
    print("SAFE STOP: syntax check failed:", e); sys.exit(4)
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
mb = main_path.with_name("main.py.v8_backup_" + stamp)
ab = ai_path.with_name("ai_fallback.py.v8_backup_" + stamp)
shutil.copy2(main_path, mb); shutil.copy2(ai_path, ab)
main_path.write_text(main, encoding="utf-8"); ai_path.write_text(ai, encoding="utf-8")
print("V8.1 patch applied. Backups:", mb, ab)
print("Gemini now answers first; local knowledge remains fallback.")
print("Brief mode uses a stronger instruction and smaller output limit.")
print("Run: cd ~/cybroethicgram && python main.py")
