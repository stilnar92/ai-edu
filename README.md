# AI — practical agents, software development, and LLM engineering

A practical learning path built from the `🤖 AI` bookmarks. Since the 18 November 2026 restructure it has one core goal and four supporting ones.

**Core goal — build and operate AI solutions for real work:** choose and map a business process, build an evaluated AI feature around it, run it with limits, traces, recovery and human approval, build a personal AI assistant, and finally deliver a prototype for a process that belongs to someone else. These are the skills of an AI engineer, an AI solutions architect, and a forward deployed engineer.

**Supporting goals, as elective tracks:**

1. **Use agents for everyday work:** delegate research, documents, app interactions, and bounded background tasks.
2. **Develop software with AI:** direct coding agents, specify changes, debug, test, and review.
3. **Understand LLMs:** implement a small model, study adaptation, and read research critically.
4. **Go deeper after the core:** compare a framework, run a multi-agent experiment, or fine-tune a model.

## About this copy

This is the public copy of a personal self-study course. Some files of the working copy are left out:

- the survey PDF and the video transcript, which belong to their authors (see [resources](resources/README.md) and [llm-textbook/source](llm-textbook/source/README.md) for how to add them);
- the author's own bookmark snapshots (`BOOKMARK_REVIEW.md`, `links.txt`), learning records, and the `.archive/` folder of earlier versions. Where a course file mentions them, they are simply not here.

Progress files are in their starting state, so you can use the course as it is.

## How to follow this course

