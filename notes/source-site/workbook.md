---
pagetitle: Workbook
description: "Your digital workbook for The Human Edge: all eight exercises, your prompt library, decision rules, delivery plan and action plan. Saves in your browser; export before you leave."
nav-workbook: true
---

::: kicker
Your workbook
:::

# Everything you write today. <em>Yours to keep.</em>

::: lede
Type straight into this page. It saves automatically in this browser on this device: no account, and nothing is sent anywhere. Before you leave, **export** it (Markdown) or **print / save as PDF**.
:::

::: note
**Before you paste anything into an AI tool:** no confidential, client or personal information unless your organisation has approved that tool for it. If in doubt, use the scenario cards and the RetailFlow data.
:::

```{=html}
<style>
.wb-bar{position:sticky;top:58px;z-index:4;display:flex;gap:10px;flex-wrap:wrap;align-items:center;background:rgba(10,12,16,.94);backdrop-filter:blur(6px);padding:12px 0;border-bottom:1px solid var(--hair);margin:10px 0 26px}
.wb-bar button{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;padding:9px 15px;border-radius:999px;border:1px solid var(--acc);background:none;color:var(--acc);cursor:pointer}
.wb-bar button.solid{background:var(--acc);color:#0A0C10}
.wb-bar #wb-state{font-size:13px;color:var(--dim);margin-left:6px}
.wb section{background:var(--card);border:1px solid var(--hair);border-radius:12px;padding:22px 24px;margin:0 0 22px}
.wb section > h2{margin:4px 0 6px;padding:0;border:0;font-size:26px}
.wb .meta{font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);font-weight:700}
.wb .how{font-size:15px;color:var(--dim);margin:0 0 6px}
.wb label{display:block;font-size:14.5px;font-weight:600;color:var(--ink);margin:16px 0 6px}
.wb label small{font-weight:400;color:var(--dim)}
.wb input[type=text],.wb textarea,.wb select{width:100%;background:#0C0F15;border:1px solid var(--hair);border-radius:8px;color:var(--ink);padding:9px 11px;font:15px/1.5 var(--sans)}
.wb textarea{min-height:70px;resize:vertical;overflow:hidden}
.wb textarea.big{min-height:130px}
.wb input:focus,.wb textarea:focus,.wb select:focus{outline:none;border-color:var(--acc)}
.wb .two{display:grid;grid-template-columns:1fr 1fr;gap:0 18px}
.wb .four{display:grid;grid-template-columns:repeat(4,1fr);gap:0 14px}
@media (max-width:720px){.wb .two,.wb .four{grid-template-columns:1fr}}
.wb table{margin:8px 0 6px}
.wb td{padding:5px 6px 5px 0;border-bottom:0}
.wb td input,.wb td select{padding:7px 8px;font-size:14px}
.wb .add{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;background:none;border:1px dashed var(--faint);color:var(--dim);border-radius:999px;padding:6px 12px;cursor:pointer;margin-top:6px}
.wb .lib{border-top:1px solid var(--hair);margin-top:14px;padding-top:4px}
.wb .chk{display:flex;gap:18px;flex-wrap:wrap;margin-top:12px;font-size:15px}
.wb .chk label{display:flex;gap:8px;align-items:center;margin:0;font-weight:500}
.wb .chk input{accent-color:var(--acc)}
@media print{
  .top,footer,.wb-bar,.kicker,.lede,.note,.add,.btns{display:none!important}
  main{padding:0;max-width:none}
  h1{color:#111;font-size:22pt;margin:0 0 10pt}
  h1 em{color:#111}
  .wb section{background:#fff;border:0;border-top:1.5pt solid #111;border-radius:0;padding:8pt 0 0;margin:0 0 14pt;break-inside:auto}
  .wb section > h2{color:#111;font-size:15pt}
  .wb .meta{color:#7a5a12}
  .wb .how{color:#444}
  .wb label{color:#111;break-after:avoid}
  .wb label small{color:#666}
  .wb a{color:#111}
  .wb input[type=text],.wb textarea,.wb select{background:#fff;color:#111;border:.6pt solid #bbb;font-size:10pt}
  .wb th{color:#111;border-bottom-color:#111}
  body{background:#fff;color:#222}
}
</style>

<div class="wb-bar">
  <button class="solid" id="wb-export">Export (.md)</button>
  <button id="wb-print">Print / save as PDF</button>
  <button id="wb-clear">Clear my answers</button>
  <span id="wb-state">Nothing saved yet</span>
</div>

<div class="wb" id="wb">
<label>Your name <small>for the export header</small></label>
<input type="text" data-wb="name" data-label="Name">

<section data-title="Exercise 1 · Your pass first">
  <div class="meta">Exercise 1 · Judge · 25 min</div>
  <h2>Your pass first. Then AI's.</h2>
  <p class="how">Task: a strong performer of three years has been late and missing deadlines for a month, and the team has noticed. Sketch your plan first, before opening any AI tool. Then give AI the same task (two tools if you have them) and compare.</p>
  <label>My rough pass <small>5 minutes, bullets are fine</small></label>
  <textarea data-wb="e1-mine" data-label="My rough pass"></textarea>
  <div class="two">
    <div><label>What AI gave me <small>tool 1, paste or summarise</small></label><textarea data-wb="e1-ai1" data-label="AI pass (tool 1)"></textarea></div>
    <div><label>Tool 2 <small>optional</small></label><textarea data-wb="e1-ai2" data-label="AI pass (tool 2)"></textarea></div>
  </div>
  <div class="two">
    <div><label>Where I beat it</label><textarea data-wb="e1-beatit" data-label="Where I beat it"></textarea></div>
    <div><label>Where it beat me</label><textarea data-wb="e1-beatme" data-label="Where it beat me"></textarea></div>
  </div>
  <label>Anything confidently wrong, or advice I would not follow</label>
  <textarea data-wb="e1-wrong" data-label="Confidently wrong / would not follow"></textarea>
</section>

<section data-title="Exercise 2 · Place it">
  <div class="meta">Exercise 2 · Judge · 22 min</div>
  <h2>Place it</h2>
  <p class="how">Blind vote, then the game at trusttool.borck.education, then three tasks from your own week.</p>
  <div class="two">
    <div><label>Where the room split, and why</label><textarea data-wb="e2-split" data-label="Where the room split"></textarea></div>
    <div><label>Game domain and first-try score</label><input type="text" data-wb="e2-game" data-label="Game domain and score"></div>
  </div>
  <label>Three tasks from my week</label>
  <table><thead><tr><th>Task</th><th>Precise or average?</th><th>Stakes</th><th>Corner</th><th>The check it needs</th></tr></thead>
  <tbody data-table="e2-tasks" data-cols="text,pa,ss,corner,text" data-rows="3"></tbody></table>
</section>

<section data-title="Exercise 3 · Brief it">
  <div class="meta">Exercise 3 · Brief · 25 min</div>
  <h2>Brief it. Twice.</h2>
  <label>My task <small>or scenario card number</small></label>
  <input type="text" data-wb="e3-task" data-label="Task">
  <label>Round 1: the way I'd normally write it</label>
  <textarea data-wb="e3-r1" data-label="Round 1 prompt"></textarea>
  <div class="four">
    <div><label>Round 1 score <small>1 to 5</small></label><select data-wb="e3-s1" data-label="Round 1 score"><option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select></div>
    <div><label>Round 2 score</label><select data-wb="e3-s2" data-label="Round 2 score"><option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select></div>
    <div style="grid-column:span 2"><label>The part that moved the score most</label><select data-wb="e3-part" data-label="Part that mattered most"><option></option><option>Role</option><option>Task</option><option>Context</option><option>Format</option></select></div>
  </div>
  <label>Round 2: RTCF, in a fresh chat</label>
  <div class="two">
    <div><label>Role</label><textarea data-wb="e3-r" data-label="Role"></textarea></div>
    <div><label>Task</label><textarea data-wb="e3-t" data-label="Task (RTCF)"></textarea></div>
    <div><label>Context <small>audience, situation, stakes, material</small></label><textarea data-wb="e3-c" data-label="Context"></textarea></div>
    <div><label>Format</label><textarea data-wb="e3-f" data-label="Format"></textarea></div>
  </div>
</section>

<section data-title="Exercise 4 · Upgrade and save">
  <div class="meta">Exercise 4 · Brief · 25 min</div>
  <h2>Upgrade it. Then save it.</h2>
  <p class="how">Weak models can't infer, so leave nothing to infer. Add one upgrade, then push back.</p>
  <div class="two">
    <div><label>Upgrade I tried</label><select data-wb="e4-up" data-label="Upgrade tried"><option></option><option>+ Example</option><option>+ Done</option><option>+ Questions</option><option>+ Steps</option></select></div>
    <div><label>Did it help? How?</label><input type="text" data-wb="e4-up-note" data-label="Effect of the upgrade"></div>
    <div><label>When I pushed back with no new evidence, it</label><select data-wb="e4-fold" data-label="Pushback, no evidence"><option></option><option>folded</option><option>held</option></select></div>
    <div><label>Push-back move I tried, and what happened</label><input type="text" data-wb="e4-move" data-label="Push-back move"></div>
  </div>
  <label>Stretch · the voice pass <small>paste about 100 words you actually wrote (sanitised), then ask: "Rewrite your last output in my voice, leading with the one thing only I would say." What changed? Nothing you can paste? Write 100 words now on why you came today.</small></label>
  <textarea data-wb="e4-voice" data-label="Voice pass"></textarea>
  <label>Optional · my style brief <small>ask the tool to summarise your style from that sample; paste it into your tool's custom instructions tonight. The full method: <a href="go-deeper.html#write-like-me">Write like me</a></small></label>
  <textarea data-wb="e4-style" data-label="Style brief"></textarea>
</section>

<section data-title="My prompt library">
  <div class="meta">Take-home · prompt library</div>
  <h2>My prompt library</h2>
  <p class="how">Three prompts you'll reuse this month. Put [blanks] where the details change, and attach the check. Prompts saved in the <a href="prompt-builder.html">prompt builder</a> are added to your export too.</p>
  <div data-lib="3"></div>
  <button type="button" class="add" data-add-lib>+ Add a prompt</button>
</section>

<section data-title="Exercise 5 · RetailFlow">
  <div class="meta">Exercise 5 · Check · 35 min</div>
  <h2>Karen needs answers by Monday</h2>
  <p class="how"><a href="downloads/retailflow-customer-service-data.csv">Download the CSV</a>. Fresh chat. Upload blocked? Paste the first 50 rows, or describe the columns, and say so in your brief.</p>
  <div class="two">
    <div><label>Did the AI's description of the data match? <small>rows, columns, dates</small></label><select data-wb="e5-desc" data-label="Description matched"><option></option><option>Yes</option><option>No, and I corrected it</option></select></div>
    <div><label>Notes</label><input type="text" data-wb="e5-desc-note" data-label="Description notes"></div>
  </div>
  <label>Top three drivers of dissatisfaction</label><textarea data-wb="e5-q1" data-label="Q1 drivers"></textarea>
  <label>When response times blow out</label><textarea data-wb="e5-q2" data-label="Q2 blow-outs"></textarea>
  <label>My brief for Karen <small>under 300 words; write a first draft, then fix it after checking the claims</small></label><textarea class="big" data-wb="e5-brief" data-label="Brief for Karen"></textarea>
  <label>Verify: three claims are doing the rounds <small>check each against the data, not the confidence</small></label>
  <table><thead><tr><th style="width:42%">Claim</th><th style="width:22%">Verdict</th><th>Evidence from the data</th></tr></thead><tbody>
    <tr><td>A. "Email is roughly three times slower than Live Chat."</td><td><select data-wb="e6-a" data-label="Claim A verdict"><option></option><option>Verified</option><option>Overstated</option><option>Refuted</option><option>Can't tell yet</option></select></td><td><input type="text" data-wb="e6-a-ev" data-label="Claim A evidence"></td></tr>
    <tr><td>B. "Account Issues has the lowest satisfaction of any category, which makes sense, because account problems are the most complex to resolve."</td><td><select data-wb="e6-b" data-label="Claim B verdict"><option></option><option>Verified</option><option>Overstated</option><option>Refuted</option><option>Can't tell yet</option></select></td><td><input type="text" data-wb="e6-b-ev" data-label="Claim B evidence"></td></tr>
    <tr><td>C. "Sunday response times are more than double the overall average."</td><td><select data-wb="e6-c" data-label="Claim C verdict"><option></option><option>Verified</option><option>Overstated</option><option>Refuted</option><option>Can't tell yet</option></select></td><td><input type="text" data-wb="e6-c-ev" data-label="Claim C evidence"></td></tr>
  </tbody></table>
  <label>Was any of them in my first brief? Which would have done the most damage if Karen acted on it?</label>
  <textarea data-wb="e6-damage" data-label="Most damaging claim"></textarea>
  <label>Other numbers I checked myself <small>optional</small></label>
  <table><thead><tr><th>The AI said</th><th>I checked by</th><th>Result</th></tr></thead>
  <tbody data-table="e5-verify" data-cols="text,text,result" data-rows="1"></tbody></table>
  <label>What I checked <small>the last line of the brief</small></label><textarea data-wb="e5-checked" data-label="What I checked"></textarea>
</section>

<section data-title="Exercise 6 · Decide like me">
  <div class="meta">Exercise 6 · Check · 24 min</div>
  <h2>Teach it to decide like you</h2>
  <p class="how">One decision you make over and over: small, repeatable, explainable, and nothing from the top-right corner. Get the rules out, then test them blind on your own past calls. Describe past cases; don't paste anything confidential. Can't use real work? Take a <a href="exercises.html#decision-cards">decision card</a>. <a href="decide-like-me.html">The full method</a>.</p>
  <div class="two">
    <div><label>The decision</label><input type="text" data-wb="dlm-decision" data-label="The decision"></div>
    <div><label>How I got the rules out</label><select data-wb="dlm-path" data-label="Method"><option></option><option>Said it out loud</option><option>Let it interview me</option><option>Mined my history</option><option>Used a decision card</option></select></div>
  </div>
  <label>My decision rules <small>every if-then branch included</small></label>
  <textarea class="big" data-wb="dlm-rules" data-label="Decision rules"></textarea>
  <label>The blind test <small>write your calls before you run it; inputs only</small></label>
  <table><thead><tr><th>Past case (inputs only)</th><th>My call at the time</th><th>Its call, and the rule it used</th><th>Match?</th></tr></thead>
  <tbody data-table="dlm-test" data-cols="text,text,text,match" data-rows="3"></tbody></table>
  <button type="button" class="add" data-add-row="dlm-test">+ Add a case</button>
  <label>The mismatch I fixed <small>a threshold I never stated, an exception I apply without noticing, or a loose preference the rules made strict</small></label>
  <textarea data-wb="dlm-patch" data-label="Fixed mismatch"></textarea>
  <label>What I would never let it decide, and why</label>
  <textarea data-wb="dlm-keep" data-label="What stays mine"></textarea>
</section>

<section data-title="Exercise 7 · Plan one delivery">
  <div class="meta">Exercise 7 · Deliver · 35 min</div>
  <h2>My delivery plan</h2>
  <p class="how">One weekly task of 30 minutes or more, treated as a small AI project. Real work, sanitised. Can't use your own? Plan <a href="exercises.html#scenario-cards">scenario card</a> 3 or 6.</p>
  <div class="two">
    <div><label>The workflow</label><input type="text" data-wb="e7-wf" data-label="Workflow"></div>
    <div><label>Owner</label><input type="text" data-wb="e7-owner" data-label="Owner"></div>
    <div><label>Success measure</label><input type="text" data-wb="e7-measure" data-label="Success measure"></div>
    <div><label>Baseline today <small>time and quality</small></label><input type="text" data-wb="e7-base" data-label="Baseline"></div>
  </div>
  <label>Steps</label>
  <table><thead><tr><th>Step</th><th>Min now</th><th>Who leads</th><th>Corner</th><th>Checkpoint: who (knows what right looks like), how</th><th>Min after</th></tr></thead>
  <tbody data-table="e7-steps" data-cols="text,num,lead,corner,text,num" data-rows="5"></tbody></table>
  <button type="button" class="add" data-add-row="e7-steps">+ Add a step</button>
  <div class="two">
    <div><label>Who's affected</label><input type="text" data-wb="e7-affected" data-label="Affected"></div>
    <div><label>Who has to agree</label><input type="text" data-wb="e7-agree" data-label="Must agree"></div>
  </div>
  <label>The step I tested live, and what happened</label><textarea data-wb="e7-test" data-label="Live test"></textarea>
  <label>My 30-day gate <small>date and criteria, set now</small></label>
  <div class="four">
    <div><label>Gate date</label><input type="text" data-wb="e7-date" data-label="Gate date"></div>
    <div><label>Scale if</label><input type="text" data-wb="e7-scale" data-label="Scale if"></div>
    <div><label>Pivot if</label><input type="text" data-wb="e7-pivot" data-label="Pivot if"></div>
    <div><label>Kill if</label><input type="text" data-wb="e7-kill" data-label="Kill if"></div>
  </div>
</section>

<section data-title="Exercise 8 · Your action plan">
  <div class="meta">Exercise 8 · Deliver · 12 min</div>
  <h2>Your action plan</h2>
  <p class="how">One line each. Specific task, specific tool, specific day. Not "use AI more".</p>
  <div class="two">
    <div><label>This week · Practise <small>two-pass one task that matters; use one saved prompt</small></label><textarea data-wb="e8-week" data-label="This week (practise)"></textarea></div>
    <div><label>This month · Deliver <small>run your delivery plan</small></label><textarea data-wb="e8-month" data-label="This month (deliver)"></textarea></div>
    <div><label>Day 30 · Gate <small>scale, pivot or kill</small></label><textarea data-wb="e8-gate" data-label="Day 30 (gate)"></textarea></div>
    <div><label>This quarter · Revisit <small>what stays human; have the corners moved?</small></label><textarea data-wb="e8-quarter" data-label="This quarter (revisit)"></textarea></div>
  </div>
  <label>What must human eyes still judge in my work? <small>start from your Exercise 6 list of what you'd never let it decide</small></label><textarea data-wb="e8-human" data-label="What stays human"></textarea>
  <div class="chk">
    <label><input type="checkbox" data-wb="e8-cal1" data-label="This week's line is in my calendar"> This week's line is in my calendar</label>
    <label><input type="checkbox" data-wb="e8-cal2" data-label="Day-30 gate is in my calendar"> My day-30 gate is in my calendar</label>
  </div>
</section>
</div>

<script>
(function () {
  var KEY = 'human-edge-workbook-v1', LIBKEY = 'ai-in-practice-library';
  var OPTS = {
    pa: ['', 'Precise', 'Average'], ss: ['', 'Small', 'Large'],
    corner: ['', 'A · Light review', 'B · Load-bearing bits', 'C · Before you ship', 'D · Human in the loop'],
    lead: ['', 'AI leads', 'AI assists', 'You lead', 'Human only'],
    result: ['', 'Right', 'Close', 'Wrong'],
    match: ['', 'Match', 'Mismatch']
  };
  var root = document.getElementById('wb'), state = document.getElementById('wb-state');
  var data = {};
  try { data = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) {}

  function cell(type, key) {
    if (OPTS[type]) {
      return '<select data-wb="' + key + '">' + OPTS[type].map(function (o) { return '<option>' + o + '</option>'; }).join('') + '</select>';
    }
    return '<input type="text" data-wb="' + key + '"' + (type === 'num' ? ' size="4"' : '') + '>';
  }
  function addRows(tb, n) {
    var cols = tb.dataset.cols.split(','), id = tb.dataset.table;
    for (var i = 0; i < n; i++) {
      var r = tb.children.length, tr = document.createElement('tr');
      tr.innerHTML = cols.map(function (c, j) { return '<td>' + cell(c, id + '-' + r + '-' + j) + '</td>'; }).join('');
      tb.appendChild(tr);
    }
  }
  function addLib(box, n) {
    for (var i = 0; i < n; i++) {
      var k = box.children.length, d = document.createElement('div');
      d.className = 'lib';
      d.innerHTML = '<div class="two"><div><label>Prompt ' + (k + 1) + ' · name</label><input type="text" data-wb="lib-' + k + '-name" data-label="Prompt ' + (k + 1) + ' name"></div>' +
        '<div><label>Use it when</label><input type="text" data-wb="lib-' + k + '-use" data-label="Use it when"></div></div>' +
        '<label>The prompt, with [blanks]</label><textarea data-wb="lib-' + k + '-prompt" data-label="Prompt"></textarea>' +
        '<label>The check it needs</label>' + cell('corner', 'lib-' + k + '-check').replace('<select', '<select data-label="Check"');
      box.appendChild(d);
    }
  }
  root.querySelectorAll('tbody[data-table]').forEach(function (tb) {
    addRows(tb, Math.max(+tb.dataset.rows, data['_rows-' + tb.dataset.table] || 0));
  });
  var libBox = root.querySelector('[data-lib]');
  addLib(libBox, Math.max(+libBox.dataset.lib, data._lib || 0));

  function grow(t) { t.style.height = 'auto'; t.style.height = (t.scrollHeight + 2) + 'px'; }
  function restore() {
    root.querySelectorAll('[data-wb]').forEach(function (el) {
      var v = data[el.dataset.wb];
      if (v === undefined) return;
      if (el.type === 'checkbox') el.checked = !!v; else el.value = v;
      if (el.tagName === 'TEXTAREA') grow(el);
    });
  }
  function save() {
    root.querySelectorAll('[data-wb]').forEach(function (el) {
      data[el.dataset.wb] = el.type === 'checkbox' ? el.checked : el.value;
    });
    root.querySelectorAll('tbody[data-table]').forEach(function (tb) { data['_rows-' + tb.dataset.table] = tb.children.length; });
    data._lib = libBox.children.length;
    try {
      localStorage.setItem(KEY, JSON.stringify(data));
      state.textContent = 'Saved in this browser · ' + new Date().toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
    } catch (e) { state.textContent = 'Could not save here (private browsing?). Export now.'; }
  }
  root.addEventListener('input', function (e) { if (e.target.tagName === 'TEXTAREA') grow(e.target); save(); });
  root.addEventListener('change', save);
  root.addEventListener('click', function (e) {
    var b = e.target.closest('[data-add-row]');
    if (b) { addRows(root.querySelector('tbody[data-table="' + b.dataset.addRow + '"]'), 1); save(); }
    if (e.target.closest('[data-add-lib]')) { addLib(libBox, 1); save(); }
  });
  restore();
  if (Object.keys(data).length) state.textContent = 'Restored your earlier answers from this browser.';

  function val(el) { return el.type === 'checkbox' ? (el.checked ? 'Yes' : '') : (el.value || '').trim(); }
  function exportMd() {
    var md = '# The Human Edge: my workbook\n\n';
    var nm = root.querySelector('[data-wb="name"]');
    if (val(nm)) md += '**' + val(nm) + '** · ' + new Date().toLocaleDateString() + '\n\n';
    root.querySelectorAll('section').forEach(function (sec) {
      var whole = md; md = '';
      sec.querySelectorAll('[data-wb]').forEach(function (el) {
        var tb = el.closest('tbody[data-table]');
        if (tb) {
          if (tb.dataset.out) return;
          tb.dataset.out = '1';
          var heads = [].map.call(tb.parentNode.querySelectorAll('th'), function (h) { return h.textContent; });
          var rows = [].filter.call(tb.children, function (tr) { return [].some.call(tr.querySelectorAll('[data-wb]'), function (x) { return val(x); }); });
          if (rows.length) {
            md += '| ' + heads.join(' | ') + ' |\n|' + heads.map(function () { return '---'; }).join('|') + '|\n';
            rows.forEach(function (tr) { md += '| ' + [].map.call(tr.querySelectorAll('[data-wb]'), val).join(' | ') + ' |\n'; });
            md += '\n';
          }
          return;
        }
        var v = val(el);
        if (!v) return;
        var lab = el.dataset.label || (el.closest('tr') ? el.closest('tr').cells[0].textContent : '');
        md += (v.indexOf('\n') > -1 ? '**' + lab + '**\n\n' + v : '**' + lab + ':** ' + v) + '\n\n';
      });
      root.querySelectorAll('tbody[data-out]').forEach(function (tb) { delete tb.dataset.out; });
      md = whole + (md ? '## ' + sec.dataset.title + '\n\n' + md : '');
    });
    var lib = [];
    try { lib = JSON.parse(localStorage.getItem(LIBKEY)) || []; } catch (e) {}
    if (lib.length) {
      md += '## From the prompt builder\n\n';
      lib.forEach(function (p) { md += '### ' + (p.name || 'Untitled') + '\n\n' + (p.use ? '**Use it when:** ' + p.use + '\n\n' : '') + (p.check ? '**Check:** ' + p.check + '\n\n' : '') + '```\n' + p.prompt + '\n```\n\n'; });
    }
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([md], { type: 'text/markdown' }));
    a.download = 'human-edge-workbook.md'; a.click();
  }
  document.getElementById('wb-export').onclick = exportMd;
  document.getElementById('wb-print').onclick = function () { root.querySelectorAll('textarea').forEach(grow); window.print(); };
  document.getElementById('wb-clear').onclick = function () {
    if (confirm('Clear all workbook answers on this device? Export first if you want to keep them.')) { localStorage.removeItem(KEY); location.reload(); }
  };
})();
</script>
```
