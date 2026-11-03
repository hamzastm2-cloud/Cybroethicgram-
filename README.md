# Cybroethicgram

AI-powered learning assistant for programming and ethical cybersecurity education.

## What it does and who it's for

Cybroethicgram helps beginners learn Python, C, and ethical cybersecurity. It has two parts:

- **Practice labs (`labs.py`):** Six offline puzzles that need no network access: Caesar cipher, Base64 decoding, password strength, ports and services, spotting a phishing link, and reading a login log. Each lab accepts `hint` for help or `skip` to give up. Finishing a lab adds 2 points, saved to your progress file.
- **AI helper (`ai_fallback.py`):** When you ask a question the lessons don't cover, it sends the question to Claude and returns a short, plain-text answer. It refuses requests to attack real systems or write malware, and offers a safe alternative instead.

It is built for students and self-taught learners who want to practise in their own lab, on TryHackMe, or in CTFs.

## How to install

You need Python 3 and an internet connection for the AI helper. The project uses only the Python standard library, so there are no packages to install.

1. Clone the repository:
