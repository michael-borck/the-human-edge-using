---
pagetitle: Responsible use
description: "Proportionate data governance, finding the quiet defaults in AI output, and four ethics dilemmas for your table."
nav-more: true
---

::: kicker
Responsible use
:::

# Data, bias and ethics. <em>Where a person stays in charge.</em>

::: lede
These run through the whole day, from "three rules before you paste" to the human checkpoints in your delivery plan. Here they get their own space: for a fast-finisher activity, a team meeting, or a policy conversation at work.
:::

## Australia's six essential practices

In October 2025 the Australian Government's [Guidance for AI Adoption](https://www.ai.gov.au/staying-safe-and-responsible/essential-ai-practices) replaced the eight AI Ethics Principles and the ten voluntary guardrails with six essential practices. They're written for organisations, but each one has a version you can practise in your own work:

| Practice | In your own work |
|---|---|
| 1 · Decide who is accountable | Every AI-assisted workflow has a named owner. Your name goes on the output, not the tool's. |
| 2 · Understand impacts and plan accordingly | Ask who is affected, and who could be treated unfairly (see the quiet defaults below). |
| 3 · Measure and manage risks | Classify data before you paste it. Place each output on the trust tool. |
| 4 · Share essential information | Tell people when AI drafted or decided something that affects them. Check what your organisation's AI policy says about disclosure, and see the privacy rule below. |
| 5 · Test and monitor | Check from outside the tool (the check loop, VET), and review at a gate. |
| 6 · Maintain human control | Human checkpoints at every amber or red step; some work stays human only. |

