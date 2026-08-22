# Eidos Apps

Opinionated SDK for **Eidos Apps** — programs that will not fit in an applet viewer.

The file is still a Prim. The app is the pairing of prims, tools that cite them, full surfaces, **human gates**, and a **Docker image**.

Applets stay tiny. This is the elsewhere the Applets charter reserved.

## Opinions

1. **Prims first.** Join prims, Prim Tools (surfaces, connectors). The Prim is the file. The tool cites it.
2. **Real surfaces.** json-render is for applets. An app is allowed a page that plays a film.
3. **Gates.** Agentic work stops for a human yes. Silence is not approval.
4. **API library always.** MCP and CLI are optional adapters on that library.
5. **Docker image.** One container per app. Applets are local workers. Not Prim.app.

## Use it

Copy [`sdk/examples/eidos-video/app.json`](sdk/examples/eidos-video/app.json).

```bash
python3 validate.py sdk/examples/eidos-video
```

```
App.api.call(method, args)     // required
App.mcp                        // option — same methods
App.cli                        // option — same methods
```

## First app

**Eidos Video** — scene video you recapture. Packs: `prim.scene`, `prim.video`. Capture is `video-3d-forge` (a forge, not a prim). Watch surfaces: `video.eidosagi.com`, `/mobile`, `/keep`. Gate: animatic yes before 3D capture.

## Status

v0 is types, `app.json`, and a validator. Runtime kind is Docker; this repo does not orchestrate. The first app still lives in its own repos; this SDK is how you declare it.
