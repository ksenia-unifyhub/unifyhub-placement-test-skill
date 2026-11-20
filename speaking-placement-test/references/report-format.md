# Report format

## The teacher's facts

What the teacher gives you with the transcript, as JSON or in plain words:

| Field | What it is |
|---|---|
| `firstName` | The person's first name. Use it only if you address them by name; the report itself has no name field. |
| `questionSet` | Which profile was used, e.g. "QA & Testing". |
| `level` | The teacher's working level, e.g. "B1+". Final. |
| `ladderNote` | How the ladder ended, e.g. "Ceiling found at B2". |
| `tasks` | Every question asked, in order: `level`, `task`, `rating` (confident / managed / struggled), `quoteThis` (true when the teacher ticked it). Ticked answers are the teacher's suggestions; other answers may be quoted too. |
| `pronunciationMark`, `fluencyMark` | 1 to 5, see the CEFR guide. |
| `notes` | The teacher's short notes. |
| `programmes` | The courses you may recommend: `name`, `forLevels`, `about`. If there are none, leave `recommendation.programme` empty and say so. |

## The report

One JSON object with these fields. A full example is in `examples/report.json`.

Mark the words a point is about with [[double square brackets]]: always in `said`, and in other quotes where it helps. In a `target`, put them around the words that changed. The words inside the brackets must still match the transcript.

| Field | What goes in |
|---|---|
| `level` | The teacher's level, copied, e.g. "B1+". |
| `levelName` | From the CEFR guide, e.g. "Independent user, upper band of B1". |
| `studyLevel` | Recommended level of study, by the rule in the CEFR guide. |
| `summary` | Two or three sentences: what is solid, what showed above it, what is missing for the next level. |
| `highlights` | Exactly three, each with `label`, `value`, `note`: "Your strongest area" (one of Range, Accuracy, Fluency, Interaction, Coherence; not Pronunciation, which comes from the teacher's mark, not from what you read), "Your main focus" (two or three words), "Study next at" (studyLevel, with one sentence on why). |
| `atWork` | `now`: three to five things the person can rely on their English for. `effort`: two or three that still take effort. `next`: three or four that the next level adds. Noun phrases that could follow "your English for…" ("Giving a status update in a daily meeting"), no full stop. `note`: one sentence saying the person was not observed in a real meeting, so this is a guide. |
| `criteria` | Exactly six, in order: Range, Accuracy, Fluency, Interaction, Coherence, Pronunciation. Each has `name`, a plain `gloss` ("Your control of grammar"), `level`, and `observed` (two or three sentences: what works, then what the next level needs). How to set each level: see "Levels per criterion" in the CEFR guide. |
| `evidence` | Up to three things done well: `criterion`, `title`, `quote`, `note` (why it matters). Two strong items are better than three with a weak quote. |
| `ceiling` | Where the interview got harder: `text` (three or four sentences built from the tasks, in your words, never "managed" or "struggled"), `quote`, `rungs`: C1, B2, B1, A2 in this order, each with `level`, `state` and a short `note`. `state` is `confident` when the level was passed (two confident answers), `partly` when questions at that level were asked but the level was not held, `not_reached` when no question at that level was asked. |
| `priorities` | Up to three changes that move the level most: `criterion`, `title`, `said` (a quote), `target` (the same idea as it sounds at the next level; better language only, no new facts, reasons or numbers the person never gave), `why`. |
| `phrases` | A list of groups, `[{"group": "Make your case", "items": ["The impact for the user is …", "I understand your point, but …"]}]`. Two or three groups that match the priorities, at most six phrases in all. "…" marks what the person fills in. |
| `recommendation` | `programme` (one, name copied exactly from the list), `levels` ("For B1 to B2", from its `forLevels`), `reason` (one or two sentences tied to what you heard and to the goals the person named), `practiceTitle` ("Something to try before the course"), `practice` (one small task to do alone this week, in a few minutes). |

Voice: friendly and direct, "you", specific. Say what you heard, not how good it was. Never mention AI, a model or a transcript: say "your interview" or "the recording".
