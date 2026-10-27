---
pagetitle: Starter prompts
title: "Starter prompts"
subtitle: "The Human Edge: using and delivering AI with judgement"
description: "Copy-and-adapt prompts for briefing, pushing back, checking and delivering, each with the check it needs."
nav-prompts: true
---

::: kicker
Starter prompts
:::

# Copy, adapt, <em>then check.</em>

::: lede
Twenty-seven prompts from the day, ready to adapt. Replace the [square brackets] with your own detail, which is where your edge goes in. Each one notes the trust tool corner its output usually lands in, so you know how hard to check it.
:::

Corners: **A** trust with light review · **B** verify the load-bearing bits · **C** verify before you ship · **D** human in the loop.

## Brief it

### 1 · The RTCF brief

*Use for any task that matters.* Check: depends on the task.

```text
ROLE: You are [who should write this, e.g. an experienced project manager who writes plainly].
TASK: [Verb and scope, e.g. Draft a 200-word update for the steering committee].
CONTEXT: The audience is [who, and what they care about]. The situation is [what happened, what's at stake]. Good looks like [your standard]. [Paste your notes or material.]
FORMAT: [Length, structure, tone, e.g. RAG status, three bullets, a risks table, next steps].
```

### 2 · + Example: match one you liked

*The strongest single upgrade.* Check: A.

```text
Here is an example I liked: [paste]. Match its length, tone and structure for [new task]. Don't copy its content.
```

### 3 · + Done: define success

*Add to any brief when the output keeps missing.* Check: as the task.

```text
Done means: [length], [structure], using only facts I've given you. Mark anything you're unsure of with [CHECK] rather than guessing.
```

### 4 · + Questions: let it ask first

*Use when you're not sure what context it needs.* Check: A.

```text
Before you start on [task], ask me up to five questions about anything you'd need to know to do it well. Ask them one at a time and wait for my answer.
```

### 5 · + Steps: split the job

*Use on long or multi-part work, especially with smaller or older models.* Check: as the task.

```text
We'll do [task] in steps. First, give me an outline only, as headings with one line each. Wait for my go-ahead, then draft one section at a time.
```

## Push back

### 6 · Guardrail

*Add at the start of any conversation where you want an honest assessment.* Check: B.

```text
Only change your assessment if I give you a new fact. If you do change it, name the fact that changed it.
```

### 7 · Devil's advocate

*Use on a plan, a proposal or an idea you like too much.* Check: B.

```text
Don't flatter me. Here is my [plan / proposal / idea]: [paste]. Give me the three strongest reasons it fails, and name the single assumption it all rests on.
```

### 8 · Board of directors

*Use when one confident answer isn't enough.* Check: B.

```text
Respond to [proposal] as a board of three: a CFO, a sceptical customer and a frontline manager. One paragraph each from their point of view. Then list where they disagree with each other.
```

### 9 · Fresh-chat second opinion

*Use in a new chat when a long conversation has gone on too long.* Check: B.

```text
I'm going to paste a conclusion reached in another conversation. Assess it independently. Where is it strongest, where is it weakest, and what would you need to see to be confident it's right? [paste]
```

### 10 · Hand over to a fresh chat

*Use when a long conversation has drifted.* Check: A.

```text
Write a handover prompt that captures everything important from this conversation: the context, the decisions made, open questions, and where we left off. I'll paste it into a new chat to continue.
```

## Check it

### 11 · Describe the data first

*Always the first prompt on a dataset.* Check: C.

```text
Describe this dataset before analysing it: number of rows, the columns and what each seems to contain, the date range, and anything missing, duplicated or inconsistent. Don't draw conclusions yet.
```

### 12 · Show your working

*Use on any figure that will drive a decision.* Check: C, then recount it yourself.

```text
For each number in your answer, show how you calculated it: which rows or columns you used, any filters you applied, and the formula. List anything you excluded and why.
```

### 13 · VET the claim

*Use on claims you can't check against your own data.* Check: B or C.

```text
You told me: [paste the claim]. Help me VET it.
VERIFY: What sources would support this, and how could I check them independently?
EXPLAIN: Break it down step by step until I could explain it to a colleague.
TEST: Under what conditions, or for whom, would it be wrong?
```

### 14 · Describe the shape, not the data

*Use when you can't share the real data. The tool never sees it.* Check: C. Run what it gives you on data where you know the answer before you trust it. If you can't read the code, treat it as top-right.

```text
I can't share the data itself. Its structure is: [number] rows, columns [list them, with types and made-up example values]. Write the steps or spreadsheet formulas I'd use to answer [question], so I can run them myself.

Or: write a single HTML page that runs entirely in my browser, lets me open the file from my computer, and shows [the result]. It must not send the data anywhere.
```

## Deliver it

### 15 · Map my workflow

*The start of a delivery plan.* Check: B.

```text
Here's how I currently do [weekly task], in my own words: [describe it]. List it as numbered steps with a time estimate for each. For each step, suggest whether AI could lead, assist, or should stay with a person, and say why. Don't assume access to any system I haven't mentioned.
```

