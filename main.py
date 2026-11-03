"""CYBROETHICGRAM AI - Student Learning Assistant (Termux)
Files needed in the same folder:
  main.py, python_knowledge.py, knowledge_extra.py, programs_library.py,
  ai_fallback.py, labs.py, progress.py, explain_code.py
"""
import os
import random
import re

import python_knowledge as pk
import programs_library as pl
import ai_fallback as ai
import labs
import progress
import explain_code as ex
from knowledge_extra import EXTRA

pk.KNOWLEDGE.extend(EXTRA)          # add networking, security, ...

UNKNOWN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "unknown_questions.txt")
MAX_UNKNOWN = 200      # keep only the latest questions

# Safety layer: refuse requests aimed at real people/systems.
UNSAFE_PHRASES = [
    "hack someone", "hack his", "hack her", "hack instagram",
    "hack facebook", "hack whatsapp", "hack account", "steal password",
    "steal data", "without permission", "ddos attack on", "write ransomware",
    "write a virus", "make a virus", "write malware", "keylogger for",
    "crack wifi", "crack someone",
]

REFUSAL = (
    "I can't help with attacking real people or systems. "
    "I can teach how attacks work in concept, how to defend against "
    "them, and how to practise legally in labs. "
    "Ask: ethical hacking, legal labs, phishing, password."
)

QUIZ = [
    ("Which system turns domain names into IP addresses?", {"dns"}),
    ("Which port does HTTPS use?", {"443"}),
    ("What does a firewall do? (filter/ignore)", {"filter"}),
    ("Which Python function shows output?", {"print", "print()"}),
    ("Which symbol starts a Python comment?", {"#"}),
    ("Is testing a system without permission legal? (yes/no)", {"no"}),
    ("2FA means two-factor ...?", {"authentication"}),
    ("Which Python type stores key-value pairs?", {"dictionary", "dict"}),
    ("How many layers does the OSI model have?", {"7", "seven"}),
    ("Which protocol is faster but unreliable: TCP or UDP?", {"udp"}),
]

HELP = """Ask me things like:
 what is dns
 python programs / c programs
 prime number in c
 c program 7
 ip address / ports / osi model
 ethical hacking / legal labs
 linux commands / termux
Commands: help, topics, quiz, labs, explain,
 progress, save, save all, exit"""


def show(text):
    print(pk.pretty(text))


_ATTACK = (r"(hack|hacking|crack|cracking|steal|stealing|spy on|spying on|"
           r"break into|brute ?force|ddos|dos attack|phish|phishing|"
           r"keylog|track|bypass|take over|get into|access)")
_TARGET = (r"(someone|somebody|anyone|his|her|their|him|them|"
           r"my (friend|ex|girlfriend|boyfriend|wife|husband|teacher|"
           r"school|neighbou?r|boss|classmate|brother|sister)|"
           r"(instagram|facebook|whatsapp|snapchat|gmail|email|"
           r"account|wifi|wi-fi|phone|website|server|network) "
           r"(of|password)|"
           r"(instagram|facebook|whatsapp|snapchat|gmail|account|"
           r"wifi|wi-fi))")
_MAKE = (r"(write|make|create|build|code|give me)\s+(a\s+|an\s+|me\s+a\s+)?"
         r"(ransomware|virus|malware|keylogger|trojan|rat|botnet|"
         r"phishing (page|site|kit)|fake login|credential stealer)")
_SAFE = ("how to defend", "how to protect", "how to prevent", "my own",
         "in my lab", "tryhackme", "ctf", "what is", "what are",
         "explain", "difference between")


def is_unsafe(text):
    t = " ".join(text.lower().split())
    if any(p in t for p in UNSAFE_PHRASES):
        return True
    if re.search(_MAKE, t):
        return True
    if re.search(r"\b" + _ATTACK + r"\b.{0,25}\b" + _TARGET, t):
        # allow clearly educational / defensive wording
        return not any(k in t for k in _SAFE)
    return False


