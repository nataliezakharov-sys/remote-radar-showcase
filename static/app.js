'use strict';
const storeKey = 'remote-radar-showcase-v1';
const app = { jobs: [], selected: null, page: 'discover', query: '', location: 'all', order: 'score', statuses: {} };
const el = id => document.getElementById(id);
const escapeHTML = input => String(input ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','\'':'&#39;'}[ch]));
function stored() { try { return JSON.parse(localStorage.getItem(storeKey) || '{}'); } catch { return {}; } }
function persist(){ localStorage.setItem(storeKey, JSON.stringify(app.statuses)); }
function status(job){ return app.statuses[job.id] || job.status; }
function label(job){ const v = job.category; return `<span class="tag ${v === 'Strong match' ? 'good' : 'warn'}">${escapeHTML(v)}</span>`; }
function filtered(){
  let jobs=app.jobs.filter(job => {
    if(app.page==='shortlist' && !['Shortlisted','Saved'].includes(status(job)))return false;
    if(app.page==='review' && status(job)!=='Needs review')return false;
    if(app.page==='applications' && !['Applied','Interview','Draft'].includes(status(job)))return false;
    return `${job.company} ${job.title}`.toLowerCase().includes(app.query.toLowerCase()) && (app.location==='all'||job.location.includes(app.location));
  });
  if(app.order==='title')jobs.sort((a,b)=>a.title.localeCompare(b.title));else jobs.sort((a,b)=>b.score-a.score);
  return jobs;
}
function render(){
  const headings={discover:['Discover roles','Explore matched opportunities with grounded eligibility and evidence.'],shortlist:['Shortlist','Saved opportunities for further consideration.'],review:['Needs review','Check restricted locations and missing skills before proceeding.'],applications:['Application tracker','Sample entries only. No live ATS integration.']};
  el('heading').textContent=headings[app.page][0];el('subtitle').textContent=headings[app.page][1];
  document.querySelectorAll('.nav').forEach(n=>{n.classList.toggle('active',n.dataset.page===app.page);n.setAttribute('aria-current',n.dataset.page===app.page?'page':'false');});
  el('shortlist-count').textContent=app.jobs.filter(j=>['Shortlisted','Saved'].includes(status(j))).length;
  el('review-count').textContent=app.jobs.filter(j=>status(j)==='Needs review').length;
  const jobs=filtered();if(!jobs.some(j=>j.id===app.selected))app.selected=jobs[0]?.id||null;
  el('list').innerHTML=jobs.length?jobs.map(j=>`<button class="job ${j.id===app.selected?'selected':''}" data-id="${j.id}" aria-pressed="${j.id===app.selected}"><div class="jobtop"><span class="company">${escapeHTML(j.company)}</span><strong class="score">${j.score}% match</strong></div><strong class="jobtitle">${escapeHTML(j.title)}</strong><span class="meta">${escapeHTML(j.location)} · ${escapeHTML(j.posted)}</span><div class="jobbottom">${label(j)}<span class="status">${escapeHTML(status(j))}</span></div></button>`).join(''):'<div class="empty">No matching sample roles. Try adjusting the search or filters.</div>';
  for(const button of el('list').querySelectorAll('button.job'))button.addEventListener('click',()=>{app.selected=button.dataset.id;render();});
  detail();
}
function detail(){
  const j=app.jobs.find(job=>job.id===app.selected);if(!j){el('detail').innerHTML='<div class="placeholder">Select a sample role to see more details.</div>';return;}
  const safe=escapeHTML;const evidence=j.evidence.map(x=>`<li><span aria-hidden="true">✓</span> ${safe(x)}</li>`).join('');
  el('detail').innerHTML=`<div class="detailtop"><span class="eyebrow">OPPORTUNITY OVERVIEW</span><span class="scorepill">${j.score}% match</span></div><h2>${safe(j.title)}</h2><p class="detailcompany">${safe(j.company)} · ${safe(j.location)}</p><div class="separator"></div><p class="eyebrow">WHY IT MATCHES</p><ul class="evidence">${evidence}</ul><div class="review-note"><strong>Before applying</strong><p>${safe(j.review)}</p></div><p class="eyebrow">ROLE FOCUS</p><p class="focus">${safe(j.focus)}</p><div class="detailactions"><button id="save-job" class="primary">${['Shortlisted','Saved'].includes(status(j))?'Remove from shortlist':'Save to shortlist'}</button><button id="review-job" class="outline">${status(j)==='Needs review'?'Mark as reviewed':'Needs review'}</button></div><p class="disclaimer">Changes are stored in this browser only. No external action is possible.</p>`;
  el('save-job').addEventListener('click',()=>{app.statuses[j.id]=['Shortlisted','Saved'].includes(status(j))?'New':'Shortlisted';persist();render();});
  el('review-job').addEventListener('click',()=>{app.statuses[j.id]=status(j)==='Needs review'?'Saved':'Needs review';persist();render();});
}
document.querySelectorAll('.nav').forEach(n=>n.addEventListener('click',()=>{app.page=n.dataset.page;app.selected=null;render();}));
el('search').addEventListener('input',e=>{app.query=e.target.value;render();});
el('location').addEventListener('change',e=>{app.location=e.target.value;render();});
el('order').addEventListener('change',e=>{app.order=e.target.value;render();});
el('reset').addEventListener('click',()=>{localStorage.removeItem(storeKey);app.statuses={};app.query='';app.location='all';app.order='score';app.page='discover';el('search').value='';el('location').value='all';el('order').value='score';render();});
(async()=>{try{const r=await fetch('/api/jobs',{credentials:'omit'});if(!r.ok)throw new Error('Server unavailable');const data=await r.json();if(!data.demo)throw new Error('Not a showcase response');app.jobs=data.jobs;app.statuses=stored();el('total-stat').textContent=app.jobs.length;el('strong-stat').textContent=app.jobs.filter(j=>j.category==='Strong match').length;el('review-stat').textContent=app.jobs.filter(j=>j.category.includes('Review')).length;el('discover-count').textContent=app.jobs.length;render();}catch(err){el('list').textContent='Unable to load fictional sample data.';el('detail').textContent='Try refreshing the page.';}})();
