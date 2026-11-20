#!/usr/bin/env python3
"""Check that every quote in a report is the person's own words, word for word.

Usage:
  python3 check_quotes.py REPORT.json TRANSCRIPT.txt [--teacher LABEL ...]

The transcript should have one speaker label per turn, like "Teacher: ..." and
"Marta: ...". Turns by the teacher are never valid quotes. Labels Teacher, Assessor,
Interviewer and Examiner are treated as the teacher; add others with --teacher.

A quote passes when it is inside ONE turn of the person. Case, punctuation and the
[[highlight]] brackets are ignored. "…" (or "...") may skip words, but every part must
come from the same turn and in the same order.

Checked:
  - evidence[].quote, ceiling.quote, priorities[].said (the quote fields);
  - any text of three words or more in quotation marks in the other fields
    (summary, criteria, notes and so on), because a quote there must be real too.
Not checked: priorities[].target and phrases, which are new language, not quotes.

Exit code 0 if everything passes, 1 if any quote fails, 2 on a usage error.
"""
import argparse
import json
import re
import sys

TEACHER_LABELS = {"teacher", "assessor", "interviewer", "examiner"}
LABEL = re.compile(r"^\s*(?:\[?[\d:.,\- >]+\]?\s*)?([A-Z][\w'\-]*(?: [A-Z0-9][\w'\-]*){0,2})\s*:\s*(.*)$")
QUOTED = re.compile(r"[\"“]([^\"“”]+)[\"”]")
SKIP_FIELDS = {"target", "phrases", "quote", "said"}


def plain(s: str) -> str:
    s = s.replace("[[", "").replace("]]", "").lower()
    s = re.sub(r"[’‘`]", "'", s)
    s = s.replace("...", "…")
    s = re.sub(r"[^\w'…]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def read_turns(text: str, teacher: set):
    """Split the transcript into turns. Returns (person_turns, teacher_turns, labelled)."""
    turns = []  # [label, text]
    for line in text.splitlines():
        m = LABEL.match(line)
        if m:
            turns.append([m.group(1).strip().lower(), m.group(2)])
        elif line.strip():
            if turns:
                turns[-1][1] += " " + line
            else:
                turns.append(["", line])
    labelled = any(label for label, _ in turns)
    person = [plain(t).replace("…", " ") for label, t in turns if label not in teacher]
    teach = [plain(t).replace("…", " ") for label, t in turns if label in teacher]
    return person, teach, labelled


def in_one_turn(quote: str, turns) -> bool:
    parts = [p.strip() for p in plain(quote).split("…") if p.strip()]
    if not parts:
        return False
    for turn in turns:
        start, ok = 0, True
        for part in parts:
            at = turn.find(part, start)
            if at < 0:
                ok = False
                break
            start = at + len(part)
        if ok:
            return True
    return False


def verdict(quote: str, person, teach) -> str:
    if in_one_turn(quote, person):
        return "OK"
    if in_one_turn(quote, teach):
        return "TEACHER'S WORDS"
    parts = [p for p in plain(quote).split("…") if p.strip()]
    if len(parts) > 1 and all(in_one_turn(p, person) for p in parts):
        return "JOINS DIFFERENT TURNS"
    return "NOT IN THE TRANSCRIPT"


def quote_fields(report: dict):
    for i, e in enumerate(report.get("evidence", []), 1):
        yield f"evidence {i}", e.get("quote", "")
    yield "ceiling", report.get("ceiling", {}).get("quote", "")
    for i, p in enumerate(report.get("priorities", []), 1):
        yield f"priority {i}, said", p.get("said", "")


def inline_quotes(node, path=""):
    """Quoted text of three words or more in the fields that are not quote fields."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k not in SKIP_FIELDS:
                yield from inline_quotes(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node, 1):
            yield from inline_quotes(v, f"{path}[{i}]")
    elif isinstance(node, str):
        for m in QUOTED.finditer(node):
            if len(plain(m.group(1)).replace("…", " ").split()) >= 3:
                yield path, m.group(1)


def main() -> int:
    ap = argparse.ArgumentParser(description="Check report quotes against the transcript.")
    ap.add_argument("report")
    ap.add_argument("transcript")
    ap.add_argument("--teacher", action="append", default=[], help="speaker label of the teacher (repeatable)")
    a = ap.parse_args()

    with open(a.report, encoding="utf-8") as f:
        report = json.load(f)
    with open(a.transcript, encoding="utf-8") as f:
        text = f.read()
    teacher = TEACHER_LABELS | {t.lower() for t in a.teacher}
    person, teach, labelled = read_turns(text, teacher)
    if not labelled:
        print("WARNING: the transcript has no speaker labels, so the teacher's words cannot be told apart.")
    elif not teach:
        print("WARNING: no teacher turns found. Name the teacher's label with --teacher.")

    failed = 0
    checks = list(quote_fields(report)) + [(f"{p} (quote in text)", q) for p, q in inline_quotes(report)]
    for where, quote in checks:
        if not quote.strip():
            continue
        v = verdict(quote, person, teach)
        failed += v != "OK"
        print(f"{v:<22} {where}: {quote.replace('[[', '').replace(']]', '')}")
    print("All quotes are the person's own words." if not failed else f"{failed} quote(s) failed. Fix them before the teacher sees the report.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