- For AI-guided study with saved progress, use the [study prompt embedded in the course](DAILY_COURSE.md#ai-tutor-prompt-and-instructions) and [progress log](PROGRESS.md). The assistant resumes unfinished work and records session results across chats.
- For a daily schedule, follow the [step-by-step weekday course](DAILY_COURSE.md): one hour per weekday, 16 core study blocks (about 17 weeks with the design drills, before method days), linked resources, daily exercises, and completion checks. Numbered days are task milestones; unfinished work extends the calendar. The [visual roadmap](ROADMAP.html) maps the specialization as skill areas and shows where the course teaches each one.
- **Week 1 is an entry self-check.** Five real tasks test whether you can already delegate with evidence, describe your assistant's capabilities and boundaries, direct a coding agent, verify a fix, and explain how LLMs behave. A gap adds only the mapped remedial tasks from tracks P and A.
- **Weeks 2–9 are Project B** (modules 4–7 below, compressed and applied to a real process from your work). **Weeks 10–13 are Project D**, the personal AI assistant. **Weeks 14–16 are Project E**, delivery for another person's process, with five design drills taken any time after week 9.
- [Agent Harness Engineering: A Survey](resources/agent-harness-engineering-survey.pdf) is assigned reading in the core route: 19 short excerpts, each tied to the day that applies it.
- Tracks P and A (modules 0–3 and the [operator labs](AGENT_OPERATOR.md)) and track C (module 9) are electives. Modules 8 and 10 are optional extensions. Module 11 is ongoing reading.
- The modules below are a **reference outline by topic**, not the study order. The daily course sets the order and is the progress record.
- Each module has required work, optional resources, a practice task, and an observable completion criterion. Check a box only after doing the work.
- Use one main resource per topic. Consult overlapping courses to resolve gaps instead of watching everything twice.
- Hours below are planning estimates including practice, assuming basic programming, Git, and testing experience. They exclude optional readings and branches. Allow extra time for unfamiliar Python or mathematics.
- Keep a runnable checkpoint after each project milestone. Use a small fixture or the last checkpoint if unfinished work blocks the next exercise.
- Use the documentation matching your installed versions. Older tutorials remain useful for concepts but may need updated code.

## How this course teaches

A coding agent can produce every file this course asks you to save, so the course is built to keep the thinking with you.

- **You draft first.** Each day names what you write by hand before any AI version exists, what the agent may build, and the check that decides the day.
- **You predict before you run.** A prediction has to name the result that would prove it wrong.
- **You read outputs before writing rubrics**, and you score them yourself. Numbers are reported as k of n.
- **A separate examiner checks each block** from the files alone and must quote them. You also try to break your own tests, and redo anything that was done for you.
- **The course changes from evidence.** Defects are logged the day they are noticed; at most one edit is decided per check day, and difficulty alone is never a reason to make a task easier.

This method is on trial for the first three blocks and is extended stage by stage; see [How you learn in this course](DAILY_COURSE.md#how-you-learn-in-this-course) and the [method rollout](DAILY_COURSE.md#method-rollout).

**What this course is not.** It is a syllabus assembled with AI and checked for consistency, not material a teacher has refined over several cohorts. No lesson in it has been run yet. The examiner is the same model family as the tutor, and no rule here can be enforced mechanically. The method above reduces those weaknesses and does not remove them. A human reviewer at the project milestones would be worth more than any of it.

### How other courses compare

Checked on their public pages on 18 November 2026. None is required.

| Course | What it does that this one does not | How to use it here |
| --- | --- | --- |
| [AI Evals for Engineers & PMs](https://maven.com/parlance-labs/evals) (Hamel Husain and Shreya Shankar; paid cohort) | Live sessions, a 200-page reader, office hours, and a full sequence from error analysis to evaluators, CI and cost | The source of this course's outputs-first order. The free [evals FAQ](https://hamel.dev/blog/posts/evals-faq/) is the assigned reading |
| [Agentic AI](https://www.deeplearning.ai/courses/agentic-ai/) (DeepLearning.AI; videos free to audit, quizzes and graded labs paid) | Authored lectures; the reflection and planning patterns, which the core route does not build | Optional viewing beside core weeks 5–6; module 4 on error analysis beside weeks 2–3 |
| [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) (free) | A final assignment ranked on a benchmark leaderboard, which is a check from outside | Optional after Part B, as an outside score |
| [Berkeley Agentic AI MOOC](https://rdi.berkeley.edu/agentic-ai/f25) (free) | Research lectures by people building these systems | Optional viewing |

## Practical projects

### Project B — Build an evaluated AI feature on a real process · core, weeks 2–9

Choose one real, repetitive process from your own work. The default is triage of real tickets from your work tracker: given a ticket and a small set of project documents, the feature produces a structured summary, suggests a category, cites relevant documentation, and asks for missing information.

Before building, map the process step by step, decide which steps stay human, which become “AI drafts, a human approves”, and which are automated, and measure the current time per item. Start with a model call. Add retrieval and read-only tools. Add an agent loop only for tasks that need dynamic tool selection; compare it against a fixed workflow. Add one reversible action that runs only after your approval. Run the system beside real work in shadow mode, then report its value in measured time, quality, and cost.

Check your employer's data policy before any work data goes to a model provider; a redacted export or public issues are the fallback. TypeScript or Python is fine. Keep the language you already know.

### Project D — Build a personal AI assistant · core, weeks 10–13

An assistant over your own tasks and notes with four parts:

1. **A read path** to your real task manager and notes through an existing connector, an API, or an export.
2. **A recurring brief** in which every item traces to a real task or note.
3. **Memory you control:** stored where you can open it, every entry with a source and date, written only after your approval, and removable.
4. **Approval-controlled actions:** two reversible actions, each proposed with a preview and executed only after your approval, with an audit log.

It reuses the Project B code for model calls, evaluation, tools, limits, traces, and the approval gate. It ends with a live week of real use and a report of what it cost and what it saved.

### Project E — Deliver for someone else's process · core, weeks 14–16

Projects B and D are your own processes. Project E is someone else's: a colleague or another volunteer who does a repetitive process you do not do yourself and can give about two hours across three weeks.

1. **Discover:** interview the owner about the last real time the process ran, watch it once, write the map in their words, compare three options (no AI, a fixed workflow, an agent), and get a written yes to a one-page proposal.
2. **Build fast inside their constraints:** their tools, their access rules, their data agreement; a low-code tool where it is the faster fit; a demo to the owner mid-week; corrections applied or declined in writing.
3. **Hand over:** a runbook they can follow without you, a requirements and risk page, a rollout plan with build-or-buy numbers, a check on whether they actually use it, and a one-page status report.

Five design drills (S01–S05) are taken any time after week 9 and are required for the Part E milestone: four short cases outside your own domain and one review of a design you did not write. If no real owner is available the tutor plays one, and the result is recorded as simulated.

### Project P — Delegate a real noncoding workflow · elective

Use an existing assistant to turn a small set of documents and public sources into a verified brief, an editable table, and a draft visual artifact. Then test a bounded update workflow. See [the five operator labs](AGENT_OPERATOR.md).

### Project A — Ship ordinary software with AI · elective

Choose an existing repository you understand. If you need a new project, build a small issue tracker with issue creation, filters, status changes, and persistence. It needs no AI features.

Deliver three changes: a small feature, a reproduced bug fix, and a larger feature specified before implementation. Use a coding agent, but own the requirements, verification, and acceptance decision. Record agent mistakes, review time, and rework rather than counting generated lines of code.

## Core reading: Agent Harness Engineering

The learner-supplied [Agent Harness Engineering: A Survey](resources/agent-harness-engineering-survey.pdf) (71 pages) is assigned reading in the core route. It organizes the infrastructure around an agent into seven layers: execution, tooling, context, lifecycle, observability, verification, and governance. The course assigns 19 excerpts of 10–15 minutes each, on the day whose exercise applies them; see the [reading map](DAILY_COURSE.md#agent-harness-engineering-survey-reading-map). Treat it as the authors' organizing framework and a dated ecosystem snapshot, not as a required architecture.

## Where the two added courses fit

[Daniel Moka — AI Agent Engineer](https://aiagentengineer.dev/) ([your CourseHunter link](https://coursehunter.net/course/inzhener-ii-agentov)) supplies selected lessons on fundamentals, harnesses, verification, review, memory, MCP, and loops. Its public syllabus lists 55 lessons and 27 tasks; video duration alone is not a practice estimate. The lessons are in English. The author demonstrates specific tools, so adapt exercises to your environment. Access to this course is optional: the other required resources and practice tasks provide a route through the curriculum.

[mlabonne/llm-course](https://github.com/mlabonne/llm-course) is a reference map used throughout: Engineer sections alongside application work, Fundamentals before model implementation, and Scientist sections for optional adaptation. Do not treat every resource linked from the repository as required homework.

## Module 0 — A working mental model of LLMs · 6–8 hours

- [ ] Watch [Karpathy: Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI).
- [ ] Read [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).
- [ ] Explain tokens, context windows, pretraining, fine-tuning, reasoning models, hallucinations, and context degradation in your own words.

**Course companion:** Moka modules 0–1; skim repeated material.

**Practice:** Give a model the same repository question with missing, relevant, and distracting context. Record the answers and their unsupported claims.

**Complete when:** You can explain why a fluent answer can be wrong and distinguish missing context from a task the model cannot reliably perform.

## Track P — Operate AI assistants

[Open the operator track](AGENT_OPERATOR.md): five labs on delegation, skills and connected tools, isolated workspaces, computer use, and background automation. Estimated effort: **24–38 hours**, independent of the coding tracks. In the daily course this is an elective track (P01–P30); Days 1–2 of the entry self-check decide whether any of it is assigned.

This track promotes relevant tools into practical exercises.

## Track A — Develop software with AI

### Module 1 — Direct a coding agent · 8–12 hours

- [ ] Learn [explore → plan → code → commit](https://github.com/mokevnin/agentic-coding-design-patterns/blob/main/book/ru/explore-plan-code-commit.md) (RU).
- [ ] Read the relevant [Claude Code best practices](https://code.claude.com/docs/en/best-practices); apply the principles to your chosen coding agent.
- [ ] Create concise repository instructions covering commands, boundaries, and verification.
- [ ] Implement the first small feature in Project A and inspect the diff yourself.

**Course companion:** Moka module 2 — Harness Engineering. Start with instructions and tools; defer elaborate skill collections and subagents.

**Practice:** Ask the agent to locate relevant code and explain its plan before implementing the feature. Give it explicit acceptance criteria. Restart the session and check whether the repository instructions provide sufficient context.

**Complete when:** The feature works, you understand the changes, and a fresh session can run the relevant checks without repeated setup explanations.

### Module 2 — Specify changes and control scope · 8–12 hours

- [ ] Write a short specification: problem, observable behavior, examples, non-goals, and acceptance criteria.
- [ ] Use [OpenSpec](https://openspec.dev/) for one feature. Learn the specification discipline without making the tool mandatory for every change.
- [ ] Challenge the plan before implementation: missing cases, unnecessary abstractions, and affected interfaces.
- [ ] Implement the larger Project A feature using the specification and actual repository context.

**Optional:** [modularity](https://github.com/vladikk/modularity) for design boundaries; Moka module 4's plan-review material.

**Practice:** Include an ambiguous requirement, resolve it before coding, and verify that the final change stays within the agreed scope. Update the specification if an implementation discovery legitimately changes the requirement.

**Complete when:** Each acceptance criterion has evidence and unrelated changes have been removed. A specification supplements code context; it does not replace it.

### Module 3 — Debug, verify, and review AI-written code · 12–18 hours

- [ ] Reproduce a Project A bug before asking the agent to fix it.
- [ ] Add a regression test that fails for the original defect and passes after the fix.
- [ ] Review the diff for behavior, scope, maintainability, and security-relevant changes.
- [ ] Challenge one important test with a deliberate mutation. Use property-based or end-to-end testing where it adds evidence.
- [ ] Add one deterministic hook or CI check that prevents a demonstrated recurring mistake.

**Course companion:** Moka modules 3–4 — Verification and Review.

**Supporting resources:** [reslop](https://github.com/tshemsedinov/reslop), [Hook-driven dev workflows](https://nick-tune.me/blog/2026-02-28-hook-driven-dev-workflows-with-claude-code/), and the [community best-practice collection](https://github.com/shanraisshan/claude-code-best-practice). Use these selectively; automated review is additional evidence, not the acceptance decision.

**Practice:** Produce a reviewable change with the issue, reproduction, relevant diff, verification results, and remaining uncertainty. Compare your effort across the three Project A changes.

**Complete when:** You can demonstrate that a meaningful defect is detected and explain what passing tests do not prove.

**Track A checkpoint:** You can deliver and verify ordinary software changes with AI. You can stop here and apply these skills without learning an AI application SDK.

## Track B — Build AI-powered software

### Module 4 — Model APIs and evaluations before frameworks · 10–16 hours

- [ ] Use one provider's client SDK to send a request and inspect its response, usage, and errors. For example, start from the [Anthropic client SDK documentation](https://platform.claude.com/docs/en/cli-sdks-libraries/overview).
- [ ] Implement Project B as a simple request-to-response function with validated structured output.
- [ ] Read [Hamel's LLM evals FAQ](https://hamel.dev/blog/posts/evals-faq/) and relevant sections of [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).
- [ ] Create ten initial model-quality cases before tuning the prompt, including ambiguity and missing information. Keep malformed-input and provider-failure software tests in a separate set.
- [ ] Record output quality, latency, and token or monetary cost with model and prompt versions.

**Course map:** mlabonne, LLM Engineer → Running LLMs. Consult provider documentation for current API behavior.

**Practice:** Classify sample issues and produce summaries with a fixed scoring rubric. Improve the prompt against development cases while reserving a few unseen cases for evaluation.

**Complete when:** A repeatable evaluation distinguishes improvement from a response that merely sounds better. Keep deterministic software tests separate from model-output evaluations.

### Module 5 — Retrieval, context, and memory · 12–18 hours

- [ ] Study mlabonne, LLM Engineer → Building a Vector Storage and Retrieval Augmented Generation.
- [ ] Add a small documentation collection to Project B. Compare a simple keyword-search baseline with embedding retrieval.
- [ ] Return source references and explicitly acknowledge missing evidence.
- [ ] Distinguish retrieved knowledge, conversation history, and durable project decisions.
- [ ] Evaluate retrieval separately from answer quality; include changed or deleted documents.

**Course companion:** Moka module 5 — Memory Engineering. **Optional:** selected RAG and memory lessons from [Stepik: AI agents — engineering and algorithms](https://stepik.org/course/259791/promo) (RU).

**Practice:** Diagnose a wrong answer: was the needed document missing, retrieved incorrectly, or ignored during generation? Fix the responsible stage and rerun the same cases.

**Complete when:** You can show whether retrieval improves the baseline, explain failures, and update the knowledge collection without retaining stale answers as facts.

### Module 6 — Tool calling, bounded agents, and MCP · 12–18 hours

- [ ] Read [Building effective agents](https://www.anthropic.com/research/building-effective-agents), distinguishing fixed workflows from model-directed tool use.
- [ ] Read [Writing effective tools for agents](https://www.anthropic.com/research/writing-tools-for-agents) and [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).
- [ ] Implement a small explicit loop: call the model → validate a requested tool → execute → return the result → stop or repeat within a limit.
- [ ] Start with two read-only tools: search documentation and retrieve an issue. Set tool permissions and step, time, and cost limits.
- [ ] Follow [MCP: build a server](https://modelcontextprotocol.io/docs/develop/build-server) to expose one existing capability through MCP.

**Course companion:** Moka module 6 — MCP, plus module 7's prompt-injection material.

**Practice:** Compare a fixed retrieval workflow with agent-directed tool selection. Test invalid arguments, unavailable tools, an unanswerable request, and malicious instructions inside a document. Verify that retrieved text cannot authorize an action.

**Complete when:** You can trace every tool call, demonstrate that limits are enforced, and explain whether your task benefits from an agent. MCP is an integration interface, not a requirement for every tool or agent.

### Optional lab — Choose a framework for a demonstrated need · 4–8 hours

This is a comparison exercise, not a requirement to master every framework.

| Need | Candidate | Exercise |
| --- | --- | --- |
| Interactive TypeScript AI feature | [Vercel AI SDK tutorial](https://www.aihero.dev/vercel-ai-sdk-tutorial) and [current documentation](https://ai-sdk.dev/docs/introduction) | Rebuild one existing feature; compare streaming, validation, tool handling, and integration effort |
| Coding automation with an existing agent runtime | [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) | Run a bounded repository task with explicit permissions |
| Explicit state and resumable workflows | [LangGraph](https://docs.langchain.com/oss/javascript/langgraph/overview) | Interrupt and resume a small workflow |
| A broader TypeScript agent framework | [Mastra](https://mastra.ai/docs) | Implement the same small task and inspect its trace |

- [ ] Choose at most one candidate and compare it with your baseline.
- [ ] Record what it simplifies, what it hides, and what dependency it introduces.

**Complete when:** You can justify adopting or rejecting it. Vercel AI SDK is optional, belongs in the application track, and is not needed to use coding agents effectively. Do not port the entire project just to finish a tutorial.

### Module 7 — Reliable workflows and deployment · 12–20 hours

- [ ] Read [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents).
- [ ] Study mlabonne, LLM Engineer → Deploying LLMs and Securing LLMs, selecting material relevant to your deployment.
- [ ] Add traces, timeouts, bounded retries, persisted progress, and protection against duplicate actions.
- [ ] Deploy Project B in a controlled environment and make failures visible.
- [ ] Expand the evaluation set with failures observed during development. Reserve unseen cases and repeat variable runs.

**Course companion:** Moka modules 7–9. Treat the always-on AI employee as an optional extension. **Optional reading:** [Building effective agent automations](https://claude.dev/blog/building-effective-agent-automations/).

**Practice:** Process a batch of sample issues, interrupt execution, and resume. Keep proposed external changes as drafts until approved. Compare quality, latency, and cost for two configurations.

**Complete when:** A failed run is diagnosable, completed work is not accidentally repeated, and the system stops within its limits. Deploying an application around a hosted model is sufficient; self-hosting model weights is optional.

**Track B checkpoint:** You can build, measure, and operate an AI feature and explain whether it needs retrieval, tools, an agent, or a simpler workflow.

**In the daily course**, modules 4–7 run as core weeks 2–9 on a real process, with three additions that the module outlines above do not list: a process map with a measured baseline (Days 6–7), one approval-controlled action (Days 34–35), and a shadow run with a value report (Days 37–43).

### Module 8 — Multi-agent orchestration experiment · optional, 8–14 hours

- [ ] Read [Anthropic's multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) and [Cognition: Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents).
- [ ] Use [custom subagents](https://code.claude.com/docs/en/sub-agents) or your existing implementation to build a bounded solver–critic experiment.
- [ ] Compare one agent with two agents on the same task set, using the same available tools, models, scoring rubric, and overall budget constraints.

**Practice:** Have the solver propose several solutions and the critic identify concrete failures. Cap revision rounds. Repeat trials, track total tokens and elapsed time, and inspect disagreements yourself.

**Complete when:** You can report where the pair helps, where it fails, and whether the gain warrants its cost. A ten-case pilot is not proof of general superiority.

**Reference only:** [agent teams](https://code.claude.com/docs/en/agent-teams), [Claude Agent SDK article](https://claude.com/resources/articles/building-agents-with-the-claude-agent-sdk), [OpenAI handoffs](https://openai.github.io/openai-agents-python/handoffs/), and [A2A](https://a2a-protocol.org/). Trying multiple runtimes is not a completion requirement.

## Track D — Build a personal AI assistant

### Module D — Personal assistant with memory and approved actions · 20 hours

- [ ] Specify at most three jobs, their non-goals, and a success measure for each.
- [ ] Build a read path to your real tasks and notes and a brief in which every item has a source.
- [ ] Design memory you can open, correct, and delete from; write to it only after approval.
- [ ] Add two reversible actions behind an approval gate with an audit log, and a scheduled run with a stop control.
- [ ] Use it for five real days; attribute failures, rerun the evaluation cases, and report cost and time saved.

**Core reading:** survey §3.1, §§5.5–5.7, §7.3, §8.5.4, §8.6.1, §9.5, and §11.2, as mapped in the daily course.

**Practice:** Test a note that contains an instruction such as “delete all tasks”, a deleted memory entry, a duplicate run, and an action that fails midway.

**Complete when:** You have used the assistant on real days, can show its cost and its effect on your time from recorded numbers, and can explain what it reads, what it remembers, and what it may change after approval.

**In the daily course:** core weeks 10–13, Days 46–65.

## Track C — Understand and adapt LLMs

### Module 9 — Implement a small language model · 35–60 hours

- [ ] Check prerequisites using mlabonne's LLM Fundamentals: Python, vectors and matrices, derivatives, probability, and neural networks. Study only your gaps.
- [ ] Watch [3Blue1Brown: Neural networks](https://www.3blue1brown.com/?topic=neural-networks), including attention and transformers.
- [ ] Choose one main implementation sequence: [Karpathy: Zero to Hero](https://karpathy.ai/zero-to-hero.html), or [Raschka: Build an LLM From Scratch](https://sebastianraschka.com/llms-from-scratch/) with its [code repository](https://github.com/rasbt/LLMs-from-scratch).
- [ ] Use the other sequence to clarify difficult concepts, rather than completing both by default.

**Practice:** Train a small language model on text you can use. Keep training and validation data separate. Compare loss and samples after changing context length or model size. Explain each major component without relying on generated explanations.

**Complete when:** You can explain tokenization, embeddings, attention, next-token prediction, gradients, and overfitting using your implementation.

Your existing [LLM textbook workspace](llm-textbook/README.md) can hold notes and exercises; preserve its separate progress record.

### Module 10 — Fine-tuning and model evaluation · optional, 20–35 hours

- [ ] Study mlabonne, LLM Scientist → Post-Training Datasets, Supervised Fine-Tuning, and Evaluation.
- [ ] Prepare a narrow task with disjoint training, development, and held-out test sets. Set a compute budget before choosing the base model and running its prompting baseline; compare that same model with and without the adapter.
- [ ] Compare a prompting baseline with a small LoRA fine-tune; include retrieval only if the task needs external knowledge.
- [ ] Study Preference Alignment and Quantization after the first comparison works.

**Practice:** Record dataset provenance, model settings, cost, and held-out performance. Inspect regressions as well as improvements. If compute is unavailable, complete dataset design and baseline evaluation, and mark the training experiment unfinished.

**Complete when:** You can justify whether changing the model improves the task enough to warrant the added maintenance and compute.

### Module 11 — Read research critically · ongoing

- [ ] After module 6: [Chain-of-Thought](https://arxiv.org/abs/2201.11903) and [ReAct](https://arxiv.org/abs/2210.03629).
- [ ] After module 9: [InstructGPT](https://arxiv.org/abs/2203.02155) and [Chinchilla](https://arxiv.org/abs/2203.15556).
- [ ] Alongside module 10: [DPO](https://arxiv.org/abs/2305.18290) and [DeepSeek-R1](https://arxiv.org/abs/2501.12948).
- [ ] Use [30papers.com](https://30papers.com/) as an additional reading queue, not a prerequisite for application work.

**Practice:** For each paper, write the question, method, baseline, evidence, limitations, and one reproducible experiment. Separate the authors' measured result from your hypothesis about its usefulness.

**Complete each reading when:** You can explain what the paper establishes and what it does not. Aim for one manageable paper a week and an occasional small reproduction.

## Progress and workload

| Milestone | Modules | Daily-course budget | Status |
| --- | --- | --- | --- |
| Entry self-check | Five checks | 5 hours · week 1 | Core |
| AI feature on a real process (Project B) | 4–7 | 40 hours · weeks 2–9 | Core |
| Personal AI assistant (Project D) | D | 20 hours · weeks 10–13 | Core |
| Delivery for someone else's process (Project E) | Part E | 20 hours · weeks 14–16 and drills S01–S05 | Core |
| Practical assistant operation (Project P) | P1–P5 | 30 hours · P01–P30 | Elective or remedial |
| AI-assisted software development (Project A) | 0–3 | 45 hours · A01–A45 | Elective or remedial |
| LLM internals (Project C) | 9 | 60 hours · C01–C60 | Elective |
| Framework lab | One comparison | 5 hours · F01–F05 | Elective |
| Multi-agent experiment | 8 | 10 hours · M01–M10 | Elective |
| Model adaptation | 10 | 30 hours · T01–T30 | Elective |

The core route is budgeted at **85 hours**: at five hours per week, about **17 study weeks**, before method days (check days and lettered days), remedial tasks, and extra setup or recovery sessions. Modules 4–7 were estimated at 46–72 hours for a learner new to this work; the 40-hour budget assumes working programming experience and daily use of a coding agent, which the entry self-check tests. The shadow run in weeks 8–9 and the live week in week 13 also need calendar time that is not study time. The elective tracks total 180 hours and are entered only by choice or when the self-check assigns specific tasks.

When following the daily course, its task checkboxes and `PROGRESS.md` are the active progress records; the module checklists here are reference outlines, not a second independently maintained tracker.

For each completed module, keep a short record: artifact or commit, checks performed, one failure you diagnosed, and one remaining question. Course completion is demonstrated by working artifacts and explanations, not certificates or the number of tools installed.

**Optional revision:** [AI Cert Guides](https://aicertguides.com/) (formerly Claude Certification Guide) is a third-party resource, not the definition of this course's learning outcomes.

## Reference — not lessons, open when needed

**Frameworks and patterns**
[Redis Patterns for Coding Agents](https://redis.antirez.com/) ·
[Archiplan](https://github.com/archiplan-ai/Archiplan) ·
[mdtask](https://github.com/syabro/mdtask)

**Skill catalogs and skills**
[skills.sh](https://skills.sh/) ·
[SkillsMP](https://skillsmp.com/) ·
[chops.md](https://chops.md/) ·
[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) ·
[BuilderIO/skills](https://github.com/BuilderIO/skills) ·
[MengTo/Skills](https://github.com/MengTo/Skills) ·
[web-quality-skills](https://github.com/addyosmani/web-quality-skills) ·
[database-skills](https://database-skills.com/) ·
[android/skills](https://github.com/android/skills) ·
[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) ·
[project-skill-audit](https://github.com/Dimillian/Skills/blob/main/project-skill-audit%2FSKILL.md) ·
[Impeccable](https://impeccable.style/) ·
[agency-agents](https://github.com/msitarzewski/agency-agents) ·
[claude-co-commands](https://github.com/SnakeO/claude-co-commands) ·
[claude-octopus](https://github.com/nyldn/claude-octopus) ·
[shadcn/improve](https://github.com/shadcn/improve) ·
[papercuts](https://github.com/treygoff24/papercuts) ·
[aso-skills](https://github.com/appeeky/aso-skills) ·
[generate-bpmn-prompt](https://github.com/yksi12/prompts/blob/main/generate-bpmn-prompt.md) ·
[lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) ·
[awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) ·
[hand-drawn-canvas-animation](https://github.com/alesha-pro/tools/tree/main/skills/hand-drawn-canvas-animation)

**Agent runtimes and orchestration**
[Orca](https://orca.dev/) ·
[Paradev (formerly Superset)](https://paradev.com/) ·
[Herdr](https://herdr.dev/) ·
[Pi](https://pi.dev/) ·
[Tau](https://twotimespi.dev/) ·
[paperclip](https://github.com/paperclipai/paperclip) ·
[hermes-agent](https://github.com/nousresearch/hermes-agent) ·
[nanobot](https://github.com/HKUDS/nanobot) ·
[stagehand](https://github.com/browserbase/stagehand) ·
[dev3000](https://dev3000.ai/) ·
[rtk](https://github.com/rtk-ai/rtk) ·
[neurogate](https://github.com/basaltcode/neurogate)

**Search and file conversion**
[qmd](https://github.com/tobi/qmd) ·
[txtai](https://github.com/neuml/txtai) ·
[markitdown](https://github.com/microsoft/markitdown)
