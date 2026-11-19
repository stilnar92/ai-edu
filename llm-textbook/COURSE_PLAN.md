# Course plan — Deep Dive into LLMs like ChatGPT

Resume at: **How BPE builds the vocabulary**.

Source line ranges are approximate editorial study ranges, not original chapter boundaries or timestamps. BPE intentionally shares the tokenization source range. All transcript lines are accessible; mapping is not proof of mastery.

## Interface

All lessons and interactive exercises run inside Codex. Save supporting notes and progress in this folder. Do not create or launch a separate website. Prepare materials just in time.

## Teaching agreement

Follow the original user prompt: short explanation and analogy → Socratic questions → short exercise → ask whether to continue or clarify. If unclear, rephrase and provide hints. Each major section ends with a review. Finish with an integrative challenge, reflection and a practical application.

Create materials just in time. Preserve questions and progress. Do not equate yes/no answers with comprehensive mastery. Do not silently skip source topics. A detour does not advance the source position.

## Source-linked syllabus

### 1. Preparing the training data — Discussed
Source: lines 1–200 in source/transcript.txt.
Crawling, extraction, language filtering, duplicates, personal information.
Evidence / gap: You explained why Spanish exposure matters and distinguished copied reports from independent evidence.

### 2. Text, tokens and vocabulary — Practiced
Source: lines 201–395 in source/transcript.txt.
Bits, bytes, vocabulary size, token IDs, encoding and decoding.
Evidence / gap: You identified reusable pieces and understood that IDs are labels. Byte-level trade-offs need review.

### 3. How BPE builds the vocabulary — Resume here
Source: lines 201–395 in source/transcript.txt.
Frequent adjacent pairs, merges, sequence length versus vocabulary size.
Evidence / gap: Named earlier, but never demonstrated. This is our earliest substantive gap.

### 4. Learning the next token — Discussed
Source: lines 396–555 in source/transcript.txt.
Context windows, target tokens, probability distributions, loss, batches and updates.
Evidence / gap: You understood which target probability to increase. Batch training still needs coverage.

### 5. Inside the neural network — Needs clarification
Source: lines 556–681 in source/transcript.txt.
Parameters, embeddings, Transformer blocks, intermediate activations.
Evidence / gap: You asked what parameters are. The numerical example has not yet been checked.

### 6. Generating one token at a time — Practiced
Source: lines 682–850 in source/transcript.txt.
Sampling, repeated inference, growing context. Temperature is a course supplement.
Evidence / gap: You distinguished changing context from changing parameters and understood random sampling.

### 7. Training at scale — Planned
Source: lines 851–1180 in source/transcript.txt.
Training demonstrations, compute, GPUs, model development and scale.
Evidence / gap: Not taught in our conversation.

### 8. What a base model learns — Partial
Source: lines 1181–1587 in source/transcript.txt.
Knowledge in parameters, memorization, continuation, prompting and in-context examples.
Evidence / gap: We covered continuation versus assistant behavior, but not all base-model examples.

### 9. Conversation format — Partial
Source: lines 1588–1850 in source/transcript.txt.
Post-training, role boundaries, special tokens and assistant turns.
Evidence / gap: We introduced SFT but skipped the conversation serialization details.

### 10. Creating assistant examples — Partial
Source: lines 1851–2151 in source/transcript.txt.
Human labelers, instructions, synthetic data and supervised fine-tuning.
Evidence / gap: You correctly identified SFT from a supplied answer. Data curation remains.

### 11. Plausibility and hallucinations — Practiced
Source: lines 2152–2463 in source/transcript.txt.
Unsupported facts, uncertainty, and training assistants to acknowledge limits.
Evidence / gap: You chose reliable evidence over confident wording.

### 12. Tools and working memory — Practiced
Source: lines 2464–2725 in source/transcript.txt.
Search results, tool calls, context versus parameter knowledge.
Evidence / gap: You explained tool results enter context and tool selection can fail.

### 13. What a model says about itself — Planned
Source: lines 2726–2865 in source/transcript.txt.
Knowledge cutoffs, self-description, training examples and system instructions.
Evidence / gap: Not covered.

### 14. Computation and intermediate steps — Practiced
Source: lines 2866–3273 in source/transcript.txt.
Finite computation per token, scratch work, arithmetic and tools.
Evidence / gap: You derived 3 × 4 = 12 and understood that intermediate text grows the context.

### 15. Uneven capabilities — Partial
Source: lines 3274–3515 in source/transcript.txt.
Tokenization-related difficulties, spelling, comparisons and practical limitations.
Evidence / gap: We discussed letter counting and prose versus arithmetic; remaining examples need review.

### 16. Learning through practice — Partial
Source: lines 3516–3980 in source/transcript.txt.
SFT versus reinforcement learning, attempts, evaluation and parameter updates.
Evidence / gap: You distinguished reward-based training from feedback used only in context.

### 17. Reasoning models and distillation — Planned
Source: lines 3981–4340 in source/transcript.txt.
Learned problem-solving strategies, reasoning demonstrations and distillation.
Evidence / gap: Only introduced; not taught systematically.

### 18. Beyond supplied demonstrations — Planned
Source: lines 4341–4580 in source/transcript.txt.
AlphaGo analogy, exploration and discovering new strategies.
Evidence / gap: Not covered.

### 19. Human preferences and reward models — Planned
Source: lines 4581–5079 in source/transcript.txt.
Subjective tasks, preference comparisons, reward models, reward exploitation.
Evidence / gap: Reward hacking was introduced, but not practiced. RLHF is a form of RL; the video uses a narrower rhetorical distinction.

### 20. Review the training pipeline — Planned
Source: lines 5080–5169 in source/transcript.txt.
Pretraining → SFT → RL, and persistent capability limitations.
Evidence / gap: Section review still required.

### 21. Beyond text — Planned
Source: lines 5170–5230 in source/transcript.txt.
Representations for images, audio and multimodal interaction.
Evidence / gap: Not covered.

### 22. Agents and future directions — Planned
Source: lines 5231–5330 in source/transcript.txt.
Long-running tasks, computer use, context limits and test-time learning ideas.
Evidence / gap: Not covered. Predictions must be labeled as the speaker’s historical outlook.

### 23. Finding and running models — Planned
Source: lines 5331–5520 in source/transcript.txt.
Leaderboards, providers, open weights, local execution, distillation and precision.
Evidence / gap: Not covered. Product names and rankings are historical examples, not current recommendations.

### 24. Synthesis and final challenge — Planned
Source: lines 5521–5761 in source/transcript.txt.
Explain the whole pipeline, evaluate a response and propose a practical assistant.
Evidence / gap: Final challenge and reflection remain.

## Section reviews

- After data + tokenization: explain filtering, run a merge, distinguish tokens from words.
- After pretraining + inference: trace a prediction, distinguish IDs/parameters/context, explain sampling.
- After assistant behavior: compare base/SFT, inspect conversation roles, assess hallucinated evidence.
- After RL: compare demonstrations, reward updates and context feedback; design and critique a reward.
- Final challenge: design a document assistant, trace tokens/tools/context, define evaluation, failure handling and a small real-world project.

## Running practical example

Use `mini-model/README.md` as the incremental project plan. The 50-word corpus is the shared concrete example for tokenizer → encoding → training pairs → tiny prediction model → generation. Only prepare later stages when reached; preserve the video syllabus and prior learning evidence.
