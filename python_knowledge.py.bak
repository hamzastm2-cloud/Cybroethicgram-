"""Python knowledge base for CYBROETHICGRAM AI.
Usage in main.py:
    from python_knowledge import answer
    reply = answer(user_text)   # returns a string or None
Add more topics by copying an entry in KNOWLEDGE.
"""
import difflib
import re
import textwrap

# Each entry: (keywords, explanation). Keywords are lowercase.
KNOWLEDGE = [
    (["python", "what is python"],
     "Python is a beginner-friendly, general-purpose language used for web, "
     "automation, data science, AI and cybersecurity tools.\n"
     "Example:\n  print('Hello, world!')"),

    (["print", "output"],
     "print() shows text or values on the screen.\n"
     "  print('Hi', 5)        # Hi 5\n"
     "  print('a', 'b', sep='-')  # a-b"),

    (["input", "user input"],
     "input() reads text typed by the user. It always returns a string.\n"
     "  name = input('Name: ')\n"
     "  age = int(input('Age: '))"),

    (["variable", "variables"],
     "A variable is a name that stores a value. No type declaration needed.\n"
     "  age = 15\n  name = 'Sam'\n  price = 9.99"),

    (["data type", "data types", "types", "type"],
     "Basic types: int (5), float (2.5), str ('hi'), bool (True), "
     "list, tuple, dict, set.\n"
     "  type(5)  # <class 'int'>"),

    (["string", "strings", "str"],
     "A string is text in quotes.\n"
     "  s = 'python'\n  s.upper()  # 'PYTHON'\n  s[0]  # 'p'\n"
     "  f'Hi {s}'  # f-string formatting\n  len(s)  # 6"),

    (["number", "numbers", "int", "float", "math", "operator", "operators"],
     "Operators: + - * / (divide) // (floor divide) % (remainder) ** (power)\n"
     "  7 // 2  # 3\n  7 % 2  # 1\n  2 ** 3  # 8"),

    (["list", "lists"],
     "A list is an ordered, changeable collection.\n"
     "  nums = [1, 2, 3]\n  nums.append(4)\n  nums[0]  # 1\n"
     "  nums.sort()\n  len(nums)  # 4"),

    (["tuple", "tuples"],
     "A tuple is like a list but cannot be changed.\n"
     "  point = (3, 4)\n  x, y = point"),

    (["dictionary", "dictionaries", "dict"],
     "A dictionary stores key-value pairs.\n"
     "  user = {'name': 'Sam', 'age': 15}\n  user['name']  # 'Sam'\n"
     "  user['city'] = 'Delhi'\n  user.get('zip', 'none')"),

    (["set", "sets"],
     "A set holds unique values with no order.\n"
     "  s = {1, 2, 2, 3}  # {1, 2, 3}\n  s.add(4)\n  a | b  # union"),

    (["if", "else", "elif", "condition", "conditions", "conditional"],
     "if/elif/else choose what code runs.\n"
     "  if score >= 90:\n      print('A')\n  elif score >= 50:\n      print('Pass')\n"
     "  else:\n      print('Fail')\n"
     "Comparisons: == != < > <= >=   Logic: and, or, not"),

    (["for loop", "for", "loop", "loops"],
     "A for loop repeats code for each item.\n"
     "  for i in range(3):\n      print(i)   # 0 1 2\n"
     "  for name in ['a', 'b']:\n      print(name)"),

    (["while loop", "while"],
     "A while loop repeats as long as a condition is True.\n"
     "  n = 3\n  while n > 0:\n      print(n)\n      n -= 1\n"
     "Use break to exit and continue to skip to the next round."),

    (["range"],
     "range(n) makes numbers 0..n-1.\n"
     "  range(5)  # 0,1,2,3,4\n  range(2, 6)  # 2..5\n  range(0, 10, 2)  # 0,2,4,6,8"),

    (["function", "functions", "def"],
     "A function is reusable code.\n"
     "  def add(a, b=0):\n      return a + b\n  add(2, 3)  # 5\n"
     "Parameters can have defaults. return sends back a result."),

    (["lambda"],
     "A lambda is a tiny one-line function.\n"
     "  square = lambda x: x * x\n  square(4)  # 16"),

    (["list comprehension", "comprehension"],
     "A short way to build lists.\n"
     "  squares = [x * x for x in range(5)]  # [0,1,4,9,16]\n"
     "  evens = [x for x in range(10) if x % 2 == 0]"),

    (["import", "module", "modules", "library", "libraries", "pip"],
     "Modules are files of reusable code.\n"
     "  import math\n  math.sqrt(16)  # 4.0\n  from random import randint\n"
     "Install third-party libraries with: pip install requests"),

    (["file", "files", "read file", "write file", "open"],
     "Use 'with' so files close automatically.\n"
     "  with open('a.txt', 'w') as f:\n      f.write('hi')\n"
     "  with open('a.txt') as f:\n      text = f.read()\n"
     "Modes: 'r' read, 'w' write (overwrites), 'a' append."),

    (["exception", "exceptions", "error handling", "try", "except"],
     "try/except stops errors from crashing your program.\n"
     "  try:\n      n = int(input('Number: '))\n"
     "  except ValueError:\n      print('Not a number')\n"
     "  finally:\n      print('done')"),

    (["class", "classes", "object", "objects", "oop"],
     "A class is a blueprint for objects (OOP).\n"
     "  class Dog:\n      def __init__(self, name):\n          self.name = name\n"
     "      def bark(self):\n          print(self.name, 'says woof')\n"
     "  d = Dog('Rex')\n  d.bark()"),

    (["inheritance"],
     "A child class reuses a parent class.\n"
     "  class Animal:\n      def speak(self): print('...')\n"
     "  class Cat(Animal):\n      def speak(self): print('meow')"),

    (["self", "__init__", "constructor"],
     "__init__ runs when an object is created (the constructor). "
     "self refers to the object itself, so each object keeps its own data."),

    (["indentation", "syntax error", "syntaxerror", "indent"],
     "Python uses indentation (4 spaces) to group code. A SyntaxError "
     "usually means a missing colon, unclosed bracket/quote, or wrong "
     "indentation. Read the line number and the ^ marker in the error."),

    (["nameerror"],
     "NameError: you used a name that doesn't exist yet. Check spelling "
     "and make sure the variable is defined before use."),

    (["typeerror"],
     "TypeError: wrong type used, e.g. 'age: ' + 5. Convert with str() "
     "or int(), or use an f-string."),

    (["indexerror"],
     "IndexError: list index out of range. Valid indexes are 0 to len-1."),

    (["keyerror"],
     "KeyError: the dictionary has no such key. Use d.get(key) or check "
     "with 'key in d' first."),

    (["valueerror"],
     "ValueError: right type, wrong value, e.g. int('abc'). "
     "Validate input or use try/except."),

    (["slicing", "slice"],
     "Slicing takes part of a sequence: seq[start:stop:step]\n"
     "  'python'[1:4]  # 'yth'\n  [1,2,3,4][::-1]  # reversed"),

    (["enumerate", "zip"],
     "enumerate gives index + item; zip pairs two lists.\n"
     "  for i, x in enumerate(['a', 'b']): print(i, x)\n"
     "  for a, b in zip([1, 2], ['x', 'y']): print(a, b)"),

    (["json"],
     "JSON is a text format for data.\n"
     "  import json\n  data = json.loads('{\"a\": 1}')\n  text = json.dumps(data)\n"
     "  json.load(open('f.json'))  # read from file"),

    (["random"],
     "  import random\n  random.randint(1, 6)\n  random.choice(['a', 'b'])\n"
     "  random.shuffle(my_list)"),

    (["virtual environment", "venv"],
     "A virtual environment keeps each project's libraries separate.\n"
     "  python -m venv env\n  source env/bin/activate"),

    (["requests", "http", "api"],
     "The requests library talks to web APIs.\n"
     "  import requests\n  r = requests.get('https://example.com')\n"
     "  print(r.status_code)\n  r.json()  # if the reply is JSON\n"
     "Install: pip install requests. Only call APIs you are allowed to use."),

    (["socket", "sockets", "networking in python"],
     "The socket module does low-level networking. Learn it on your own "
     "machine or lab network (e.g. localhost) so you stay legal and safe.\n"
     "  import socket\n  print(socket.gethostname())"),

    (["hash", "hashlib", "password hashing"],
     "Hashing turns data into a fixed fingerprint. Never store plain "
     "passwords.\n  import hashlib\n"
     "  hashlib.sha256(b'hello').hexdigest()\n"
     "For real passwords use bcrypt or argon2 (with salt), not plain SHA."),

    (["recursion", "recursive"],
     "Recursion: a function that calls itself, with a stopping case.\n"
     "  def fact(n):\n      return 1 if n <= 1 else n * fact(n - 1)"),

    (["generator", "yield"],
     "A generator makes values one at a time with yield, saving memory.\n"
     "  def count(n):\n      for i in range(n):\n          yield i"),

    (["decorator", "decorators"],
     "A decorator wraps a function to add behaviour.\n"
     "  def shout(f):\n      def w(*a):\n          return f(*a).upper()\n"
     "      return w\n  @shout\n  def hi(): return 'hi'"),

    (["comment", "comments"],
     "Comments start with # and are ignored by Python.\n"
     "  # this explains the next line\n  x = 1  # inline comment"),

    (["boolean", "bool", "true", "false"],
     "bool is True or False. Falsy values: 0, '', [], {}, None. "
     "Everything else is truthy."),
]

