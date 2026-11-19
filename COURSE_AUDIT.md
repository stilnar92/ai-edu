# Course audit

## Audit — 18 November 2026 (third): mistakes, links, and contradictions

A read-through of every live course file after the two revisions below. `.archive/`, `links.txt`, and `BOOKMARK_REVIEW.md` are dated snapshots and were not edited.

**Checked and found correct:** all local links and anchors; the survey's section and page references against the PDF (71 pages, main text ends on p. 51); task counts (80 core, 5 drills, 5 method days, 180 elective, 20 method lines, 19 core excerpts); hour totals (85 core, 180 elective, 24–38 for the operator labs); the Moka syllabus figures (55 lessons, 27 tasks) against its public page; the figures in the `llm-textbook` notes.

**Links.** 133 unique external URLs were requested; 126 returned the expected page.

| Link | Finding | Correction |
| --- | --- | --- |
| Claude Certification Guide | Redirects to a renamed site | Points to `aicertguides.com` |
| `Eronred/aso-skills` | Repository moved | Points to `appeeky/aso-skills` |
| Orca (`onorca.dev`) | Site moved | Points to `orca.dev` |
| Superset (`superset.sh`) | Product renamed | “Paradev (formerly Superset)”, `paradev.com`; also in `AGENT_OPERATOR.md` |
| MCP “Build a server” | Pinned to one dated documentation version | Unpinned URL, which redirects to the current version |
| `skillsmp.com` | 403 to automated requests; the site is up | Unchanged |

**Contradictions and mistakes corrected**

| File | Problem | Correction |
| --- | --- | --- |
| `DAILY_COURSE.md` | Tutor instructions still planned “5 minutes recall”, which the opening act replaced | Opening act, work, saving evidence |
| `DAILY_COURSE.md` | “Keep the first seven weeks read-only” against an action added in week 7 | Weeks 2–6 are read-only |
| `DAILY_COURSE.md`, `README.md` | 16 weeks in one place and 17 in another; method days not mentioned | 16 blocks, about 17 weeks with the drills, before method days |
| `DAILY_COURSE.md` | Check-day row opened the examiner before the closed-book answers | Row follows the order in K1–K3 |
| `DAILY_COURSE.md`, `PROGRESS.md` | The tutor-judged list was “for the examiner”, who may not read `PROGRESS.md` | The examiner re-marks every task from the files; the tutor copies the verdict |
| `DAILY_COURSE.md`, `PROGRESS.md` | Day 5 checks why more context can make an answer worse, but A01–A05 do not teach it | A06–A09 are added when that point is the gap |
| `DAILY_COURSE.md` | Drill wording and pass did not fit S05, which is a review | Four cases, plus a pass line for S05 |
| `DAILY_COURSE.md` | Reading map labelled §11.2 as Governance | Synthesis, marked as a re-read from Day 43 |
| `README.md` | Design drills “run alongside” weeks 14–16 | Any time after week 9, as in the daily course |
| `README.md` | Module 8 (multi-agent) sat under the Track D heading | Moved to the end of Track B |
| `README.md` | Milestone table named a module “E” that does not exist; shadow run placed in week 8 only | “Part E”; weeks 8–9 |
| `EXAMINER.md` | “Open a new chat in this repository” against `ai-edu/...` paths in the prompt | Open it in the same folder as the tutor chat |
| `ROADMAP.html` | Code comment said “13-week core” | “16-block core”; nothing visible changed, so the published page was not republished |
| `llm-textbook/README.md` | File list omitted two files that the plan uses | Added |

**Flagged and left unchanged**

- **Debatable claims stated as fact.** “The skills an AI engineer or AI solutions architect is hired for” and “model internals, which these roles are rarely hired for” are this course's view and cite no source. Track T requires track C, although a LoRA comparison does not strictly need a model built from scratch.
- **An ordering question in the method rollout.** The Day 28a judge may score the Day 41 repeats only after Day 41a, which comes after Day 41. Decide the order when that stage is written.
- **A data gap (corrected afterwards, same day).** The examiner runs on the provider recorded in the data decision, but K1 comes before Day 6 records one. A week 1 rule now covers it in the data rule and tutor instructions of `DAILY_COURSE.md` and in `EXAMINER.md`: use only tasks and a repository the assistant is already allowed to see, and keep confidential work data out of block 1 evidence or redact it.
- **Not re-verified.** The details of the Maven course, and the tool claims dated 6 November in `AGENT_OPERATOR.md`.
- **In the bookmark snapshot only.** `app.promptdrive.ai` reports a suspended service; `python.langchain.com` and one X handle redirect.

