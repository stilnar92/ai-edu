# Track P — Operate AI assistants

Use existing agents to accomplish useful work across documents, browsers, and desktop applications. No programming prerequisite and no AI SDK required. Module 0 in the [main course](README.md) is optional background. Product examples can be replaced without changing the learning outcomes.

**Project:** turn a set of learning materials into a verified brief, a comparison table, and one draft visual artifact; then test an assistant that reports meaningful changes. You may substitute document organization, study preparation, or another bounded personal workflow.

**Place in the daily course:** since the 18 November 2026 restructure this is an elective track with task IDs P01–P30. Days 1–2 of the entry self-check test delegation, capabilities, boundaries, and background work; only a gap assigns tasks from these labs. Lab P5 is also a reference for scheduling the personal assistant's recurring run on Day 59.

**Estimated practice:** 24–38 hours across five labs. The daily course allocates about 30 hours; setup and recovery can extend it. Infrastructure setup can take longer. Choose one assistant and one execution environment; a working existing tool is enough to start. No installation or scheduled job was performed when this curriculum was updated.

<a id="p1"></a>

## P1 — Delegate outcomes and demand evidence · 3–5 hours

- [ ] Write a task brief with a goal, inputs, permitted actions, output location, completion check, and budget or stopping condition.
- [ ] If the outcome is unclear, ask the assistant to interview you, then give the resulting brief to a fresh session.
- [ ] Compare a short clear brief with a longer instruction set on the same task. Add instructions only for observed failures.
- [ ] Ask for evidence appropriate to the artifact: source references, calculated totals, an exported file, or a screenshot of the final state.

