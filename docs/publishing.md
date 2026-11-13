# Publishing the engineering website

[← Technical documentation](README.md) · [← Repository](../README.md)

## How it works

The public site is generated directly from the repository case study.

The script in scripts/prepare_docs_site.py copies **only the allowlisted Markdown documentation** and selected public policies into a temporary directory. MkDocs Material builds the static site from those files.

The public site does **not** connect to the private Cercle 8 application or its third-party accounts.

## Activation in GitHub

1. Open repository Settings → Pages.
2. Set Build and deployment → Source to GitHub Actions.
3. Open Actions → Engineering portfolio website.
4. Use Run workflow on the main branch.
5. Check that both Build engineering website and Publish GitHub Pages site succeed.

Expected project URL: https://lilouwen.github.io/cercle8-engineering/

This URL should not be presented as active until GitHub confirms publication. Normal commits and pull requests trigger **build validation only**. Publication is intentionally a manual action.

## Optional local preview

Run these commands from the repository root:

    python3 -m pip install -r requirements-docs.txt
    python3 scripts/prepare_docs_site.py
    mkdocs serve

For a static build:

    python3 scripts/prepare_docs_site.py
    mkdocs build --clean --site-dir site

Generated .site-docs and site directories are Git-ignored.

## Evidence boundary

The case study is about software architecture and engineering decisions, not claims of a production security audit or full V1 completion. Publishing does not require proprietary code, credentials, customer data or commercial analytics.