**Not verified.** As before, no lesson was run. Reachability of a link is not a check of its content.

## Revision — 18 November 2026 (second): Part E and the learning method

Made on branch `course-improvements`, after the restructure below was committed as `ff62db8`.

**Prompted by** a course author's criticism that an AI-assembled programme is a pile of topics and that agents should be a learner's hands and not their brain, and by a comparison with existing courses.

**What changed**

| Area | Change |
| --- | --- |
| Part E | New core part, weeks 14–16 (Days 66–80) and design drills S01–S05: discovery with a real process owner, a time-boxed prototype inside their constraints, handover and a check on real use. Added for solutions-architect and forward-deployed work, which the learner's own processes cannot train |
| Division of work | Method lines (**Yours first / Agent may / Check**) on Days 1–15; a draft-first rule that binds every session; a stuck exit that records `assisted` and requires a redo |
| Opening act | The undefined five-minute recall is replaced by one act per day type: a decision record rewritten from memory, a prediction that can fail, or a prediction per case |
| Evaluation order | Day 9a reads and annotates real outputs before any evaluation design; Day 11 writes the rubric from observed categories and seals three unseen cases; the learner scores by hand; Day 13a holds the single held-out run and a self-consistency check |
| Examination | A check day after each block (K1–K3 so far) with a fresh examiner session that quotes files, one mutation against the learner's own tests, and a stated rule for whose verdict stands; `EXAMINER.md` |
| Course improvement | A course defects log filled on the day a defect is noticed; at most one edit per check day for a day not yet started; difficulty protected |
| Calendar | The learner is in no hurry: mechanisms get their own days. “Week” now means a block, and the “five-task block” wording is removed |

**How the method was chosen.** Two rounds of independent proposals and adversarial review (the find-solution procedure). Round 1 produced eight proposals and none was rated strong; stacked, they would have taken 110–135 of 300 weekly minutes. Round 2 produced four budgeted proposals. The review rated a combination strong as a design to enter a trial, not as proven.

| Proposal | Verdict | Fate |
| --- | --- | --- |
| Ownership line on every day | viable | Backbone |
| Outputs-first evaluation with its own days | viable | Kept; the judge may not be used as a measurement until checked against hand labels per class |
| Separate examiner | examiner viable, separate builder session rejected | Examiner kept on check days; builder split dropped because a short brief leaves the design to the builder |
| Project D as a delayed test of Project B | viable | Closed-book days kept in narrowed form; its claim to audit the tutor dropped, because forgetting is not tutor error |
| By-hand spec days ahead of build runs | new in round 2 | Kept; first one is tried after K3 |
| Tutor-made defective artifacts to critique | viable in round 1 | Dropped: the learner would edit the tutor's design, and the answer key is unvalidated |
| Spaced-review question bank | weak | Dropped: the queue overflows; retrieval is done from decision records instead |
| Course edits from time overrun and hints | weak | Dropped: it would smooth the hardest tasks |
| Borrowed lecture spine with external quizzes | weak | Dropped as a requirement: the quizzes are paid; kept as optional companions |

**One deliberate difference from the review's final version.** It proposed an examiner day every two blocks. This course keeps one after every block, because calendar time is not a constraint and a shorter interval means a wrong pass cannot carry into a second block.

**Structural checks run:** 80 core tasks with consecutive IDs; five drills S01–S05; method days Day 9a, Day 13a, K1–K3; 20 method lines; every task has a **Save:** deliverable; all in-file anchors resolve; no “five-task” wording remains.

**Not verified.** Nothing has been run. The day-type budgets are plans. Whether the tutor follows the method rules, whether the examiner finds anything, and whether the draft-first rule survives a hard day are exactly what the trial in blocks 1–3 is for. Risks that remain: rule sprawl and ritual decay; an examiner that agrees by habit; check days that feel like no progress; small numbers of cases teaching false confidence; a longer route losing momentum.

