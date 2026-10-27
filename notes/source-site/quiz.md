---
pagetitle: Where's your edge?
description: "A two-minute self-check: six questions that place you on your AI journey and point to the part of the day built for you."
nav-more: true
---

::: kicker
Two-minute self-check
:::

# Where's your <em>edge?</em>

::: lede
Six quick questions. No score is better than another; the result points you to the part of the day that will stretch you most. Nothing is stored or sent anywhere.
:::

```{=html}
<style>
.qz{background:var(--card);border:1px solid var(--hair);border-radius:12px;padding:26px 28px;margin-top:20px}
.qz .prog{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);display:flex;justify-content:space-between}
.qz .bar{height:4px;background:var(--hair);border-radius:2px;margin:8px 0 22px;overflow:hidden}
.qz .bar i{display:block;height:100%;background:var(--acc);transition:width .3s}
.qz .q{font-family:var(--serif);font-size:24px;color:var(--ink);line-height:1.3;margin-bottom:16px}
.qz .opt{display:block;width:100%;text-align:left;background:#0C0F15;border:1px solid var(--hair);border-radius:10px;color:var(--ink);font:16px/1.4 var(--sans);padding:13px 16px;margin:8px 0;cursor:pointer}
.qz .opt:hover{border-color:var(--faint)}
.qz .opt.on{border-color:var(--acc);background:color-mix(in srgb,var(--acc) 10%,#0C0F15)}
.qz .nav{display:flex;justify-content:space-between;margin-top:18px}
.qz button.nb{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;padding:9px 16px;border-radius:999px;border:1px solid var(--acc);background:none;color:var(--acc);cursor:pointer}
.qz button.nb:disabled{opacity:.3;cursor:default}
.qz button.nb.solid{background:var(--acc);color:#0A0C10}
.qz .res h2{border:0;padding:0;margin:6px 0 10px}
.qz .badge{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);font-weight:700}
</style>
<div class="qz" id="qz"></div>
<script>
(function () {
  var Q = [
    ['How often do you use AI tools like ChatGPT, Claude, Gemini or Copilot?',
      [['Never, or hardly ever', {ex: 3}], ['Once in a while', {ex: 1, us: 1}], ['Most weeks', {us: 2, op: 1}], ["Daily; it's part of how I work", {op: 2, bu: 1}]]],
    ['When AI gives you an answer, you usually...',
      [['Use it pretty much as it is', {us: 3}], ['Skim it to see if it looks right', {us: 2}], ['Check the key facts before I rely on it', {op: 2}], ['Treat it as a draft and verify anything that matters', {op: 1, bu: 1}]]],
    ['How do you usually prompt?',
      [['I type a question and hope for the best', {ex: 2, us: 1}], ['I rephrase until it gets better', {us: 2}], ['I give it a role, context and format', {op: 2}], ["I've built reusable prompts or set up custom instructions", {op: 1, bu: 2}]]],
    ['How confident would you be explaining AI to a colleague?',
      [["Not very; I'm still finding my feet", {ex: 3}], ['I could cover the basics', {us: 2}], ['Fairly confident on practical uses', {op: 2}], ['Very; people already ask me', {op: 1, bu: 2}]]],
    ['Have you put AI into a team process or project?',
      [['No, not yet', {ex: 1, us: 1}], ["I've thought about it", {us: 1, op: 1}], ['One is under way', {op: 1, bu: 2}], ['Yes, several', {bu: 3}]]],
    ['Where do you feel least confident right now?',
      [['Using AI day to day at all', {ex: 2, us: 1}], ['Knowing when to trust it, and when not to', {us: 2}], ['Getting good output, not generic output', {op: 2}], ['Making it work reliably for a team, week after week', {bu: 3}]]]
  ];
  var P = {
    ex: ['The Explorer', 'Early on your journey',
      "You're at the best place to build the habit that lasts: judging AI before you trust it. Don't worry about delivery yet.",
      'Session 1, Judge, is your sweet spot: the trust tool and checking from outside the tool. Then the RTCF brief in Session 2.',
      [['Before the day', 'before.html'], ['The four tools', 'tools.html']]],
    us: ['The Hands-on User', "You're using it, and trust is doing the work",
      "You use AI, but your trust in it is carrying the load. Your biggest win today is making that trust deliberate rather than instinctive.",
      'The trust tool in Session 1 and the check loop in Session 3, especially VET and the verification challenge.',
      [['The trust tool', 'tools.html#trust-tool'], ['Go deeper: VET', 'go-deeper.html']]],
    op: ['The Confident Operator', "You're fluent; time to make it stick",
      "You're fluent. Your edge now is output that sounds like you, and judgement that holds up when someone else relies on it.",
      'The upgrades and push-back moves in Session 2, the voice pass, and Write like me. Then Session 4.',
      [['Starter prompts', 'prompts.html'], ['Go deeper: Write like me', 'go-deeper.html#write-like-me']]],
    bu: ['The Builder', "You're thinking at the team level",
      "You're already putting AI into real work. Today is about designing the human in, and making a clean scale, pivot or kill call.",
      'Session 4, Deliver: why AI projects fail differently, checkpoints staffed by the right people, and the 30-day gate.',
      [['The four tools: Deliver', 'tools.html#opportunity-finder'], ['Responsible use', 'responsible-use.html']]]
  };
  var box = document.getElementById('qz'), cur = 0, ans = [];
  function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function show() {
    var q = Q[cur];
    box.innerHTML = '<div class="prog"><span>Question ' + (cur + 1) + ' of ' + Q.length + '</span><span>' + Math.round(cur / Q.length * 100) + '%</span></div>' +
      '<div class="bar"><i style="width:' + (cur / Q.length * 100) + '%"></i></div><div class="q">' + esc(q[0]) + '</div>' +
      q[1].map(function (o, i) { return '<button class="opt' + (ans[cur] === i ? ' on' : '') + '" data-i="' + i + '">' + esc(o[0]) + '</button>'; }).join('') +
      '<div class="nav"><button class="nb" id="qz-b"' + (cur ? '' : ' disabled') + '>Back</button><button class="nb solid" id="qz-n"' + (ans[cur] === undefined ? ' disabled' : '') + '>' + (cur === Q.length - 1 ? 'See my result' : 'Next') + '</button></div>';
  }
  function result() {
    var t = {ex: 0, us: 0, op: 0, bu: 0};
    ans.forEach(function (a, i) { var w = Q[i][1][a][1]; for (var k in w) t[k] += w[k]; });
    var best = Object.keys(t).sort(function (a, b) { return t[b] - t[a]; })[0], p = P[best];
    box.innerHTML = '<div class="res"><div class="badge">' + p[1] + '</div><h2>' + p[0] + '</h2><p>' + p[2] + '</p>' +
      '<p><b>Where today will stretch you:</b> ' + p[3] + '</p><div class="btns">' +
      p[4].map(function (l) { return '<a href="' + l[1] + '">' + l[0] + '</a>'; }).join('') + '</div>' +
      '<div class="nav"><button class="nb" id="qz-r">Start again</button></div></div>';
  }
  box.addEventListener('click', function (e) {
    var o = e.target.closest('.opt');
    if (o) { ans[cur] = +o.dataset.i; show(); return; }
    if (e.target.id === 'qz-b') { cur--; show(); }
    if (e.target.id === 'qz-n') { if (cur < Q.length - 1) { cur++; show(); } else result(); }
    if (e.target.id === 'qz-r') { cur = 0; ans = []; show(); }
  });
  show();
})();
</script>
```
