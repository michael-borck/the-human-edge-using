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

1. Editorial pass to house style across all seeds. Converted appendices need the closest look; site voice assumes the day happened ("on the day", "Exercise 4") in places the book must reframe. *Appendices B to E reframed for book readers on 2026-11-02 (see entry below). A full house-style pass across the chapters was not part of that work and is not certified here.*
2. Fresh-reader pass with one non-participant professional reader.
3. Recompute every RetailFlow figure from the CSV and record the script or worksheet used. *Chapter prose and the README state the figures were recomputed at seeding, but no script or worksheet is on record in this repo, and the 2026-11-02 pass did not recompute them. Recording the script or worksheet remains open.*
4. Trust Tool figure for Chapter 2 and Appendix A. The course site SVG was dropped during conversion; commission or redraw in the interior style rather than reusing the dark-site version.
5. ISBN application, KDP record in `publishing.yml`, print proof, cover collection pass.
6. GitHub repo creation (`michael-borck/the-human-edge-using`), first publish to GitHub Pages, AnythingLLM workspace and `chatbot.html` embed.
7. Book-site listing on books.borck.education and cross-links from the course site and from CND.
8. The course copy currently offers participants CND as the companion book. Decide whether the offer changes once this book publishes; involve Exec Ed if catalogue copy changes.

Known seed compromises, recorded honestly:

- Appendix C answer keys are in Chapter 6 and the facilitator guide, not in the appendix. Participants do the exercises blind; book readers may want a separate answers note. Decide at editorial pass. *2026-11-02: no new answer keys written. Appendix C now carries an explicit pointer in its introduction: Exercise 5 is worked in Chapter 6, the decision cards carry their own keys, and the other exercises run on the reader's own work. Whether to add a separate answers note remains an author decision.*
- Appendix E product details were checked October 2026 and will drift. Re-check at every reprint; that is why they live in one appendix.
- No `references.bib`. Sources are linked inline and collected in Appendix F, matching the course-site practice. Add a bib file only if the editorial pass wants formal citations.

## 2026-11-02: appendix reframe and first local online build

Built on the uncommitted author and humanizer edits already in the working tree. Nothing was reverted, committed, or pushed. Chapters were not edited in this pass, so the "In the masterclass / in class" anecdotes stand as sourced evidence. RetailFlow figures, Trust Tool tables, and the bold Corner A to D text in Chapter 2 were not touched. Every URL and in-book anchor present before the pass is still present after it (checked file by file against HEAD).

What changed, appendix by appendix:

- **Appendix B (Starter prompts).** Removed the leftover site introduction ("Copy, adapt, then check", "Twenty-seven prompts from the day", and the second corner key). The book introduction already states the contents and the corner key once, with the Chapter 2 reference.
- **Appendix C (The eight exercises).** Removed the site introduction ("Eight exercises. Mostly your own work" and "exports before you leave"), keeping the exercise table under the book introduction. Added the worked-answers pointer described above. Recast room instructions as reader instructions: the facilitator and ClassPulse blind vote became "commit blind" in writing, with the masterclass vote kept as past-tense explanation; "then tables", "room, then solo", "quiet, then share" and "then blind vote" became solo, in-pairs, or with-a-colleague timings; "why you came today", the "Before the day" prerequisite, "rule 2 from the morning", "today's baseline", "criteria you set today", "Before you leave", "on course days" and "if you didn't bring a decision" were recast to book voice (Chapter 2's second rule, "before you close the book", and past-tense references to masterclass participants where a course link is deliberately kept). All eight exercises, scenario cards, and decision cards are otherwise unchanged.
- **Appendix D (Responsible use).** Removed the site introduction ("Data, bias and ethics. Where a person stays in charge", "the whole day", "fast-finisher activity"). "Take one or two at your table" became "Take one or two into a team meeting, or work through them on your own". The four "*The link to the day:*" dilemma notes became "*The connection:*", and "the judgement the whole day is about" became "the judgement this book is about".
- **Appendix E.** Renamed from "Beyond the day" to "Beyond the chapters" (section id and filename unchanged, so cross-references are unaffected). Removed the site introduction ("The course was tool-agnostic. This page isn't", "come up in the room"), folding its contents list into the book introduction. Recast "All day you typed", "The day worked in text", "Two habits from the day", "Not on the agenda, but they come up in the room", "the day put the check", "Today you saw it fall short" and "The day's answers were" to chapters and book voice. The author additions already in the working tree (the Skill row and the *Build Web, Guide AI* note) were kept as written.

Builds run locally through `book-publisher` (no `--chatbot`, `--commit`, or `--publish`):

- `publish.py --book heu --preprocess --llm --rag`: print source regenerated; `llm.txt` refreshed (21 chapters, about 26,347 words as reported by the publisher); RAG documents extracted (21 files as reported).
- `publish.py --book heu --render`: HTML, PDF, and EPUB rendered. `_book/the-human-edge-using.pdf` is 144 pages at 6 x 9 in (877,992 bytes); `_book/the-human-edge-using.epub` is 941K; `llm.txt` copied into `_book/`.
- `publish.py --book heu --validate`: 0 errors. 21 HTML pages, 1,432 local targets and anchors checked, EPUB spine 24 entries, 53 distinct external URLs inventoried, not fetched.
- `python3 scripts/check_manuscript.py`: passed, 27,051 words.

Still open after this pass: item 1 beyond Appendices B to E, item 2 (fresh-reader pass), item 3 to the extent noted above, items 4 to 8, the Appendix E title change for author approval, and everything at push stage (repo publish, AnythingLLM workspace refresh via `--chatbot`, ISBN and print proof).

Item 3 update (2026-11-02, parent review): every RetailFlow figure quoted in Chapter 6 was recomputed from `resources/retailflow-customer-service-data.csv` and matches (260 tickets, 8 agents, overall 9.2h, channels 4.0/6.1/9.4/13.2, Sunday 13.7 vs Thursday 7.4, December 13.6 vs November 7.2, satisfaction 4.09 within 4h vs 1.64 over 12h, ratio 3.3). The recomputation is recorded in `scripts/recompute_retailflow.py`; run it after any change to the CSV or the chapter.
