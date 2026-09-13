# -*- coding: utf-8 -*-
"""Gera dados.json e roteiro-brasil-2026.html."""
import json
from dados_a import DIAS_A
from dados_b import DIAS_B

D = DIAS_A + DIAS_B
dados = {"PEND": __import__("dados_b").PEND, "D": D}

json.dump(dados, open("dados.json", "w"), ensure_ascii=False, indent=1)

PAYLOAD = json.dumps(dados, ensure_ascii=False)

HTML = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#12191f">
<title>Roteiro Brasil 2026</title>
<style>
:root{
  --ink:#12191f; --paper:#fff; --soft:#f4f6f8; --mut:#68747f; --rule:#e3e8ec;
  --voo:#2d6cdf; --onibus:#6d4bc4; --hotel:#0d8a68; --passeio:#c07000;
  --jantar:#c03a50; --livre:#7b8896; --via:#9aa6b0; --festa:#b13a8e;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  background:var(--paper); color:var(--ink);
  font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:720px;margin:0 auto;padding:0 18px 64px}
header.top{padding:26px 0 14px}
h1{font-size:23px;line-height:1.2;letter-spacing:-.02em;margin:0 0 4px;font-weight:650}
.sub{color:var(--mut);font-size:14px}
nav.dias{
  position:sticky;top:0;z-index:20;background:rgba(255,255,255,.96);
  backdrop-filter:saturate(180%) blur(8px);
  border-bottom:1px solid var(--rule);margin:0 -18px;padding:9px 18px;
  display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;
}
nav.dias::-webkit-scrollbar{display:none}
nav.dias button{
  flex:0 0 auto;font:600 13px/1 inherit;color:var(--mut);background:var(--soft);
  border:1px solid transparent;border-radius:999px;padding:8px 11px;cursor:pointer;
  font-variant-numeric:tabular-nums;
}
nav.dias button[aria-current="true"]{background:var(--ink);color:#fff}
nav.dias button:focus-visible{outline:2px solid var(--voo);outline-offset:2px}
.cabdia{display:flex;gap:14px;align-items:baseline;padding:24px 0 6px;border-bottom:1px solid var(--rule)}
.num{font-size:40px;font-weight:680;letter-spacing:-.04em;font-variant-numeric:tabular-nums;line-height:1}
.num i{font-style:normal;font-size:15px;font-weight:600;color:var(--mut);margin-left:5px}
.cabtxt{flex:1}
.cidade{display:block;font-weight:620;font-size:16px}
.resumo{display:block;color:var(--mut);font-size:14px}
.item{display:flex;gap:13px;padding:17px 0;border-bottom:1px solid var(--rule)}
.hora{flex:0 0 52px;font-variant-numeric:tabular-nums;font-weight:620;font-size:14px;padding-top:1px}
.corpo{flex:1;min-width:0}
.tag{
  display:inline-block;font-size:11px;font-weight:700;letter-spacing:.04em;
  padding:2px 7px;border-radius:4px;color:#fff;margin-bottom:5px;
}
.t{font-weight:620;font-size:16px;margin:0 0 3px}
.x{color:#39434c;font-size:14.5px;margin:0}
.cod{
  display:inline-block;margin-top:8px;font-variant-numeric:tabular-nums;font-size:13px;
  background:var(--soft);border:1px solid var(--rule);border-radius:6px;padding:5px 9px;
}
.cod b{font-weight:600;color:var(--mut);margin-right:6px}
.av{
  margin-top:9px;font-size:13.5px;color:#5b4a20;background:#fdf6e3;
  border-left:3px solid #e0b53f;border-radius:0 5px 5px 0;padding:8px 11px;
}
.via{color:var(--mut);font-size:13.5px;display:flex;gap:13px;padding:9px 0;border-bottom:1px dashed var(--rule)}
.via .hora{color:var(--mut);font-weight:600}
.via b{font-weight:600;color:#4b5560}
.pend{margin:30px 0 10px}
.pend h2{font-size:15px;font-weight:650;margin:0 0 10px}
.p{border:1px solid var(--rule);border-left:3px solid var(--jantar);border-radius:0 8px 8px 0;padding:11px 13px;margin-bottom:8px}
.p.feito{border-left-color:var(--hotel);opacity:.62}
.p .q{font-size:11px;font-weight:700;letter-spacing:.04em;color:var(--mut);text-transform:uppercase}
.p .r{font-weight:620;font-size:15px;margin:2px 0 3px}
.p .s{font-size:14px;color:#39434c}
footer{color:var(--mut);font-size:12.5px;padding-top:22px}
@media print{
  nav.dias{display:none}
  .dia{display:block !important;page-break-after:always}
  body{font-size:11pt}
}
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <h1>Roteiro Brasil 2026</h1>
  <div class="sub">Rafael e mãe · 11 de novembro a 3 de dezembro · 23 dias</div>
</header>
<nav class="dias" id="nav" aria-label="Dias da viagem"></nav>
<main id="tela"></main>
<section class="pend" id="pend"></section>
<footer>Toda a informação fica neste arquivo. Funciona sem internet.</footer>
</div>
<script>
const DADOS = __PAYLOAD__;
const D = DADOS.D, PEND = DADOS.PEND;
const ROT = {voo:'Voo',onibus:'Ônibus',hotel:'Hospedagem',passeio:'Passeio',jantar:'Refeição',livre:'Tempo livre',via:'Trajeto',festa:'Família'};
const esc = s => String(s??'').replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

function item(it){
  if(it.mv){
    const p = it.mv.split('|');
    return `<div class="via"><div class="hora">${esc(p[3]||'')}</div>
      <div class="corpo"><b>${esc(p[1])} · ${esc(p[0])}</b> · ${esc(p[2])}</div></div>`;
  }
  const k = it.k || 'livre';
  return `<div class="item">
    <div class="hora">${esc(it.h||'')}</div>
    <div class="corpo">
      <span class="tag" style="background:var(--${k})">${esc(it.g || ROT[k] || '')}</span>
      <p class="t">${esc(it.t)}</p>
      ${it.x ? `<p class="x">${esc(it.x)}</p>` : ''}
      ${it.cod ? `<span class="cod"><b>${esc(it.cl||'Código')}</b>${esc(it.cod)}</span>` : ''}
      ${it.av ? `<div class="av">${esc(it.av)}</div>` : ''}
    </div></div>`;
}

function dia(d, n){
  return `<section class="dia" data-n="${n}">
    <div class="cabdia">
      <div class="num">${esc(d.d)}<i>${esc(d.m)}</i></div>
      <div class="cabtxt">
        <span class="cidade">${esc(d.c)}</span>
        <span class="resumo">${esc(d.sem)} · ${esc(d.r)}</span>
      </div>
    </div>
    ${d.i.map(item).join('')}
  </section>`;
}

let atual = 0;
function abrir(n){
  atual = n;
  document.getElementById('tela').innerHTML = dia(D[n], n);
  [...document.querySelectorAll('#nav button')].forEach((b,i) =>
    b.setAttribute('aria-current', i === n ? 'true' : 'false'));
  const b = document.querySelectorAll('#nav button')[n];
  if (b) b.scrollIntoView({inline:'center', block:'nearest'});
  window.scrollTo({top:0});
}

document.getElementById('nav').innerHTML =
  D.map((d,i) => `<button type="button" data-i="${i}">${esc(d.d)}/${d.m==='dez'?'12':'11'}</button>`).join('');
document.getElementById('nav').addEventListener('click', e => {
  const b = e.target.closest('button');
  if (b) abrir(+b.dataset.i);
});

document.getElementById('pend').innerHTML =
  '<h2>Pendências</h2>' + PEND.map(p => `
    <div class="p${p.n.toLowerCase()==='feito'?' feito':''}">
      <div class="q">${esc(p.n)}</div>
      <div class="r">${esc(p.t)}</div>
      <div class="s">${esc(p.p)}</div>
    </div>`).join('');

// abre no dia de hoje, se a viagem estiver acontecendo
const hoje = new Date();
const iHoje = D.findIndex(d => +d.d === hoje.getDate() && (d.m === 'nov' ? 10 : 11) === hoje.getMonth());
abrir(iHoje >= 0 ? iHoje : 0);

window.addEventListener('beforeprint', () => {
  document.getElementById('tela').innerHTML = D.map(dia).join('');
});
window.addEventListener('afterprint', () => abrir(atual));
</script>
</body>
</html>
"""

open("roteiro-brasil-2026.html", "w").write(HTML.replace("__PAYLOAD__", PAYLOAD))
print("dias:", len(D), "| itens:", sum(len(x["i"]) for x in D), "| pendências:", len(dados["PEND"]))