## Revision — 18 November 2026: restructure around the core route

The audit below describes the course as it stood on 15 November 2026 (245 tasks: 200 core in the order P → A → B → C, plus 45 optional). That structure was replaced on 18 November 2026. Its task numbers, week numbers, and totals no longer match the current files; the previous versions are kept in `.archive/2026-11-18-before-restructure/`.

**Why:** the goal is to enter AI engineering and solutions architecture work early. In the old order the first model API call came in week 16 and the application track ended around month seven; 135 of the 200 core hours went to operating assistants and coding with agents, which the learner already does daily, and to model internals, which these roles are rarely hired for. The application project used sample data and had no action behind human approval and no measure of value.

**What changed:**

| Area | Before | After |
| --- | --- | --- |
| Core route | P → A → B → C, 200 tasks, 40 weeks | Part 0 → Part B → Part D, 65 tasks, 13 weeks |
| Tracks P and A | Core, 75 tasks | Elective, entered through a five-task self-check that assigns only mapped remedial tasks |
| Track C | Core, 60 tasks | Elective after the core |
| Part B | 65 tasks at beginner granularity on sample issues | 40 tasks on a real process: process map and baseline, one approval-controlled action, shadow run, value report, case study |
| Personal AI assistant | Described as not an assigned project | Project D, 20 core tasks: read path, brief, memory under user control, approved actions, scheduled run, live week |
| Survey | Optional companion, 12 mapped excerpts | Assigned core reading, 19 excerpts in **Read:** lines, plus 3 elective excerpts |
| Task IDs | Day 1–245 | Core Day 1–65; electives P01–P30, A01–A45, C01–C60, F01–F05, M01–M10, T01–T30 |
| Roadmap | Table only | Table plus `ROADMAP.html` |

**Carried over unchanged in substance:** the tutor protocol (evidence before completion, pending block checks, deferral, reconciliation), and the wording of all 180 elective tasks apart from their IDs and cross-references. The 15 November corrections that concerned those tasks still apply to them.

**Structural checks run on 18 November 2026:**

- 65 core tasks with consecutive IDs Day 1–65 in Monday–Friday order across 13 weeks.
- 180 elective tasks with consecutive IDs per track: P 30, A 45, C 60, F 5, M 10, T 30, in 36 blocks.
- All 245 checkboxes unchecked; every task has a **Save:** deliverable; every week and block has a pass condition.
- No remaining references to old day numbers, old week numbers, or the old survey anchor; both in-file anchors resolve; Markdown fences are balanced.
- Every survey section and page range in the reading map was checked against the PDF's section headings.

**Not verified:** this was a document restructure, not execution of lessons. No lesson was run or marked complete. The 40-hour budget for Part B and the 20-hour budget for Part D are untested estimates, the self-check thresholds are a judgment by the tutor from evidence, and whether the learner's employer allows work data to be sent to a model provider is unknown until Day 6.

## Audit — 15 November 2026 (previous structure)

## Result and scope

Reviewed all 245 daily tasks, their order, deliverables, weekly pass conditions, workload, embedded tutor instructions, and the supporting `README.md`, `AGENT_OPERATOR.md`, `PROGRESS.md`, and `STUDY_PROMPT.md`. Applied the corrections below. A second independent review found no remaining material contradictions in the inspected changes.

This was a curriculum and instruction audit, not execution of all lessons. No learning session was created and no lesson was marked complete. Runtime compatibility, paid-course contents, model quality, and actual completion time remain to be tested during study. The unrelated bookmark catalog in README was not exhaustively checked for external link availability.

## Findings and corrections

