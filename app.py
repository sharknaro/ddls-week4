from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, Response

ROOT = Path(__file__).parent
RESULTS = ROOT / "results"
app = FastAPI(title="p53 structure evidence")


def evidence():
    return json.loads((RESULTS / "results.json").read_text(encoding="utf-8"))

@app.get("/api/results")
def results():
    return evidence()

@app.get("/api/structure/{source}")
def structure(source: str):
    item = evidence()["structures"].get(source)
    if not item:
        raise HTTPException(404, "Unknown structure")
    if item["format"] == "pdb":
        payload = json.loads((ROOT / item["path"]).read_text(encoding="utf-8"))["pdb"]
        return Response(payload, media_type="chemical/x-pdb")
    return Response((ROOT / item["path"]).read_text(encoding="utf-8"), media_type="chemical/x-cif")

@app.get("/api/pae/{source}")
def pae(source: str):
    item = evidence()["structures"].get(source)
    if not item:
        raise HTTPException(404, "Unknown source")
    path = ROOT / item["pae_path"]
    if source == "course":
        payload = json.loads((ROOT / item["path"]).read_text(encoding="utf-8"))["pae"]
    else:
        payload = json.loads(path.read_text(encoding="utf-8"))[0]["predicted_aligned_error"]
    return {"pae": payload}

@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse(INDEX)

