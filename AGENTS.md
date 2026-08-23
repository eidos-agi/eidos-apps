# Eidos Apps

Read [`CHARTER.md`](CHARTER.md) before adding a file.

- Product graph: `prim.opf/` (`product.json` is authority)
- Contract lives in `sdk/`. An App is a Docker image.

## Do

- Keep prims as files. Tools cite them. Do not copy cameras into an app manifest.
- Give each app real surfaces. Do not force json-render.
- Declare **gates** with `requires: human-yes`. Silence is not a pass. Do not pre-fill a yes.
- Ship a **Dockerfile** next to `app.json`. Declare `EXPOSE`. That is pack syntax, not a listen proof.
- Drive the app through the API library when one exists. MCP and CLI are optional adapters.

## Do not

- Grow this into Applets, or Applets into this.
- Name it Prim App. Prim.app is the host.
- Declare `prim.eidosagi.com` as `kind: eidos-app`.
- Vendor a capture pipeline or a model. Those stay forges (`video-3d-forge`, Imagine).
- Add a manager, a Dock icon, Kubernetes, or a worker runtime here. Apps are Docker images; this repo does not orchestrate a fleet.
- Treat a validator `declaration-ok` or an image name string as “the app runs” or “the human said yes”.
- Call the eidos-video pack the first App. It is a declaration fixture until the image listens.

## Validate

```bash
python3 validate.py sdk/examples/eidos-video
PYTHONPATH=~/repos-eidos-agi/opf python3 -m opf.validate prim.opf
```