| Area | Problem found | Correction |
| --- | --- | --- |
| Workload | README used six hours/week while the daily plan used five. | Aligned to five hours/week: A+B+C = 115–182 hours; with P = 139–220 hours, about 28–44 study weeks. The daily plan budgets 200 hours / 40 study weeks, with prerequisite overruns explicit. |
| Task versus session | Checkboxes were described as completed one-hour sessions despite partial and shorter sessions being permitted. | A numbered day is a task milestone; one or more actual sessions may complete it. |
| Weekly checks | Calendar Fridays could trigger checks too early or skip checks completed on another weekday. | Evaluate a block after its five tasks, save a pending check before advancement, and reconstruct missing checks after interrupted saves. |
| Resume behavior | Every message could be interpreted as a new session; template S001 could be mistaken for history. | Distinguish new sittings from same-session messages, status requests, and templates. |
| Deferred work | Week 4 allowed continuing while setup was blocked, but “next unfinished task” could immediately return to the blocker or forget it. | Persist deferred IDs, dependencies, return conditions, and review points; continue only independent work. |
| Completion | Counts alone could imply completion, and optional Day 201 could start automatically. | Require evidence and all applicable checks; stop after selected core scope; optional branches require selection. |
| Corrections and interrupted writes | Reopening an earlier task could leave its weekly pass or milestone falsely complete. | Reassess affected gates and dates; reconcile summaries from evidence; retain valid history. Document the need for a single tracker writer when chats overlap. |
| Scope | Starting at Day 1 conflicted with choosing an independent coding-only route. | Default to Day 1 for the full course, otherwise use the first eligible task in the explicitly selected scope. |
| Repository prerequisite | Days 37–38 used a repository before Day 39 selected it. | Move repository selection and baseline verification to Day 36. |
| Context experiment | Shared chat history or full repository access could invalidate the missing-context comparison. | Use fresh equivalent sessions and controlled input packs without repository/search access. |
| Missing organic failures | A course could stall waiting for a real bug or repeated agent mistake. | Permit clearly labeled historical or seeded exercise defects; never invent real-world failure history. |
| Model evaluations | Failure-path software tests reduced the intended model-quality set; configuration selection and final testing were ambiguous. | Separate deterministic tests from ten quality cases; select on development cases, freeze, then report unseen results. Apply the same discipline in week 28. |
| Citations and retrieval | Project B asked for references before sources existed; retrieval comparisons could change several factors without disclosure. | Require empty references without supplied evidence; control corpus/top-k/chunking and compare grounded answers against the no-retrieval baseline. |
| Agent limits | First calls and repeated loops could precede explicit limits; exact cost control was overstated. | Start with a single-call cap, bound loops before repetition, account for retries and per-request budget limits, and report actual usage. |
| Agent adoption | Later lessons could imply deploying the agent even after the fixed workflow won the comparison. | Harden whichever workflow the experiment supports; preserve the rejected agent as a learning artifact. |
| Failure and recovery claims | Prompt-injection tests could imply universal immunity; duplicate suppression did not distinguish changed inputs. | Test concrete dispatcher boundaries and version work identities so changed input can be intentionally reprocessed. |
| Model prerequisites | PyTorch setup and implementation-resource mapping were vague; Day 180 overfitting preceded the Day 181 training-loop lesson. | Add Appendix A and chapter pointers, set up tensors earlier, reuse the small update loop for Day 180, then extend it on Day 181. |
| Data leakage | Tokenizer fitting could precede the training/validation split. | Split first; fit learned tokenizer parameters only on training text, or explicitly use a fixed pretrained tokenizer. |
| Checkpoint claims | Reloading weights could be mistaken for resuming training. | Distinguish inference reload from training resumption and specify the state required for the latter. |
| Framework lab | Every candidate was assigned Project B despite the coding-agent option targeting repository tasks. | Permit a matched Project A task for coding automation, with its own same-task baseline. |
| Fine-tuning | No explicit training partition; prompting baseline preceded budget/model feasibility; using different models could confound the adapter effect. | Use train/development/test partitions; set budget and select the base model before the baseline; compare that model with and without the adapter. |
| Optional reading | Replacing scheduled work with papers could silently drop core tasks. | Move displaced tasks later without marking them complete. |
| Links | Seven operator-lab references pointed to nonexistent fragments because headings included duration suffixes. | Add stable P1–P5 anchors and update all seven references. |
| Resource navigation | The Russian workflow page could not be retrieved through the web tool; the provider SDK URL redirected. | Use the author's reachable GitHub chapters, including English and Russian versions, and the provider's redirected documentation URL. |

