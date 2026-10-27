---
pagetitle: The four tools
description: "The trust tool, RTCF, the check loop and the Opportunity Finder: four tools for using AI with judgement."
nav-tools: true
---

::: kicker
The four tools
:::

# One question each. <em>All four work on any AI tool.</em>

::: lede
Each tool answers one question you'll face every time you use AI at work. The full version, with examples and worked cases, is in the [field guide (PDF)](downloads/field-guide.pdf).
:::

| Tool | The question | The move |
|---|---|---|
| [1 · Trust tool](#trust-tool) | How much should I trust this output? | Two questions place it in a corner; the corner sets the check. |
| [2 · RTCF](#rtcf) | How do I ask for what I need? | Brief it like a capable new colleague. Context does most of the work. |
| [3 · Check loop](#check-loop) | How do I know it's right? | Frame, explore, verify from outside, then say what you checked. |
| [4 · Opportunity Finder](#opportunity-finder) | Where does AI fit, and will it work every week? | Spot, assign, prioritise; then deliver with checkpoints and a 30-day gate. |

## 1 · The trust tool {#trust-tool .s1}

Ask two questions about any output before you act on it.

- **How exact must it be?** *Average* means the ballpark is fine: a draft, a summary, ideas. *Precise* means there's one right answer and close is the same as wrong: a figure, a name, a date, a citation.
- **What happens if it's wrong?** *Small* means cheap to fix and nobody harmed. *Large* means money, safety, reputation, or someone's job or wellbeing.

<figure>
<svg viewBox="0 0 640 400" role="img" aria-label="The trust tool: a two by two grid. Precision needed runs across, from average to precise. Consequences if wrong run up, from small to large. Bottom left: trust with light review. Top left: verify the load-bearing bits. Bottom right: verify before you ship. Top right: human in the loop.">
  <g font-family="Funnel Sans, sans-serif">
    <rect x="72" y="10" width="270" height="170" rx="10" fill="rgba(232,181,77,.10)" stroke="rgba(232,181,77,.5)"/>
    <rect x="350" y="10" width="270" height="170" rx="10" fill="rgba(229,116,90,.14)" stroke="rgba(229,116,90,.6)"/>
    <rect x="72" y="188" width="270" height="170" rx="10" fill="rgba(108,197,154,.10)" stroke="rgba(108,197,154,.5)"/>
    <rect x="350" y="188" width="270" height="170" rx="10" fill="rgba(232,181,77,.10)" stroke="rgba(232,181,77,.5)"/>
    <g font-family="Nanum Gothic Coding, monospace" font-size="11" font-weight="700" letter-spacing="1">
      <text x="88" y="38" fill="#E8B54D">VERIFY THE LOAD-BEARING BITS</text>
      <text x="366" y="38" fill="#E5745A">HUMAN IN THE LOOP</text>
      <text x="88" y="216" fill="#6CC59A">TRUST WITH LIGHT REVIEW</text>
      <text x="366" y="216" fill="#E8B54D">VERIFY BEFORE YOU SHIP</text>
    </g>
    <g font-size="15" fill="#ECE7DB">
      <text x="88" y="62">Check the claims it rests on.</text>
      <text x="366" y="62">AI can help. A person decides.</text>
      <text x="88" y="240">Use it. Skim before it goes out.</text>
      <text x="366" y="240">Check every figure, name, date.</text>
    </g>
    <g font-size="13" fill="rgba(236,231,219,.6)">
      <text x="88" y="160">e.g. a strategy memo for the exec team</text>
      <text x="366" y="160">e.g. the figures in a board paper</text>
      <text x="88" y="338">e.g. a birthday message for a colleague</text>
      <text x="366" y="338">e.g. a statistic quoted in a newsletter</text>
    </g>
    <line x1="58" y1="358" x2="58" y2="12" stroke="rgba(236,231,219,.6)" stroke-width="1.5"/><path d="M52 20 L58 8 L64 20" fill="none" stroke="rgba(236,231,219,.6)" stroke-width="1.5"/>
    <line x1="72" y1="372" x2="622" y2="372" stroke="rgba(236,231,219,.6)" stroke-width="1.5"/><path d="M614 366 L626 372 L614 378" fill="none" stroke="rgba(236,231,219,.6)" stroke-width="1.5"/>
    <g font-family="Nanum Gothic Coding, monospace" font-size="11" letter-spacing="1.2" fill="rgba(236,231,219,.6)">
      <text transform="translate(44 184) rotate(-90)" text-anchor="middle">CONSEQUENCES IF WRONG</text>
      <text x="346" y="394" text-anchor="middle">PRECISION NEEDED</text>
    </g>
  </g>
</svg>
<figcaption>Same layout and corner names as the practice game below.</figcaption>
</figure>

**Rule of thumb:** lean in where about-right on low stakes is fine; keep a person in charge where exactly-right meets high stakes.

**Check from outside the tool.** Asking the AI "are you sure?" doesn't count, because it tends to agree with itself. The check comes from the data, the source document, a colleague who knows, or your own arithmetic. Better models move the corners. They never remove the check.

**Sharp where you know, trusting where you don't.** You catch AI's errors in your own field, then believe it on the law, the market or the numbers. Be most sceptical where you know least. (Michael Crichton called this Gell-Mann amnesia, after the physicist Murray Gell-Mann.) The mirror-image trap is the *AI dismissal fallacy*: "that's just ChatGPT" isn't a critique. Judge the reasoning, not where it came from.

### Practise it

Ten scenarios from a domain you choose, with an explanation on every card. It runs full screen, on a laptop or a phone, with no login.

::: btns
[Play the trust tool game](https://trusttool.borck.education/){target="_blank" rel="noopener"}
:::

## 2 · RTCF {#rtcf .s2}

Prompting is briefing, not spell-casting. Write the prompt the way you'd brief a smart, fast colleague who is new to your job.

| Part | Ask yourself | Example |
|---|---|---|
| **Role** | Who should it write as? | A senior HR adviser in a mid-sized Australian firm |
| **Task** | What exactly, and how much? | Draft a reply to the client. Under 200 words. |
| **Context** | What does it need to know? | 18-month client. Their board shifted priorities. I want a meeting, not a rewrite. |
| **Format** | What should it look like? | Email. Acknowledge, explain, propose, close. |

Context does most of the work, because it's the only part the tool can't guess. Role does the least.

**One task, or every task.** RTCF shapes the prompt you type for one job. It also shapes the standing brief you save once in custom instructions, a project or a Gem. The standing brief holds what's true every time: who it writes as, the context that doesn't change, your format and your Done line. The task stays in the chat. [Set it once](beyond.html#set-it-once) shows where each tool keeps it.

**Still weak? Add one upgrade** before you rewrite from scratch. They help smaller, older and free-tier models the most.

| Upgrade | Line to add |
|---|---|
| + Example | `Match the length and tone of this example: [paste]` |
| + Done | `Done means under 200 words, figures only from my notes, and anything you're unsure of marked [CHECK].` |
| + Questions | `Before you start, ask me up to five questions.` |
| + Steps | `Give me an outline only. We'll draft one section at a time.` |

**Push back: three ways.** Models are tuned to please, and many fold the moment you disagree.

| Move | Line to add |
|---|---|
| Guardrail | `Only change your assessment if I give you a new fact. Name the fact that changed it.` |
| Devil's advocate | `Don't flatter me. Give me three reasons this fails, and name the assumption it all rests on.` |
| Board of directors | `Respond as a board: a CFO, a sceptical customer and a frontline manager. One paragraph each, then where they disagree.` |

Long chats drift towards your view. For an independent read, start a fresh chat.

[Build and save prompts with the prompt builder →](prompt-builder.html)

## 3 · The check loop {#check-loop .s3}

AI makes analysis fast. It doesn't make it trustworthy.

1. **Frame.** Write the question and the decision it feeds. Start a fresh chat.
2. **Explore.** Ask it to describe the data first: rows, columns, dates. Does that match what you know? Then go broad to deep.
3. **Verify.** If a number would change a decision, check it yourself: filter, recount, open the source. If it doesn't hold, go back.
4. **Shape.** Write for the reader. End with one line saying what you checked and how.

**Five ways a smooth answer goes wrong:** miscounts after filtering; correlation sold as cause; missing rows skipped silently; numbers that can't all be true; detail that isn't in the file.

**VET claims you can't check against your own data.** *Verify* the source yourself. *Explain* it back in your own words; if you can't, you don't understand it yet. *Test* the edges: when, where or for whom would it be wrong?

## 4 · The Opportunity Finder {#opportunity-finder .s4}

**1 · Spot.** Look for four signals in your week: work you do often the same way (*Automate*); reading, gathering and comparing (*Assist*); writing from a blank page (*Generate*); hunting for meaning in numbers (*Analyse*).

**2 · Assign who leads each step.**

| AI leads | AI assists | You lead | Human only |
|---|---|---|---|
| AI drafts it; you review and approve. | You steer; AI does much of the work. | You do the thinking; AI takes sub-tasks. | Empathy, ethics, accountability. |
| Minutes from your notes | A client proposal | A strategy paper | Telling someone their role is going |

**3 · Prioritise.** Start with quick wins: high time saved, low effort to set up. Count the checking as effort. Quick wins usually sit in the trust tool's green corner, because they're cheap to check.

### Deliver it: why AI projects fail differently

| You usually assume | With AI | So you |
|---|---|---|
| "Done" can be specified. | Outputs vary: a spread, not one right answer. | Decide what "good enough" means, up front. |
| A working demo means nearly there. | The demo is a trap; it shows the happy path. | Treat the demo as the start of the hard part. |
| The data is a known input. | The data is the uncertainty. | Plan for discovery, not slippage. |
| The build is the product. | Checking is the product. | Design the checking in, and ship it. |
| Capability is our edge. | Everyone has the same models. | Compete on your people's judgement. |

### Design the human in

A redesigned workflow is a small AI project. Decide four things before you start:

| Move | Decide |
|---|---|
| **Scope** | One workflow, one owner, one success measure. Record today's time and quality as the baseline. |
| **Checkpoints** | Every step in an amber or red corner gets a named person and a specific check. Pick someone who knows what right looks like, and keep at least one human step on purpose, to build capability. |
| **People** | Who's affected, who has to agree, who will do the checking. Tell them before you start. |
| **Gate** | A date, about 30 days out, and the criteria for each call below. |

At the gate: **scale** if it met the measure with a light review; **pivot** if it's close but the checking costs too much; **kill** if it missed or the errors mattered. Killing is a good outcome: you found where the line is, cheaply. Watch for three mistakes at the gate: sunk cost, cherry-picking the measures that passed, and treating "not perfect" as "broken".

::: note
**Delegate the task. Keep the learning.** Routine work used to teach you while you did it. When AI does it, practice is a choice. Once a week, do a rough pass of a task that matters yourself, then give AI the same brief and compare. Where it beat you is your blind spot; where you beat it is where its output needs your check. And revisit every few months: the corners move as models improve, but the check stays.
:::
