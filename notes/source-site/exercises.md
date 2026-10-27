---
pagetitle: Exercises
description: "The eight exercises, with copyable prompts, scenario cards, decision cards and the RetailFlow data."
nav-exercises: true
---

::: kicker
Exercises
:::

# Eight exercises. <em>Mostly your own work.</em>

::: lede
Copy the prompts from here and write your answers in the [digital workbook](workbook.html); it saves in your browser and exports before you leave. If your own work is confidential, use a [scenario card](#scenario-cards) or a [decision card](#decision-cards) instead.
:::

| | Exercise | Session | Time |
|---|---|---|---|
| 1 | [Your pass first](#ex1) | Judge | 25 min |
| 2 | [Place it](#ex2) | Judge | 22 min |
| 3 | [Brief it](#ex3) | Brief | 25 min |
| 4 | [Upgrade and save](#ex4) | Brief | 25 min |
| 5 | [RetailFlow: Karen needs answers](#ex5) | Check | 35 min |
| 6 | [Decide like me](#ex6) | Check | 24 min |
| 7 | [Plan one delivery](#ex7) | Deliver | 35 min |
| 8 | [Your action plan](#ex8) | Deliver | 12 min |

::: {.ex .s1}
## Exercise 1 · Your pass first {#ex1}

[25 min · solo, then tables]{.mins}

1. **Your pass first.** Five minutes, no AI: sketch your own plan for the task below, in the workbook.
2. **Then AI's.** Paste the task, unedited, into an AI tool (two tools if you have them; the [class chat](https://chat.locopuente.org/register) has two, on course days).
3. **Compare side by side.** Where did you beat it? Where did it beat you? What did it get confidently wrong?

> I manage a team of 8 in a mid-sized company. One of my team, a strong performer for three years, has been late and missing deadlines for the past month. Others are starting to notice. Write me a plan to address this.
:::

::: {.ex .s1}
## Exercise 2 · Place it {#ex2}

[22 min · room, then solo]{.mins}

1. **Blind vote.** The facilitator reads a scenario. Decide in silence, then vote on "three": in ClassPulse (scan the code on screen), or by showing 1 to 4 fingers for corners A to D.
2. **Play the game** at [trusttool.borck.education](https://trusttool.borck.education/). Choose your domain and place all ten cards.
3. **Place three tasks from your own week** in the [workbook](workbook.html). For each, note the check it needs. Swap with a neighbour: where do you disagree, and why?
:::

::: {.ex .s2}
## Exercise 3 · Brief it {#ex3}

[25 min · solo]{.mins}

1. Pick a real task from your week, or a scenario card below.
2. **Round 1:** write the prompt the way you normally would. Run it. Score the output from 1 (unusable) to 5 (ready to use).
3. **Round 2:** rewrite it with RTCF and run it in a fresh chat. Score it again.
4. Note which part moved the score most.

> ROLE: You are a ...
> TASK: Write / summarise / compare ... (how much?)
> CONTEXT: The audience is ... The situation is ... Good looks like ...
> FORMAT: Length ... Structure ... Tone ...

The [prompt builder](prompt-builder.html) assembles the four parts for you.
:::

::: {.ex .s2}
## Exercise 4 · Upgrade and save {#ex4}

[25 min · solo]{.mins}

1. Take your best Round 2 prompt. Add one upgrade and run it: an example, a definition of done, questions first, or steps.
2. Push back with no new evidence: *"I don't think that's right."* Does it fold or hold? Then try one of the three push-back moves:

> GUARDRAIL: Only change your assessment if I give you a new fact. Name the fact that changed it.
> DEVIL'S ADVOCATE: Don't flatter me. Give me three reasons this fails, and name the assumption it all rests on.
> BOARD: Respond as a board: a CFO, a sceptical customer and a frontline manager. One paragraph each, then where they disagree.

3. Save three prompts to your library: a name, when to use it, the prompt with [blanks], and the check it needs. Use the [workbook](workbook.html) or the [prompt builder](prompt-builder.html).
4. **Stretch: the voice pass.** Paste about 100 words you actually wrote (sanitised), then ask: *"Rewrite your last output in my voice, leading with the one thing only I would say."* What changed? Optionally, ask it to summarise your style as a short brief and paste that into your tool's custom instructions. Nothing you can paste? Write 100 words now, to a colleague, on why you came today. It's your voice, and it's safe. The full version is [Write like me](go-deeper.html#write-like-me).
:::

::: {.ex .s3}
## Exercise 5 · RetailFlow: Karen needs answers by Monday {#ex5}

[35 min · solo or pairs, then blind vote]{.mins}

Karen manages customer service at RetailFlow, an online retailer. She has six months of ticket data and three questions:

1. What are the top three drivers of customer dissatisfaction?
2. When do our response times blow out?
3. What should I do about it?

::: btns
[Download the data (CSV)](downloads/retailflow-customer-service-data.csv)
:::

260 tickets, July to December 2024. Columns: `ticket_id`, `date`, `day_of_week`, `month`, `category`, `channel`, `priority`, `agent`, `response_time_hours`, `resolution_time_hours`, `satisfaction_score` (1 to 5), `resolved`.

1. **Frame.** Write Karen's questions down. Start a fresh chat.
2. **Explore.** Upload the CSV (or paste it) and start with:

> Describe this dataset: number of rows, columns, date range, and anything that looks incomplete. Don't analyse it yet.

3. **Shape** a first brief for Karen, under 300 words. Don't send it yet.
4. **Verify.** Three claims about the data are doing the rounds, and at least one is wrong. Check each against the data with a spreadsheet filter, recount or pivot table. Not "are you sure?"

- **A.** "Email is roughly three times slower than Live Chat."
- **B.** "Account Issues has the lowest satisfaction of any category, which makes sense, because account problems are the most complex to resolve."
- **C.** "Sunday response times are more than double the overall average."

Verdicts: **Verified** (accurate as stated), **Overstated** (right direction, wrong number), **Refuted** (the data contradicts it), or **Can't tell yet** if you haven't been able to check it. Is any of them in your brief? Fix it, and end the brief with a line that starts *What I checked:*

**Your own data can't go into a tool?** Describe its shape instead and have the AI write the formulas, a short script, or a single web page that runs on your computer ([prompt 14](prompts.html#describe-the-shape-not-the-data)). Try it on the RetailFlow data first, where you now know the answers.
:::

::: {.ex .s3}
## Exercise 6 · Decide like me {#ex6}

[24 min · solo, then tables]{.mins}

Pick one decision you make over and over: small, repeatable, explainable, and nothing from the top-right corner of the trust tool. Get your rules out of your head, then test them blind on your own past calls. Method after Dylan Davis; the [full method](decide-like-me.html) has its own page. If you followed [Before the day](before.html), you've brought the decision and three past cases. If not, or if your work can't go into an AI tool, take a [decision card](#decision-cards).

1. **Get the rules out.** Talk the why through, or let it interview you:

> Help me write down the rules I use for one decision: [the decision]. Question me one at a time, choosing each question from my last answer. Each time I say "it depends", dig until it becomes an if-then rule. Stop after ten questions and list my rules, every branch included.

2. **Write down three past cases:** the inputs only, and your call on each. Do this before you run anything.
3. **Test it blind.** In a new chat, give it the rules and the three cases, inputs only. Have it make each call and name the rule it used.
4. **Fix one mismatch.** A mismatch is a rule you've never put into words: a threshold you didn't state, an exception you apply without noticing, or a loose preference the rules made strict. Add it as one if-then line, then re-test that case in a new chat.
5. **Last question:** what would you never let it decide, and why? That list is the other half of the output.

Describe your past cases. Don't paste anything confidential.
:::

::: {.ex .s4}
## Exercise 7 · Plan one delivery {#ex7}

[35 min · solo, then tables]{.mins}

1. **Map** a task you do weekly that takes 30 minutes or more. Five to eight steps, with honest minutes for each. Note the owner, a success measure and today's baseline.
2. **Assign** each step: who leads (AI leads, AI assists, you lead, human only) and its trust corner.
3. **Design the checkpoints.** Who checks each amber or red step, and how? Pick someone who knows what right looks like. Who is affected, who has to agree, and who will do the checking?
4. **Test** one AI step live with an RTCF brief. Then **set your 30-day gate**: what result would make you scale, pivot or kill?

The [Map my workflow](prompts.html#map-my-workflow) and [Pre-mortem](prompts.html#pre-mortem) starter prompts help with steps 1 and 3.

Mapping your workflow needs no data, only step names and minutes. If the inputs for the live test can't go into a tool, invent a few lines in the same shape (rule 2 from the morning: describe it, don't paste it). Can't use your own workflow at all? Plan [scenario card 3](#scenario-cards) (the Friday status update) or scenario card 6 (monthly invoicing), and test with the notes on the card.
:::

::: {.ex .s4}
## Exercise 8 · Your action plan {#ex8}

[12 min · quiet, then share]{.mins}

One line each: a specific task, tool and day.

- **This week (practise):** two-pass one task that matters, and use one saved prompt for real.
- **This month (deliver):** run your delivery plan, with checkpoints in place from day one.
- **Day 30 (gate):** scale, pivot or kill, against the criteria you set today.
- **This quarter (revisit):** name what must stay human in your role, and check whether the corners have moved.

Before you leave, put this week's line and your day-30 gate in your calendar.
:::

## Scenario cards {#scenario-cards}

Use one of these in Exercises 3 and 4 if your own work is confidential. Paste the details into your Context. Scenarios 3 and 6 also work as the workflow for Exercise 7.

:::::: {.cards .two}
::: card
[Scenario 1]{.lab}

### The difficult client email

Your client, David Chen (VP Operations, GreenLeaf Industries), says your latest deliverable is "too generic". The work is solid, but his board changed priorities at a meeting you weren't in. It's an 18-month, mostly positive relationship. You want to acknowledge his frustration without conceding the work is poor, and propose a one-hour alignment meeting.
:::

::: card
[Scenario 2]{.lab}

### The policy summary

A new 22-page flexible work policy needs to become an email your 12-person marketing team will actually read: how many days from home, how to request changes, busy periods, and part-time rules. Friendly, practical, under 400 words. (Paste any policy you have, or ask the AI to invent a plausible one first.)
:::

::: card
[Scenario 3]{.lab}

### The Friday status update

CRM migration for a steering committee (CIO, sponsor, two business leads). Notes: data batch 2 done but 3 days late (2,300 duplicate records, Sarah leading review); vendor hasn't confirmed training dates; UAT going well, 2 minor bugs; $12K under budget; 68% complete against a 72% target. They want RAG status, wins, risks, next steps. No surprises.
:::

::: card
[Scenario 4]{.lab}

### The interview questions

Hiring a mid-level Digital Marketing Coordinator for a 5-person B2B team: social campaigns, Google Analytics and Meta Ads, agency coordination, monthly reports to leadership. 45-minute panel with the Marketing Director. HR's generic questions won't tell you whether they can do the job. You want behavioural and situational questions.
:::

::: card
[Scenario 5]{.lab}

### The logistics decision

Renew, switch or insource your third-party logistics? Current provider: $1.8M a year, 96.2% on time (benchmark 97%), 2.1% damage (benchmark 1.5%), slow on volume spikes, just raised prices 8%. Competitor: $1.65M, promises 97.5%. In-house: $2.5M upfront, $1.2M a year, 12 months to set up. 15,000 orders a month, growing 20% a year. A discussion starter for leadership, not the decision.
:::

::: card
[Scenario 6]{.lab}

### The process document

You're the only person who knows monthly invoicing: export billable hours from Harvest, group by client in Excel, apply the rate card ($250 strategy, $180 execution, $120 support), create invoices in Xero, add PO numbers from the account managers' Google Sheet, send, update the tracker, then email Finance a summary with anything unusual. Write it so a colleague can do it while you're on leave.
:::
::::::

## Decision cards {#decision-cards}

For Exercise 6, if you didn't bring a decision or your work can't go into an AI tool. The people and figures are invented, so everything here is safe to paste.

Each card hands you someone else's decision. You're taking it over from the person who made it, and their record is below.

1. **Read the record.** Then write your own call on test cases A to C before you run anything.
2. **Get the rules out.** Mine the record with [prompt 23](prompts.html#decide-like-me), or say the rules you'd use if the job were yours.
3. **Test it blind.** In a new chat, give it the rules and the three test cases (prompt 24).
4. **Open the answer key.** Compare its calls, your calls and the record-holder's. One test case turns on a rule they never wrote down.

::: {.card .s3}
[Decision card 1]{.lab}

### RetailFlow: does this ticket go to a senior agent?

Priya leads Karen's customer service team. Each morning she sends some open tickets to one of the two senior agents and leaves the rest in the general queue.

| # | Category | Channel | Amount | Waiting | Note | Priya's call |
|---|---|---|---|---|---|---|
| 1 | Returns & Refunds | Email | $340 | 6 h | First contact | Senior agent |
| 2 | Order Tracking | Live Chat | $45 | 2 h | Customer marked it High priority | General queue |
| 3 | Delivery Problems | Phone | $120 | 30 h | First contact | Senior agent |
| 4 | Billing Queries | Email | $80 | 5 h | Second contact about the same charge | Senior agent |
| 5 | Returns & Refunds | Live Chat | $150 | 3 h | First contact | General queue |
| 6 | Delivery Problems | Email | $95 | 10 h | First contact | General queue |

**Test cases, inputs only**

| | Category | Channel | Amount | Waiting | Note |
|---|---|---|---|---|---|
| A | Returns & Refunds | Phone | $380 | 4 h | First contact |
| B | Order Tracking | Email | $30 | 8 h | Customer marked it High priority |
| C | Delivery Problems | Social Media | $90 | 3 h | Public post, 40 replies so far |

<details><summary>Answer key: Priya's calls</summary>

- **A · Senior agent.** Refunds over $200 go to a senior agent.
- **B · General queue.** Priya ignores the priority customers set themselves; it's on almost every ticket.
- **C · Senior agent.** Anything public on social media goes to a senior agent the same morning. It isn't in the record because it only happens a few times a year. That's an **unstated exception**.

Her other rules: anything waiting over 24 hours, and any second contact about the same issue, goes to a senior agent.

</details>
:::

::: {.card .s3}
[Decision card 2]{.lab}

### Expense claims: approve, or query first?

Sam manages a small operations team and approves their expense claims. Most go straight through. Some get a query first.

| # | Claim | Amount | Receipt | Age | Sam's call |
|---|---|---|---|---|---|
| 1 | Taxi to a client site | $38 | Yes | 5 days | Approve |
| 2 | Team lunch, 4 people | $300 ($75 each) | Yes | 10 days | Approve |
| 3 | Parking | $55 | No | 3 days | Query |
| 4 | Dinner with a client, 2 people | $190 ($95 each) | Yes | 7 days | Query |
| 5 | Train fare | $24 | No | 2 days | Approve |
| 6 | Conference registration | $420 | Yes | 6 days | Approve |
| 7 | Taxi home after a late event | $32 | Yes | 75 days | Query |

**Test cases, inputs only**

| | Claim | Amount | Receipt | Age |
|---|---|---|---|---|
| A | Coffee with a supplier, 2 people | $14 | No | 4 days |
| B | Dinner after a site visit, 3 people | $330 ($110 each) | Yes | 12 days |
| C | Laptop stand and keyboard | $640 | Yes | 9 days |

<details><summary>Answer key: Sam's calls</summary>

- **A · Approve.** No receipt is fine under $50.
- **B · Query.** Meals over $80 a head get a query.
- **C · Query.** Sam queries anything over $500, receipt or not, because equipment that size should go through IT purchasing. Nothing in the record was over $500, so the rule never showed. That's a **threshold never put into words**.

Sam's other rule: claims more than 60 days old get a query.

</details>
:::

::: {.card .s3}
[Decision card 3]{.lab}

### Meeting requests: accept, ask for an agenda, or send a delegate?

Jo runs a team of nine and gets several meeting requests a day.

| # | Request | Length | Jo is | Agenda | Jo's call |
|---|---|---|---|---|---|
| 1 | Weekly 1:1 with someone in Jo's team | 30 min | Required | None | Accept |
| 2 | Product demo from a vendor's sales rep | 60 min | Required | None | Ask for an agenda |
| 3 | Quarterly planning | 2 hours | Optional | Attached | Send a delegate |
| 4 | Budget review with Jo's manager | 45 min | Required | Attached | Accept |
| 5 | Cross-team workshop | 90 min | Required | Attached | Accept |
| 6 | "Quick sync" from a peer in finance | 45 min | Required | None | Ask for an agenda |

**Test cases, inputs only**

| | Request | Length | Jo is | Agenda |
|---|---|---|---|---|
| A | Follow-up from the same vendor | 30 min | Required | None |
| B | All-hands rehearsal | 2 hours | Optional | Attached |
| C | "Quick question on the contract" from a peer in legal | 15 min | Required | None |

<details><summary>Answer key: Jo's calls</summary>

- **A · Ask for an agenda.** No agenda means Jo asks for one, unless it's her own team or her manager.
- **B · Send a delegate.** Long meetings where she's optional get a delegate.
- **C · Accept.** Jo holds the agenda rule loosely: for anything 15 minutes or shorter she just accepts. The rules made it strict. That's a **loose rule applied strictly**.

</details>
:::
