# Development roadmap

The developer writes the game in PyCharm. Tasks are ordered learning milestones, not instructions to generate the entire implementation automatically. Phase 1 deliberately keeps story progression linear. Phase 2 adds player-dependent outcomes. No public release, expenditure, or Steam submission is authorised by a task alone.

Only P1-01 is complete, based on the developer's confirmed manual run. All other tasks are pending. Each future task requires focused verification and review before completion.

## Phase 1 — Complete linear game

### P1-01 | Opening window and contextual buttons
Status: Done

Kestrel Station opens in a desktop window with readable introductory text. Inspecting the signal and asking Patch show different responses. The window closes normally.

Acceptance: developer has run the game and confirmed both buttons work after correcting the mouse-event indentation. No automated UI verification is claimed.

### P1-02 | Scene state and linear navigation
Status: Todo

Replace ad hoc text changes with a small scene/state model. Separate authored content from drawing and event handling. Finish the current observe action: its click handler exists but its button is not drawn yet. Correct the window caption from Narce to Nacre. Add an information-gathering action and a clearly labelled advance action; every route follows the same ordered chapter.

Acceptance: repeat interactions do not skip scenes; navigation cannot jump past required investigation. Check first, middle and final scenes and irrelevant input events. Depends on P1-01.

### P1-03 | Readable terminal interface and controls
Status: Todo

Add text wrapping, scrolling where needed, a consistent terminal layout, keyboard focus/activation, visible focus, and readable contrast. Support a practical minimum window size and resize handling.

Acceptance: long dialogue fits without overlap; every essential action works with keyboard and mouse; resizing preserves usable controls. Depends on P1-02.

### P1-04 | Linear opening: scanner, drone and Meridian lock
Status: Todo

Author Kestrel departure, scanner observations, drone inspection and safe lock repair as an ordered sequence. Teach stored state, fallback configured before launch, stale data and UNKNOWN status through consequences. Contextual inspection does not create branches.

Acceptance: the sequence completes; fresh engaged, disengaged and missing sensor readings have distinct explanations. Preserve historical readings separately from current status. Depends on P1-02 and P1-03.

### P1-05 | Linear middle: Vale rescue and carrier repair
Status: Todo

Author isolation checks, carrier bracket interference, disconnected-power testing, harness repair and safe lab release. Explain unit versus integration testing and root-cause versus symptom repair without code quizzes.

Acceptance: assembled and disconnected carrier checks are both shown; rescue succeeds and the specimen remains sealed. Depends on P1-04.

### P1-06 | Linear arrival: gate, towing and Nacre landing
Status: Todo

Author gate containment, packet/timestamp inspection, measured mass, independently surveyed approach, Venn introduction and staged landing with abort checks. Keep progression fixed.

Acceptance: restarts remain paused with broken remote sensing; remote control is disabled while status remains available; Meridian lands successfully. A signature is not treated as proof of truthful content. Depends on P1-05.

### P1-07 | Linear investigation and chapter conclusion
Status: Todo

Author archive containment, Graves support, heating, Kite cable inspection and Venn's timeline. Use relative in-game dates: yesterday 09:12 receipt, 09:24 departure, today 16:24 arrival, 31-hour flight. End with a completed local objective, specialist handoff and downtime. The established investigation reaches the request to Graves for a security team and ETA; any later events need new authored scenes.

Acceptance: Rook's survival/location and the shuttle's arrival remain unconfirmed without independent evidence. Anchor Nine is a configured destination, not a verified physical endpoint. Lena Chen and Mara Chen remain distinct. Depends on P1-06.

### P1-08 | Evidence board, mission history and concept journal
Status: Todo

Record discoveries with source, acquisition context, freshness and confidence. Separate observations, testimony, hypotheses, predictions and unknowns. Keep mission progress and short post-action programming explanations available without replay.

Acceptance: new records appear once; viewing panels preserves the scene; stale evidence is labelled; testimony is not promoted to verified fact. Depends on P1-04; extend through P1-07.

### P1-09 | Ship/crew status and contextual communications
Status: Todo

Show location, ship readiness, crew and completed objectives. Add authored requests to Graves and relevant specialists with useful responses. These are fictional in-game communications, not network messages.

Acceptance: statuses match narrative events; requests explain who can act and why; repeat requests cannot corrupt progress. Depends on P1-07 and P1-08.

### P1-10 | Versioned saves and both starting options
Status: Todo

