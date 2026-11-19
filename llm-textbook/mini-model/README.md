# Our tiny language model

This is a learning project inside Codex, not a separate website. Prepare each stage when we reach it. Fifty words cannot produce a broadly capable assistant; this is a miniature laboratory for the same pipeline ideas.

## Dataset
`corpus.txt` has 10 separate samples, 50 word occurrences, and 36 distinct words. Lowercase English and repeated patterns are deliberate. Line breaks separate samples; they are not part of each sample. Spaces within sentences are preserved.

## Incremental plan
1. **Current — tokenizer:** train byte-level BPE; observe frequencies, merge rules and IDs.
2. Encode samples with the saved vocabulary; decode them exactly.
3. Create context/next-token training pairs and reserve evaluation examples.
4. Introduce a tiny prediction model, its parameters, loss and updates.
5. Train and visualize changes; compare training results with held-out results.
6. Sample continuations, adjust temperature, and inspect limitations.

Stages 2–6 are planned, not completed. Do not skip the foundations review or existing course gaps. This project supplies concrete examples alongside the video syllabus.

## Current files
- `tokenizer-lab.html`: interactive fragment rendered in Codex.
- `train_tokenizer.py`: executable tokenizer trainer; Python standard library only.
- `training-stages.json`: computed snapshots for the inline lesson.
- `tokenizer.json`: saved ordered merge rules and added vocabulary.

Run from the edu project root:

```sh
python3 ai-edu/llm-textbook/mini-model/train_tokenizer.py
```

The trainer starts with all 256 single-byte entries, using byte values as IDs, and adds 16 entries. It counts adjacent pairs within each sentence. Pairs can include spaces or cross word boundaries. It never joins separate samples. Ties use first encounter order; replacements are left-to-right and non-overlapping. Unlike many production tokenizers, this tiny implementation has no regex pre-tokenization or special conversation tokens.

Verified: 259 initial tokens become 184 after 16 merges; vocabulary grows from 256 to 272. Every stage decodes losslessly. Replaying saved rules reproduces the final encodings. IDs belong only to this tokenizer. This program does not train neural-network parameters.

The inline lab displays precomputed, executed training stages. If the corpus changes, rerun the trainer and regenerate the embedded data in the HTML before showing it again.

## First question
Why does the first added piece contain a space? Predict what the token and vocabulary counters will do after the first merge, then check.
