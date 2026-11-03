"""explain_code.py - line-by-line explanations for every program in
programs_library.py (Python and C). Works offline in Termux.

Used by main.py:
    import explain_code as ex
    if low.startswith("explain"):
        show(ex.find_explain(text) or ex.HELP)
"""
import re
import programs_library as pl

HELP = (
    "Explain a program line by line.\n"
    "Examples:\n"
    "  explain 1 in c\n"
    "  explain prime number in python\n"
    "  explain factorial in c\n"
    "Type 'explain list' to see all programs."
)

LIBS = {
    "stdio": "the input/output library (printf, scanf)",
    "string": "the string library (string functions)",
    "ctype": "the character library (checks like isdigit)",
    "stdlib": "the general utilities library",
    "math": "the math library",
    "stdbool": "the boolean library (true/false)",
}

FMT = {"%d": "an integer", "%i": "an integer", "%f": "a decimal number",
       "%lf": "a decimal number", "%s": "a word or text",
       "%c": "a single character", "%u": "an unsigned integer"}

# ------------------------------------------------------------ helpers
def _vars(text):
    """'&a, b[i]' -> 'a, b[i]'"""
    return ", ".join(v.strip().lstrip("&") for v in text.split(",") if v.strip())


def _fmt_desc(fmt):
    kinds = [FMT[t] for t in re.findall(r"%[lu]?[dfsci]", fmt) if t in FMT]
    return " and ".join(kinds) if kinds else "text"


def _cond(c):
    return c.strip().rstrip(";").strip()


# ----------------------------------------------------------- C lines
def _c(s):
    m = re.match(r"#include\s*<(\w+)\.h>", s)
    if m:
        return f"Includes {LIBS.get(m.group(1), 'a library')}."
    if re.match(r"int main\(void\)\s*\{?$", s):
        return "Starts the main function. The program begins running here."
    if re.match(r"return 0;?$", s):
        return "Ends the program and reports success to the operating system."
    m = re.match(r"return (.+?);?$", s)
    if m:
        return f"Ends the function and returns {m.group(1)}."
    if re.match(r"\}\s*(else.*)?\{?$", s) or s == "}":
        if re.match(r"\}\s*else", s):
            return "Ends the previous block, then continues with the else part."
        return "Closes the current block."
    m = re.match(r"else if\s*\((.*)\)\s*\{?$", s)
    if m:
        return f"Otherwise, if {_cond(m.group(1))}, runs the block below."
    if re.match(r"else\s*\{?$", s):
        return "Otherwise (if no earlier condition was true), runs the block below."
    m = re.match(r"if\s*\((.*?)\)\s*(\{)?$", s)
    if m:
        return f"Runs the block below only if {_cond(m.group(1))}."
    m = re.match(r"if\s*\((.*?)\)\s*(.+;)$", s)          # one-line if
    if m:
        return f"Only if {_cond(m.group(1))}: {_c(m.group(2))}"
    m = re.match(r"for\s*\((.*?);(.*?);(.*?)\)\s*\{?$", s)
    if m:
        init, cond, step = (x.strip() for x in m.groups())
        return (f"Loop: starts with {init}, repeats while {cond}, "
                f"and after each pass runs {step}.")
    m = re.match(r"while\s*\((.*?)\)\s*\{?$", s)
    if m:
        return f"Repeats the block below while {_cond(m.group(1))}."
    if re.match(r"break;?$", s):
        return "Exits the loop immediately."
    if re.match(r"continue;?$", s):
        return "Skips the rest of this loop pass and goes to the next one."
    m = re.match(r"fclose\((\w+)\);?$", s)
    if m:
        return f"Closes the file {m.group(1)}."
    m = re.match(r"printf\((\"(.*)\")\);?$", s)
    if m:
        text = m.group(2)
        if text == r"\n":
            return "Prints a blank line."
        if text == "*":
            return "Prints a * on the same line (no new line)."
        return f'Prints the text "{text.replace(chr(92) + "n", "")}"' + (
            " and then moves to a new line." if text.endswith(r"\n") else ".")
    m = re.match(r"printf\(\"(.*?)\",\s*(.+)\);?$", s)
    if m:
        fmt, args = m.groups()
        return (f"Prints the message, putting in the value of {args} "
                f"(as {_fmt_desc(fmt)}).")
    m = re.match(r"scanf\(\"(.*?)\",\s*(.+)\);?$", s)
    if m:
        fmt, args = m.groups()
        return (f"Reads {_fmt_desc(fmt)} typed by the user and stores it "
                f"in {_vars(args)}.")
    m = re.match(r"(int|float|double|char|long)\s+(.+);$", s)
    if m:
        typ, names = m.groups()
        kind = {"int": "integer", "float": "decimal", "double": "decimal",
                "char": "single-character", "long": "large integer"}[typ]
        names = re.sub(r"\s*=\s*[^,]+", "", names)
        plural = "s" if "," in names else ""
        return f"Declares {kind} variable{plural} {names}."
    m = re.match(r"(\w+)\s*\+\+;?$", s)
    if m:
        return f"Adds 1 to {m.group(1)}."
    m = re.match(r"(\w+)\s*--;?$", s)
    if m:
        return f"Subtracts 1 from {m.group(1)}."
    m = re.match(r"(.+?)\s*(\+|-|\*|/|%)=\s*(.+);$", s)
    if m:
        target, op, val = m.groups()
        verb = {"+": "Adds", "-": "Subtracts", "*": "Multiplies",
                "/": "Divides", "%": "Takes the remainder of"}[op]
        word = {"+": "to", "-": "from", "*": "by", "/": "by", "%": "by"}[op]
        return f"{verb} {target} {word} {val} and stores the result back in {target}."
    m = re.match(r"(.+?)\s*=\s*(.+);$", s)
    if m:
        target, val = m.groups()
        return f"Calculates {val} and stores the result in {target}."
    return None


