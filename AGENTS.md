# Eidos Apps

Read [`CHARTER.md`](CHARTER.md) before adding a file.

- Product graph: `prim.opf/` (`product.json` is authority)
- Create apps with `sdk/`. This *is* the SDK repo.

## Do

- Keep prims as files. Tools cite them. Do not copy cameras into an app manifest.
- Give each app real surfaces. Do not force json-render.
- Declare **gates**. Silence is not a pass.
- Declare a **Docker image**. Apps are containers. Applets are workers.
- Drive the app through the API library. MCP and CLI are optional adapters.

## Do not

- Grow this into Applets, or Applets into this.
- Name it Prim App. Prim.app is the host.
- Vendor a capture pipeline or a model. Those stay forges (`video-3d-forge`, Imagine).
- Add a manager, a Dock icon, Kubernetes, or a worker runtime here. Apps are Docker images; this SDK does not orchestrate a fleet.
- Treat an agent draft as approved.

## Validate

```bash
python3 validate.py sdk/examples/eidos-video
PYTHONPATH=~/repos-eidos-agi/opf python3 -m opf.validate prim.opf
```
