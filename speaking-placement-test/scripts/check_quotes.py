#!/usr/bin/env python3
"""Check that every quote in a report is word for word in the transcript.

Usage: python3 check_quotes.py report.json transcript.txt

Case, punctuation and the [[highlight]] brackets are ignored. A quote cut with "…"
passes when every part is in the transcript, in this order. Exit code 1 if any quote
is missing, so a report with an invented quote cannot slip through.
"""
import json
import re
import sys


def plain(s: str) -> str:
    s = s.replace("[[", "").replace("]]", "").lower()
    s = re.sub(r"[’‘`]", "'", s)
    s = s.replace("...", "…")
    s = re.sub(r"[^\w'…]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def in_transcript(quote: str, transcript: str) -> bool:
    parts = [p.strip() for p in plain(quote).split("…") if p.strip()]
    if not parts:
        return False
    start = 0
    for part in parts:
        at = transcript.find(part, start)
        if at < 0:
            return False
        start = at + len(part)
    return True


def quotes(report: dict):
    for i, e in enumerate(report.get("evidence", []), 1):
        yield f"What you do well, quote {i}", e.get("quote", "")
    yield "Where it got harder", report.get("ceiling", {}).get("quote", "")
    for i, p in enumerate(report.get("priorities", []), 1):
        yield f"Priority {i}, you said", p.get("said", "")


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as f:
        report = json.load(f)
    with open(sys.argv[2], encoding="utf-8") as f:
        transcript = re.sub(r"\s+", " ", plain(f.read()).replace("…", " "))
    missing = 0
    for where, quote in quotes(report):
        if not quote.strip():
            continue
        ok = in_transcript(quote, transcript)
        missing += not ok
        print(f"{'OK     ' if ok else 'MISSING'}  {where}: {quote.replace('[[', '').replace(']]', '')}")
    print("All quotes found." if not missing else f"{missing} quote(s) not in the transcript. Fix them before the teacher sees the report.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
