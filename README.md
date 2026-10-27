# The Human Edge: Using AI with Judgement

A Quarto book by Michael Borck for professionals who use AI at work. When everyone has the same AI tools, generic competence is the baseline. The edge is judgement: knowing what to ask, when to trust the answer, and where a person stays in charge.

The free source and online edition are the primary versions. The book is built from the Curtin Executive Education one-day masterclass of the same name (four sessions: Judge, Brief, Check, Deliver; eight exercises; four reusable tools). RetailFlow and Northbridge are fictional teaching companies.

## Status

Seed manuscript, October 2026. Chapters 1 to 11 and Appendices A and F were drafted for the book from the course deck, facilitator guide, and field guide. Appendices B to E were converted from the course companion site. Verbatim course sources are archived under `notes/source-site/` for provenance. Editorial pass, fresh-reader pass, ISBN, and print build are pending. See `EDITORIAL-REVISION.md`.

The companion volume, *The Human Edge: Leading AI with Judgement*, is deliberately not part of this repo. Its course is still being redesigned. It gets its own book after it has run.

## Reading

Start with the Preface in `index.qmd`. Work the exercises in Appendix C as you finish each part. Exercise 5 and Chapter 6 use `resources/retailflow-customer-service-data.csv` (260 tickets). Nothing requires pasting confidential material into an AI tool.

## Build

```sh
quarto render --to html
quarto preview
```

From the parent books workspace, the shared publisher handles print:

```sh
python book-publisher/publish.py --book heu --audit
python book-publisher/publish.py --book heu --llm --preprocess --render
```

That builds locally. It does not push commits, publish GitHub Pages, or upload to KDP. PDF rendering needs the TeX toolchain. `print-config.yml` holds the 6 x 9 inch layout.

Do not edit generated `_print_source/`, `_book/`, or `llm.txt` as manuscript sources.

## Checks

```sh
python scripts/check_manuscript.py
```

Checks that every file named in `_quarto.yml` exists, that each chapter has exactly one H1, that no em-dashes or leftover site markup remain, and reports word counts. It does not certify factual accuracy or print layout. RetailFlow figures in Chapter 6 were recomputed from the CSV at seeding; recompute after any data change.

## Links

- [Online book](https://michael-borck.github.io/the-human-edge-using/) (after first publish)
- [The masterclass](https://michael-borck.github.io/the-human-edge/)
- [Conversation, Not Delegation](https://michael-borck.github.io/conversation-not-delegation/)
- [All books](https://books.borck.education)

Corrections and reproducible issue reports are welcome through this repository.

## Licence

Book content is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0 International)](https://creativecommons.org/licenses/by/4.0/). Original code examples and accompanying software are licensed under the [MIT License](https://opensource.org/licenses/MIT).

These grants cover material the author has authority to license. Separately credited third-party material retains its stated terms. The Decide Like Me method draws on Dylan Davis, as credited in Chapter 8.

See [LICENSE](LICENSE), [LICENSE-CONTENT.md](LICENSE-CONTENT.md) and [LICENSE-CODE.md](LICENSE-CODE.md).