### 16 · Pre-mortem

*Use before you start a new workflow or project.* Check: B.

```text
Imagine it's 30 days from now and [the workflow / project] has failed. Write the five most likely reasons it failed, and for each, one early warning sign I could watch for and one thing I could put in place now.
```

### 17 · Gate review

*Use at your 30-day gate. You make the call.* Check: D.

```text
At the start I set these criteria. Scale if: [criteria]. Pivot if: [criteria]. Kill if: [criteria]. Here's what happened over 30 days: [log, numbers, issues]. Assess the evidence against each criterion and tell me what's missing. Don't make the decision for me.
```

## Decide and rehearse

### 18 · Pros and cons, against your criteria

*Use when you're choosing between options.* Check: B.

```text
I'm choosing between [options] for [situation, with the key facts]. For each option give a short description, three advantages and three disadvantages, judged against [criteria, e.g. cost, risk, effort, impact on staff]. Then recommend one for my situation and say what would change your recommendation.
```

### 19 · Rehearse a difficult conversation

*Use before a performance conversation, a negotiation or bad news.* Check: A. The decision and the words you use stay yours.

```text
You are [the other person: role, temperament, what they care about]. I need to [goal of the conversation]. Play that person realistically, including pushback. Stay in role until I type PAUSE; then give me feedback on what I said that was unclear, unfair or legally risky, and how to say it better.
```

### 20 · Practise and test me

*Use to check your own understanding before a high-stakes call.* Check: C. Confirm anything you'll rely on.

```text
I need to get better at [skill or topic, e.g. reading a variance report, applying our leave policy]. Give me one short realistic scenario at a time, ask me what I'd do, then tell me whether I'm right and why. Make them harder if I get two right in a row, easier if I miss two.
```

## Practise

### 21 · Two-pass habit

*Once a week, on a task that matters. Do your own rough pass first.* Check: A.

```text
Here are two versions of the same [task]: mine (A) and an AI draft (B). [paste both]. Without flattering either, list where A is stronger, where B is stronger, and what both missed. Be specific.
```

## Decide like me

Turn one decision you make over and over into if-then rules, then test them blind on your own past calls. The [Decide like me](decide-like-me.html) page has the full method, including how to save the rules and why the re-test goes in a new chat. Method after Dylan Davis.

### 22 · Interview me for my rules

*Use when your answer to "why?" is "it depends".* Check: B.

```text
Help me write down the rules I use for one decision: [the decision]. Question me one at a time, choosing each question from my last answer. Each time I say "it depends" or stay vague, dig until you can state it as an if-then rule. Stop after fifteen to twenty questions and list the rules you've heard, every branch included, for me to check.
```

### 23 · Find the rules in my past decisions

*Use when the decisions are on file but the reasons never were.* Check: B. Read every rule and ask whether you'd have said it.

```text
Here are past cases of one decision I make: what came in, and what I decided. [Describe each case; leave out names and client details.] Work out which rules would explain these decisions, including any I've never written down. List them as if-then rules, and point out any case that doesn't fit them.
```

### 24 · Blind test my rules

*Run in a new chat before you rely on the rules. You make the final call.* Check: D.

```text
Using the decision rules below, make the call on each of these [three to five] cases. I've left out what I decided. For each case, give your call, the rule you used, and your reasoning in two or three short steps. Then stop, and I'll compare your calls with mine.

[Paste the rules, then the cases.]
```

## Write like me

Teach it how you sound, then test it on a real draft. The partner to Decide like me: one teaches it your voice, the other your rules. The full method is [Write like me](go-deeper.html#write-like-me) on the Go deeper page, and [Style Mirror](https://stylemirror.eduserver.au) does prompts 26 and 27 for you.

### 25 · Voice pass

*Use on a draft that sounds like everyone.* Check: A. Read it aloud. Would you have said it?

```text
Here's about 100 words I wrote: [paste, with anything confidential removed]. Rewrite your last output in my voice, leading with the one thing only I would say.
```

### 26 · Describe my style

*Use once, on three or four things you've written at your best.* Check: B. It will be slightly off, and slightly a parody. Edit it until it's you.

```text
Here are [three or four] things I've written: [paste, with anything confidential removed]. Describe my writing style as a brief another writer could follow: tone, sentence length and structure, vocabulary, how I open and close, the habits that make it sound like a person, and anything I never do. Quote a short example from my samples for each point.
```

### 27 · Write from my style brief

*Use for a first draft in your voice. Save the brief in your custom instructions and you can skip pasting it.* Check: depends on the task.

```text
Here's my style brief: [paste]. Write [format] about [topic] for [audience]. Match the voice, not the content of my samples. Mark anything you're unsure I'd say with [CHECK].
```

::: note
Saved one that works? Add its name, when to use it and its check in the [prompt builder](prompt-builder.html), and export your library.
:::
