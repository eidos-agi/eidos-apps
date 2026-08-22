# Eidos Apps

**The App is a Docker image.** Programs that will not fit in an applet viewer.

The file is still a Prim. The app is the pairing of prims, tools that cite them, full surfaces, **human gates**, and **one image**.

Applets stay tiny workers. This is the elsewhere the Applets charter reserved.

## Opinions

1. **Prims first.** Join prims and connectors. The Prim is the file. The tool cites it.
2. **Real surfaces.** json-render is for applets. An app is allowed a page that plays a film.
3. **Gates.** Agentic work stops for a human yes. Silence is not approval. `app.json` says *requires*, not *passed*.
4. **API library always** (when it exists). MCP and CLI optional on that library.
5. **Docker image.** One container per app. It listens. Applets do not.

## Use it

Copy [`sdk/examples/eidos-video/`](sdk/examples/eidos-video/). Pack = `app.json` + `Dockerfile`.

```bash
python3 validate.py sdk/examples/eidos-video
```

A green validator means the pack is a legal image declaration. It does not mean the image was built, and it does not mean a human said yes.

## First app

**Eidos Video** — scene video you recapture. Packs: `prim.scene`, `prim.video`. Capture is `video-3d-forge` (a forge, not a prim). Watch surfaces: `video.eidosagi.com`, `/mobile`, `/keep`. Gate: animatic yes before 3D capture.

The image name is `eidos-agi/eidos-video`. The Dockerfile builds; capture is not in it yet. A running `cat` of `app.json` is not Eidos Video.

## Status

v0 is the contract: types, `app.json`, Dockerfile, validator. This repo does not orchestrate. The first app still lives in its own repos; this is how you declare it as an App.
