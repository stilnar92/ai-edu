# Examiner

The examiner is a fresh session of the same assistant that has not seen any tutoring for this course. It checks a finished block from the files alone, so that the session that taught the block is not the only one that judges it. It is used on every check day (K1, K2, …); see [How you learn in this course](DAILY_COURSE.md#how-you-learn-in-this-course).

The examiner is the same model family as the tutor, so it shares the tutor's blind spots. It reduces the problem of one model teaching and judging; it does not remove it. The stronger evidence is the executed checks, the mutation you run against your own tests, and, in Part E, the process owner's response.

## How to run it

1. Open a new chat in the same folder as the tutor chat (the parent of `ai-edu`, so the `ai-edu/...` paths in the prompt resolve). Do not continue the tutoring chat.
2. Paste the prompt below and fill in the block.
3. Answer its questions without opening the files. It then quotes the files.
4. Open every quote yourself and confirm it says what the examiner claims.
5. Let the examiner append its entry to the log at the end of this file. Then return to the tutor session and say that the check day is recorded.

## Examiner prompt

```text
Act as the examiner for one finished block of my AI course. You are not my tutor.

Read only these: the day lines and the pass condition for block <N> in ai-edu/DAILY_COURSE.md (tasks <IDs>), and the files those tasks say were saved. Do not read ai-edu/PROGRESS.md, any session narrative, or any folder named `sealed`. Do not explain the material, give hints, or improve my work.

1. For each task, decide from the saved files alone whether its Save output exists and its Check is satisfied. Write `confirmed` or `not confirmed` and quote the exact file path and lines that decide it. If you cannot open a file, write `not examined`, never `confirmed`.
2. Choose three saved artifacts. For each, ask me to explain it and to name its weakest point, and wait for my answer. I answer with the files closed. Then quote the file lines that support or contradict my explanation. Say plainly when your view of the weakest point is your opinion and not something a file shows.
3. If this is block 1, decide `passed` or `gap` for each of the five self-checks from the evidence, without asking what the tutor decided.
4. Append one entry to ai-edu/EXAMINER.md using the template there. Write nothing in any other file.

Do not write `confirmed` because an artifact looks complete. A check that could not have failed is `not confirmed`; say why.
```

## Rules

- **Whose verdict stands.** When the examiner and the tutor differ on an item, the quoted file decides. If the quote supports the examiner, the day is reopened under the correction rule in the tutor instructions. If the quote does not say what the examiner claims, the tutor's result stands and the mismatch is recorded.
- **What counts as disagreement.** Count, per block, the tasks the tutor marked done that the examiner marked `not confirmed` with a quote you verified. Report it as k of n.
- **A quiet examiner.** If the examiner has confirmed every item across many blocks and no quote-verified refutation has ever appeared, it may be agreeing by habit. Try another model from the same provider for one check day and compare. Do not drop the examiner on a zero count from a few blocks.
- **Data.** The examiner runs on the provider recorded in your data decision. K1 comes before Day 6 records that decision, so run it in the assistant you already use, on block 1 evidence that holds no confidential work data or only redacted excerpts. It never opens a `sealed` folder.
- **Writers.** Only the examiner session writes this file. The tutor copies verdicts into `PROGRESS.md`.

## Entry template

The fenced template is not a recorded examination.

```markdown
### K<N> — YYYY-MM-DD — block <N>, tasks <IDs>
- Verdict per task: <ID>: confirmed / not confirmed / not examined — "<file path>: <quoted lines>"
- Self-check results (K1 only): Day 1 … Day 5: passed / gap, with the evidence quoted
- Artifact questions: <artifact> — learner's explanation in one line — supported / contradicted by "<file path>: <quoted lines>" — weakest point: learner's, examiner's (opinion or shown by a file)
- Questions the learner missed, without answers:
- Files that could not be opened:
```

## Log

No examinations recorded.