::: note
**Practice 4 is now also law.** From 10 December 2026, the Privacy Act requires an organisation's privacy policy to say where it uses a computer program to make a decision, or to do something substantially and directly related to making one, when the decision could significantly affect a person's rights or interests and uses their personal information (APP 1.7 to 1.9). The policy must name the kinds of personal information used and the kinds of decisions. AI scoring, triage and saved decision rules can all fall inside it. The [OAIC's guidance and flowchart](https://www.oaic.gov.au/news/media-centre/new-resources-on-transparency-for-use-of-ai-and-automated-decision-making) set out the test. If your team uses AI on decisions about people, tell whoever owns your privacy policy.
:::

## Data governance: proportionate, not prohibitive

Many organisations land on "don't put anything into AI". That treats every interaction as equally risky, and it mixes up a few real concerns with one imaginary one.

**The real risk is the pipeline, not the model.** When you paste data into a tool, the exposure is transmission, storage, jurisdiction and contract: where it goes, who keeps it, under which law. It isn't someone later "extracting" your document from the model. Email, Slack and shared drives carry the same pipeline risks; AI only feels riskier because it's newer.

A proportionate approach:

1. **Classify the data.** Public, internal, confidential or regulated?
2. **Match the tool to the class.** Approved work tools with a data-processing agreement for internal and confidential work. Consumer tools for public or non-sensitive material. Regulated data (health, financial, personal) needs a specific assessment first.
3. **Manage the real risks.** Never paste passwords, API keys or access tokens. Remove personal details where you can. Know the provider's logging and retention terms.
4. **Drop the imaginary one.** Stop treating "model extraction" as a likely threat, and put the effort where the exposure actually is.

That's ordinary professional data hygiene, applied consistently.

### Set it up safely

A checklist for your own accounts. Your organisation's AI policy and privacy officer have the final say on what's approved. The regulator agrees with the cautious line: the OAIC's [guidance on commercially available AI products](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products) says the Privacy Act applies to personal information you put into an AI tool, and to output that contains it, and recommends as best practice not entering personal information, especially sensitive information, into publicly available AI tools.

- **Two accounts: work and personal.** Client work only in a work account on a business plan your organisation has approved. Business plans generally don't train on your data and come with a data agreement. Keep personal use in a personal account, in a separate browser profile, so the two never share a login, history or connected apps.
- **Turn off training on personal accounts.** Look under Settings, then Data controls or Privacy. The names vary: "Improve the model for everyone", "AI data usage", "Help improve".
- **Memory off, or a temporary chat, for anything sensitive.** Memories are kept separately from chat history, so deleting a chat may not delete them.
- **Connect only what you need.** Each connection to your email, files or calendar widens what the tool can read, and what [hidden instructions](beyond.html#try-it-a-document-that-talks-to-the-ai) in those files can reach.
- **Regulated data stays out unless it's approved.** Information about children, health or finances of identifiable people only goes into a tool your organisation has approved for that kind of data, and even then without names. Your sector may have stricter rules.
- **Check client agreements.** Some contracts and NDAs now say whether AI can be used on client material. If yours are silent, ask the client.
- **Can't share it? Have it build the tool instead.** Describe the shape of the data and ask for spreadsheet formulas, a short script, or a single web page that runs on your own computer ([prompt 14](prompts.html#describe-the-shape-not-the-data)). The tool never sees the data. Test what it gives you on data where you know the answer first, and if you can't read the code, treat it as top-right.
- **Any product you're unsure of:** ask three questions. Which plan am I on? Does it train on what I type? Is there a data agreement with my organisation? Perplexity, for example, uses personal searches to improve its models unless you turn off "AI Data Usage" in Settings ([Perplexity help](https://www.perplexity.ai/help-center/en/articles/10354855-what-data-does-perplexity-collect-about-me)), and says it doesn't train on enterprise customers' data.

**If your team already uses AI on its own.** Unapproved use is common, and the data is already going somewhere. Banning it usually drives it out of sight. A better order: find out what people are using and for what, approve a tool that fits the work, teach the three rules before you paste, and make it easy to ask before pasting something borderline.

## Find the quiet defaults

> **Activity, about 5 minutes.** Ask your AI tool: *"Write a one-paragraph scene of a respected senior manager on a busy Monday."* Then, in a new chat: *"Write a one-paragraph scene of a respected administrative officer on a busy Monday."* Read them side by side.

The interesting bias isn't the blatant one; models are trained hard against obvious stereotypes. It's in the small choices. What is each person called: a title and surname, or a first name? Who is described as warm, and who as capable? What does each one worry about? Who holds authority in the scene?

Try other pairs from your own work:

- "a strong graduate applicant" vs "a strong mature-age applicant"
- "a high-performing team member" vs "a team member returning from parental leave"
- "a successful founder" vs "a successful small-business owner"

If you use AI to draft position descriptions, references or performance reviews, these defaults leak into them. The generic output inherits the generic average, including its skew. Noticing it is your job.

**Prefer a guided game?** Play [Survival of the Best Fit](https://www.survivalofthebestfit.com/) (about 10 minutes) and watch an "objective" hiring algorithm reproduce and amplify the bias in its training data. Then ask: where did the bias get in, and whose job was it to notice? On the trust tool, that's a precise, large-stakes call: top-right corner.

## Four ethics dilemmas

Take one or two at your table. There's no answer key. The point is to make the trade-off explicit and decide where a person stays in charge.

### 1 · The biased screen

Your team deploys an AI résumé-screening tool. Six months in, an analyst notices it quietly marks down applicants from one group. By its efficiency measure, it's "working". Do you switch it off immediately, or audit it first? Who is responsible: the vendor, the team that deployed it, or the executive who sponsored it?

*The link to the day:* the bias came in through the data, not malice. Screening decisions are precise and large-stakes, so a person owns them, and "the algorithm did it" is not a defence.

### 2 · The confidently wrong policy bot

A customer is quoted a returns policy that doesn't exist, in writing, by your chatbot, and acts on it. Who's accountable? What do you owe the customer, and what do you change in the system?

*The link to the day:* checking is the product. The checkpoint belongs before a wrong answer reaches a customer, designed in from the start, not added after the apology.

### 3 · Efficiency or apprenticeship?

Automating 80% of a junior's routine work looks like a win, until you realise they never learn to judge the output, because the work that trained their predecessors has gone. Is that an ethics question or just an HR one?

*The link to the day:* the juniors lost the easy reps. Hollowing out expertise for short-term speed deletes your team's future judgement. Keep at least one checkpoint human on purpose, to build capability.

### 4 · "Ship it now, govern it later"

A competitor launches an AI feature, and your manager says to match it this quarter and sort out the governance afterwards. Do you? What do you say?

*The link to the day:* the demo is a trap, and "everyone else is doing it" isn't a plan. Governance added after something goes wrong costs more, in money and in trust, than governance designed in.

::: note
**The thread:** every dilemma is the same question. Where does a person stay in the loop, and who owns the consequence when they don't? It isn't a technical question; it's the judgement the whole day is about. For depth on governance, risk and regulation, see Curtin Executive Education's [Ethics of artificial intelligence](https://www.curtin.edu.au/study/prof-development/ethics-of-artificial-intelligence/) masterclass.
:::
