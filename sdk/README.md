# @eidos-agi/apps

Opinionated SDK for creating Eidos Apps. This repo is the home. Do not start a second SDK.

## Opinions

1. **Prims first.** Join prims and Prim Tools. The Prim is the file. The tool cites it.
2. **Real surfaces.** Not json-render. If it fits a Look card, it is an applet.
3. **Gates.** Human yes. Silence is not a pass.
4. **API library always.** MCP and CLI optional, same methods.
5. **Docker image.** Not an applet worker. Not Prim.app.

## Control

```
App.api.call(method, args)     // required
App.mcp                        // option — same methods
App.cli                        // option — same methods
```

Copy [`examples/eidos-video/app.json`](examples/eidos-video/app.json).
