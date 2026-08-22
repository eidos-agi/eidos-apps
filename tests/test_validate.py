import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validate  # noqa: E402


class ValidateApp(unittest.TestCase):
    def test_example_ok(self):
        errs = validate.validate(ROOT / "sdk" / "examples" / "eidos-video")
        self.assertEqual(errs, [])

    def test_rejects_applet_kind(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            body = json.loads((ROOT / "sdk" / "examples" / "eidos-video" / "app.json").read_text())
            body["kind"] = "applet"
            (p / "app.json").write_text(json.dumps(body))
            errs = validate.validate(p)
            self.assertTrue(any("eidos-app" in e or "applet" in e for e in errs))

    def test_rejects_empty_gates(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            body = json.loads((ROOT / "sdk" / "examples" / "eidos-video" / "app.json").read_text())
            body["gates"] = []
            (p / "app.json").write_text(json.dumps(body))
            errs = validate.validate(p)
            self.assertTrue(any("gates" in e for e in errs))

    def test_rejects_missing_docker(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            body = json.loads((ROOT / "sdk" / "examples" / "eidos-video" / "app.json").read_text())
            body["runtime"] = {"kind": "worker"}
            (p / "app.json").write_text(json.dumps(body))
            errs = validate.validate(p)
            self.assertTrue(any("docker" in e for e in errs))

    def test_rejects_json_render_surface(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            body = json.loads((ROOT / "sdk" / "examples" / "eidos-video" / "app.json").read_text())
            body["surfaces"] = [{"id": "card", "url": "x", "kind": "json-render"}]
            (p / "app.json").write_text(json.dumps(body))
            errs = validate.validate(p)
            self.assertTrue(any("json-render" in e for e in errs))


if __name__ == "__main__":
    unittest.main()
