# @eidos-agi/apps

Contract for Eidos Apps. An App is a Docker image. This folder is how you declare one.

Do not start a second contract repo.

## Opinions

1. **Prims first.** Join prims and connectors. The Prim is the file. The tool cites it.
2. **Real surfaces.** Not json-render. If it fits a Look card, it is an applet.
3. **Gates.** `requires: human-yes`. Silence is not a pass.
4. **API library** later. MCP and CLI optional, same methods. Not in `app.json`.
5. **Docker image.** Dockerfile in the pack. Listens. Not an applet worker. Not Prim.app.

Copy [`examples/eidos-video/`](examples/eidos-video/).
