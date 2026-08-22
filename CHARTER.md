# Eidos Apps

Larger programs. Prim-native. Not applets. Not Prim.app.

This repo is the **opinionated SDK** that creates them. Nothing else.

## What this is

| Noun | Role |
|------|------|
| **Eidos App** | A program too big for Look. Real surfaces. Prims stay the files. Tools cite them. |
| **eidos-apps SDK** | How you declare one. Opinions as types and an `app.json`. |
| **Gate** | A human yes. Silence is not a pass. Agentic work stops here. |

Applets are tiny programs a person builds with AI and glances at in a small viewer. Eidos Apps are the programs that do not fit that viewer. The Applets charter already said so: *Do not grow Applets until they are Apps.* This is that elsewhere.

**Prim.app** is the Mac host that double-clicks a `.prim` file. An Eidos App *uses* prims. It is not the host.

## What an app is made of

Join **prims**, **Prim Tools** (surfaces and connectors), and a **control API**. The file stays the Prim. The tool cites it. The app is the pairing plus the surfaces a person actually uses.

That composition is **per app**. Each app owns its prims, surfaces, connectors, and store. A shared website is how you look; it is not a shared stack.

Stay **web** when the surface is a page. A Mac icon may open the existing browser. Do not invent a private WebKit to look native.

json-render is an **applet** fallback. Apps are allowed a real surface. If a surface can be a card in Look, it is an applet citing the same prims — not this app wearing a smaller coat.

## Agentic work

An app may let an agent draft, sketch, assemble, capture. It may not let the agent approve.

Gates are first-class. The agent works **between** them. A typed human yes is the only pass. Do not treat a timeout, a green test, or “the model liked it” as approval.

## Control

Every app is controllable through an **API library**. MCP and CLI are optional adapters on that library. They do not grow a second method table.

## What this is not

- **Eidos Applets** — tiny programs, json-render fallback, applet workers, ~6 MB viewers. Different repo.
- **Prim.app** — the double-click host for a `.prim`. Peer, not this SDK.
- A pipeline editor, a DAW, Cinema Forge revived as a website.
- A vibe-coded monolith with prims taped on.

## Anti-bloat

This repo may only grow work that is:

1. prim-app composition (prims + Prim Tools + connectors)
2. `app.json` and the SDK types
3. gates (human yes)
4. the API library, with optional MCP and CLI adapters
5. examples that are real apps (Eidos Video is the first)

If a feature is not on that list, it belongs somewhere else or it does not belong.
