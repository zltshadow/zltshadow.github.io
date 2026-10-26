# Langtao Zhou · Academic homepage

A lightweight academic website for Langtao Zhou (周浪涛), with an author sidebar,
research interests, representative publications, education, and a printable CV.
The layout takes inspiration from [Academic Pages](https://academicpages.github.io/)
and its [source](https://github.com/academicpages/academicpages.github.io).

## Preview

Run `python -m http.server 8765` from this directory, then open
<http://localhost:8765>. No package installation or Ruby/Jekyll runtime is needed.
`index.html` and `cv.html` are committed static pages; `.nojekyll` makes them usable
directly by GitHub Pages.

## Update content

- `data/publications.json`: publication order, authorship markers, year, venue,
  acceptance status, and verified public code links.
- `data/profile.json`: profile metadata and education records.
- `scripts/build.py`: biography, sections, page templates, and static rendering.
- `assets/style.css`: desktop, mobile, and print styles.
- `assets/site.js`: publication filters, search, mobile navigation, and CV printing.
- `assets/portrait-formal.png`: formal author portrait (AI-edited from the original photo).

After changing content, run `python scripts/build.py`. The publication list is
rendered into the HTML, so it stays readable with JavaScript disabled. JavaScript
adds combined authorship/year/search filters without third-party services.

On `cv.html`, choose **Print / Save PDF** to print the academic CV.

## Content basis

The 17 publications and author markers follow the author's updated
`近五年代表性成果.docx` (October 2026), preserving its order. TIP and QIMS are
marked accepted, as confirmed by the author. DOI fields are intentionally omitted.
The 12 first/co-first/corresponding papers include accepted papers.

Education and earlier software-development experience were checked against the
author's personal CVs. Only year ranges and professional details are included;
original CVs, identity documents, transcripts, and contact phone numbers are not
part of the site. The undergraduate CVs disagree on exact start/end months, so
only the consistent year range (2013–2017) is shown.

Public links checked during preparation:

- [GitHub profile](https://github.com/zltshadow)
- [DDKTN](https://github.com/zltshadow/DDKTN)
- [ASLDM](https://github.com/zltshadow/ASLDM)
- [MSHM](https://github.com/zltshadow/MSHM)
- [ORCID](https://orcid.org/0000-0002-4290-867X)

No citation counts, impact factors, or unverified awards are displayed.

## Previous site

All previous top-level content except `.git` was moved into the sibling directory
`../zltshadow.github.io-backup-20261026/` before this redesign. This backup sits
outside the published site. The original Git history and remote are preserved.
Changes have not been committed or pushed.

## Attribution

The sidebar and article composition were informed by Academic Pages' `single.html`,
`author-profile.html`, and `_sidebar.scss`. Upstream MIT terms are retained in
`LICENSE-ACADEMICPAGES`. This site is a standalone static implementation, rather
than a full Jekyll installation of the Academic Pages theme.
