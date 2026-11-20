---
name: speaking-placement-test
description: Run an English placement test as a live conversation with a teacher, then turn the recording into a CEFR report the teacher approves. Use it to plan a test for a role (general, business or role-specific questions from A2 to C1), to guide the teacher through the call with a simple level ladder, and to draft the report from a verbatim transcript with every quote checked against it. Triggers - "placement test", "speaking test", "level test", "assess my employee's English", "CEFR report", "write the test report", "make role-specific test questions".
---

# Speaking placement test

A placement test that is a conversation, not a questionnaire. A teacher talks with the person for about 25 minutes. The skill helps before, during and after the call. The teacher sets the level. Claude prepares questions, keeps the call on track and writes the first draft of the report.

This is how UnifyHub tests learners. It is shared as a starting point: adapt the questions and the report to your company.

## The three jobs

Find out which job the user wants, then follow that section.

1. **Plan a test**: questions for one person or one team.
2. **Run the call**: the teacher's run sheet and the level ladder.
3. **Draft the report**: from the transcript and the teacher's notes.

## 1. Plan a test

Ask for: the person's job (or the team's), what the company wants from English (general, business, a role), and anything the company asked to check (for example, client calls or incident reviews).

Then build a question set from [references/question-bank.md](references/question-bank.md):

- Four levels: A2, B1, B2, C1. Three questions per level.
- Each question has a main question, a follow-up, a "push" (the harder follow-up that tests whether the person holds the level) and what to listen for.
- **Every level tests the same skill in every profile. Only the topic changes.** B1 is always "tell a story about a problem you solved", B2 is always "justify a choice or argue a view", whatever the job. This keeps tests comparable across roles.
- For a role-specific test, keep the skill map from the question bank and write the topics from the person's real work. Use words from their job description, not general business words.
- Give the set to the teacher as a table they can read during the call.

## 2. Run the call

About 25 minutes on video, recorded with the person's consent.

| Part | Time | What happens |
|---|---|---|
| Hello | 2 min | Who you are, what will happen, that there are no right or wrong answers and nothing to prepare. Confirm consent to recording. |
| Questions | about 18 min | The ladder below. |
| Goals | about 5 min | What the person needs English for at work, what they expect from the course. This is where the studies start. |

**The ladder.** Start at A2, first question. After each answer the teacher marks it: confident, managed or struggled.

- Two confident answers at a level: move up to the next level.
- Two struggled answers at a level: stop. The ceiling is found. The working level is the level below with a "+" (struggled twice at B2 means B1+).
- All questions at a level asked without either: the working level is that level.
- Confident at C1: the top of the ladder is reached.

The teacher also notes pronunciation and fluency on a 1 to 5 scale (see [references/cefr-guide.md](references/cefr-guide.md)) and marks answers worth quoting in the report.

If the teacher asks Claude for help during the call, answer in one line: the next question, or the push for the current one.

## 3. Draft the report

Inputs:

- A **verbatim** transcript of the recording, with the false starts and "um"s left in. Tidied transcripts (like most video-call auto-transcripts) hide the mistakes the report must quote.
- The teacher's facts: first name, question set, each task with its rating, the working level, pronunciation and fluency marks, notes, and the programmes you may recommend.

Read [references/cefr-guide.md](references/cefr-guide.md) and [references/report-format.md](references/report-format.md), then write the report as JSON in that format.

Rules that cannot bend:

1. **The teacher's level is final.** Copy it. Never argue with it.
2. **Quotes are the person's own words, exactly as spoken**, mistakes included. Never tidy grammar, never join sentences that were not next to each other, never quote the teacher. A quote may be cut at the start or end with "…". If nothing in the transcript supports a point, drop the point.
3. Describe only what the transcript and the teacher's data show. Nothing about listening, reading, writing, personality or motivation.
4. Pronunciation cannot be heard in a transcript. Base it only on the teacher's mark and notes.
5. The teacher's marks and notes are not for the student. Say what was heard ("you speak at length with few pauses"), never "4 out of 5".
6. Friendly and direct, "you", specific. No praise words, no exclamation marks. Write at the person's level: short sentences for A2 to B1.

Then check every quote against the transcript:

```bash
python3 scripts/check_quotes.py report.json transcript.txt
```

A report with a quote that is not in the transcript goes back for a fix. Only then does the teacher read it, edit it and approve it.

## Who sees what

The person sees the full report. Their employer sees the level, the recommended level of study and the programme, without quotes. Say this to the person at the start of the call, and get their consent to the recording and to what the employer sees. In the EU this is personal data: keep recordings only as long as you need them.