# ------------------------------------------------------- Python lines
def _py(s):
    if s == "print()":
        return "Prints a blank line."
    m = re.match(r"print\((.*)\)$", s)
    if m:
        args = m.group(1)
        if re.match(r"^'[^']*'$|^\"[^\"]*\"$", args):
            return f"Prints the text {args}."
        if "," in args:
            return f"Prints {args}, with the parts separated by spaces."
        return f"Prints the value of {args}."
    m = re.match(r"(\w+)\s*=\s*(int|float|str)?\(?input\((.*?)\)\)?$", s)
    if m:
        name, typ, prompt = m.groups()
        conv = {"int": "a whole number", "float": "a decimal number",
                "str": "text"}.get(typ, "text")
        return f"Shows the prompt {prompt} and stores the answer as {conv} in {name}."
    m = re.match(r"(\w+)\s*=\s*list\(map\(int, input\((.*?)\)\.split\(\)\)\)$", s)
    if m:
        return (f"Shows the prompt {m.group(2)}, splits the typed numbers by "
                f"spaces, and stores them as a list in {m.group(1)}.")
    m = re.match(r"import (.+)$", s)
    if m:
        return f"Imports the {m.group(1)} module so its tools can be used."
    m = re.match(r"def (\w+)\((.*)\):$", s)
    if m:
        return f"Defines a function named {m.group(1)}."
    m = re.match(r"for (\w+) in range\((.*)\):$", s)
    if m:
        return (f"Repeats the block below, with {m.group(1)} taking each value "
                f"from range({m.group(2)}) in turn.")
    m = re.match(r"for (\w+) in (.+):$", s)
    if m:
        return f"Repeats the block below once for each item {m.group(1)} in {m.group(2)}."
    m = re.match(r"while (.+):$", s)
    if m:
        return f"Repeats the block below while {m.group(1)} is true."
    m = re.match(r"elif (.+):$", s)
    if m:
        return f"Otherwise, if {m.group(1)}, runs the block below."
    if s == "else:":
        return "Otherwise, runs the block below."
    m = re.match(r"if (.+):$", s)
    if m:
        return f"Runs the block below only if {m.group(1)}."
    if s == "break":
        return "Exits the loop immediately."
    if s == "continue":
        return "Skips the rest of this loop pass and goes to the next one."
    if s == "pass":
        return "Does nothing (a placeholder)."
    m = re.match(r"return (.+)$", s)
    if m:
        return f"Sends back {m.group(1)} as the result of the function."
    m = re.match(r"(\w+)\.append\((.+)\)$", s)
    if m:
        return f"Adds {m.group(2)} to the end of the list {m.group(1)}."
    m = re.match(r"(\w+)\s*\+=\s*(.+)$", s)
    if m:
        return f"Adds {m.group(2)} to {m.group(1)}."
    m = re.match(r"(\w+)\s*-=\s*(.+)$", s)
    if m:
        return f"Subtracts {m.group(2)} from {m.group(1)}."
    m = re.match(r"(\w+)\s*(\*\*|\*|//|/|%)=\s*(.+)$", s)
    if m:
        name, op, val = m.groups()
        verb = {"*": "Multiplies", "**": "Raises", "//": "Divides",
                "/": "Divides", "%": "Takes the remainder of"}[op]
        return f"{verb} {name} by {val} and stores the result back in {name}."
    m = re.match(r"(\w+(?:\[.+\])?)\s*=\s*(.+)$", s)
    if m:
        return f"Calculates {m.group(2)} and stores the result in {m.group(1)}."
    return None



