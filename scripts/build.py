"""Build the static academic homepage. Python 3 standard library only."""
from pathlib import Path
from html import escape as esc
import json
import re

ROOT = Path(__file__).resolve().parents[1]
profile = json.loads((ROOT / 'data/profile.json').read_text(encoding='utf-8'))
papers = json.loads((ROOT / 'data/publications.json').read_text(encoding='utf-8'))


def author_html(author):
    name = author.rstrip('#*')
    marks = author[len(name):]
    label = f'<strong>{esc(name)}</strong>' if name == profile['name'] else esc(name)
    return label + (f'<sup>{esc(marks)}</sup>' if marks else '')


def publication(p):
    authors = ', '.join(author_html(a) for a in p['authors'])
    citation = p['citation'].rstrip('.')
    accepted = '<span class="status">Accepted</span>' if p['status'] == 'Accepted' else ''
    code = f'<a class="paper-link" href="{esc(p["code"])}">Code <span aria-hidden="true">↗</span></a>' if p['code'] else ''
    search = esc(' '.join([p['title'], ' '.join(p['authors']), citation]).lower(), quote=True)
    return f'''<li class="publication" data-year="{p['year']}" data-lead="{str(p['lead']).lower()}" data-search="{search}">
      <div class="paper-index" aria-hidden="true">{p['id']:02}</div>
      <article><div class="paper-topline"><span class="venue-label">{esc(p['venue_short'])}</span><span class="paper-year">{p['year']}</span>{accepted}</div>
      <h3>{esc(p['title'])}</h3><p class="authors">{authors}.</p>
      <p class="citation">{esc(citation)}.</p>{code}</article></li>'''


def education():
    return ''.join(f'''<li><div class="edu-years">{esc(e['years'])}</div><div><h3>{esc(e['institution'])}</h3><p>{esc(e['degree'])}</p><p class="education-zh" lang="zh-CN">{esc(e['institution_zh'])}</p></div></li>''' for e in profile['education'])


def header(cv=False):
    prefix = 'index.html' if cv else ''
    return f'''<a class="skip-link" href="#main">Skip to content</a>
    <header class="masthead"><div class="masthead-inner"><a class="brand" href="index.html">Langtao Zhou<span class="brand-dot">.</span></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="navigation" type="button"><span class="menu-icon" aria-hidden="true">☰</span> Menu</button>
    <nav id="navigation" aria-label="Main navigation"><a href="{prefix}#about">About</a><a href="{prefix}#research">Research</a><a href="{prefix}#publications">Publications</a><a href="{prefix}#education">Education</a><a href="cv.html"{' aria-current="page"' if cv else ''}>CV <span aria-hidden="true">↗</span></a></nav></div></header>'''


def head(title):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title><meta name="description" content="Langtao Zhou (周浪涛), Ph.D. student at Beijing Institute of Technology. Research in medical image analysis, generative models, and medical artificial intelligence.">
    <meta name="theme-color" content="#17695e"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="Medical image analysis · Medical artificial intelligence · Beijing Institute of Technology"><meta property="og:type" content="website"><meta property="og:url" content="https://zltshadow.github.io/"><meta property="og:image" content="https://zltshadow.github.io/assets/portrait-formal.png">
    <link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"><script src="assets/site.js" defer></script></head>'''


sidebar = '''<aside class="sidebar" aria-label="Author profile"><img class="portrait" src="assets/portrait-formal.png" width="164" height="190" alt="Portrait of Langtao Zhou" fetchpriority="high">
    <h2 class="author-name">Langtao Zhou</h2><p class="chinese-name" lang="zh-CN">周浪涛</p><p class="author-role">Ph.D. student<br> Optical Engineering</p>
    <p class="affiliation">School of Optics and Electronics<br> Beijing Institute of Technology</p>
    <div class="profile-rule"></div><ul class="profile-links">
    <li><span class="link-icon" aria-hidden="true">⌖</span>Beijing, China</li>
    <li><span class="link-icon" aria-hidden="true">@</span><a href="mailto:zlt_shadow@163.com">zlt_shadow@163.com</a></li>
    <li><span class="link-icon" aria-hidden="true">⌘</span><a href="https://github.com/zltshadow">GitHub <span aria-hidden="true">↗</span></a></li>
    <li><span class="link-icon orcid-icon" aria-hidden="true">iD</span><a href="https://orcid.org/0000-0002-4290-867X">ORCID <span aria-hidden="true">↗</span></a></li>
    <li><span class="link-icon" aria-hidden="true">R</span><a href="https://www.researchgate.net/profile/Langtao-Zhou">ResearchGate <span aria-hidden="true">↗</span></a></li></ul>
    <a class="cv-link" href="cv.html">View curriculum vitae <span aria-hidden="true">↗</span></a></aside>'''

research = '''<div class="research-list">
    <div><span class="research-number">01</span><div><h3>Generative medical imaging</h3><p>Anatomy-aware diffusion models, missing-modality MRI synthesis, and pre-to-postoperative CT prediction.</p></div></div>
    <div><span class="research-number">02</span><div><h3>Segmentation &amp; diagnosis</h3><p>Fine-grained 3D anatomy segmentation and multimodal disease diagnosis with Mamba, CNNs, and foundation models.</p></div></div>
    <div><span class="research-number">03</span><div><h3>Image restoration &amp; quantitative analysis</h3><p>CT metal artifact reduction, cardiac MRI radiomics, and cerebrovascular imaging for clinical assessment.</p></div></div></div>'''

