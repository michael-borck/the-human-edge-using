---
pagetitle: Decide like me
description: "Exercise 6 in full: write down how you make one repeatable decision as if-then rules, save them, and test them blind against your own past calls. Method after Dylan Davis."
nav-more: true
---

::: kicker
Decide like me
:::

# Teach it your rules. <em>Keep the call.</em>

::: lede
Exercise 6 in full. Pick one decision you make over and over, get the reasoning out of your head as if-then rules, and test those rules on calls you've already made before you let them near a new one. The method is Dylan Davis's. The wording, the examples and the limits on this page are ours.
:::

It pairs with [Write like me](go-deeper.html#write-like-me) on the Go deeper page. That one teaches the tool how you sound; this one teaches it how you choose. In both, it drafts and you decide.

::: note
**Pick the decision carefully.** This suits decisions that repeat, that you can explain, and that you can check against what you decided before. Leave anything in the top-right corner of the trust tool alone. Writing a decision down doesn't lower its stakes.
:::

## Say, interview or mine

There are three ways to get the rules out: Say, Interview, Mine, or SIM for short. Start with one question: could you tell a new starter, out loud, why you decide the way you do?

| Your answer | Method | What you do | What you end up with |
|---|---|---|---|
| Yes | **Say** | Talk it through and let the tool transcribe. Most people trim the exceptions when they type; spoken, they stay in. Then have it ask you three to five follow-up questions, in turn. | Your process, with the gaps filled |
| "It depends" | **Interview** | The tool questions you in turn, choosing each question from your last answer, until every "it depends" is an if-then rule. Fifteen to twenty questions is usually enough. | A set of if-then rules |
| No, but the decisions are on file | **Mine** | Dig the rules out of the record, as in data mining. Give it past cases: what came in, and what you decided. It works out the rules you were following, including the ones you never wrote down. | Rules inferred from what you actually did |

"It depends" means there's a rule you haven't put into words yet. Take a team deciding which enquiries get a same-day reply. Asked why, the lead says it depends. Pushed, that turns into: *an existing client with a deadline this week gets a reply today; a general enquiry waits for the Monday batch.* Those branches are what you're writing down. The interview and mining prompts are in the [starter prompts](prompts.html#decide-like-me). No decision you can use? Practise on a [decision card](exercises.html#decision-cards).

## Save it

Stay in the same chat, so it still has the conversation, and ask:

```text
Write these decision rules up as a short brief I can reuse on new cases of this decision. Take out the names, clients and figures from the cases we talked about, and keep the rules.
```

Keep it short. A brief stuffed with history and anecdotes buries the rules, and the tool gives them less weight. A screen of if-then rules is plenty. This isn't the Example upgrade from Exercise 4 in reverse: an example shows tone and shape, but here the rules are the content, and real cases carry client details. If a rule only makes sense with an example, invent one.

Save it wherever your tool keeps standing instructions: a project, a Gem, custom instructions. [Beyond the day](beyond.html) shows where each tool keeps them. Agent tools call a saved brief like this a skill. It's the finished version of the prompt library you started in Exercise 4.

## Test it blind

Give it cases you've already decided, without your decisions, and see whether it reaches the same calls.

1. **Pick three to five past cases.** Mix routine ones with at least one awkward one. Three is the least that tells you anything; more than five is slow for a first test.
2. **Write down the inputs only.** What you knew at the time: the email, the figures, the request. Leave out what you decided and why.
3. **Write your own calls first,** before you run anything.
4. **Run the cases in a new chat** with only the saved rules loaded. Ask for a call on each, the rule it used, and its reasoning in a few short steps.

Then put the calls side by side:

| Case | Its call | Your call | Result |
|---|---|---|---|
| 1 | Same day: existing client, deadline Friday | Same day | Match |
| 2 | Monday batch: general question about services | Monday batch | Match |
| 3 | Monday batch: new contact, no deadline | **Same day**: referred by a current client | **Mismatch** |

Case 3 is the useful one. You answer referrals the same day and never said so. Most mismatches are one of three things:

- **A threshold you never stated.** You had a cut-off in mind and didn't put it into words.
- **An exception you apply without noticing.** A referral, a precedent, a long relationship.
- **A loose rule applied strictly.** You treat something as a preference, and the rules made it a requirement.

Four out of five on the first run is a good result. In the room, don't push for five out of five. The mismatch is where you find a rule you didn't know you had.

## Fix it, then test again in a new chat

Add the missing rule as one if-then line. Leave the other rules alone, and don't add explanation. Then run the whole batch again **in a new chat**. The chat where you built the rules has watched you decide, so it can pass on memory. A new chat with only the rules loaded tests the rules.

Models aren't deterministic. The same case can come back with a different call on a second run, so one flip doesn't mean the rules are broken. Look at the whole batch, and re-run any case that matters before you rely on it.

At work, hold the rules to the full standard: every case in the batch matches, in a new chat, before you sign them off.

## After you sign it off

The rules draft the call. You still make it. The source method goes a step further and lets the tool decide on its own once it passes. This course stops short of that.

- **Place every new case on the trust tool.** The rules came from you, and so does the accountability.
- **Keep a human checkpoint where the stakes are higher,** and tell people when an AI tool drafted a decision that affects them. In Australia that is also law from 10 December 2026: if rules like these make or substantially inform a decision that could significantly affect someone, using their personal information, your organisation's privacy policy has to say so (Privacy Act, APP 1.7 to 1.9; [OAIC guidance](https://www.oaic.gov.au/news/media-centre/new-resources-on-transparency-for-use-of-ai-and-automated-decision-making)). Tell whoever owns it.
- **Set a 30-day gate,** as for any workflow. Is it holding up? Does checking it cost more than it saves? Scale, pivot or kill.
- **Re-test each quarter.** Models change, and so do your rules. When the corners move, run the blind test again.

Keep the cases that didn't fit any rule. They show where your judgement does work a page of rules can't, and they're what to explain in person when you teach someone the job.

::: note
**Mining means pasting.** Showing a tool your past decisions means showing it your clients, so classify before you paste, or describe the cases instead. And expect the tool to praise its own rules. That's why the test is blind: it can't agree with an answer it hasn't seen.
:::
