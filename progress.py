"""Progress tracker: saves quiz and lab results in progress.json."""
import json
import os
import time

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "progress.json")


def _blank():
    return {"quiz": {"taken": 0, "right": 0, "asked": 0, "best": 0},
            "labs": {}, "days": []}


def load():
    try:
        with open(FILE) as f:
            data = json.load(f)
        base = _blank()
        base.update(data)
        return base
    except (OSError, ValueError):
        return _blank()


def save(data):
    try:
        with open(FILE, "w") as f:
            json.dump(data, f)
        os.chmod(FILE, 0o600)
    except OSError:
        pass


def _mark_day(data):
    today = time.strftime("%Y-%m-%d")
    if today not in data["days"]:
        data["days"] = (data["days"] + [today])[-60:]


def record_quiz(score, total):
    d = load()
    q = d["quiz"]
    q["taken"] += 1
    q["right"] += score
    q["asked"] += total
    q["best"] = max(q["best"], score)
    _mark_day(d)
    save(d)


def record_lab(name, passed):
    d = load()
    lab = d["labs"].setdefault(name, {"tries": 0, "passed": 0})
    lab["tries"] += 1
    if passed:
        lab["passed"] += 1
    _mark_day(d)
    save(d)


def level(points):
    steps = [(0, "Newcomer"), (5, "Beginner"), (15, "Learner"),
             (30, "Defender"), (60, "Ethical Hacker in training")]
    name = steps[0][1]
    for need, title in steps:
        if points >= need:
            name = title
    return name


def streak(days):
    """Consecutive days ending today or yesterday."""
    if not days:
        return 0
    from datetime import date, timedelta
    have = {date.fromisoformat(x) for x in days}
    day = date.today()
    if day not in have:
        day -= timedelta(days=1)
    n = 0
    while day in have:
        n += 1
        day -= timedelta(days=1)
    return n


def report():
    d = load()
    q = d["quiz"]
    lab_pts = sum(v["passed"] for v in d["labs"].values())
    points = q["right"] + lab_pts * 2
    lines = ["YOUR PROGRESS", "-" * 22]
    lines.append(f"Level: {level(points)} ({points} points)")
    lines.append(f"Study days: {len(d['days'])}   Streak: {streak(d['days'])}")
    if q["taken"]:
        pct = 100 * q["right"] // max(q["asked"], 1)
        lines.append(f"Quizzes: {q['taken']} taken, best {q['best']}/5, "
                     f"{pct}% correct")
    else:
        lines.append("Quizzes: none yet (type 'quiz')")
    if d["labs"]:
        lines.append("Labs:")
        for name, v in sorted(d["labs"].items()):
            bar = "#" * min(v["passed"], 10)
            lines.append(f"  {name}: {v['passed']}/{v['tries']} {bar}")
    else:
        lines.append("Labs: none yet (type 'labs')")
    lines.append("Next goal: " + next_goal(points))
    return "\n".join(lines)


def next_goal(points):
    for need in (5, 15, 30, 60):
        if points < need:
            return f"{need - points} more points to level up"
    return "You reached the top level!"


def reset():
    save(_blank())