## Independent approach comparison

Used the find-solution skill for one solver–discriminator round, followed by implementation and a separate read-only verification of the changes. The existing request authorized the audit and corrections; no additional approval step was introduced.

| Candidate | Essence | Verdict | Main failure mode |
| --- | --- | --- | --- |
| S1: Targeted prose corrections | Fix individual contradictions in place. | Viable; used for lesson corrections | Scattered prose alone does not reliably preserve pending checks or deferred work. |
| S2: Explicit saved progression | Persist active work, pending checks, deferred work, and selected branches. | Strong with bounded scope | Redundant state can drift unless evidence and reconciliation rules are explicit. |
| S3: Dependency-driven milestone graph | Make the calendar a view over eligible tasks. | Viable; full graph rejected | A second graph needs maintenance and still does not fix intra-lesson prerequisites or session state. |
| Selected combination | S1 curriculum corrections plus minimal S2 saved-state rules. | Applied and reviewed | Remains dependent on the tutor following the written protocol. |

The selected combination beats prose-only S1 because interrupted sessions have an explicit pending-check and deferred-work record. It avoids a new runtime or a duplicate 245-task dependency graph. Stop criterion: a strong candidate existed after one round.

Residual risks and mitigations:

1. **Tutor inconsistency:** written instructions cannot enforce behavior mechanically. Re-read saved state, require evidence, and verify file writes; audit questionable completion claims.
2. **Partial or concurrent writes:** Markdown files do not provide transactions or locks. Reconcile from dated evidence and keep one active writer when sessions overlap.
3. **Workload uncertainty:** unfamiliar prerequisites and infrastructure may exceed one hour per task. Keep the daily cap, reduce example size, and add sessions without weakening pass criteria.
4. **Resource drift:** links and APIs can change over a long course. Use official version-matched documentation and save exact lesson/chapter resume points.

## Verification

Structural checks passed:

- 245 unique consecutive task IDs; 200 core plus 45 optional.
- 49 consecutive study blocks, each containing five tasks in the intended weekday-label order.
- A saved deliverable for every task and a pass condition for every block.
- All 30 local file/fragment references in the five audited course files resolve, including the seven repaired lab references.
- Markdown fences are balanced.
- All task checkboxes remain unchecked; `PROGRESS.md` remains at Day 1 with no recorded sessions.

Instruction walkthroughs covered an incomplete task, same-session resume, a new sitting, interruption before a weekly check, a blocked operator lab followed by independent work, correction of earlier evidence, selected-track completion, and the end of core before optional branches. These were document-level consistency checks, not live tutor sessions.

All 51 original unique external URLs in the daily course were submitted to the web tool. Most returned readable pages. Important limitations:

- [Original Russian workflow page](https://mokevnin.github.io/agentic-coding-design-patterns/ru/explore-plan-code-commit.html): inaccessible through the tool; this does not prove a global outage. The author's [English chapter](https://github.com/mokevnin/agentic-coding-design-patterns/blob/main/book/en/explore-plan-code-commit.md) and [Russian chapter](https://github.com/mokevnin/agentic-coding-design-patterns/blob/main/book/ru/explore-plan-code-commit.md) were reachable and are used instead.
- [Karpathy's overview video](https://www.youtube.com/watch?v=7xTGNNLPyMI): page identity was available; video playback and full content were not inspected.
- [Stepik](https://stepik.org/course/259791/promo), [30papers](https://30papers.com/), and the [3Blue1Brown topic catalog](https://www.3blue1brown.com/?topic=neural-networks): limited extracted content. No claim is made that every lesson or media item was verified.
- [Provider SDK documentation](https://platform.claude.com/docs/en/cli-sdks-libraries/overview): followed the redirect and updated course links.
- The model implementation mapping was checked against [Raschka's chapter index](https://github.com/rasbt/LLMs-from-scratch) and [Karpathy's syllabus](https://karpathy.ai/zero-to-hero.html). The two sequences are treated as alternatives with different ordering, not interchangeable chapter lists.

Reachability is not a compatibility test or an endorsement of every claim in a resource. The audit did not install all tools, run paid labs, or execute model-training experiments.
