#!/usr/bin/env python3
"""Stage the documentation and existing installer, then build GitHub Pages."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGED = ROOT / "build/docs"


def main():
    if STAGED.exists():
        shutil.rmtree(STAGED)
    shutil.copytree(ROOT / "readme_docs", STAGED)
    releases = (ROOT / "RELEASES.md").read_text()
    (STAGED / "releases.md").write_text(
        "---\nedit_uri: edit/main/RELEASES.md\n---\n\n"
        + releases.replace("(readme_docs/", "(")
    )
    loader = ROOT / "docs"
    manifest = json.loads((loader / "manifest.json").read_text())
    for build in manifest["builds"]:
        for part in build["parts"]:
            path = (loader / part["path"]).resolve()
            if not path.is_relative_to((loader / "firmware").resolve()) or not path.is_file():
                raise ValueError("Missing or invalid firmware path: " + part["path"])
    (STAGED / "install").mkdir()
    shutil.copy2(loader / "index.html", STAGED / "install/index.html")
    # Preserve published manifest/firmware URLs and make the relocated loader work.
    for destination in (STAGED, STAGED / "install"):
        shutil.copy2(loader / "manifest.json", destination / "manifest.json")
        shutil.copytree(loader / "firmware", destination / "firmware")
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--clean"],
        cwd=ROOT, check=True,
    )


if __name__ == "__main__":
    main()