Add new game at Kestrel, continue from the established Nacre investigation, save/load, JSON export/import and confirmed restart. The continue state places Meridian safely in Nacre's hangar, Vale rescued with the specimen sealed, gate restarts paused, remote gate control disabled, archive outbound messages contained, heating restored, Kite's navigation cable disconnected, and security support requested from Graves. Keep Rook's whereabouts and the departing shuttle's arrival unconfirmed. Use a versioned JSON schema and validate imported state before applying it. Store saves in a writable user-data location outside packaged assets.

Acceptance: both starts reach the same linear chapter conclusion; canonical history is browsable without replay; save round trips preserve progress; invalid/truncated/unsupported saves do not replace current progress; cancelling restart preserves state. Depends on P1-07 through P1-09.

### P1-11 | Gameplay regression checks and release review
Status: Todo

Add meaningful automated checks for scene progression, journal deduplication, save validation and both starting states. Manually play the complete linear chapter and verify mouse/keyboard controls. Review the actual release candidate for unsafe file handling, untrusted data, secrets, assets and dependency licences; backend route checks are not applicable to this offline game.

Acceptance: record test commands/results, negative save cases, manual playthrough evidence and resolved blocking review findings. A passing syntax check alone is insufficient. Depends on P1-10.

### P1-12 | Desktop packaging and Phase 1 release candidate
Status: Todo

Choose and document a desktop packager, explain the added build dependency, bundle required assets/notices and prepare a Windows build. Add launch, save location and troubleshooting instructions. Keep distribution preparation separate from publication approval.

Acceptance: verify the build on a suitable clean Windows environment without a development Python installation; saves work without writing to the installation folder; document any unverified environment. No Steam upload in Phase 1. Depends on P1-11.

## Phase 2 — RPG elements

Phase 2 depends on the verified Phase 1 baseline. Details and balancing remain open until their tasks are specified.

### P2-01 | Specify RPG rules and compatibility
Status: Todo

Define exploration-focused progression, meaningful choices, resource limits, failure recovery and save compatibility. Keep learning through practical decisions. Agree the smallest RPG scope before implementation; combat, procedural worlds and external AI are not assumed.

Acceptance: written player-visible rules and acceptance criteria cover each new system; define migration of Phase 1 saves and synthetic test scenarios. Depends on P1-12.

### P2-02 | Branching missions and persistent consequences
Status: Todo

Introduce a small number of authored alternative approaches, consequences and reconverging paths. Add compatible multi-order selection with explicit conflicts and atomic validation. Preserve a playable fallback path after recoverable mistakes.

Acceptance: at least two approaches yield distinct observable outcomes; incompatible orders apply no partial changes; every supported branch can reach a resolution. Depends on P2-01.

### P2-03 | Ship upgrades and exploration equipment
Status: Todo

Add equipment choices with documented costs, capabilities and trade-offs, including scanner and drone upgrades. Preserve the vessel's exploration purpose.

Acceptance: an upgrade changes a mission option; insufficient resources cause no deduction; duplicate installation cannot charge twice; save/load preserves loadout. Depends on P2-01.

### P2-04 | Inventory, resources and recovery
Status: Todo

Introduce a small inventory and agreed resources such as energy, repair supplies or credits. Add resupply and recovery opportunities so ordinary exploration does not create unwinnable states.

Acceptance: spending/gaining is consistent and bounded; invalid transactions do not mutate state; a documented low-resource scenario remains recoverable. Depends on P2-01 and integrates with P2-03.

### P2-05 | Crew relationships and specialist delegation
Status: Todo

Add crew trust and specialist strengths that affect authored interactions. Track delegated tasks with visible progress and outcomes. Do not treat trust, credentials or a witness statement as proof that a claim is true.

Acceptance: at least one relationship and one delegated task produce a visible consequence; repeat dialogue cannot farm progression; save/load preserves task state. Depends on P2-02.

### P2-06 | RPG balancing, migration and distribution readiness
Status: Todo

Test branches, resources, upgrades, crew systems and migration from representative Phase 1 saves. Verify multiple endings and accessible controls. Review the new release candidate for security/licensing and package compatibility. Assess Steam requirements and costs separately before any paid onboarding or submission.

Acceptance: record branch coverage, migration outcomes, complete playthroughs and unresolved platform limitations. A future Steam release requires explicit approval and platform review. Depends on P2-02 through P2-05.
