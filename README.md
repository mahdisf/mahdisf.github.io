# mahdisf.ir

Source for [mahdisf.ir](https://mahdisf.ir/), the portfolio of Mahdi Sarfarazi, a technical product manager for AI and engineering software. It is a bilingual (English and Persian) Hugo site using the PaperMod theme, with a custom design layer on top.

## Where things live

| Path | What it holds |
| --- | --- |
| `data/home/en.yaml`, `data/home/fa.yaml` | Homepage copy |
| `data/publications.yaml` | Publications and their status labels |
| `content/projects/` | Case studies (English), with Persian card text in each page's `fa:` front matter |
| `content/about.md`, `content/now.md`, `content/contact.md` | Main pages; each has a `.fa.md` Persian twin |
| `layouts/` | Templates that override or extend PaperMod |
| `assets/css/extended/custom.css` | Colours, type and components |
| `static/` | Files served as-is (CV PDF, images, CMS) |

The theme in `themes/PaperMod` is vendored and should not be edited. `public/` is build output and is not committed.

## Run it locally

Install Hugo extended 0.161.0, the same version the deploy workflow uses, then run:

```bash
hugo server
```

## Publish

Pushing to `main` runs `.github/workflows/static.yml`, which builds the site and deploys it to GitHub Pages. The custom domain is set in the repository's Pages settings.

## Quarterly update

The site is built to need attention about once a quarter:

1. Rewrite `content/now.md` and `content/now.fa.md`, and set `updated:` in both to the date you make the change.
2. Add or update any case study, publication status or job detail that has changed.
3. Run `hugo server`, check the pages, then push to `main`.

If a quarter is missed, the Now page shows visitors a short note that the update is more than three months old. The copyright year updates on each build.

## License

The theme's license is in `themes/PaperMod/LICENSE`.
