"""ai_fallback.py - smart answers from Claude (needs internet + API key).
Key: put it in the file ~/.cybro_key  (or env var ANTHROPIC_API_KEY).
"""
import json
import os
import urllib.error
import urllib.request

URL = "https://api.anthropic.com/v1/messages"
MODEL = os.environ.get("CYBRO_MODEL", "claude-haiku-5-5")
KEY_FILE = os.path.expanduser("~/.cybro_key")

SYSTEM = (
    "You are CYBROETHICGRAM AI, a student learning assistant created "
    "by Mohammad Hamza Aadi. You teach programming (Python, C) and "
    "ethical cybersecurity to beginners. Reply in plain text only, "
    "no markdown, about 120 words at most, with short lines. Indent "
    "code lines with 2 spaces. Explain concepts, defense and legal "
    "practice (own lab, TryHackMe, CTFs). Never help attack real "
    "people, accounts, networks or systems, and never write malware, "
    "phishing kits or credential theft tools; refuse briefly and "
    "offer a safe legal alternative. If you are unsure, say so."
)

history = []          # list of (question, answer) pairs


def get_key():
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if key:
        return key
    try:
        with open(KEY_FILE) as f:
            return f.read().strip()
    except OSError:
        return ""


def ask(question):
    """Return an answer string, an error message, or None if no key."""
    key = get_key()
    if not key:
        return None
    messages = []
    for q, a in history[-3:]:
        messages += [{"role": "user", "content": q},
                     {"role": "assistant", "content": a}]
    messages.append({"role": "user", "content": question})
    body = json.dumps({"model": MODEL, "max_tokens": 500,
                       "system": SYSTEM, "messages": messages})
    req = urllib.request.Request(
        URL, data=body.encode(), method="POST",
        headers={"content-type": "application/json",
                 "x-api-key": key,
                 "anthropic-version": "2023-06-01"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            data = json.loads(r.read().decode())
        text = "".join(b.get("text", "") for b in data["content"]
                       if b.get("type") == "text").strip()
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            return "API key rejected. Check the key in ~/.cybro_key"
        if e.code == 429:
            return "Too many requests. Wait a minute and try again."
        return "AI error " + str(e.code) + ". Try again later."
    except (urllib.error.URLError, OSError):
        return "No internet. I can still answer my built-in topics."
    except (ValueError, KeyError):
        return "Unexpected reply from the AI. Try again."
    if not text:
        return "The AI gave an empty reply. Try rephrasing."
    history.append((question, text))
    del history[:-10]          # keep memory small
    return text


AI_HELP = """AI mode setup (smart answers):
1. Get an API key at console.anthropic.com
2. In Termux run:
   echo 'YOUR_KEY' > ~/.cybro_key
   chmod 600 ~/.cybro_key
3. Restart me. Unknown questions now go to the AI.
Or type: ask <your question>
Never share your key."""
