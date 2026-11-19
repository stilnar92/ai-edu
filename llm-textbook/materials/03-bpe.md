# Lesson 03 — How BPE builds a vocabulary

Source: transcript lines 201–395 (approximate study range).

## Starting point
You know tokens are reusable text pieces and IDs identify vocabulary entries. We have not practiced constructing that vocabulary. Resume here without resetting later chat progress.

## Objective
Explain how merging frequent adjacent pieces trades a larger vocabulary for a shorter token sequence. Distinguish tokenizer construction from model training.

## Explanation
Start with small pieces. Count pairs of neighboring pieces in a corpus. Merge a frequent pair into a new vocabulary entry. Replace its occurrences, count again, and repeat. Older pieces remain in the vocabulary so they can represent other text.

Analogy: a printer starts with letter stamps. A stamp for a frequent group of letters reduces the number of stamping operations, at the expense of a larger collection of stamps.

## Interactive experiment
Use the BPE experiment rendered inside the Codex chat. The corpus is `low`, `low`, `lower`, `lowest`.

- Initially: 17 character pieces and 7 distinct vocabulary entries.
- Merge `l` + `o`: 13 pieces and 8 vocabulary entries.
- Merge `lo` + `w`: 9 pieces and 9 vocabulary entries.

This is a character-based teaching simplification. Byte-level BPE starts with bytes. The workbench keeps word boundaries and breaks ties by first appearance; real tokenizers use their own preprocessing and learned merge rules. These are not production token IDs.

## Socratic questions
1. Why merge frequent pairs rather than arbitrary pairs?
2. Why retain the original small pieces?
3. Does building a vocabulary teach whether a claim is true?

## Exercise
Perform two merges and record both counters. Explain the trade-off in your own words. Predict what another merge would do before trying it.

## If unclear
Think of adding a keyboard shortcut: your list of shortcuts grows, but entering the same phrase takes fewer operations. Compare the counters one merge at a time. Ask the tutor to explain “vocabulary” or “sequence” separately if needed.

## Review
A token need not be a word. A token ID is a label. BPE constructs pieces. Model training adjusts parameters to predict tokens. Compression is not fact-checking.

## Readiness
Answer the tutor in the Codex chat. The tutor checks your explanation and updates PROGRESS.md after substantive progress. Say whether you want to continue or need clarification.

Next: foundations review, then unfinished pretraining details and parameters.

## Building a vocabulary from data

Run `python3 ai-edu/llm-textbook/materials/train_tiny_bpe.py` from the project root. This dependency-free example trains on three separate samples: cat, cat, car. It starts with 256 byte entries, merges c+a into ID 256, then ca+t into ID 257, and stops at 258 entries. The remaining car encodes as [256,114]. The IDs belong to this toy tokenizer, not cl100k_base. The inline build-vocabulary.html visual presents the executed results.
