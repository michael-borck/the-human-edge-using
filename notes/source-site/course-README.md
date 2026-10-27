# The Human Edge: using and delivering AI with judgement

Materials and companion site for a one-day Curtin Executive Education masterclass. It was first marketed as *AI for professionals: building everyday capability*; the companion masterclass is *AI in Strategy: Choosing where to invest*.

**Live site:** https://michael-borck.github.io/the-human-edge/

## The course

Everyone has the same AI tools now, so the edge is judgement. The day runs four sessions, each built around one tool, with the rhythm *a few slides, then an exercise* all day.

| Session | Time | Tool | Question | Exercises |
|---|---|---|---|---|
| 1 · Judge | 9:00 | Trust tool | How much should I trust this output? | 1 Your pass first · 2 Place it (blind vote and game) |
| 2 · Brief | 11:00 | RTCF and four upgrades | How do I ask for what I need? | 3 Brief it · 4 Upgrade and save |
| 3 · Check | 1:15 | Check loop | How do I know it's right? | 5 RetailFlow analysis and verification challenge · 6 Decide like me |
| 4 · Deliver | 3:00 | Opportunity Finder (spot, assign, prioritise), Scale/Pivot/Kill | Where does it fit, and will it work every week? | 7 Plan one delivery · 8 Action plan |

What participants leave with: a personal prompt library (Exercise 4); the rules behind one of their own decisions, tested blind against their past calls, with a list of what stays theirs (Exercise 6); four reusable decision tools (field guide and desk card); a delivery plan for one real workflow with human checkpoints and a 30-day gate (Exercise 7); and an action plan (Exercise 8).

## Layout

```
deck/            The slides: deck.html (with speaker notes), deck.css, deck.js
handouts/        Field guide, desk card, optional voting cards (HTML, printed to PDF), print.css
site/            Companion site pages (Markdown, rendered with pandoc): home, before, tools, exercises, workbook, prompts,
                 prompt builder, go deeper, decide like me, beyond the day, responsible use, resources, quiz. prompts.md also builds the starter prompt PDF
assets/          Site stylesheet, favicon, and local copies of the fonts
data/            RetailFlow customer service dataset (Exercise 5); prompt-injection demo document (build/make_demo_doc.py)
instructor/      Facilitator guide, optional agent demo kit (not published)
build/           build.py, screens.py, pandoc templates
docs/            Generated site, served by GitHub Pages. Don't edit; rebuild.
```

## Build

Needs `pandoc`, `weasyprint`, Python with `playwright`, and Google Chrome.

```sh
python3 build/build.py            # site, workbook, public deck, PDFs
python3 build/build.py --no-pdf   # quick rebuild of pages and deck
python3 build/screens.py          # render every slide to PNG for checking
```

The build publishes a copy of the deck with all speaker notes removed and the instructor-only answer slide (`data-private="true"`) dropped. The repository is public, so `instructor/` is readable on GitHub even though it isn't on the site.

Preview locally with `python3 -m http.server -d docs`.

## Presenting

Open `deck/deck.html` from the repo (not the site): it has the notes and the answer slide. Keys: arrows, Space or a clicker to advance; `1` to `4` to jump to a session; `N` for the presenter window; `T` to start the exercise timer; `B` to blank the screen; `F` for full screen. It uses local fonts and runs offline. See `instructor/facilitator-guide.md` for the run sheet, card-vote scenarios and answer keys.

## Editing

- **Slides:** edit `deck/deck.html`. Each slide is a `<section>` with `data-ch` (session 0 to 3). Steps reveal with `data-s="1"`, `data-s="2"` and so on. Exercise slides use `class="slide ex"`, `data-min` for the timer, and `data-steps="1"` to switch from instructions to debrief. Speaker notes go in `<aside class="notes">`.
- **Site:** edit `site/*.md`. Pandoc fenced divs (`::: card`) give the cards and notes.
- **Handouts:** edit `handouts/field-guide.html`, `handouts/desk-card.html`, `handouts/voting-cards.html` or `site/prompts.md`. The digital workbook is `site/workbook.md` (fields, autosave and export in one file).

The trust tool's corner names and orientation (precision across, consequences up) match the practice game at trusttool.borck.education. Keep them in step.

## Sources and credits

- Australian evidence: DEWR (2026) *AI and employment in Australia*; Jobs and Skills Australia (2025) *Generative AI Capacity Study*. US: Brynjolfsson, Chandar & Chen (rev. 2026) "Canaries in the Coal Mine?".
- The "broken ladder" framing of the junior pipeline problem, and the decide-like-me method (Exercise 6 and the Decide like me page), draw on Dylan Davis. Slides and text are original.
- "Gell-Mann amnesia" is Michael Crichton's term (2002).
- The delivery-is-different table, data governance, the quiet-defaults activity, ethics dilemmas, go-deeper techniques and the quiz were carried over from the earlier Human Edge site, now archived at github.com/michael-borck/the-human-edge-archive.
- The trust tool, RTCF and conversation-not-delegation ideas: *Conversation, Not Delegation* (michael-borck.github.io/conversation-not-delegation).

## Licence

MIT for code. Course content © Michael Borck. Fonts (Domine, Funnel Sans, Nanum Gothic Coding) are under the SIL Open Font License.
