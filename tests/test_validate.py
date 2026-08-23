import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import validate  # noqa: E402

EXAMPLE = ROOT / "sdk" / "examples" / "eidos-video"
DOCKERFILE = (EXAMPLE / "Dockerfile").read_text()


def _pack(body: dict, dockerfile: str | None = DOCKERFILE) -> Path:
    d = Path(tempfile.mkdtemp())
    (d / "app.json").write_text(json.dumps(body))
    if dockerfile is not None:
        name = body.get("runtime", {}).get("dockerfile") or "Dockerfile"
        (d / name).write_text(dockerfile)
    return d


class ValidateApp(unittest.TestCase):
    def test_example_ok(self):
        errs = validate.validate(EXAMPLE)
        self.assertEqual(errs, [])

    def test_cli_says_declaration_ok(self):
        import io
        from contextlib import redirect_stdout

        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = validate.main(["validate.py", str(EXAMPLE)])
        self.assertEqual(rc, 0)
        lines = buf.getvalue().splitlines()
        self.assertTrue(lines[0].startswith("declaration-ok"))
        self.assertFalse(any(line == f"ok {EXAMPLE.resolve()}" or line.startswith("ok ") for line in lines))

    def test_rejects_applet_kind(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["kind"] = "applet"
        errs = validate.validate(_pack(body))
        self.assertTrue(any("eidos-app" in e or "applet" in e for e in errs))

    def test_rejects_empty_gates(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["gates"] = []
        errs = validate.validate(_pack(body))
        self.assertTrue(any("gates" in e for e in errs))

    def test_rejects_missing_docker(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["runtime"] = {"kind": "worker"}
        errs = validate.validate(_pack(body))
        self.assertTrue(any("docker" in e for e in errs))

    def test_rejects_json_render_surface(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["surfaces"] = [{"id": "card", "url": "x", "kind": "json-render"}]
        errs = validate.validate(_pack(body))
        self.assertTrue(any("json-render" in e for e in errs))

    def test_rejects_pass_field(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["gates"] = [{"id": "g", "title": "t", "requires": "human-yes", "pass": "human-yes"}]
        errs = validate.validate(_pack(body))
        self.assertTrue(any("pass" in e for e in errs))

    def test_rejects_timeout(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["gates"] = [{"id": "g", "title": "t", "requires": "timeout"}]
        errs = validate.validate(_pack(body))
        self.assertTrue(any("human-yes" in e or "timeout" in e for e in errs))

    def test_rejects_green_test(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["gates"] = [{"id": "g", "title": "t", "requires": "green-test"}]
        errs = validate.validate(_pack(body))
        self.assertTrue(any("green-test" in e or "human-yes" in e for e in errs))

    def test_rejects_model_liked_it(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["gates"] = [{"id": "g", "title": "the model liked it", "requires": "human-yes"}]
        errs = validate.validate(_pack(body))
        self.assertTrue(any("model liked" in e for e in errs))

    def test_rejects_missing_dockerfile(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        errs = validate.validate(_pack(body, dockerfile=None))
        self.assertTrue(any("Dockerfile" in e for e in errs))

    def test_rejects_dockerfile_without_expose(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        errs = validate.validate(_pack(body, dockerfile="FROM alpine\nCMD true\n"))
        self.assertTrue(any("EXPOSE" in e for e in errs))

    def test_rejects_api_in_json(self):
        body = json.loads((EXAMPLE / "app.json").read_text())
        body["api"] = {"call": True}
        errs = validate.validate(_pack(body))
        self.assertTrue(any("api" in e for e in errs))


if __name__ == "__main__":
    unittest.main()
