# Report format

Write the report as one JSON object with these fields. In any quote, put [[double square brackets]] around the exact words the point is about; in a "target", around the words that changed. The words inside the brackets must still match the transcript.

| Field | What goes in |
|---|---|
| `level` | The teacher's level, copied, e.g. "B1+". |
| `levelName` | From the CEFR guide, e.g. "Independent user, upper band of B1". |
| `studyLevel` | Recommended level of study, by the rule in the CEFR guide. |
| `summary` | Two or three sentences: what is solid, what showed above it, what is missing for the next level. |
| `highlights` | Exactly three: "Your strongest area" (one of Range, Accuracy, Fluency, Interaction, Coherence), "Your main focus" (two or three words), "Study next at" (studyLevel, with one sentence on why). Each has `label`, `value`, `note`. |
| `atWork` | `now`: three to five things the person can rely on their English for. `effort`: two or three that still take effort. `next`: three or four that the next level adds. Noun phrases that could follow "your English for…" ("Giving a status update in a daily meeting"), no full stop. `note`: one sentence saying the person was not observed in a real meeting, so this is a guide. |
| `criteria` | Exactly six, in order: Range, Accuracy, Fluency, Interaction, Coherence, Pronunciation. Each has `name`, a plain `gloss` ("Your control of grammar"), `level`, and `observed` (two or three sentences: what works, then what the next level needs). |
| `evidence` | Up to three things done well: `criterion`, `title`, `quote`, `note` (why it matters). |
| `ceiling` | Where the interview got harder: `text` (three or four sentences from the tasks and ratings), `quote`, `rungs` (C1, B2, B1, A2 in this order, each with `level`, `state` = confident / partly / not_reached, and a short `note`). |
| `priorities` | Up to three changes that move the level most: `criterion`, `title`, `said` (a quote), `target` (the same idea at the next level, keeping only the facts the person gave), `why`. |
| `phrases` | At most six phrases in all, in two or three groups that match the priorities. "…" for the gaps the person fills in. |
| `recommendation` | `programme` (one, name copied exactly from the list you were given), `levels` ("For B1 to B2"), `reason`, `practiceTitle` ("Something to try before the course"), `practice` (one small task to do alone this week). |

Voice: friendly and direct, "you", specific. Say what you heard, not how good it was. Never mention AI, a model or a transcript: say "your interview" or "the recording".
