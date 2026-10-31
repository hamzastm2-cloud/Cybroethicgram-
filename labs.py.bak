"""Safe practice labs. Every lab is a self-contained puzzle:
no network access and no real systems are touched."""
import base64
import random

import progress

WORDS = ["firewall", "network", "packet", "router", "secure", "python",
         "server", "update", "backup", "access", "cipher", "domain"]

PORTS = [("SSH", "22"), ("HTTP", "80"), ("HTTPS", "443"), ("DNS", "53"),
         ("FTP", "21"), ("SMTP", "25"), ("Telnet", "23")]


def _ask(prompt, check, hint=None, tries=3):
    """Ask up to `tries` times. Type 'hint' for help, 'skip' to give up."""
    for i in range(tries):
        reply = input(prompt + " ").strip()
        low = reply.lower()
        if low == "skip":
            return False
        if low == "hint":
            print("Hint:", hint or "Think step by step.")
            continue
        if check(low):
            return True
        print("Not yet." if i < tries - 1 else "Out of tries.")
    return False


def _finish(name, ok, answer):
    progress.record_lab(name, ok)
    print("Lab passed! +2 points" if ok else "Answer: " + str(answer))


def caesar():
    word = random.choice(WORDS)
    shift = random.randint(1, 25)
    enc = "".join(chr((ord(c) - 97 + shift) % 26 + 97) for c in word)
    print("LAB: Caesar cipher")
    print("Every letter was moved forward in the alphabet by the same")
    print(f"number. The shift is {shift}. Decode this word: {enc}")
    ok = _ask("Decoded word:", lambda r: r == word,
              "Move each letter BACK by the shift.")
    _finish("caesar", ok, word)


def base64_lab():
    word = random.choice(WORDS)
    enc = base64.b64encode(word.encode()).decode()
    print("LAB: Base64 decoding")
    print("Base64 is an encoding, not encryption. Anyone can reverse it.")
    print("Decode:", enc)
    print("(In Python: import base64; base64.b64decode(...))")
    ok = _ask("Decoded word:", lambda r: r == word,
              "Use base64.b64decode(text).decode() in Python.")
    _finish("base64", ok, word)


def password():
    pools = [
        ["123456", "password", "qwerty", "iloveyou", "admin123"],
        ["blue-horse-staple-moon", "Xk#9vL!2qPz$7", "R7!vq$Lm2#Zp"],
    ]
    weak = random.choice(pools[0])
    strong = random.sample(pools[1], 2)
    options = strong + [weak]
    random.shuffle(options)
    print("LAB: Password strength")
    for i, p in enumerate(options, 1):
        print(f"  {i}. {p}")
    ok = _ask("Which number is the WEAKEST?",
              lambda r: r == str(options.index(weak) + 1),
              "Attackers try common passwords first.")
    print("Common and short passwords fall in seconds. Long, unique")
    print("passwords plus 2FA protect accounts best.")
    _finish("password", ok, options.index(weak) + 1)


def ports():
    picks = random.sample(PORTS, 3)
    print("LAB: Ports and services")
    done = 0
    for name, port in picks:
        if _ask(f"Default port for {name}?", lambda r, p=port: r == p,
                "Common: SSH 22, HTTP 80, HTTPS 443, DNS 53."):
            done += 1
    ok = done == 3
    _finish("ports", ok, ", ".join(f"{n}={p}" for n, p in picks))


def phishing():
    real = random.choice(["paypal.com", "google.com", "instagram.com",
                          "amazon.com"])
    fakes = {"paypal.com": "paypa1.com", "google.com": "g00gle.com",
             "instagram.com": "instagram.com.login-verify.net",
             "amazon.com": "amazon-support-help.xyz"}
    options = [f"https://{real}/login",
               f"https://{fakes[real]}/login",
               f"https://www.{real}/account"]
    fake_url = options[1]
    random.shuffle(options)
    print("LAB: Spot the phishing link")
    for i, u in enumerate(options, 1):
        print(f"  {i}. {u}")
    ok = _ask("Which number is the fake?",
              lambda r: r == str(options.index(fake_url) + 1),
              "Read the real domain: the part right before the first '/'.")
    print("Tip: look at the exact domain, not just the brand name.")
    _finish("phishing", ok, options.index(fake_url) + 1)


def logs():
    ips = ["10.0.0.5", "10.0.0.8", "10.0.0.13", "10.0.0.21"]
    attacker = random.choice(ips)
    n = random.randint(4, 7)
    lines = [(attacker, "FAILED")] * n
    for ip in ips:
        if ip != attacker:
            lines += [(ip, "OK")] * random.randint(1, 2)
            lines += [(ip, "FAILED")] * random.randint(0, 1)
    random.shuffle(lines)
    print("LAB: Read a login log (defender view)")
    for i, (ip, res) in enumerate(lines, 1):
        print(f" {i:02d} login {res:<6} from {ip}")
    print("These are made-up lines. Defenders look for repeats.")
    ok = _ask("Which IP has the MOST failed logins?",
              lambda r: r == attacker,
              "Count the FAILED lines per IP.")
    print("A defender would block or rate-limit that address.")
    _finish("logs", ok, attacker)


LABS = {
    "1": ("Caesar cipher", caesar),
    "2": ("Base64 decoding", base64_lab),
    "3": ("Password strength", password),
    "4": ("Ports and services", ports),
    "5": ("Spot the phishing link", phishing),
    "6": ("Read a login log", logs),
}

INTRO = ("Practice labs (safe, offline puzzles).\n"
         "Type 'lab 1' to 'lab 6'. In a lab: 'hint' or 'skip'.")


def menu():
    print(INTRO)
    for k, (name, _) in LABS.items():
        print(f"  {k}. {name}")


def run(arg=None):
    if arg in LABS:
        LABS[arg][1]()
    elif arg == "random":
        random.choice(list(LABS.values()))[1]()
    else:
        menu()