TOPIC_GROUPS = [
    ("PYTHON BASICS", "python, print, input, variable, data type, string, "
     "number, list, tuple, dictionary, set, if, for loop, while loop, range, "
     "function, lambda, list comprehension, import, file, exception, class, "
     "inheritance, self, comment, boolean, slicing, enumerate, recursion, "
     "generator, decorator, json, random, virtual environment, requests, "
     "socket, hash"),
    ("PYTHON ERRORS", "indentation, nameerror, typeerror, indexerror, "
     "keyerror, valueerror"),
    ("NETWORKING", "networking, ip address, dns, dns record, dns security, "
     "dhcp, mac address, router, osi model, tcp ip, tcp, port, https, http, "
     "status code, subnet, nat, vpn, firewall, ping, nmap, wireshark, wifi, "
     "localhost, bandwidth"),
    ("CYBERSECURITY", "cybersecurity, learn ethical hacking, ethical hacking, "
     "legal labs, certification, malware, phishing, password, encryption, "
     "sql injection, xss, owasp, dos, vulnerability, authentication, backup, "
     "kali"),
    ("LINUX AND LANGUAGES", "linux, permissions, termux, bash, c, java, "
     "javascript, html, sql, git, data structure, algorithm"),
    ("PROGRAMS", "programs, first code ... tenth code, dns lookup program, "
     "echo server, http request program, port checker"),
    ("GENERAL", "hi, developer, who are you"),
]


def topics():
    names = [kw[0] for kw, _ in pk.KNOWLEDGE]
    print(f"I know {len(names)} topics and {len(pl.PROGRAMS)} programs "
          "(Python + C).\n")
    for title, text in TOPIC_GROUPS:
        print("[" + title + "]")
        show(text)
        print()
    print("Type any topic name to learn it.")


def quiz():
    try:
        return _quiz()
    except (EOFError, KeyboardInterrupt):
        print("\nQuiz stopped.")


def _quiz():
    questions = random.sample(QUIZ, 5)
    score = 0
    for q, answers in questions:
        reply = input(q + " ").strip().lower()
        if reply in answers:
            print("Correct!")
            score += 1
        else:
            print("Not quite. Answer:", sorted(answers)[0])
    print(f"Score: {score}/5")
    progress.record_quiz(score, 5)


def save_unknown(question):
    """Log unanswered questions (latest MAX_UNKNOWN only, owner-only file)."""
    try:
        with open(UNKNOWN_FILE) as f:
            lines = f.read().splitlines()
    except OSError:
        lines = []
    lines = (lines + [question[:200]])[-MAX_UNKNOWN:]
    with open(UNKNOWN_FILE, "w") as f:
        f.write("\n".join(lines) + "\n")
    try:
        os.chmod(UNKNOWN_FILE, 0o600)
    except OSError:
        pass


def save_last(files):
    if not files:
        print("Ask for a program first, then type 'save'.")
        return
    paths = pl.save_files(files)
    print("Saved:")
    for p in paths:
        print(" " + p)
        if p.endswith(".py"):
            print("Run: python " + p)
        else:
            print("Run: clang " + p + " -o prog -lm && ./prog")


def main():
    print("=" * 34)
    print("   CYBROETHICGRAM AI")
    print(" Student Learning Assistant")
    print("=" * 34)
    print("Type 'help' to start.\n")
    last_files = []
    while True:
        try:
            text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not text:
            continue
        low = text.lower()
        if low in ("exit", "quit", "bye"):
            print("Keep learning. Goodbye!")
            break
        if low == "help":
            print(HELP)
        elif low == "topics":
            topics()
        elif low == "quiz":
            quiz()
        elif low in ("labs", "lab"):
            labs.menu()
        elif low.startswith("lab "):
            labs.run(low[4:].strip())
        elif low in ("progress", "my progress", "stats"):
            print(progress.report())
        elif low == "reset progress":
            if input("Erase all progress? (y/n) ").strip().lower() == "y":
                progress.reset()
                print("Progress erased.")
        elif low in ("save", "save program"):
            save_last(last_files)
        elif low in ("save all", "save all programs"):
            n = pl.save_all()
            print(f"Saved {n} programs in the 'programs' folder")
            print("(programs/python and programs/c).")
        elif low.startswith("explain"):
            show(ex.find_explain(text))
        elif is_unsafe(low):
            show(REFUSAL)
        elif low == "ai help":
            print(ai.AI_HELP)
        elif low.startswith("ask "):
            show(ai.ask(text[4:]) or ai.AI_HELP)
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
                    ans = ai.ask(text)
                    if ans:
                        show(ans)
                    else:
                        show(pk.HELP_TEXT)
                        print("Tip: type 'ai help' for smart answers.")
        print()


if __name__ == "__main__":
    main()
