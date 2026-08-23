# Eidos Apps

Larger programs. Prim-native. Not applets. Not Prim.app.

**The App is a Docker image.** That is the shippable unit.

This repo is the contract that declares one. Nothing else.

## What this is

| Noun | Role |
|------|------|
| **Eidos App** | A Docker image. Too big for Look. Real surfaces. Prims stay the files. Tools cite them. **Listens.** |
| **eidos-apps contract** | How you declare that image: `app.json`, a Dockerfile, types, a validator. |
| **Gate** | A human yes required before spend. Silence is not a pass. |
| **Applet worker** | Tiny isolate. No listen-port. Other repo. |
| **Prim.app** | Double-click host for a `.prim`. Peer, not this. |
| **prim.eidosagi.com** | How you look at prims. A catalog surface. Not an Eidos App. |

Applets are tiny programs a person builds with AI and glances at in a small viewer. Eidos Apps are the programs that do not fit that viewer. The Applets charter already said so: *Do not grow Applets until they are Apps.* This is that elsewhere.

**Prim.app** is the Mac host that double-clicks a `.prim` file. An Eidos App *uses* prims. It is not the host.

**prim.eidosagi.com** is a look surface. Do not declare it as `kind: eidos-app`. A catalog with a costume gate is not an App.

## What an app is made of

The artifact is **one Docker image**. `app.json` is the label on that image. The Dockerfile in the pack is the recipe. This repo does not orchestrate.

Join **prims**, **connectors** (Prim Tools that cite a file), and a **control API**. Surfaces are app pages — URLs the image owns, runs, or controls. They are not Prim Tools. Do not reuse Prim’s `surface | connector` union here.

That composition is **per app**. Each app owns its prims, surfaces, connectors, store, and image. A shared website is how you look; it is not a shared stack.

Stay **web** when the surface is a page. A Mac icon may open the existing browser. Do not invent a private WebKit to look native.

**Runtime is the image.** Capture, ffmpeg, Chrome, models live in that image, not in an applet isolate. Applets stay local workers with no listen-port. Apps listen. Do not run an App as an applet worker. Do not run an applet as a container to look bigger.

json-render is an **applet** fallback. Apps are allowed a real surface. If a surface can be a card in Look, it is an applet citing the same prims — not this app wearing a smaller coat.

## Agentic work

An app may let an agent draft, sketch, assemble, capture. It may not let the agent approve.

Gates are first-class. The agent works **between** them. A typed human yes is the only pass. Do not treat a timeout, a green test, or “the model liked it” as approval.

`app.json` declares that a gate *requires* a human yes. It does not record that anyone said yes. A validator `declaration-ok` is not approval and not “the app listens.”

## Control

Every app is controllable through an **API library**. MCP and CLI are optional adapters on that library. They do not grow a second method table. v0 does not ship that library; the image will.

## What this is not

- **Eidos Applets** — tiny programs, json-render fallback, applet workers, ~6 MB viewers. Not Docker. Different repo.
- **Prim.app** — the double-click host for a `.prim`. Peer.
- **prim.eidosagi.com** — look / catalog. Not an App.
- A pipeline editor, a DAW, Cinema Forge revived as a website.
- Kubernetes, Compose-as-the-product, or a worker runtime in this repo.
- A vibe-coded monolith with prims taped on.

## Anti-bloat

This repo may only grow work that is:

1. prim-app composition (prims + connectors + surfaces)
2. `app.json` and the Dockerfile that make the image
3. gates (human yes required; records live elsewhere)
4. Docker as the App (declare the image; do not invent an orchestrator)
5. the API library, with optional MCP and CLI adapters, when a second app needs shared `call()`
6. examples that are real apps — Eidos Video is the intended first; until its image listens, the pack in this repo is a **declaration fixture**, not the App

If a feature is not on that list, it belongs somewhere else or it does not belong.
