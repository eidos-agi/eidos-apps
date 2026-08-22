#!/usr/bin/env python3
"""Fail-closed checks for an Eidos App pack (app.json + Dockerfile)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

FORBIDDEN_PASSES = ("timeout", "green-test", "model-liked-it", "the model liked it")


def validate(pack: Path) -> list[str]:
    err: list[str] = []
    p = pack / "app.json"
    if not p.is_file():
        return ["missing app.json"]
    try:
        app = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        return [f"app.json: {e}"]

    for k in ("kind", "id", "name", "summary", "prims", "tools", "surfaces", "gates", "store", "runtime"):
        if k not in app:
            err.append(f"app.json missing {k}")
    if app.get("kind") != "eidos-app":
        err.append("kind must be eidos-app")
    if app.get("kind") in {"applet", "prim-applet", "prim-app"}:
        err.append("this is Eidos Apps, not an applet and not Prim.app")
    if "api" in app:
        err.append("api does not belong in app.json — that is runtime, after the image exists")

    prims = app.get("prims") or []
    if not prims:
        err.append("prims empty — an app cites files")
    for i, c in enumerate(prims):
        if not isinstance(c, dict) or "profile" not in c or "path" not in c:
            err.append(f"prims[{i}] needs profile and path")

    surfaces = app.get("surfaces") or []
    if not surfaces:
        err.append("surfaces empty — an app has a real page, not json-render")
    for i, s in enumerate(surfaces):
        if not isinstance(s, dict) or not s.get("id") or not s.get("url"):
            err.append(f"surfaces[{i}] needs id and url")
        if s.get("kind") == "json-render":
            err.append(f"surfaces[{i}] is json-render — that is an applet")

    gates = app.get("gates") or []
    if not gates:
        err.append("gates empty — silence is not a pass")
    for i, g in enumerate(gates):
        if not isinstance(g, dict) or not g.get("id") or not g.get("title"):
            err.append(f"gates[{i}] needs id and title")
            continue
        if "pass" in g:
            err.append(f"gates[{i}] uses pass — that is a record elsewhere; declare requires")
        req = g.get("requires")
        if req != "human-yes":
            err.append(f"gates[{i}] requires must be human-yes")
        blob = json.dumps(g).lower()
        for bad in FORBIDDEN_PASSES:
            if bad in blob:
                err.append(f"gates[{i}] {bad!r} is not a pass")

    store = app.get("store") or {}
    if store.get("kind") not in {"sqlite-vec", "files"}:
        err.append("store.kind must be sqlite-vec or files")

    runtime = app.get("runtime") or {}
    if runtime.get("kind") != "docker":
        err.append("runtime.kind must be docker — the App is a Docker image")
    if not runtime.get("image"):
        err.append("runtime.image missing — name the image")
    if runtime.get("kind") in {"worker", "applet-worker"}:
        err.append("an App is not an applet worker")
    df_name = runtime.get("dockerfile") or "Dockerfile"
    df = pack / str(df_name)
    if not df.is_file():
        err.append("Dockerfile missing — an App is an image")
    else:
        text = df.read_text()
        if "EXPOSE" not in text:
            err.append("Dockerfile must EXPOSE a port — Apps listen, Applets do not")
    return err


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate.py <app-dir>", file=sys.stderr)
        return 2
    pack = Path(argv[1]).expanduser().resolve()
    errs = validate(pack)
    if errs:
        print("FAIL")
        for e in errs:
            print(" ", e)
        return 1
    print("ok", pack)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