INDEX = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>p53 evidence readout</title><script src="https://cdn.tailwindcss.com"></script><script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script><style>body{background:#f7f8fa}.chart{height:230px}.swatch{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px}</style></head><body class="text-slate-900"><main class="max-w-7xl mx-auto px-5 py-8"><header class="mb-7"><div class="flex items-center gap-3 text-sm text-slate-500"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 20 7.5v9L12 21l-8-4.5v-9L12 3Z"/><path d="m4.5 7.7 7.5 4.4 7.5-4.4M12 12.1V21"/></svg>STRUCTURE EVIDENCE READOUT</div><h1 class="text-3xl font-semibold mt-2">Human p53: model-supported starting region</h1><p class="text-slate-600 mt-2">A narrow, auditable comparison of the supplied structure confidence data.</p></header><section class="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm"><div class="flex gap-3"><svg class="text-emerald-600 shrink-0 mt-1" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="m8 12 2.5 2.5L16.5 9"/></svg><div><h2 class="font-semibold text-lg">Headline answer</h2><p id="headline" class="mt-1 text-slate-700"></p><p id="structure" class="mt-3 text-sm text-slate-600 border-t pt-3"></p></div></div></section><section class="grid lg:grid-cols-2 gap-5 mt-5"><div class="bg-white border rounded-2xl p-5"><div class="flex justify-between items-center"><h2 class="font-semibold">3D structure · pLDDT</h2><div class="text-xs"><span class="swatch bg-blue-600"></span>AlphaFold DB <span class="swatch bg-red-600 ml-3"></span>Course fold</div></div><div id="viewer" class="h-[520px] w-full rounded-xl mt-3 bg-slate-50 border border-slate-200 relative"><div id="viewer-status" class="absolute inset-0 grid place-items-center text-sm text-slate-500">Loading structure…</div></div><div class="flex gap-2 mt-3 text-xs flex-wrap"><span class="px-2 py-1 rounded bg-orange-100">18–28</span><span class="px-2 py-1 rounded bg-blue-100">94–312 core</span><span class="px-2 py-1 rounded bg-red-100">294–312 weak region</span></div></div><div class="bg-white border rounded-2xl p-5"><h2 class="font-semibold">Confidence matching the claim</h2><p class="text-sm text-slate-600 mt-1">Fold/region claim → per-residue pLDDT. Marked regions are the owner’s comparison intervals.</p><div class="mt-3 overflow-x-auto border rounded-lg"><canvas id="chart" class="chart w-full min-w-[760px]"></canvas></div><div class="mt-3 overflow-x-auto border rounded-lg"><table class="min-w-[760px] w-full text-[10px]" id="sequence-table"><thead><tr class="bg-slate-50"><th class="sticky left-0 bg-slate-50 px-2 py-1 text-left">Residue</th></tr></thead><tbody><tr><th class="sticky left-0 bg-slate-50 px-2 py-1 text-left">AA</th></tr><tr><th class="sticky left-0 bg-slate-50 px-2 py-1 text-left">pLDDT</th></tr></tbody></table></div><div id="stats" class="grid grid-cols-2 gap-3 mt-3"></div><div class="mt-5"><h3 class="font-medium text-sm">Confidence scale</h3><div class="h-3 rounded mt-2" style="background:linear-gradient(90deg,#d73027,#fee08b,#1a9850)"></div><div class="flex justify-between text-xs text-slate-500"><span>0 low</span><span>50</span><span>70</span><span>90</span><span>100 high</span></div></div></div></section><section class="bg-amber-50 border border-amber-200 rounded-2xl p-5 mt-5"><div class="flex gap-3"><svg class="text-amber-700 shrink-0" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 22 21H2L12 3Z"/><path d="M12 9v5M12 18h.01"/></svg><div><h2 class="font-semibold">Caveat / trap</h2><p id="caveat" class="text-sm text-amber-950 mt-1"></p></div></div></section><p class="text-xs text-slate-500 mt-6">This readout is limited to the supplied wild-type, isolated single-chain models. It does not validate the experimental construct, assembly, interface, or partner-bound conformation.</p></main><script>
let ev,viewer;const $=id=>document.getElementById(id);function color(b){return b<50?'#d73027':b<70?'#fee08b':b<90?'#66bd63':'#1a9850'}
async function init(){ev=await (await fetch('/api/results')).json();$('headline').textContent=ev.headline;$('structure').textContent=ev.structure_check;$('caveat').textContent=ev.caveat;const r=ev.regions;$('stats').innerHTML=`<div class="bg-slate-50 rounded-lg p-3"><div class="text-xs text-slate-500">N-terminal 1–93 mean</div><b>${r.n_terminal.mean.toFixed(2)}</b></div><div class="bg-blue-50 rounded-lg p-3"><div class="text-xs text-slate-500">Core 94–312 mean / min</div><b>${r.core.mean.toFixed(2)} / ${r.core.min.toFixed(2)}</b></div><div class="col-span-2 text-sm text-slate-600">Difference: <b>${ev.comparison.difference.toFixed(2)}</b> · Ratio: <b>${ev.comparison.ratio.toFixed(2)}</b> · Rule: <b>${ev.comparison.decision}</b></div>`;drawChart();await draw3d()}
async function drawChart(){const c=$('chart'),d=devicePixelRatio||1,w=Math.max(c.parentElement.clientWidth,760),h=230;c.width=w*d;c.height=h*d;c.style.width=w+'px';const x=c.getContext('2d');x.scale(d,d);const t=await (await fetch('/api/structure/alphafold')).text(),af=[],aa=[];for(const l of t.split('\\n'))if(l.startsWith('ATOM')){const n=+l.slice(22,26);if(!af[n-1]){af[n-1]=+l.slice(60,66);aa[n-1]=l.slice(17,20)}}const vals=af.filter(v=>v!==undefined),sx=w/392;x.strokeStyle='#cbd5e1';for(let y of [50,70,90]){let py=h-y*h/100;x.beginPath();x.moveTo(0,py);x.lineTo(w,py);x.stroke()}for(const [a,b,col] of [[18,28,'#f59e0b'],[94,312,'#2563eb'],[294,312,'#dc2626']]){x.fillStyle=col+'22';x.fillRect((a-1)*sx,0,(b-a+1)*sx,h)}x.strokeStyle='#334155';x.beginPath();vals.forEach((v,i)=>{let px=i*sx,py=h-v*h/100;i?x.lineTo(px,py):x.moveTo(px,py)});x.stroke();x.fillStyle='#334155';x.font='12px sans-serif';x.fillText('pLDDT',5,15);let rows=$('sequence-table').querySelectorAll('tr');for(let i=1;i<=393;i++){let cells=[i,aa[i-1]||'',af[i-1]?.toFixed(1)||''];cells.forEach((v,j)=>{let td=document.createElement('td');td.textContent=v;td.className='px-1 py-1 text-center';if(j===2)td.style.backgroundColor=color(af[i-1])+'66';rows[j].appendChild(td)})}}
async function draw3d(){const status=$('viewer-status');try{if(!window.$3Dmol)throw new Error('3Dmol.js did not load');viewer=$3Dmol.createViewer($('viewer'),{backgroundColor:'white',antialias:true});const a=await fetch('/api/structure/alphafold').then(x=>{if(!x.ok)throw Error('AlphaFold structure unavailable');return x.text()});let ma=viewer.addModel(a,'cif');if(!ma)throw Error('CIF structure could not be parsed');ma.setStyle({}, {cartoon:{color:'spectrum',opacity:.9}});ma.addStyle({resi:'18-28'},{stick:{color:'orange',radius:.25}});ma.addStyle({resi:'294-312'},{stick:{color:'red',radius:.3}});viewer.zoomTo({},1.2);viewer.render();status.remove()}catch(err){status.textContent='3D structure could not be loaded: '+err.message;status.className='absolute inset-0 grid place-items-center text-sm text-red-700 p-4 text-center'}}init();</script></body></html>'''
