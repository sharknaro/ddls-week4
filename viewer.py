from pathlib import Path
import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

ROOT = Path(__file__).parent
app = FastAPI(title="p53 structure comparison")


def load_text():
    alpha = (ROOT / "data/p53_alphafold_model.cif").read_text()
    course = json.loads((ROOT / "results/course_fold_p53.json").read_text())["pdb"]
    return {"alpha": alpha, "course": course}


@app.get("/structures")
def structures():
    return load_text()


@app.get("/", response_class=HTMLResponse)
def index():
    return r'''<!doctype html>
<html><head><meta charset="utf-8"><title>p53 structure comparison</title>
<style>html,body,#viewport{width:100%;height:100%;margin:0}#panel{position:fixed;z-index:2;top:12px;left:12px;background:#ffffffeF;padding:14px;border-radius:8px;font:14px system-ui;box-shadow:0 2px 10px #0003;min-width:270px}label{display:block;margin:7px 0}.source{font-weight:600}.swatch{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:5px}.legend{margin-top:10px;border-top:1px solid #ddd;padding-top:8px;font-size:12px}.bar{height:12px;border-radius:4px;background:linear-gradient(90deg,#d73027,#fee08b,#1a9850);margin:4px 0}.ticks{display:flex;justify-content:space-between;color:#555}.note{font-size:12px;color:#444;margin-top:8px}button{margin-top:6px}</style>
<script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script></head>
<body><div id="panel"><b>p53 structure comparison</b><label class="source"><input id="alpha" type="checkbox" checked> <span class="swatch" style="background:#1976d2"></span>AlphaFold DB (confidence gradient)</label><label class="source"><input id="course" type="checkbox" checked> <span class="swatch" style="background:#d32f2f"></span>Course fold (confidence gradient)</label><label><input id="overlay" type="checkbox" checked> Overlay models</label><label>Opacity <input id="opacity" type="range" min="0.1" max="1" step="0.05" value="0.9"></label><button id="reset">Reset view</button><div class="legend"><b>pLDDT confidence</b><div class="bar"></div><div class="ticks"><span>0 low</span><span>50</span><span>70</span><span>90</span><span>100 high</span></div></div><div class="note">Blue/red identifies the source. Within each model, the gradient shows its own per-residue pLDDT: red = low, yellow = intermediate, green = high.</div><div>Drag: rotate · scroll: zoom · right-drag: pan</div></div><div id="viewport"></div>
<script>
let viewer, models={};
function confidenceColor(atom){const v=Number(atom.b||0);if(v<50)return '#d73027';if(v<70)return '#fee08b';if(v<90)return '#66bd63';return '#1a9850'}
async function start(){
 viewer=$3Dmol.createViewer('viewport',{backgroundColor:'white'});
 const d=await (await fetch('/structures')).json();
 models.alpha=viewer.addModel(d.alpha,'cif'); models.course=viewer.addModel(d.course,'pdb');
 render(); viewer.zoomTo(); viewer.render();
}
function gradientStyle(model,visible,sourceColor){
 model.setVisibility(visible);
 model.setStyle({}, {cartoon:{colorscheme:{prop:'b',map:confidenceColor},opacity:Number(document.getElementById('opacity').value)}});
 // Add a thin source-colored trace so overlapping models remain identifiable.
 model.addStyle({}, {line:{color:sourceColor,opacity:0.35,linewidth:1}});
}
function render(){
 const a=document.getElementById('alpha').checked,c=document.getElementById('course').checked;
 gradientStyle(models.alpha,a,'#1976d2'); gradientStyle(models.course,c,'#d32f2f');
 viewer.render();
}
document.querySelectorAll('input').forEach(x=>x.addEventListener('input',render));document.getElementById('reset').onclick=()=>{viewer.zoomTo();viewer.render()};start();
</script></body></html>'''
