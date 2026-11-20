---
name: speaking-placement-test
description: Run an English placement test as a live conversation with a teacher, then turn the recording into a CEFR report the teacher approves. Use it to plan a test for a role (general, business or role-specific questions from A2 to C1), to guide the teacher through the call with a simple level ladder, and to draft the report from a verbatim transcript with every quote checked against it. Works for learners, candidates and team members. Triggers - "placement test", "speaking test", "level test", "assess my employee's English", "assess a candidate's English", "CEFR report", "write the test report", "make role-specific test questions".
---

# Speaking placement test

A placement test that is a conversation, not a questionnaire. A teacher talks with the person for about 25 minutes. The skill helps before, during and after the call. The teacher sets the level. Claude prepares the questions, keeps the call on track and writes the first draft of the report.

This is how UnifyHub tests learners. It is shared as a starting point: adapt the questions and the report to your company. A worked example (an invented interview, the teacher's facts and the finished report) is in [examples/](examples/).

## The three jobs

Find out which job the user wants, then follow that section.

1. **Plan a test**: the question sheet for one person or one team.
2. **Run the call**: the run sheet and the level ladder.
3. **Draft the report**: from the transcript and the teacher's notes.

## 1. Plan a test

Ask for: the person's job (or the team's), what the company wants from English (general, business, a role), and anything the company asked to check (for example, client calls, interviews with candidates, incident reviews). Whenever you fill in details nobody gave you, use typical topics for the role and mark them "[check with the company]".

Then build the set from [references/question-bank.md](references/question-bank.md):

- Four levels: A2, B1, B2, C1. Three questions per level.
- Each question has a main question, a follow-up, a push (the harder follow-up that shows whether the person holds the level) and what to listen for.
- **Follow the skill map in the question bank.** Each level has three slots, and each slot tests the same skill in every profile. Only the topic changes, so a developer's test and a recruiter's test stay comparable.
- **Topics come from the person's real work**: their tools, meetings, clients and problems, in the words of their job, not general business words.
- **First fit company requests into the slots as topics.** A sensitive update or an incident review for senior managers is the C1 "sensitive topic" slot, not a change.
- **A request that no slot covers replaces one slot**, at most one per level. Put it at the level where the task is typical and replace the slot nearest to it: a status update or a short update to a manager replaces "plans and reasons" at B1 (as in the Engineering profile); running an interview or a negotiation replaces "opinion" at B2. Two such requests go to two different levels.
- **A skill the company wants to see in action is a short role-play** in that replaced slot: the teacher plays the other person (a candidate, a manager, a client). Give the follow-up and the push in role, and mark the whole role-play once.

**The question sheet** the teacher reads during the call. At the top, all of section 2: the timing table, the asking rules and the ladder. Then one table per level, with the columns Topic, Question, Follow-up, Push, Listen for, Mark (C / M / S).

## 2. Run the call

About 25 minutes on video, recorded with the person's consent.

| Part | Time | What happens |
|---|---|---|
| Hello | 2 min | Who you are, what will happen, that there are no right or wrong answers and nothing to prepare. Get consent to the recording and say who sees what (see the last section). |
| Questions | about 18 min | The ladder below. Usually 6 to 9 questions, about 2 minutes each. |
| Goals | about 5 min | What the person needs English for at work and what they expect from the course. This is where the studies start. |

**Asking.** Ask the main question and the follow-up every time. Ask the push when the answer so far sounds confident or when you can't decide between confident and managed. Mark the whole exchange, not only the first answer: confident (C), managed (M) or struggled (S).

**The ladder.** Start at A2, first question.

- Two confident answers at a level: move up straight away, even if a question at that level is left.
- Two struggled answers at a level: stop. The ceiling is found. The working level is the level below with a "+" (struggled twice at B2 means B1+). Struggled twice at A2 means A1.
- All three questions at a level asked with neither two confident nor two struggled answers: the working level is that level.
- Two confident answers at C1: the top of the ladder is reached, the working level is C1.

**Short on time:** drop the push at levels already passed, never the goals part.

The teacher also marks pronunciation and fluency on a 1 to 5 scale (see [references/cefr-guide.md](references/cefr-guide.md)), writes short notes and ticks the answers worth quoting in the report.

If the teacher asks Claude for help during the call, answer in one line: the next question, or the push for the current one.

## 3. Draft the report

Inputs:

- A **verbatim** transcript of the recording, with false starts and "um"s left in, and a speaker label on every turn ("Teacher:", "Marta:"). Tidied transcripts (like most video-call auto-transcripts) hide the mistakes the report should quote.
- The teacher's facts, in the format in [references/report-format.md](references/report-format.md#the-teachers-facts).

Read [references/cefr-guide.md](references/cefr-guide.md) and [references/report-format.md](references/report-format.md), then write the report as JSON in that format.

Rules that cannot bend:

1. **The teacher's level is final.** Copy it. Never argue with it.
2. **Quotes are the person's own words, exactly as spoken**, mistakes included. Never tidy the grammar and never quote the teacher. A quote comes from one answer: "…" may skip words inside that answer, never join two answers. If nothing in the transcript supports a point, drop the point.
3. **Put quotes in the quote fields** (evidence, ceiling, priorities "said"). Elsewhere, quote the person only in double quotation marks and only with three words or more, so the script can check them too.
4. Describe only what the transcript and the teacher's data show. Nothing about listening, reading, writing or personality. What the person said about their goals may be used for the recommendation.
5. Pronunciation cannot be heard in a transcript. Base it only on the teacher's mark and notes.
6. The teacher's marks, notes and ratings are not for the person. Say what was heard ("you speak at length with few pauses"), never "4 out of 5" and never "you struggled".
7. Friendly and direct, "you", specific. No praise words, no exclamation marks. Write at the person's level: short sentences and common words up to B1+, plain professional English from B2.

Then check every quote. Run the script from the skill folder, with the paths to your files:

```bash
python3 <skill folder>/scripts/check_quotes.py path/to/report.json path/to/transcript.txt
```

If the teacher's label is not Teacher, Assessor, Interviewer or Examiner, add `--teacher "Anna"`. Any line that is not OK goes back for a fix. Only then does the teacher read the draft, edit it and approve it.

## Who sees what

The person sees the full report. Their employer sees the level, the recommended level of study and the programme, without quotes. Say this at the start of the call and get consent to the recording and to what the employer sees. For a job candidate, say who in the company will read the report. In the EU this is personal data: keep recordings only as long as you need them.
