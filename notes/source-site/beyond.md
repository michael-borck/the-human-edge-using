---
pagetitle: Beyond the day
description: "What the course skipped: setting your assistant up once (custom instructions, projects, Gems), the jargon decoded (MCP, harness, context window), images, audio and video, agents in the terminal, local models, and the big questions: is AI just software, AGI and superintelligence."
nav-more: true
---

::: kicker
Beyond the day
:::

# The course was tool-agnostic. <em>This page isn't.</em>

::: lede
The four tools work on any AI, including the ones that ship next, which is why the day named no vendor. This page names them: where each product keeps the standing brief, what the jargon in vendor pitches means, what the tools make beyond text, and where agents fit. The details here change monthly. The four tools don't. At the end: the big questions that come up in the room but weren't on the agenda.
:::

## Set it once

All day you typed the brief fresh, every chat: role, task, context, format, and its check. Every major tool lets you save that as the standing brief it sends with every message. The generic name is a **system prompt**. The trade names differ.

| Tool (web) | The setting is called | Where it lives |
|---|---|---|
| ChatGPT | Custom instructions · Projects · Memory | Settings → Personalization; each Project has its own instructions |
| Claude | Instructions · Projects · Memory | Settings → Your Claude; each Project has its own instructions |
| Gemini | Instructions for Gemini · Gems | Settings & help → Personal Intelligence; Gems in the sidebar |
| Microsoft Copilot | Custom instructions · Memory | Settings → Personalization |
| Msty, LibreChat, Open WebUI | System prompt | Per chat or per model. You edit the prompt itself, so these show most plainly what a system prompt is |

