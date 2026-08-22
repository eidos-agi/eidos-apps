#!/usr/bin/env python3
"""Fail-closed checks for an Eidos App pack (app.json)."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def validate(pack: Path) -> list[str]:
    err: list[str] = []
    p = pack / "app.json"
    if not p.is_file():
        return ["missing app.json"]
    try:
        app = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        return [f"app.json: {e}"]

    for k in ("kind", "id", "name", "summary", "prims", "tools", "surfaces", "gates", "store"):
        if k not in app:
            err.append(f"app.json missing {k}")
    if app.get("kind") != "eidos-app":
        err.append("kind must be eidos-app")
    if app.get("kind") in {"applet", "prim-applet", "prim-app"}:
        err.append("this is Eidos Apps, not an applet and not Prim.app")

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
        elif g.get("pass") != "human-yes":
            err.append(f"gates[{i}] pass must be human-yes")

    store = app.get("store") or {}
    if store.get("kind") not in {"sqlite-vec", "files"}:
        err.append("store.kind must be sqlite-vec or files")
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