**Starting point:** your [Addy Osmani bookmark](https://x.com/addyosmani/status/2115688494865465370) and its pasted text. Treat model-specific claims and product rollouts as dated observations, not permanent course requirements.

**Practice:** Produce a comparison of five learning resources with source links, prerequisites, and an explanation of uncertain claims. Permitted actions: read sources and create local drafts. Do not contact anyone or publish anything.

**Pass:** You independently check the key claims and can open the delivered artifact. **Recovery:** if a source fails or the result is unsupported, the assistant marks the gap instead of inventing an answer.

<a id="p2"></a>

## P2 — Equip an assistant with context, skills, and integrations · 5–8 hours

- [ ] Distinguish instructions/skills, tool access through a connector or MCP, retrieved documents, and saved memory.
- [ ] Select one repeated task and inspect a relevant skill before using it. Record its inputs, outputs, dependencies, and permissions.
- [ ] Give the assistant a small approved document collection and test five questions with known answers.
- [ ] Use a suitable existing integration instead of asking the agent to click through every task.

**Bookmark lab choices:** [MarkItDown](https://github.com/microsoft/markitdown) for document conversion and [qmd](https://github.com/tobi/qmd) for searching a local knowledge collection. [Skills.sh](https://skills.sh/), [SkillsMP](https://skillsmp.com/), and [Chops](https://chops.md/) are discovery/organization references, not required catalogs to install wholesale. Moka module 5 can supplement this lab.

**Practice:** Convert copies of a few documents, make them searchable, and ask for a sourced brief. Compare the conversion with originals, especially tables and headings. Keep unrelated files outside the allowed collection.

**Pass:** Answers cite the correct documents; conversion omissions are visible. **Recovery:** replace one source and verify the assistant stops using the obsolete version. If an optional tool is unavailable, complete the exercise using direct file reading.

<a id="p3"></a>

## P3 — Give the agent a separate workspace · 5–8 hours

- [ ] Distinguish a separate browser profile, a process sandbox, a VM, and a cloud session. Record what is actually isolated and what is shared.
- [ ] Choose one environment, verify prerequisites, and use a separate test account or copies of data.
- [ ] Record access to shared folders, network services, credentials, and clipboard. A VM does not undo actions on an account logged into a remote service.
- [ ] Keep a known-good starting state and test a supported reset or restore procedure.

**Verified tool options, 6 November 2026:**

| Tool | Role | What to know before the lab |
| --- | --- | --- |
| [terminal-mac](https://github.com/govijr/terminal-mac) | Separate macOS guest with terminal display and MCP control | Apple silicon, macOS 14+; early release candidate; initial guest setup is guided. It already includes computer-use tools. Its README names Ghostty, Kitty, and iTerm2 for inline display, with a native-window fallback. |
| [Lume](https://cua.ai/docs/lume) | Manage macOS/Linux VMs on Apple silicon | Supports a CLI, HTTP API, and MCP. Terminal management and rendering a desktop inside a terminal are different features. |
| [Claude cloud sessions](https://support.claude.com/en/articles/12618689-use-claude-code-in-the-cloud) | Remote repository tasks | Useful for the coding track; not a substitute for access to your local desktop applications. |

**Practice:** Create a scratch document and edit it in the isolated environment. Check that the original host document is unchanged. Use only a test folder/account and retain the exported result before resetting.

**Pass:** You can describe the real boundary, recover the starting state, and identify resources that remain shared. **Recovery:** if VM setup is blocked, record that lab as incomplete; continue P4 in an already available test environment. Buying hardware is not a prerequisite for the rest of the track.

<a id="p4"></a>

## P4 — Use browser and desktop applications · 5–8 hours

- [ ] Choose the interface for the job: connector/API/MCP, browser controls, or desktop computer use.
- [ ] Practice observe → act → verify on a copied document or test application.
- [ ] Compare background interaction with isolated execution. Avoiding focus changes is useful but is not an isolation boundary.
- [ ] Inspect the saved result instead of accepting an agent's completion statement.

[Cua Driver](https://cua.ai/cua-driver) advertises background app control and accessibility-tree access across macOS, Windows, and Linux. Accessibility information can reduce dependence on screenshot coordinates; it does not prove universal accuracy or lowest cost. The claim that it is the “best” tool is not established here. It is an optional control layer, not a prerequisite for terminal-mac, and combining them needs its own compatibility check.

**Choose one bookmark-based mission:**

- A design artifact: use [Figma Console MCP](https://github.com/southleft/figma-console-mcp) with a test file to inspect or modify a small design.
- A short visual explanation: try [HyperFrames](https://hyperframes.heygen.com/) or one of your saved video/animation skills and inspect the rendered output.
- A document task: extract a few source facts into an editable comparison table, then reopen it to verify contents.

[Stagehand](https://github.com/browserbase/stagehand) belongs to the browser-automation implementation branch if you later want to program the interaction; it is not required to operate an existing assistant.

**Pass:** The artifact opens, contains the requested content, and survives a fresh inspection. **Recovery:** introduce one UI interruption and require the assistant to inspect the new state before retrying. Keep sending, publishing, purchases, and destructive changes outside this practice task.

<a id="p5"></a>

## P5 — Run bounded background and proactive work · 6–9 hours

- [ ] Distinguish one task continuing across turns, a scheduled task, an event-triggered task, and a persistent personal assistant.
- [ ] Complete a task manually once before enabling repeat runs. Define the trigger, allowed sources/actions, output, stopping condition, and notification rule.
- [ ] Compare one existing assistant runtime only: your current application, [Hermes Agent](https://github.com/nousresearch/hermes-agent), or [nanobot](https://github.com/HKUDS/nanobot).
- [ ] Test cancellation, unavailable sources, duplicate input, interrupted execution, and a run with no meaningful change.

In Claude Code, [auto mode](https://claude.com/resources/articles/auto-mode-default-in-claude-code) concerns action permissions; [/goal](https://code.claude.com/docs/en/goal) concerns continuing toward a completion condition. Its evaluator reads evidence in the conversation rather than independently checking the computer. A model verdict does not replace a reliable artifact check. Availability and defaults can depend on account and version.

**Practice:** Run a learning-resource digest against three controlled input snapshots: unchanged, one real update, and an unavailable source. Save drafts locally. Require “no change” on the first, a sourced update on the second, and an explicit failure on the third. Only enable a real schedule later if you want ongoing delivery; this course edit does not create one.

**Pass:** No duplicate results, no false success after a failed check, and a tested stop control. Record whether the host must remain awake and what happens to missed runs. **Recovery:** restart and verify whether work resumes or must be explicitly retried. Nanobot's documentation specifically warns that missed scheduled times are not replayed after restart.

## What to defer

- Parallel session managers such as Orca, Paradev (formerly Superset), and Herdr: evaluate when one session can finish and report evidence without supervision.
- Paperclip and extensive multi-agent organizations: optional advanced exploration after a useful single-assistant workflow.
- Muse: an interest to investigate once the exact product URL is identified; the name alone is ambiguous.
- Claims that Windows has no equivalents, fixed model rankings, token-saving percentages, and social-media benchmarks: investigate separately before adopting them as selection criteria.

## Keep the workflow current

Every few months, rerun the same small task set with shorter instructions, a fresh session, and updated tools. Compare success, corrections, cost, elapsed time, and interruptions. Remove rules only when evidence shows they are unnecessary. Keep permissions and acceptance criteria explicit.

The practical result is a repeatable delegation workflow with evidence and recovery—not a large collection of installed agents.