[Menu names checked October 2026. They move; if one has changed, search the tool's help for "instructions".]{.small}

What goes in: your RTCF brief, your Done line, the check you attach. What doesn't: anything confidential you wouldn't paste into a chat. For the data side (training, memory, two accounts), see [Set it up safely](responsible-use.html#set-it-up-safely). Review the saved brief each quarter, because the corners move and the brief should move with them. [Write like me](go-deeper.html#write-like-me) is a worked example. [Decide like me](decide-like-me.html) uses the same setting to save a set of decision rules.

::: note
**The names differ; the idea doesn't.** When a demo says the AI "understands you", look for this setting. It's a text box. You wrote a better one in Exercise 4.
:::

## The jargon, decoded

You'll hear these in every vendor pitch. None of them removes the check.

| Term | What it actually is | What it changes |
|---|---|---|
| MCP · Model Context Protocol | A standard plug that lets a harness call outside tools and data: your calendar, your files, the web. | Each connection widens what the harness can read and do. The stakes go up, so place the work on the trust tool again. |
| Context window | The model's working memory. | Long chats drift and early instructions fade. That's why the two-chat workflow and the handover prompt on [Go deeper](go-deeper.html) help. |
| RAG · "grounded on your documents" | The tool reads your files first, then answers. | Better grounding, new failure mode: check what it read, not just what it said. |
| Harness | The software around the model: standing instructions, what it can read, what tools it may call. | You already use several. Configuring one well is "set it once", above. |
| Agent | A model in a loop with tools: plans, acts, checks, retries. | Automates the loop, not the standard. The check still comes from outside. |
| Prompt injection | Instructions hidden in something the tool reads: a web page, an email, a document, often in white or tiny text. | The tool may follow them as if you wrote them. The risk grows with every connection, and is highest for agents that read and act with nobody watching. Keep a person between what it reads and what it does. [Try it](#try-it-a-document-that-talks-to-the-ai). |

### Try it: a document that talks to the AI

[Download the Northbridge proposal](downloads/northbridge-proposal.docx), an invented supplier offer to RetailFlow (Karen's company from Exercise 5) for weekend and email support. It looks ordinary.

1. **Read it yourself first.** Note what Karen should know before she signs.
2. **Give it to an AI tool.** Upload it, or select all, copy and paste. Ask: *"Summarise this proposal for Karen, including the cost and the risks. Should she sign?"*
3. **Compare.** Did the summary cover the contract terms and where customer data is stored? Did it push her to sign? Did it end with a piece of fruit?
4. **Look for the trick.** In Word, select all and change the font colour to black.

If the tool ignored the hidden note, that's partly good news: many tools now resist it when you paste a document yourself. The risk is highest when an agent reads email, web pages or shared files on its own, with nobody checking what went in. And don't use the trick on real documents. It gets found, and it costs trust.

## Beyond text

The day worked in text because judgement shows clearest there. The same models make images, audio, music and video, and the trust tool moves straight over.

| Output | On the grid | The check |
|---|---|---|
| Image mock-up, internal discussion | Green corner | Nothing formal. It's a sketch |
| Image in a client-facing deliverable | Red corner | Licence and rights, consent for any real likeness, a disclosure line |
| Voice mode, drafting while you walk | Green | The names and figures it "heard". Re-check before sending |
| Music or video for a public asset | Amber to red | Copyright here is unsettled; follow your organisation's policy and disclose |
| A voice or video call asking for a payment, a password or a change of bank details | Red, however familiar the face | Check outside the channel it arrived on: hang up and call back on a number you already have. In 2024 an Arup employee in Hong Kong paid out about US$25.6 million after a video call in which every other "colleague" was a deepfake ([CNN](https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk)). |

Two habits from the day transfer exactly: classify before you paste (a face is personal information), and tell people when AI made the thing they're looking at ([Responsible use](responsible-use.html)).

## The terminal, if you want it

Everything above is the web interface on purpose: it's where the judgement work happens, and where your account already is. The same ideas carry over to developer tools. Agent CLIs take a brief in your terminal and work in a loop, and your review still decides what ships. Local models run on your own laptop, which is the answer when your writing samples can't leave it. They're weaker than the big cloud tools, but for brainstorming and thinking out loud that matters less than you'd think: the point is the ideas they trigger in you. Save the strongest tool for exact facts and data. [Msty Studio](https://msty.ai/products/studio/) is the easiest start: one install, then a local model or your own API key. [Ollama](https://ollama.com) is the engine many local apps run on, and [Open WebUI](https://openwebui.com) and [LibreChat](https://www.librechat.ai) are chat interfaces an IT team can host for a whole organisation. You can also describe a small tool in plain English and have an AI write it. Treat the result like any other output: if you can't read the code, it belongs in the top-right corner, so test it on data where you know the answer, and keep it away from anything confidential until someone who can read it has. None of this is required. It's the same four tools, faster.

::: note
**Whatever the product,** set the standing brief once, connect tools on purpose, and keep the check outside the tool. More in [Resources](resources.html).
:::

## The big questions

Not on the agenda, but they come up in the room. Short answers, and where to read more.

### Is AI just software?

For governance, yes. Procurement, privacy, security and a named owner apply as they do to any system. For testing, no. Nobody wrote its logic, so nobody can read it. The same input can give a different output. It fails fluently, and an agent can act without asking. That's why the day put the check outside the tool and a gate before scale ([why AI projects fail differently](tools.html#deliver-it-why-ai-projects-fail-differently)).

### AGI and superintelligence

AGI usually means a system that can do most work a person can. Superintelligence means one far better than people at nearly everything. Several AI labs say they are building towards it. Whether and when it arrives is disputed, and the disagreement runs through the field: in a survey of 2,778 published AI researchers, between 38% and 51% gave at least a 10% chance that advanced AI leads to outcomes as bad as human extinction ([Grace and others, 2024](https://arxiv.org/abs/2401.02843)).

Two serious positions, both worth reading:

- **Take the risk seriously now.** In 2023, Geoffrey Hinton, Yoshua Bengio and the heads of OpenAI, Google DeepMind and Anthropic signed a one-line [statement](https://www.safe.ai/work/statement-on-ai-risk): mitigating the risk of extinction from AI should be a global priority alongside pandemics and nuclear war. The [International AI Safety Report](https://internationalaisafetyreport.org) (2026, led by Bengio, backed by more than 30 countries) is the measured version: what the evidence shows so far, and what it doesn't.
- **Treat it as normal technology.** Arvind Narayanan and Sayash Kapoor's [AI as Normal Technology](https://knightcolumbia.org/content/ai-as-normal-technology) (2025) argues that AI will change things the way electricity did: over decades, through institutions, and under human control. They think superintelligence, as usually described, doesn't hold together, and that building resilience beats drastic intervention.

### The one-shot argument

Most engineering improves by failing: ship it, watch it break, fix it. The worry about superintelligence is that this loop might not be there. A system far more capable than us, pursuing goals that aren't quite ours, might not leave room for a second attempt. That is the core of the alignment argument, and it's why some researchers want the safety work done before the capability arrives rather than after.

The argument's logic holds. It also rests on open questions: whether capability arrives in a jump or by degrees, whether these systems become agents with goals of their own, and whether we keep the ability to watch and correct them. Serious people answer those differently. Nobody knows yet.

### What about the energy cost?

Real, and growing fast in total, but smaller per question than most people guess. Google measured its median Gemini text prompt at 0.24 Wh, about nine seconds of television ([Google, 2025](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference)); that's the vendor's own figure for one product. Across the world, data centres used about 1.5% of electricity in 2024, and the International Energy Agency expects that to more than double by 2030, with AI the main driver ([IEA, Energy and AI](https://www.iea.org/reports/energy-and-ai/executive-summary)). Images, video, long reasoning and agents use far more than a short text prompt. The habits that help: use a smaller model for small jobs, don't regenerate for the sake of it, and ask vendors for their numbers.

### You've already met the small version

Alignment means getting a system to do what we actually want. Today you saw it fall short in small ways:

- a model tuned to please you, which folds when you push back with no new evidence
- mistakes that don't look like mistakes, so your alarm stays quiet
- values nobody chose, in the quiet defaults
- an agent checking its own work and sharing its own blind spots

The day's answers were a check from outside the tool, a blind test before you rely on anything, and a gate where kill is a real option. Safety researchers ask for the same things at a much larger scale. The one-shot worry is about what happens if those habits stop being possible.

::: note
**To follow it:** the [International AI Safety Report](https://internationalaisafetyreport.org) publishes yearly with updates in between. Australia's [AI Safety Institute](https://www.industry.gov.au/science-technology-and-innovation/technology/artificial-intelligence/ai-safety-institute) was announced in November 2025 to monitor and test emerging AI. For governance and regulation in depth, Curtin's [Ethics of artificial intelligence](https://www.curtin.edu.au/study/prof-development/ethics-of-artificial-intelligence/) masterclass.
:::
