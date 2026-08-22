## Verdict

The Eidos Apps SDK is a *declarations* framework, not a runtime. It defines structure (types, validator) to prevent Applets from growing upward and to keep Prim.app's name unclaimed, but provides no execution model. The terminology (Apps vs. Applets vs. Prim.app) is clarified and the decision record is sound, but the SDK leaves each App to build its own API layer. The first example (Eidos Video) is specific enough to reveal the limits: the choices made for scene capture (gates, surfaces, 3D forge pairing) may not generalize to other App categories like headless processors or document editors.

---

## Findings

- **[P1] Adapter stubs claim existence without implementation** — `/Users/dshanklinbv/repos-eidos-agi/eidos-apps/sdk/src/adapters/cli.ts`, `/src/adapters/mcp.ts`  
  Both files export only type signatures with zero implementation. The charter says "MCP and CLI are optional adapters on that library," implying the library exists; instead, each App must invent its own. The stubs are cargo-cult implementation — they signal intent but deliver no reuse. Either implement a real adapter or delete the files; importing a type that does nothing is debt masquerading as infrastructure.

- **[P1] No API library; only a function signature** — `/Users/dshanklinbv/repos-eidos-agi/eidos-apps/sdk/src/index.ts:41–43`  
  `AppApi` is `{ call(method: string, args?: unknown): Promise<unknown> }`. The charter promises "Every app is controllable through an **API library**. MCP and CLI are optional adapters on that library." But there is no library — no method table, no dispatch, no contract per method. Each App writes its own `call()` function from scratch. If a second App does something slightly different with dispatch or error handling, there is no shared pattern to enforce. This is a type, not a library. The distinction matters: a library codes patterns; a type just codes shape.

- **[P2] First App is highly specific; generality untested** — `/Users/dshanklinbv/repos-eidos-agi/eidos-apps/sdk/examples/eidos-video/app.json`  
  Eidos Video pairs scene prims, a 3D forge (connector), three surfaces (reel/share/keep, all video.eidosagi.com), and one gate (animatic). This is scene *capture* with post-processing. But what happens when the second App is, say, a document editor (no forge), or a batch processor (no interactive surfaces)? The gate might stay, but the prims+forge+surface topology is specific to capture. The validator checks structure but not plausibility for other App types. Risk: the SDK's assumptions are category-shaped (video), not app-shaped (general).

- **[P2] Surface array has no priority or routing** — `/Users/dshanklinbv/repos-eidos-agi/eidos-apps/sdk/src/index.ts:20–24`  
  `surfaces: Surface[]` lists URLs with an id and title, but no priority, default, or platform affinity. Eidos Video has three: reel (full), share (mobile), keep (storyboard). When the app is invoked, which surface opens? Does "the first one" work for all Apps? If an App on desktop should prefer "keep" but mobile should prefer "share," the SDK offers no way to express that. This is a minor gap now (three surfaces), but if catalog/discovery grows, this under-specifies the surface contract.

- **[P3] json-render ban is categorical, not contextual** — `/Users/dshanklinbv/repos-eidos-agi/eidos-apps/validate.py:41–42`  
  The validator fails any app that declares a surface with `kind: "json-render"`. The charter says "If a surface can be a card in Look, it is an applet." But what if an App legitimately offers multiple surfaces — e.g., "use as a full web app, or quick-glance card in Look"? The ban is absolute. It prevents Apps from degrading gracefully to applet-like fallbacks, even if the app is primarily a full surface. The question is not "is this wrong" but "is the ban too categorical for all future Apps."

- **[P3] Gate structure assumes one human decision point** — `/Users/dshanklinbv/repos-eidos-agi/eidos-apps/sdk/src/index.ts:30–34`  
  Gates are `{ id, title, pass: "human-yes" }`. Eidos Video has one: animatic approval. But what if a future App needs sequential gates (review → approve → deploy) or conditional gates (approve if > confidence, else iterate)? The current structure is "a gate is a human yes, full stop." It doesn't model pipelines, preconditions, or rollback. This is fine for Eidos Video but may be restrictive for other App genres (e.g., scientific workflows with review stages).

- **[P3] OPF governance document lives in the Apps repo** — `/Users/dshanklinbv/repos-eidos-agi/eidos-apps/prim.opf/product.json`  
  The product graph (intent, decision, authority) is stored here as the canonical record. If the "Eidos Apps" product concept evolves, changes live in this repo. But OPF might be shared governance infrastructure. If another product (e.g., Applets, Prim.app) also uses OPF, this repo hosting its own governance document may cause coupling. Not urgent, but worth noting: centralized governance in the Apps repo assumes Apps stay this repo's responsibility forever.

---

## What you would not change

- **The split from Applets is real and is preserved.** CHARTER.md and the validator enforce it. An Applet cannot be accepted as an App. The boundary is sharp: "real surfaces, not json-render; gates, not timeouts; prims, not embedded data." This clarity is valuable.

- **The naming decision (Eidos App, not Prim App) is correct.** The product.json decision record shows the alternatives were considered. Prim.app is the Mac host. Eidos Applets are tiny. Eidos Apps own this namespace. The decision is locked in and well-reasoned.

- **The Gates principle is fundamental.** "Silence is not a pass" (line 46 of validator) is a hard requirement, not a guideline. Any App that omits gates fails. This prevents silent approvals and agent overreach. Correct.

- **The validator is fail-closed.** It rejects ambiguous cases (json-render surfaces, missing prims, missing gates, wrong store kind) rather than defaulting. The error messages are specific. This is good validation hygiene.

- **The "prims as files" principle is clear.** Apps cite prims via external URLs (GitHub repos), not embedded data. Tools cite the prims. The prims stay the ground truth. This is stated correctly and is not violated.

---

## Questions for the other reviewers

1. **Is "API library first" honest, or should we name it "API shape first"?** The charter says apps are "controllable through an API library," but no library exists in this repo—only a type signature. The second App will invent its own `call()` dispatch. Is the current naming an aspirational goal (we will extract a library later) or is this the correct framing (each App is a library unto itself)? How do we know when it's time to extract a real shared library from App-specific implementations?

2. **If the second App has zero interactive surfaces (e.g., a batch processor that emails results), does the SDK need to evolve, or does that App belong in Applets or elsewhere?** Eidos Video is a capture+review workflow. But what if an App is headless—API-only, no UI? The surfaces array would be empty or contain webhook/email endpoints instead of web URLs. Should the validator allow that, or does "real surfaces" mandate interactive pages for all Apps?

3. **Could a surface be contextually json-render (e.g., "view in Look as an applet OR full web") without violating the Apps/Applets boundary, or does offering json-render at all risk merging the two categories?** The validator bans it. But does the charter forbid an App from offering multiple surfaces where one is a degraded mode? Or does the existence of json-render capability automatically make it an Applet wearing a coat?