# ------------------------------------------------- extra C constructs
def _c_extra(s):
    if s.startswith("//"):
        return "A comment: " + s[2:].strip() + "."
    if re.match(r"(srand\(|srandom\()", s):
        return "Seeds the random number generator with the current time so numbers differ each run."
    if s.startswith("#define") or s.startswith("#"):
        return "A preprocessor directive, handled before the program is compiled."
    if re.match(r"switch\s*\((.*)\)\s*\{?$", s):
        m = re.match(r"switch\s*\((.*)\)", s)
        return f"Checks the value of {m.group(1)} and jumps to the matching case below."
    m = re.match(r"case\s+(.+?):\s*(.*)$", s)
    if m:
        val, rest = m.groups()
        base = f"If the value is {val}, runs the cases below."
        if rest:
            return f"If the value is {val}: {_c_extra_or(rest)}"
        return base
    if re.match(r"default:", s):
        rest = s[len("default:"):].strip()
        if rest:
            return f"If no case matched: {_c_extra_or(rest)}"
        return "If no case matched, runs the code below."
    if re.match(r"do\s*\{?$", s):
        return "Starts a loop that runs at least once, then checks its condition at the end."
    m = re.match(r"\}\s*while\s*\((.*)\);?$", s)
    if m:
        return f"End of the do-loop: repeats while {m.group(1)}."
    if re.match(r"struct\s+\w+\s*\{?$", s):
        name = s.split()[1].rstrip("{").strip()
        return f"Defines a structure (a group of related fields) named {name}."
    if re.match(r"\};$", s):
        return "Ends the structure definition."
    m = re.match(r"struct\s+(\w+)\s+(\w+);$", s)
    if m:
        return f"Declares a variable {m.group(2)} of type {m.group(1)}."
    m = re.match(r"(\w+)\s+(\w+);$", s)
    if m and m.group(1) not in ("return", "else", "break"):
        return f"Declares a variable {m.group(2)} of type {m.group(1)}."
    m = re.match(r"fgets\((\w+),.*stdin\);?$", s)
    if m:
        return f"Reads a whole line of text from the keyboard into {m.group(1)}."
    m = re.match(r"fgets\((\w+),.*\);?$", s)
    if m:
        return f"Reads a whole line of text from the file into {m.group(1)}."
    m = re.match(r"putchar\((.+)\);?$", s)
    if m:
        return f"Prints the single character {m.group(1)}."
    m = re.match(r"fprintf\((\w+),\s*\"(.*?)\"(?:,\s*(.+))?\);?$", s)
    if m:
        f, fmt, args = m.groups()
        where = f"into the file {f}"
        return f'Writes the text "{fmt.replace(chr(92)+"n", "")}" {where}.'
    m = re.match(r"printf\((\w+)\s*\?\s*\"(.*?)\"\s*:\s*\"(.*?)\"\);?$", s)
    if m:
        cond, yes, no = m.groups()
        return (f'If {cond} is true, prints "{yes.replace(chr(92)+"n", "")}"; '
                f'otherwise prints "{no.replace(chr(92)+"n", "")}".')
    m = re.match(r"(?:else\s+)?printf\(\"(.*?)\"\);?$", s)
    if m and s.startswith("else"):
        return f'Otherwise, prints "{m.group(1).replace(chr(92)+"n", "")}".'
    m = re.match(r"if\s*\((.*?)\)\s*\{(.*)\}$", s)
    if m:
        cond, body = m.groups()
        return f"If {_cond(cond)}: {_c_extra_or(body.strip())}"
    m = re.match(r"else\s+(.+;)$", s)
    if m:
        return f"Otherwise: {_c_extra_or(m.group(1))}"
    m = re.match(r"(\w+)\s*=\s*(\w+)\s*;$", s)
    return None


def _c_extra_or(stmt):
    """Explain a short inline statement, falling back to the generic text."""
    out = _c_extra(stmt.strip()) or _c(stmt.strip())
    return out.rstrip(".") + "." if out else "runs this step."