footer = '''<footer class="footer"><div><span>© 2026 Langtao Zhou</span><span>Last updated: October 2026</span></div><p>Design inspired by <a href="https://academicpages.github.io/">Academic Pages</a> · <a href="https://github.com/zltshadow/zltshadow.github.io">Source</a></p></footer>'''

home = head('Langtao Zhou | Medical Image Analysis') + '<body>' + header() + f'''
<div class="site-layout">{sidebar}<main id="main">
<section id="about" class="about-section"><p class="eyebrow">MEDICAL IMAGE ANALYSIS · MEDICAL AI</p><h1>About me<span class="heading-dot">.</span></h1>
<p class="intro">I study how artificial intelligence can help us see, understand, and quantify medical images.</p>
<p>I am a Ph.D. student in Optical Engineering at <a href="https://www.bit.edu.cn/">Beijing Institute of Technology</a>, in the School of Optics and Electronics. My research focuses on medical image analysis and medical artificial intelligence, particularly image synthesis, segmentation, and multimodal diagnosis.</p>
<p>My work spans orbital MRI and CT, temporal bone CT, cerebrovascular imaging, and cardiac MRI. I am interested in combining anatomical priors with generative models and representation learning to address challenges in clinical imaging.</p>
<p>I received my master’s degree in Cyberspace Security from Guangzhou University in 2024 and my bachelor’s degree in Information Engineering from Beijing Technology and Business University in 2017. Before graduate study, I worked in web and cross-platform software development.</p>
<div class="intro-links"><a href="#publications">Explore my publications <span aria-hidden="true">↓</span></a><a href="mailto:zlt_shadow@163.com">Get in touch <span aria-hidden="true">↗</span></a></div>
</section>
<section id="research"><div class="section-heading"><h2>Research interests</h2><span>Methods × clinical imaging</span></div>{research}</section>
<section id="publications"><div class="section-heading"><h2>Publications</h2><span>2023–2026</span></div>
<p class="section-intro">17 representative publications, including 12 as first, co-first, or corresponding author. Includes accepted papers.</p>
<p class="author-legend"><strong>Langtao Zhou</strong> · <sup>#</sup> Equal contribution · <sup>*</sup> Corresponding author</p>
<div class="publication-controls"><div class="filter-buttons" role="group" aria-label="Filter by authorship"><button type="button" class="filter-button active" data-filter="all" aria-pressed="true">All <span>17</span></button><button type="button" class="filter-button" data-filter="lead" aria-pressed="false">First / corresponding <span>12</span></button></div>
<div class="search-controls"><label class="sr-only" for="paper-search">Search publications</label><input id="paper-search" type="search" placeholder="Search title, author, journal…"><label class="sr-only" for="year-filter">Filter by year</label><select id="year-filter"><option value="all">All years</option><option>2026</option><option>2025</option><option>2024</option><option>2023</option></select></div></div>
<p id="result-count" class="result-count" aria-live="polite">Showing all 17 publications</p>
<ol class="publications-list">{''.join(publication(p) for p in papers)}</ol><p id="no-results" hidden>No publications match your search. Try a different title, author, or year.</p>
</section>
<section id="education"><div class="section-heading"><h2>Education</h2><span>Academic background</span></div><ol class="education-list">{education()}</ol></section>
<section id="experience"><div class="section-heading"><h2>Earlier experience</h2></div><div class="experience-row"><span class="edu-years">2017 — 2021</span><div><h3>Web &amp; cross-platform development</h3><p>Software development experience across web applications, enterprise systems, and mobile applications, from implementation to deployment.</p></div></div></section>
<section id="contact" class="contact-section"><p class="eyebrow">LET’S CONNECT</p><h2>Interested in medical imaging research?</h2><p>Feel free to reach out to discuss research and potential collaborations.</p><a href="mailto:zlt_shadow@163.com">zlt_shadow@163.com <span aria-hidden="true">↗</span></a></section>
</main></div>{footer}</body></html>'''

cv = head('Curriculum Vitae | Langtao Zhou') + '<body class="cv-page">' + header(True) + f'''<main id="main" class="cv-main"><div class="cv-top"><div><p class="eyebrow">CURRICULUM VITAE</p><h1>Langtao Zhou <span lang="zh-CN">周浪涛</span></h1></div><button class="print-button" type="button">Print / Save PDF</button></div><p>Ph.D. student · Optical Engineering · Beijing Institute of Technology</p><p><a href="mailto:zlt_shadow@163.com">zlt_shadow@163.com</a> · <a href="https://github.com/zltshadow">GitHub</a> · <a href="https://orcid.org/0000-0002-4290-867X">ORCID</a></p>
<section><h2>Research interests</h2><p>Medical image synthesis and restoration; anatomical segmentation; multimodal diagnosis; radiomics and quantitative imaging.</p></section>
<section><h2>Education</h2><ol class="education-list">{education()}</ol></section>
<section><h2>Experience</h2><p><strong>Web &amp; cross-platform development</strong> · 2017–2021</p><p>Development of web applications, enterprise systems, and mobile applications.</p></section>
<section><h2>Representative publications</h2><p>First / co-first / corresponding author: 12 of 17 papers (including accepted papers).</p><p class="author-legend"><sup>#</sup> Equal contribution · <sup>*</sup> Corresponding author</p><ol class="publications-list">{''.join(publication(p) for p in papers)}</ol></section></main>{footer}</body></html>'''

(ROOT / 'index.html').write_text(home, encoding='utf-8')
(ROOT / 'cv.html').write_text(cv, encoding='utf-8')
print(f'Built index.html and cv.html from {len(papers)} publications.')
