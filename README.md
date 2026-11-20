# Speaking placement test: a Claude skill

A Claude skill for testing employees' spoken English as a conversation with a teacher, not a questionnaire.

At [UnifyHub](https://unifyhub.ee) we dropped written placement tests and an AI chatbot test. What's left is a 25-minute conversation with a teacher. Claude does the work around it:

- **Before the call:** builds a question set for the person's role, from A2 to C1. Every level tests the same skill in every profile, so a developer's test and a recruiter's test stay comparable.
- **During the call:** gives the teacher a run sheet and a simple level ladder (two confident answers move up a level, two struggles find the ceiling).
- **After the call:** drafts a CEFR report from a verbatim transcript and the teacher's notes. A script checks that every quote is word for word in the transcript. The teacher sets the level, edits the draft and approves it.

## What's inside

```
speaking-placement-test/
  SKILL.md                     the skill: three jobs and the rules
  references/question-bank.md  skill map + starter questions (general, business, engineering)
  references/cefr-guide.md     CEFR summaries in our own words, levels at work, teacher's marks
  references/report-format.md  the report structure
  scripts/check_quotes.py      checks every quote against the transcript
```

## Install

**Claude Code:** copy the `speaking-placement-test` folder into `~/.claude/skills/` (for you) or `.claude/skills/` in a project (for your team).

**Claude.ai:** zip the `speaking-placement-test` folder and upload it in Settings → Capabilities → Skills.

Then ask, for example: "Plan a placement test for a QA engineer whose team runs client demos" or "Draft the report from this transcript and my notes".

## Before you use it

- The questions are a starting point. Have your own methodologist or lead teacher adapt them.
- The report needs a verbatim transcript (with "um"s and false starts). Most video-call auto-transcripts tidy speech and hide the mistakes the report should quote.
- Recordings are personal data. Get consent, tell the person what their employer will see, and delete recordings you no longer need.
- The CEFR descriptions are paraphrased from the Council of Europe's CEFR. They are not the official text.

## Licence

MIT. Use it, change it, share it.