# ----------------------------------------------- extra Python constructs
def _py_extra(s):
    if s.startswith("#"):
        return "A comment: " + s[1:].strip() + "."
    m = re.match(r"(\w+),\s*(\w+)\s*=\s*(\w+),\s*(\w+)$", s)
    if m:
        a, b, c, d = m.groups()
        if a == d and b == c:
            return f"Swaps the values of {a} and {b}."
        return f"Assigns {c} to {a} and {d} to {b} at the same time."
    m = re.match(r"(\w+),\s*(\w+)\s*=\s*(.+),\s*(.+)$", s)
    if m:
        a, b, c, d = m.groups()
        if a == d and b == c:
            return f"Swaps the values of {a} and {b}."
        return f"Assigns {c} to {a} and {d} to {b} at the same time."
    m = re.match(r"(\w+)\s*=\s*(\w+),\s*(\w+)$", s)
    if m:
        return f"Sets {m.group(1)} ... (see the code)."
    m = re.match(r"(\w+)\s*=\s*(\d+)\s*,\s*(.+)$", s)
    if m:
        names = [m.group(1)] + [x.strip() for x in s.split("=")[1:]]
        return f"Sets several variables at once (starting values shown on this line)."
    m = re.match(r"with open\((.+?)\)\s+as\s+(\w+):$", s)
    if m:
        return f"Opens the file {m.group(1)} (as {m.group(2)}); it closes automatically at the end of the block."
    m = re.match(r"(\w+)\.write\((.+)\)$", s)
    if m:
        return f"Writes {m.group(2)} to the file {m.group(1)}."
    m = re.match(r"(\w+)\.close\(\)$", s)
    if m:
        return f"Closes the file {m.group(1)}."
    m = re.match(r"class (\w+)(\(.*\))?:$", s)
    if m:
        return f"Defines a class (a blueprint for objects) named {m.group(1)}."
    m = re.match(r"self\.(\w+)\s*=\s*(.+)$", s)
    if m:
        return f"Stores {m.group(2)} in the object's {m.group(1)} field."
    if re.match(r"\w+\(.*\)\.\w+\(.*\)$", s):
        return f"Creates an object and calls one of its methods: {s}."
    if re.match(r"\w+\(.*\)$", s) and s.split("(")[0] in ("Student",):
        return f"Creates a new {s.split('(')[0]} object."
    m = re.match(r"(\w+)\s*=\s*\[(.+) for (\w+) in (.+)\]$", s)
    if m:
        return f"Builds a list {m.group(1)} by computing {m.group(2)} for each {m.group(3)} in {m.group(4)}."
    m = re.match(r"(\w+)\s*=\s*\((.*)\)$", s)
    if m:
        return f"Stores {m.group(2)} in {m.group(1)}."
    return None


# ------------------------------------------------------------- public
def explain_line(line, lang):
    s = line.strip()
    if not s:
        return None
    # split off a trailing comment, explain the code, then add the comment
    comment = None
    if lang == "c" and "//" in s and not s.startswith("//"):
        code, comment = s.split("//", 1)
        code = code.strip()
    elif lang == "python" and "#" in s and not s.startswith("#") and "'" not in s.split("#")[-1] and '"' not in s.split("#")[-1]:
        code, comment = s.split("#", 1)
        code = code.strip()
    else:
        code = s
    if lang == "c":
        out = _c(code) or _c_extra(code)
    else:
        out = _py(code) or _py_extra(code)
    if out is None:
        out = "Runs this step (see the code for the details)."
    if comment and comment.strip():
        out = out.rstrip(".") + ". (Note: " + comment.strip() + ")"
    return out


def explain_program(i, lang):
    p = pl.PROGRAMS[i]
    code = p["py"] if lang == "python" else p["c"]
    label = "Python" if lang == "python" else "C"
    lines = [f"{i + 1}. {p['title']} ({label}) - line by line", ""]
    for ln in code.split("\n"):
        if not ln.strip():
            continue
        lines.append(ln.rstrip())
        lines.append("  -> " + explain_line(ln, lang))
        lines.append("")
    return "\n".join(lines).rstrip()


def _lang_of(words):
    if "c" in words:
        return "c"
    if "python" in words or "py" in words:
        return "python"
    return "python"


def _program_index(words, text):
    nums = [int(w) for w in words if w.isdigit()]
    if nums and 1 <= nums[0] <= len(pl.PROGRAMS):
        return nums[0] - 1
    wset = set(words)
    best, best_score = None, 0
    for i, p in enumerate(pl.PROGRAMS):
        for kw in p["kws"] + [p["title"]]:
            k = pl._norm(kw)
            if k and all(w in wset for w in k) and len(k) > best_score:
                best, best_score = i, len(k)
    return best


def find_explain(question):
    """Return the explanation text for 'explain ...' requests, else None."""
    q = question.strip()
    if not re.match(r"explain\b", q, re.I):
        return None
    rest = re.sub(r"^explain\s*", "", q, flags=re.I)
    words = pl._norm(rest)
    if not words or words == ["help"]:
        return HELP
    if words[0] == "list":
        titles = "\n".join(f"{i}. {p['title']}"
                           for i, p in enumerate(pl.PROGRAMS, 1))
        return "Programs you can explain:\n" + titles
    i = _program_index(words, rest)
    if i is None:
        return "I couldn't find that program. Type 'explain list' to see all."
    return explain_program(i, _lang_of(words))


if __name__ == "__main__":
    while True:
        q = input("\nExplain: ").strip()
        if q in ("quit", "exit"):
            break
        print(find_explain(q) or HELP)
