# Maintaining this site

The documentation is built with MkDocs and Material for MkDocs. Markdown in `readme_docs/` is the canonical site content; it remains readable directly on GitHub. `mkdocs.yml` defines navigation, search, syntax highlighting, Mermaid diagrams, and strict link validation.

## Local build and preview

From the repository root, using Python 3.12 or later:

```sh
python3 -m venv .venv-docs
. .venv-docs/bin/activate
python -m pip install -r requirements-docs.txt
python tools/build_docs.py
python -m http.server 8000 --directory site
```

Open `http://localhost:8000`. Re-run the build after editing source pages and refresh the browser. Generated files live in `build/docs/` and `site/`; both are ignored by Git. Do not edit generated files. No firmware build or submodule checkout is required for the documentation build.

The builder stages the Markdown, imports root `RELEASES.md` as a site page, and includes the existing firmware installer at `install/index.html`. Root `manifest.json` and `firmware/` URLs are retained for existing consumers. It verifies that every manifest firmware path exists before building with `mkdocs build --strict`.

## GitHub Pages deployment

In the repository's **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. Ensure repository Actions are enabled and the `github-pages` environment permits deployment from `main`. This is the one-time repository setup required by [GitHub's custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

The workflow in `.github/workflows/documentation.yml`:

1. Builds and validates pull requests targeting `main`, without deployment permissions.
2. Builds every push to `main`, including merges, and uploads `site/` as the Pages artifact.
3. Deploys the successful artifact using the `github-pages` environment and the workflow's short-lived token.
4. Supports manual runs; deployment is restricted to `main`.

There is no deployment branch or personal access token. After a successful deployment, the expected project URL is [ROSMicroPy.github.io/ROSMicroPy/](https://ROSMicroPy.github.io/ROSMicroPy/). For forks or custom domains, update `site_url` and repository links in `mkdocs.yml` and the documentation.

## Content conventions

- Add new pages to `readme_docs/` and list them in the navigation.
- Use relative `.md` links between documentation pages, so MkDocs can validate and rewrite them.
- Link to repository files outside the site using full GitHub URLs.
- Keep code samples consistent with the embedded implementation; document compatibility boundaries explicitly.
- Edit release notes in root `RELEASES.md`; the build imports them automatically.
- Keep historical documents under `old_docs/` out of the current navigation.

## Firmware loader ownership

`docs/` remains the source for the existing standalone installer. Its firmware assets are deliberately separate from Markdown documentation. The workflow publishes both together; there is no need to move or replace the existing directory. See [Building firmware](building-firmware.md#refresh-the-browser-installer) for asset updates.

The installer loads ESP Web Tools from its existing external URL. Documentation text and search are built into the site; Mermaid diagrams require JavaScript in the browser.
