# Editorial revision log

## 2026-10-27: seed manuscript

Book scaffolded in the shared publisher structure from the *Prove, Don't Persuade* template (judgement family). Registry key `heu`.

Done at seeding:

- `_quarto.yml` with 11 chapters in four parts and six appendices, mirroring the masterclass sessions Judge, Brief, Check, Deliver.
- Standard front matter: Preface (new, with the vibe-professionalism framing), Copyright (HTML and PDF page), Acknowledgments, About the Author, licences copied from *Conversation, Not Delegation*.
- Chapters 1 to 11 drafted for the book from the course deck, facilitator guide, field guide, and companion site. Each file carries a provenance comment. Verbatim site sources archived in `notes/source-site/`.
- Appendices B to E converted from site Markdown: interactive elements (workbook, quiz, prompt builder) removed, internal links pointed at the live course site, site-only div markup stripped.
- RetailFlow dataset copied to `resources/` for Chapter 6 and Exercise 5. All figures in Chapter 6 taken from the facilitator answer key, which was checked against the CSV for the course; recompute before first print.
- Placeholder editorial cover generated from local Trust Tool artwork (`cover-art.png` plus editable `cover-art.svg`, recipe in `cover-design.yml`). Treat as a working cover until the collection pass.
- Book registered in `book-publisher/books.yml`, `publishing.yml` (not-yet-published, no ISBN), `design/books.yml` and `design/covers.yml` (judgement family, gold accent from the course site), and the workspace `README.md`.

Not done, in rough order:

1. Editorial pass to house style across all seeds. Converted appendices need the closest look; site voice assumes the day happened ("on the day", "Exercise 4") in places the book must reframe.
2. Fresh-reader pass with one non-participant professional reader.
3. Recompute every RetailFlow figure from the CSV and record the script or worksheet used.
4. Trust Tool figure for Chapter 2 and Appendix A. The course site SVG was dropped during conversion; commission or redraw in the interior style rather than reusing the dark-site version.
5. ISBN application, KDP record in `publishing.yml`, print proof, cover collection pass.
6. GitHub repo creation (`michael-borck/the-human-edge-using`), first publish to GitHub Pages, AnythingLLM workspace and `chatbot.html` embed.
7. Book-site listing on books.borck.education and cross-links from the course site and from CND.
8. The course copy currently offers participants CND as the companion book. Decide whether the offer changes once this book publishes; involve Exec Ed if catalogue copy changes.

Known seed compromises, recorded honestly:

- Appendix C answer keys are in Chapter 6 and the facilitator guide, not in the appendix. Participants do the exercises blind; book readers may want a separate answers note. Decide at editorial pass.
- Appendix E product details were checked October 2026 and will drift. Re-check at every reprint; that is why they live in one appendix.
- No `references.bib`. Sources are linked inline and collected in Appendix F, matching the course-site practice. Add a bib file only if the editorial pass wants formal citations.