HELP_TEXT = "I don't know that yet. Try: " + ", ".join(
    k[0][0] for k in KNOWLEDGE[:12]) + "..."


def _tokens(text):
    return re.findall(r"[a-z_0-9]+", text.lower())


def _score(keywords, text, words):
    best = 0
    for kw in keywords:
        if " " in kw:                     # multi-word phrase
            if kw in text:
                best = max(best, 2 + len(kw.split()))   # longer phrase wins
        elif kw in words:                 # exact word
            best = max(best, 2)
        elif len(kw) >= 5:                # typo-tolerant for longer words
            if difflib.get_close_matches(kw, words, n=1, cutoff=0.85):
                best = max(best, 1)
    return best


def answer(question):
    """Return the best explanation for a question, or None."""
    text = " ".join(_tokens(question))
    words = set(text.split())
    scored = [(_score(kw, text, words), i) for i, (kw, _) in enumerate(KNOWLEDGE)]
    top, idx = max(scored)
    if top == 0:
        return None
    return KNOWLEDGE[idx][1]


def pretty(text, width=38):
    """Wrap prose lines for a phone screen but keep code lines intact."""
    out = []
    for line in text.split("\n"):
        out.append(line if line.startswith(" ") else textwrap.fill(line, width))
    return "\n".join(out)


if __name__ == "__main__":
    while True:
        q = input("\nYou: ").strip()
        if q.lower() in ("quit", "exit"):
            break
        print(pretty(answer(q) or HELP_TEXT))
