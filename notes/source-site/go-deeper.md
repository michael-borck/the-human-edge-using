---
pagetitle: Go deeper
description: "Self-paced extensions: VET in depth, the three cognitive traps, the two-chat workflow, the handover prompt, and Write like me: teaching it your voice."
nav-more: true
---

::: kicker
Go deeper
:::

# Five minutes each. <em>All on your own work.</em>

::: lede
For fast finishers on the day, or the week after. Each one keeps your judgement in charge from a different angle. Most are drawn from the free companion book, [*Conversation, Not Delegation*](https://michael-borck.github.io/conversation-not-delegation/).
:::

## VET, in depth

The trust tool tells you *how much* to check. VET tells you *how*, for claims you can't check against your own data. The most dangerous output isn't the obvious mistake; it's the one that sounds completely right.

| The AI says... | Verify | Explain | Test |
|---|---|---|---|
| "Studies show..." | Find the actual studies. | Can I explain the mechanism? | Does it hold in a different context? |
| "The best figure is X." | Where does that number come from? | Why X, specifically? | What happens if I change one variable? |
| "This method is 95% effective." | Source? | What does 95% mean here? | Under what conditions? |

- **Verify:** can I find this independently? AI produces plausible references that don't exist, because a fake citation is generated the same way as any other text. [CiteSight](https://citesight.eduserver.au) checks references for you.
- **Explain:** can I say it in my own words? Where you struggle to rephrase is where your understanding has a gap.
- **Test:** does it survive a "what if"? Change a variable, try an edge case. Fragile answers break; robust ones flex.
- **Verify the channel, not just the claim.** A voice or video asking for money, a password or new bank details gets checked outside the channel it came in on: hang up and call back on a number you already have. A familiar face on a call is no longer proof ([deepfakes on the trust tool](beyond.html#beyond-text)).

Use it hardest when a decision hangs on the claim, or when people will assume you checked. [Full chapter: VET your AI](https://michael-borck.github.io/conversation-not-delegation/chapters/vet-your-ai.html).

## The three cognitive traps

Not technical problems: human ones. Knowing their names is the first defence.

- **Gell-Mann amnesia.** You catch AI's errors in your own field, then trust it on the law, the market or the numbers, exactly where you're least able to check. Be more sceptical where you know less. (Michael Crichton named it in 2002, after the physicist Murray Gell-Mann.)
- **The AI dismissal fallacy.** "That's just ChatGPT" is a refusal to engage, not a critique. Judge the reasoning, not where it came from.
- **Sycophancy.** Models are tuned on human approval, and people prefer agreeable answers. Don't ask "what do you think?"; ask "what are the three weakest points in this?" See the push-back moves in the [starter prompts](prompts.html).

## The two-chat workflow

Separate thinking from building.

1. **Thinking chat.** Explore, challenge your assumptions, follow tangents, find out what your actual question is. Messy by design, and disposable.
2. **In between: you curate.** Read what came out, keep what matters, drop what doesn't, and write a short, focused brief. Don't copy and paste. That curation is where your judgement lives.
3. **Building chat.** A fresh chat that produces the output from your brief. Better input, better output.

Neither chat has the whole picture. Only you hold both, which is what "human in the loop" really means.

**Why the thinking chat works.** It triggers ideas in you. Research on teaching critical thinking keeps finding that dialogue is one of the strongest levers ([Abrami et al., 2015](https://doi.org/10.3102/0034654314551063)). That research is about people talking with people, so the AI version only works if it pushes back: use the [push-back moves](prompts.html#push-back), or it drifts towards your own view. And for thinking out loud, the model hardly matters. An average idea is fine and you're the filter, so a small or local model is enough. Save the strongest tool for exact facts and data.

## The handover prompt

Long chats drift and lose the thread. Before you close one, ask for a handover, then start fresh and paste it in. You keep the thinking and lose the noise.

```text
Write a handover prompt that captures everything important from this conversation: the context, the decisions made, open questions, and where we left off. I'll paste it into a new chat to continue.
```

Useful for anything that runs over several sessions: a proposal, a policy, a board paper.

## []{#make-your-voice-persistent}Write like me {#write-like-me}

Generic output sounds like everyone. The voice pass in Exercise 4 fixes one draft; this fixes every future one. It pairs with [Decide like me](decide-like-me.html): this teaches the tool how you sound, that teaches it how you choose. In both, it drafts and you decide. The prompts are [25 to 27](prompts.html#write-like-me) in the starter prompts.

1. Collect three or four things you've written that sound like you at your best: emails, reports, a proposal. Remove anything confidential.
2. Ask a model to describe your style as a two-page brief: sentence length, structure, vocabulary, how you open and close, what you never do. [Style Mirror](https://stylemirror.eduserver.au) does this step for you.
3. Read the brief critically. It will be slightly off, and slightly a parody. Edit it until it's right; that editing is your judgement.
4. Paste it into your tool's custom instructions or a saved project. Every draft now starts closer to your voice. Where the setting lives in each tool: [Beyond the day](beyond.html).

If your samples are sensitive, do step 2 with a local model so nothing leaves your laptop.

## Ethics and governance

The day covers the practical side: classify before you paste, find the quiet defaults, keep a person accountable, and tell people when AI was involved. To go further:

- The [Responsible use](responsible-use.html) page: Australia's six essential practices, proportionate data governance, and four ethics dilemmas for your team.
- The Australian Government's [Guidance for AI Adoption](https://www.ai.gov.au/staying-safe-and-responsible/essential-ai-practices) (October 2025), with an AI policy template and step-by-step actions.
- Curtin Executive Education's [Ethics of artificial intelligence](https://www.curtin.edu.au/study/prof-development/ethics-of-artificial-intelligence/) masterclass, for governance, risk and regulation in depth.

::: note
**One thread through all of these:** each one stops you accepting fluent, generic output. Verify it, separate thinking from building, argue against it, make it sound like you. [Decide like me](decide-like-me.html) has the full method behind Exercise 6. [Beyond the day](beyond.html) covers what the day left out: setting up your assistant, MCP, images, audio and video, and agents. Questions that come up but weren't on the agenda (energy, deepfakes, AGI, staff using unapproved tools) are answered in [the big questions](beyond.html#the-big-questions), the [deepfake row](beyond.html#beyond-text) and [Responsible use](responsible-use.html#data-governance-proportionate-not-prohibitive). More in [Resources](resources.html).
:::
