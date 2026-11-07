import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("render_projects", ROOT / "tools/render_projects.py")
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class ProjectRenderingTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
        self.template = (ROOT / "templates/projects.html").read_text(encoding="utf-8")
        self.page = (ROOT / "index.html").read_text(encoding="utf-8")

    def test_committed_page_is_current_and_regeneration_is_idempotent(self):
        generated = renderer.render_projects(self.data, self.template)
        updated = renderer.update_page(self.page, generated)
        self.assertEqual(self.page, updated)
        self.assertEqual(updated, renderer.update_page(updated, generated))

    def test_text_and_attributes_are_escaped(self):
        self.data["savvit"]["summary"] = '<script>alert("x")</script>'
        self.data["savvit"]["evidence"][0]["accessible_label"] = '" onfocus="alert(1)'
        generated = renderer.render_projects(self.data, self.template)
        self.assertNotIn("<script>", generated)
        self.assertIn("&lt;script&gt;", generated)
        self.assertIn('&quot; onfocus=&quot;', generated)

    def test_optional_evidence_is_rendered_only_when_present(self):
        before = renderer.render_projects(self.data, self.template)
        self.assertNotIn("Try demo", before)
        self.data["search"]["evidence"].append({
            "label": "Try demo", "url": "https://example.com/demo?a=1&b=2",
            "accessible_label": "Try the search demo",
        })
        after = renderer.render_projects(self.data, self.template)
        self.assertIn("Try demo", after)
        self.assertIn("demo?a=1&amp;b=2", after)

    def test_invalid_urls_are_rejected(self):
        for url in ("javascript:alert(1)", "http://example.com", "//example.com",
                    "https://user:secret@example.com", "https://example.com/a b",
                    "https://", "https://example.com:bad", "https://example.com/\\x"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                renderer.evidence_url(url)

    def test_invalid_data_is_rejected(self):
        mutations = [
            lambda d: d.pop("savvit"),
            lambda d: d["savvit"].update(summary=""),
            lambda d: d["savvit"].update(technologies=[]),
            lambda d: d["savvit"].update(evidence=[]),
            lambda d: d["savvit"].update(unexpected=True),
            lambda d: d["savvit"]["evidence"][0].pop("url"),
        ]
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                data = copy.deepcopy(self.data)
                mutate(data)
                with self.assertRaises(ValueError):
                    renderer.render_projects(data, self.template)

    def test_missing_duplicate_or_reordered_markers_are_rejected(self):
        for page in ("", renderer.BEGIN * 2 + renderer.END,
                     renderer.END + renderer.BEGIN):
            with self.subTest(page=page), self.assertRaises(ValueError):
                renderer.update_page(page, "")

    def test_template_mismatch_is_rejected(self):
        for template in ("", self.template + "$unknown",
                         self.template + "${savvit_title}"):
            with self.subTest(template=template), self.assertRaises(ValueError):
                renderer.render_projects(self.data, template)

    def test_check_detects_stale_html_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "templates").mkdir()
            (root / "data/projects.json").write_text(json.dumps(self.data), encoding="utf-8")
            (root / "templates/projects.html").write_text(self.template, encoding="utf-8")
            page = root / "index.html"
            stale = self.page.replace("ranked results.", "stale results.")
            page.write_text(stale, encoding="utf-8")
            with patch.object(renderer, "ROOT", root):
                self.assertEqual(1, renderer.main(["--check"]))
                self.assertEqual(stale, page.read_text(encoding="utf-8"))
                self.assertEqual(0, renderer.main([]))
                self.assertEqual(0, renderer.main(["--check"]))


if __name__ == "__main__":
    unittest.main()
