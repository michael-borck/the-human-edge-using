---
pagetitle: Prompt builder
description: "Build an RTCF prompt, add upgrades, attach its check, and save it to your own prompt library."
nav-builder: true
---

::: kicker
Tool 2 · RTCF
:::

# Prompt builder. <em>Your library stays with you.</em>

::: lede
Fill in the four parts, add an upgrade if the output is weak, and attach the check the output needs. Saved prompts stay in this browser only; nothing is sent anywhere. Export your library as a text file to keep it.
:::

::: note
**One prompt, or a standing brief.** For one task, fill in all four parts. For a brief you save once in custom instructions, a project or a Gem, fill in Role, Context and Format with what's true every time, and leave the Task for each chat. [Set it once](beyond.html#set-it-once) shows where each tool keeps it.
:::

```{=html}
<style>
.pb{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:26px}
@media (max-width:820px){.pb{grid-template-columns:1fr}}
.pb label{display:block;font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);font-weight:700;margin:16px 0 6px}
.pb label span{color:var(--dim);font-weight:400;letter-spacing:.04em;text-transform:none;font-family:var(--sans);font-size:13.5px;margin-left:6px}
.pb input[type=text],.pb textarea,.pb select{width:100%;background:#0C0F15;border:1px solid var(--hair);border-radius:8px;color:var(--ink);padding:10px 12px;font:15px/1.5 var(--sans)}
.pb textarea{min-height:76px;resize:vertical}
.pb textarea#c{min-height:130px}
.pb input:focus,.pb textarea:focus,.pb select:focus{outline:none;border-color:var(--acc)}
.ups{display:flex;flex-direction:column;gap:8px;margin-top:4px}
.ups label{display:flex;gap:10px;align-items:flex-start;margin:0;font-family:var(--sans);font-size:15px;letter-spacing:0;text-transform:none;color:var(--ink);font-weight:500}
.ups input{margin-top:5px;accent-color:var(--acc)}
.ups small{display:block;color:var(--dim);font-size:13px}
#ex-wrap{display:none}
.out{background:#0C0F15;border:1px solid var(--hair);border-radius:10px;padding:16px 18px;font-family:var(--mono);font-size:13.5px;line-height:1.7;color:var(--ink);white-space:pre-wrap;min-height:240px}
.out.empty{color:var(--faint)}
.hint{font-size:14px;color:var(--dim);margin-top:10px;min-height:22px}
.hint b{color:var(--coral)}
.row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.row button{font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;padding:10px 16px;border-radius:999px;border:1px solid var(--acc);background:none;color:var(--acc);cursor:pointer}
.row button.solid{background:var(--acc);color:#0A0C10}
.lib{margin-top:14px;display:flex;flex-direction:column;gap:12px}
.item{background:var(--card);border:1px solid var(--hair);border-radius:10px;padding:14px 16px}
.item h4{margin:0;font-family:var(--sans);font-size:17px;color:var(--ink)}
.item p{margin:4px 0 0;font-size:14px;color:var(--dim)}
.item .row{margin-top:10px}
.item .row button{padding:6px 12px;font-size:11px}
</style>
<div class="pb" id="pb">
  <div>
    <label for="n">Name <span>what you'll call it</span></label>
    <input type="text" id="n" placeholder="Friday status update">
    <label for="u">Use it when <span>the situation</span></label>
    <input type="text" id="u" placeholder="Turning my raw notes into the steering committee update">
    <label for="r">Role <span>who should it write as?</span></label>
    <input type="text" id="r" placeholder="You are an experienced project manager who writes plainly.">
    <label for="t">Task <span>what exactly, and how much?</span></label>
    <textarea id="t" placeholder="Turn my notes into a weekly status update for the steering committee."></textarea>
    <label for="c">Context <span>audience, situation, constraints, stakes, material</span></label>
    <textarea id="c" placeholder="Audience: CIO, sponsor and two business leads. They want no surprises; bad news comes with a mitigation. My notes: [paste]"></textarea>
    <label for="f">Format <span>length, structure, tone</span></label>
    <textarea id="f" placeholder="RAG status with one line, wins as bullets, a risks table (risk, impact, mitigation, owner), next week. Under 250 words."></textarea>
    <label>Upgrades <span>add one when the output is weak</span></label>
    <div class="ups">
      <label><input type="checkbox" id="u-ex"><span>+ Example <small>Show one you liked.</small></span></label>
      <div id="ex-wrap"><textarea id="ex" placeholder="Paste an example you liked."></textarea></div>
      <label><input type="checkbox" id="u-done"><span>+ Done <small>Say what done looks like, and allow it to be unsure.</small></span></label>
      <label><input type="checkbox" id="u-q"><span>+ Questions <small>Let it ask you first.</small></span></label>
      <label><input type="checkbox" id="u-steps"><span>+ Steps <small>Split the job.</small></span></label>
    </div>
    <label>Push back <span>keep it honest</span></label>
    <div class="ups">
      <label><input type="checkbox" id="u-guard"><span>Guardrail <small>Only change its view for a new fact, and name it.</small></span></label>
    </div>
    <label for="k">The check it needs <span>trust tool corner</span></label>
    <select id="k">
      <option value="">Choose a corner</option>
      <option>A · Trust with light review</option>
      <option>B · Verify the load-bearing bits</option>
      <option>C · Verify before you ship</option>
      <option>D · Human in the loop</option>
    </select>
  </div>
  <div>
    <label>Your prompt</label>
    <div class="out empty" id="out">Your assembled prompt appears here as you type.</div>
    <div class="hint" id="hint"></div>
    <div class="row">
      <button class="solid" id="copy">Copy prompt</button>
      <button id="save">Save to library</button>
      <button id="clear">Clear</button>
    </div>
    <label style="margin-top:30px">Your library <span id="count"></span></label>
    <div class="lib" id="lib"></div>
    <div class="row">
      <button id="export">Export library (.md)</button>
    </div>
  </div>
</div>
<script>
(function(){
  const $=id=>document.getElementById(id);
  const F=['n','u','r','t','c','f','ex','k'];
  const KEY='ai-in-practice-library';
  const UP={
    'u-done':'Done means: it meets the format above, it uses only facts I have given you, and anything you are unsure of is marked [CHECK].',
    'u-q':'Before you start, ask me up to five questions about anything you need to know.',
    'u-steps':'Work in steps. Give me an outline first and wait for my go-ahead before drafting.',
    'u-guard':'Only change your assessment if I give you a new fact. Name the fact that changed it.'
  };
  function build(){
    const v=Object.fromEntries(F.map(k=>[k,$(k).value.trim()]));
    const parts=[];
    if(v.r) parts.push('ROLE\n'+v.r);
    if(v.t) parts.push('TASK\n'+v.t);
    if(v.c) parts.push('CONTEXT\n'+v.c);
    if(v.f) parts.push('FORMAT\n'+v.f);
    if($('u-ex').checked && v.ex) parts.push('EXAMPLE\nMatch the length and tone of this example:\n'+v.ex);
    const extra=Object.keys(UP).filter(k=>$(k).checked).map(k=>UP[k]);
    if(extra.length) parts.push('INSTRUCTIONS\n'+extra.join('\n'));
    return {v, text:parts.join('\n\n')};
  }
  function hint(v){
    const w=s=>s?s.split(/\s+/).length:0;
    if(!v.t) return 'Start with the Task: a verb and a scope.';
    if(w(v.c)<15) return '<b>Context is thin.</b> Who is it for, what happened, what does good look like? Context does most of the work.';
    if(!v.f) return '<b>No Format.</b> Name the shape you want to paste: length, structure, tone.';
    if(!v.k) return 'Attach the check: which trust tool corner does the output land in?';
    return 'Looks complete. Run it, then decide whether it needs an upgrade.';
  }
  function render(){
    const {v,text}=build();
    $('out').textContent=text||'Your assembled prompt appears here as you type.';
    $('out').classList.toggle('empty',!text);
    $('hint').innerHTML=hint(v);
    $('ex-wrap').style.display=$('u-ex').checked?'block':'none';
  }
  const load=()=>{try{return JSON.parse(localStorage.getItem(KEY))||[]}catch(e){return []}};
  const store=l=>localStorage.setItem(KEY,JSON.stringify(l));
  function esc(s){return s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
  function showLib(){
    const l=load();
    $('count').textContent=l.length?`${l.length} saved`:'nothing saved yet';
    $('lib').innerHTML=l.map((e,i)=>`<div class="item"><h4>${esc(e.name||'Untitled')}</h4><p>${esc(e.use||'')}${e.check?' · Check: '+esc(e.check):''}</p>
      <div class="row"><button data-a="copy" data-i="${i}">Copy</button><button data-a="load" data-i="${i}">Edit</button><button data-a="del" data-i="${i}">Delete</button></div></div>`).join('');
  }
  function copy(t,btn){navigator.clipboard.writeText(t).then(()=>{const o=btn.textContent;btn.textContent='Copied';setTimeout(()=>btn.textContent=o,1200)})}
  F.concat(['u-ex','u-done','u-q','u-steps','u-guard']).forEach(id=>$(id).addEventListener('input',render));
  $('copy').onclick=e=>{const {text}=build(); if(text) copy(text,e.target)};
  $('save').onclick=()=>{
    const {v,text}=build(); if(!text) return;
    const l=load();
    const ups=Object.fromEntries(['u-ex','u-done','u-q','u-steps','u-guard'].map(k=>[k,$(k).checked]));
    const entry={name:v.n,use:v.u,check:v.k,prompt:text,fields:v,ups};
    const at=l.findIndex(e=>e.name&&e.name===v.n);
    if(at>=0) l[at]=entry; else l.push(entry);
    store(l); showLib();
  };
  $('clear').onclick=()=>{F.forEach(k=>$(k).value='');['u-ex','u-done','u-q','u-steps','u-guard'].forEach(k=>$(k).checked=false);render()};
  $('lib').onclick=e=>{
    const b=e.target.closest('button'); if(!b) return;
    const l=load(), i=+b.dataset.i, it=l[i];
    if(b.dataset.a==='copy') copy(it.prompt,b);
    if(b.dataset.a==='del'){l.splice(i,1);store(l);showLib()}
    if(b.dataset.a==='load'){F.forEach(k=>$(k).value=(it.fields||{})[k]||'');Object.entries(it.ups||{}).forEach(([k,on])=>$(k).checked=on);render();window.scrollTo({top:$('pb').offsetTop-80,behavior:'smooth'})}
  };
  $('export').onclick=()=>{
    const l=load(); if(!l.length) return;
    const md='# My prompt library\n\n'+l.map(e=>`## ${e.name||'Untitled'}\n\n**Use it when:** ${e.use||''}\n\n**Check:** ${e.check||''}\n\n\`\`\`\n${e.prompt}\n\`\`\`\n`).join('\n');
    const a=document.createElement('a');
    a.href=URL.createObjectURL(new Blob([md],{type:'text/markdown'}));
    a.download='my-prompt-library.md'; a.click();
  };
  render(); showLib();
})();
</script>
```

::: note
**Why the check matters.** A saved prompt with its check attached is the first draft of what agent tools call a skill: a reusable brief an assistant loads when your request matches it. Because it's plain text, it moves with you between tools.
:::
