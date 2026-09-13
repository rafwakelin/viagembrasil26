# -*- coding: utf-8 -*-
HTML = r"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#101419">
<title>Roteiro Brasil 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#eef1f4;            --bg:oklch(95.5% .006 250);
  --surf:#ffffff;          --surf:oklch(100% 0 0);
  --surf2:#f5f7f9;         --surf2:oklch(97.6% .004 250);
  --ink:#101419;           --ink:oklch(21% .015 255);
  --ink2:#3b4552;          --ink2:oklch(41% .018 255);
  --mut:#6d7885;           --mut:oklch(58% .016 255);
  --line:#e0e5ea;          --line:oklch(91% .007 255);
  --line2:#cdd5dc;         --line2:oklch(85% .011 255);
  --h-voo:255; --h-onibus:300; --h-hotel:165; --h-passeio:70;
  --h-jantar:20; --h-livre:250; --h-via:250; --h-festa:330;
  --ft:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;
  --fm:'Roboto Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  --col:64px; --mk:34px; --gap:16px; --esc:1;
  --r:14px;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#0d1116;   --bg:oklch(17% .012 255);
    --surf:#141a21; --surf:oklch(21.5% .014 255);
    --surf2:#1a212a;--surf2:oklch(25% .015 255);
    --ink:#e9eef3;  --ink:oklch(94% .008 255);
    --ink2:#b7c2ce; --ink2:oklch(81% .014 255);
    --mut:#8593a1;  --mut:oklch(65% .018 255);
    --line:#232c36; --line:oklch(29% .016 255);
    --line2:#313d49;--line2:oklch(36% .018 255);
  }
}
*{box-sizing:border-box}
.grao{position:fixed;inset:0;z-index:1;pointer-events:none;opacity:.5;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='.22'/%3E%3C/svg%3E")}
@media (prefers-color-scheme:dark){.grao{mix-blend-mode:screen;opacity:.22}}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font:400 16px/1.55 var(--ft);-webkit-font-smoothing:antialiased;text-wrap:pretty}
svg{display:block}
h1,h2,h3{text-wrap:balance}

/* cabeçalho */
.topo{position:sticky;top:0;z-index:50;background:color-mix(in oklab,var(--bg) 88%,transparent);
  backdrop-filter:saturate(180%) blur(14px);border-bottom:1px solid var(--line)}
.topo .in{max-width:1180px;margin:0 auto;padding:13px 22px;display:flex;gap:18px;align-items:center}
.marca{display:flex;align-items:center;gap:12px;min-width:0}
.marca .anel{flex:0 0 auto}
.marca h1{margin:0;font-size:16.5px;font-weight:600;letter-spacing:-.02em;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
.marca p{margin:1px 0 0;font-size:12.5px;color:var(--mut);white-space:nowrap}
.cmd{margin-left:auto;display:flex;align-items:center;gap:9px;cursor:pointer;background:var(--surf);
  border:1px solid var(--line);border-radius:10px;padding:8px 11px;color:var(--mut);font:400 13.5px var(--ft)}
.cmd:hover{border-color:var(--line2);color:var(--ink2)}
.cmd kbd{font:500 11px var(--fm);border:1px solid var(--line);border-radius:5px;padding:2px 5px;color:var(--mut)}
@media(max-width:640px){.cmd span{display:none}.marca p{display:none}}

/* herói */
.heroi{position:relative;overflow:hidden;background:oklch(19% .03 255);color:#fff;isolation:isolate}
.heroi .malha{position:absolute;inset:-30%;z-index:-1;filter:blur(48px);opacity:.85;
  background:
   radial-gradient(38% 42% at 18% 32%,oklch(52% .17 255/.85),transparent 62%),
   radial-gradient(36% 40% at 76% 24%,oklch(50% .15 190/.75),transparent 64%),
   radial-gradient(44% 46% at 58% 82%,oklch(46% .16 300/.7),transparent 66%),
   radial-gradient(30% 34% at 92% 70%,oklch(58% .16 60/.55),transparent 62%);
  animation:deriva 34s ease-in-out infinite alternate}
@keyframes deriva{
  0%{transform:translate3d(0,0,0) scale(1)}
  50%{transform:translate3d(-3%,2%,0) scale(1.08)}
  100%{transform:translate3d(3%,-2%,0) scale(1.03)}}
.heroi .in{max-width:1180px;margin:0 auto;padding:52px 22px 26px;position:relative}
.heroi .et{display:inline-flex;align-items:center;gap:9px;font:500 11.5px var(--ft);letter-spacing:.09em;
  color:rgba(255,255,255,.72);border:1px solid rgba(255,255,255,.22);border-radius:20px;padding:6px 13px}
.heroi .et i{width:6px;height:6px;border-radius:50%;background:oklch(72% .17 150);
  box-shadow:0 0 0 0 oklch(72% .17 150/.7);animation:pulso 2.6s ease-out infinite}
@keyframes pulso{70%{box-shadow:0 0 0 9px oklch(72% .17 150/0)}100%{box-shadow:0 0 0 0 oklch(72% .17 150/0)}}
.heroi h1{margin:18px 0 0;font-size:clamp(38px,8.4vw,82px);font-weight:700;letter-spacing:-.05em;line-height:.94}
.heroi h1 span{display:block;color:transparent;background:linear-gradient(92deg,#fff 12%,oklch(83% .1 210) 58%,oklch(78% .12 60));
  -webkit-background-clip:text;background-clip:text}
.heroi .sob{margin:16px 0 0;max-width:44ch;font-size:15.5px;line-height:1.6;color:rgba(255,255,255,.74)}
.heroi .nums{display:flex;flex-wrap:wrap;gap:30px;margin:28px 0 6px}
.heroi .nums div b{display:block;font-size:27px;font-weight:600;letter-spacing:-.035em;font-variant-numeric:tabular-nums}
.heroi .nums div span{font-size:12px;color:rgba(255,255,255,.6);letter-spacing:.02em}

/* mapa da rota */
.mapa{position:relative;max-width:1180px;margin:0 auto;padding:6px 22px 20px;overflow-x:auto;scrollbar-width:none}
.mapa::-webkit-scrollbar{display:none}
.mapa svg{min-width:940px;width:100%;height:120px;overflow:visible}
.mapa .fio{fill:none;stroke:rgba(255,255,255,.26);stroke-width:1.5;stroke-linecap:round}
.mapa .fio.feito{stroke:#fff;stroke-width:2;stroke-dasharray:var(--L);stroke-dashoffset:var(--L);
  animation:tracar 1.5s cubic-bezier(.6,0,.2,1) .25s forwards}
@keyframes tracar{to{stroke-dashoffset:0}}
.mapa .no{cursor:pointer}
.mapa .no circle{fill:oklch(19% .03 255);stroke:rgba(255,255,255,.45);stroke-width:1.5;transition:r .18s,stroke .18s}
.mapa .no:hover circle{stroke:#fff;r:7}
.mapa .no.at circle{fill:#fff;stroke:#fff;r:7.5}
.mapa .no.hoje circle{stroke:oklch(72% .17 150);stroke-width:2.5}
.mapa .no text{font:500 10.5px var(--fm);fill:rgba(255,255,255,.62);text-anchor:middle}
.mapa .no.at text{fill:#fff;font-weight:600}
.mapa .cid{font:600 11px var(--ft);fill:rgba(255,255,255,.5);letter-spacing:.05em}
.mapa .cid.at{fill:#fff}

/* trilho de dias */
.trilho{max-width:1180px;margin:0 auto;padding:0 22px}
.rol{display:flex;gap:7px;overflow-x:auto;scroll-snap-type:x proximity;padding:14px 0 15px;scrollbar-width:none}
.rol::-webkit-scrollbar{display:none}
.chip{flex:0 0 auto;scroll-snap-align:center;cursor:pointer;background:var(--surf);border:1px solid var(--line);
  border-radius:11px;padding:8px 11px 9px;font:inherit;color:var(--ink);text-align:left;min-width:74px;
  transition:border-color .16s,transform .16s}
.chip:hover{border-color:var(--line2);transform:translateY(-1px)}
.chip b{display:block;font:600 14px/1.1 var(--ft);font-variant-numeric:tabular-nums}
.chip i{display:block;font-style:normal;font-size:11px;color:var(--mut);margin-top:3px}
.chip u{display:block;height:3px;border-radius:2px;margin-top:7px;background:var(--rc);opacity:.5;text-decoration:none}
.chip[aria-current="true"]{background:var(--ink);border-color:var(--ink);color:var(--surf)}
.chip[aria-current="true"] i{color:color-mix(in oklab,var(--surf) 62%,transparent)}
.chip[aria-current="true"] u{opacity:1}
.chip.hoje b:after{content:"hoje";font:500 9.5px var(--ft);letter-spacing:.04em;margin-left:6px;
  color:var(--rc);vertical-align:1px}

/* folha */
.palco{max-width:1180px;margin:0 auto;padding:4px 22px 40px}
.folha{container-type:inline-size;background:var(--surf);border:1px solid var(--line);border-radius:var(--r);
  overflow:hidden;view-transition-name:folha}
.capa{position:relative;overflow:hidden;padding:30px 26px 26px;color:#fff;isolation:isolate;
  background:linear-gradient(140deg,oklch(40% .1 var(--rh)),oklch(26% .07 calc(var(--rh) + 26)))}
.capa:before{content:"";position:absolute;inset:-40% -10%;z-index:-1;filter:blur(42px);opacity:.75;
  background:radial-gradient(42% 52% at 22% 26%,oklch(62% .17 var(--rh)/.75),transparent 64%),
             radial-gradient(38% 48% at 82% 74%,oklch(54% .16 calc(var(--rh) + 60)/.6),transparent 66%);
  transform:translateY(var(--par,0px))}
.capa:after{content:attr(data-n);position:absolute;right:-14px;bottom:-46px;z-index:-1;
  font:700 168px/.72 var(--ft);letter-spacing:-.06em;color:rgba(255,255,255,.085);font-variant-numeric:tabular-nums}
.capa .l1{display:flex;gap:18px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}
.capa .dt{display:flex;align-items:baseline;gap:12px}
.capa .dt b{font-size:clamp(38px,7vw,52px);font-weight:700;letter-spacing:-.05em;line-height:.82;
  font-variant-numeric:tabular-nums}
.capa .dt i{font-style:normal;font:500 13px var(--fm);color:rgba(255,255,255,.72);letter-spacing:.02em}
.capa .tag{font:500 11.5px var(--ft);letter-spacing:.03em;color:rgba(255,255,255,.86);
  border:1px solid rgba(255,255,255,.26);border-radius:20px;padding:5px 11px}
.capa h2{margin:16px 0 0;font-size:clamp(20px,3.4cqi + 14px,27px);font-weight:600;letter-spacing:-.028em;line-height:1.15}
.capa p{margin:6px 0 0;font-size:14.5px;color:rgba(255,255,255,.72)}
.medidas{display:flex;gap:0;border-top:1px solid var(--line);background:var(--surf2)}
.medidas div{flex:1;padding:11px 16px;border-right:1px solid var(--line)}
.medidas div:last-child{border-right:0}
.medidas b{display:block;font:600 17px/1.2 var(--ft);letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.medidas div{transition:background .2s}.medidas div:hover{background:var(--surf)}
.medidas span{font-size:11.5px;color:var(--mut)}

/* linha do tempo proporcional */
.tl{padding:10px 26px 26px;position:relative}
.tl:before{content:"";position:absolute;top:26px;bottom:30px;width:1px;background:var(--line2);
  left:calc(26px + var(--col) + var(--gap) + var(--mk)/2)}
.linha{display:grid;grid-template-columns:var(--col) var(--mk) minmax(0,1fr);gap:var(--gap);align-items:start}
.hh{text-align:right;font:500 13.5px/1 var(--fm);letter-spacing:-.02em;padding-top:9px;color:var(--ink2);
  font-variant-numeric:tabular-nums}
.mk{width:var(--mk);height:var(--mk);border-radius:50%;display:flex;align-items:center;justify-content:center;
  background:oklch(95% .04 var(--h));border:1px solid oklch(88% .06 var(--h))}
.mk svg{width:16px;height:16px;stroke:oklch(48% .12 var(--h));fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
@media (prefers-color-scheme:dark){
  .mk{background:oklch(30% .05 var(--h));border-color:oklch(38% .06 var(--h))}
  .mk svg{stroke:oklch(78% .11 var(--h))}
}
.par{padding:6px 0 8px}
.par .cx{position:relative;background:var(--surf);border:1px solid var(--line);
  border-left:3px solid oklch(55% .13 var(--h));border-radius:0 12px 12px 0;padding:14px 17px;min-height:var(--alt);
  transition:border-color .2s,box-shadow .2s,transform .2s}
.par .cx:hover{border-color:oklch(72% .08 var(--h));box-shadow:0 6px 22px oklch(55% .13 var(--h)/.12);transform:translateX(2px)}
.linha{opacity:0;transform:translateY(10px)}
.linha.vis{opacity:1;transform:none;transition:opacity .5s cubic-bezier(.2,.7,.3,1),transform .5s cubic-bezier(.2,.7,.3,1)}
@media (prefers-reduced-motion:reduce){.linha{opacity:1;transform:none}}
.par .rot{font:600 11.5px var(--ft);letter-spacing:.04em;color:oklch(45% .12 var(--h))}
@media (prefers-color-scheme:dark){.par .rot{color:oklch(76% .1 var(--h))}}
.par h3{margin:6px 0 5px;font-size:18px;font-weight:600;letter-spacing:-.018em;line-height:1.25}
.par p{margin:0;font-size:14.8px;line-height:1.55;color:var(--ink2)}
.cod{display:inline-flex;align-items:center;gap:10px;margin-top:12px;border:1px solid var(--line);
  background:var(--surf2);border-radius:9px;padding:7px 11px;font:500 13px var(--fm);letter-spacing:-.02em}
.cod b{font:600 10.5px var(--ft);letter-spacing:.06em;color:var(--mut)}
.av{display:flex;gap:10px;margin-top:12px;font-size:14px;line-height:1.5;
  color:oklch(38% .07 75);background:oklch(96% .04 85);border-left:3px solid oklch(72% .12 80);padding:10px 13px}
@media (prefers-color-scheme:dark){.av{color:oklch(88% .05 85);background:oklch(28% .04 80)}}
.av svg{flex:0 0 auto;width:16px;height:16px;stroke:oklch(60% .11 70);fill:none;stroke-width:1.8;stroke-linecap:round;margin-top:1px}
.via{color:var(--mut);font-size:13.4px;padding:5px 0 6px;min-height:var(--alt);display:flex;align-items:center}
.via .mk{background:none;border:0}
.via .mk svg{stroke:var(--mut);width:15px;height:15px}
.via b{font-weight:600;color:var(--ink2)}
.vao{grid-column:1/-1;display:flex;align-items:center;gap:12px;height:var(--alt);
  padding-left:calc(var(--col) + var(--gap) + var(--mk) + 4px);color:var(--mut);font-size:12px}
.vao:before{content:"";flex:0 0 18px;height:1px;background:var(--line2)}
.vao.corte:before{background:repeating-linear-gradient(90deg,var(--line2) 0 3px,transparent 3px 6px)}

/* passos */
.passos{display:flex;gap:11px;margin-top:16px}
.passos button{flex:1;display:flex;align-items:center;gap:13px;cursor:pointer;background:var(--surf);
  border:1px solid var(--line);border-radius:13px;padding:13px 16px;font:inherit;color:var(--ink);text-align:left;
  transition:border-color .16s,transform .16s}
.passos button:hover:not(:disabled){border-color:var(--line2);transform:translateY(-1px)}
.passos button:disabled{opacity:.28;cursor:default}
.passos .fim{justify-content:flex-end;text-align:right}
.passos svg{flex:0 0 auto;width:17px;height:17px;stroke:var(--mut);fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.passos b{display:block;font:600 11px var(--ft);letter-spacing:.05em;color:var(--mut);margin-bottom:4px}
.passos em{font-style:normal;font-size:14.5px;font-weight:600;letter-spacing:-.015em}

/* paleta de comandos */
.overlay{position:fixed;inset:0;z-index:100;background:color-mix(in oklab,var(--ink) 42%,transparent);
  display:none;align-items:flex-start;justify-content:center;padding:14vh 18px 18px;backdrop-filter:blur(3px)}
.overlay.on{display:flex}
.pal{width:min(640px,100%);background:var(--surf);border:1px solid var(--line2);border-radius:15px;overflow:hidden;
  box-shadow:0 24px 60px rgba(0,0,0,.28)}
.pal input{width:100%;border:0;border-bottom:1px solid var(--line);background:none;color:var(--ink);
  padding:16px 18px;font:400 16px var(--ft)}
.pal input:focus{outline:none}
.pal .saida{max-height:52vh;overflow:auto;padding:6px}
.pal .it{display:flex;gap:13px;align-items:center;width:100%;text-align:left;background:none;border:0;cursor:pointer;
  border-radius:9px;padding:10px 12px;font:inherit;color:var(--ink)}
.pal .it[data-sel="1"]{background:var(--surf2)}
.pal .it .d{font:500 12px var(--fm);color:var(--mut);flex:0 0 46px}
.pal .it b{font-size:14.5px;font-weight:500}
.pal .it small{display:block;color:var(--mut);font-size:12.5px}
.pal .rod{border-top:1px solid var(--line);padding:9px 14px;color:var(--mut);font-size:11.5px;display:flex;gap:14px}
.pal .vazio{padding:20px;color:var(--mut);font-size:14px;text-align:center}

.rodape{max-width:1180px;margin:0 auto;padding:0 22px 44px;color:var(--mut);font-size:12.5px;
  display:flex;gap:13px;flex-wrap:wrap;align-items:center}
.rodape button{cursor:pointer;background:var(--surf);border:1px solid var(--line);border-radius:9px;
  padding:7px 12px;font:500 12.5px var(--ft);color:var(--ink2)}
:focus-visible{outline:2px solid oklch(60% .14 255);outline-offset:2px}

@container (max-width:560px){
  :root{--col:52px;--mk:30px;--gap:11px}
  .tl{padding:8px 16px 20px}
  .tl:before{left:calc(16px + var(--col) + var(--gap) + var(--mk)/2)}
  .capa{padding:18px}
  .medidas{flex-wrap:wrap}
}
@media(max-width:560px){.palco{padding:2px 14px 34px}.trilho{padding:0 14px}.topo .in{padding:11px 14px}}

@media print{
  .topo,.trilho,.passos,.rodape,.overlay{display:none}
  body{background:#fff}
  .palco{padding:0;max-width:none}
  .folha{page-break-after:always;border:0;border-radius:0;margin-bottom:0}
  .capa{color:#000;background:none;border-bottom:2px solid #000}
  .capa .dt i,.capa p{color:#444}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto}}
::view-transition-old(folha),::view-transition-new(folha){animation-duration:.22s}
</style>
</head>
<body>
<div class="grao" aria-hidden="true"></div>

<section class="heroi">
  <div class="malha" aria-hidden="true"></div>
  <div class="in">
    <span class="et"><i></i>partida em <b id="faltam" style="font-weight:600;margin-left:4px"></b></span>
    <h1>Roteiro<span>Brasil 2026</span></h1>
    <p class="sob">Vinte e três dias entre Dubai e o Brasil, com a sua mãe do dia 13 ao 29. Cada dia é uma linha do tempo em escala real: a altura de cada parada é o tempo que ela leva.</p>
    <div class="nums" id="nums"></div>
  </div>
  <div class="mapa"><div id="rota"></div></div>
</section>

<header class="topo"><div class="in">
  <div class="marca">
    <span class="anel" id="anel"></span>
    <span><h1>Roteiro Brasil 2026</h1><p id="sub">Rafael e mãe · 23 dias</p></span>
  </div>
  <button class="cmd" id="abrirPal" type="button">Buscar <span>hotel, passeio, código</span> <kbd>Ctrl K</kbd></button>
</div></header>

<nav class="trilho"><div class="rol" id="rol"></div></nav>
<div class="palco">
  <main id="tela"></main>
  <nav class="passos" id="passos"></nav>
</div>
<p class="rodape"><span>Arquivo único, funciona sem internet.</span>
  <button type="button" id="imp">Imprimir os 23 dias</button></p>

<div class="overlay" id="ov"><div class="pal">
  <input id="q" type="text" placeholder="Ir para um dia, hotel, passeio ou código" autocomplete="off">
  <div class="saida" id="saida"></div>
  <div class="rod"><span>↑↓ navegar</span><span>Enter abrir</span><span>Esc fechar</span></div>
</div></div>

<script>
const DADOS=__PAYLOAD__, D=DADOS.D, PEND=DADOS.PEND;
const ROT={voo:'Voo',onibus:'Ônibus',hotel:'Hospedagem',passeio:'Passeio',jantar:'Refeição',livre:'Tempo livre',via:'Trajeto',festa:'Família'};
const HUE={voo:255,onibus:300,hotel:165,passeio:70,jantar:20,livre:250,via:250,festa:330};
const RH={golfo:60,metropole:255,interior:140,cataratas:190,ilha:225,serra:290};
const CENA={'11':'golfo','12':'metropole','13':'interior','14':'interior','15':'interior','16':'cataratas','17':'cataratas','18':'cataratas','19':'cataratas','20':'ilha','21':'ilha','22':'ilha','23':'ilha','24':'serra','25':'serra','26':'serra','27':'serra','28':'serra','29':'serra','30':'metropole','01':'metropole','02':'golfo','03':'golfo'};
const calmo=()=>typeof matchMedia==='function'&&matchMedia('(prefers-reduced-motion:reduce)').matches;
const esc=s=>String(s??'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const mm=d=>d.m==='dez'?'12':'11';
const rh=d=>RH[CENA[d.d]]??255;

const SV='<svg viewBox="0 0 24 24">%</svg>';
const IC={
 voo:'<path d="M12 2.6c1 0 1.8 1.4 1.8 3.1v2.9l7 4v2l-7-2v4.2l2.3 1.7v1.6L12 19l-4.1 1.1v-1.6l2.3-1.7v-4.2l-7 2v-2l7-4V5.7c0-1.7.8-3.1 1.8-3.1Z"/>',
 onibus:'<rect x="4.5" y="4" width="15" height="12" rx="2.2"/><path d="M4.5 10.5h15M8.5 16v2.6M15.5 16v2.6"/>',
 hotel:'<path d="M3 18.5v-7a1.8 1.8 0 0 1 1.8-1.8h9.4A4.8 4.8 0 0 1 19 14.5v4M3 14.6h16M6.4 9.7V6.6h6.8"/>',
 passeio:'<path d="M12 20.8s6.6-5.5 6.6-10.3A6.6 6.6 0 0 0 5.4 10.5C5.4 15.3 12 20.8 12 20.8Z"/><circle cx="12" cy="10.2" r="2.3"/>',
 jantar:'<path d="M6.4 3.2v7.4a1.9 1.9 0 0 0 3.8 0V3.2M8.3 10.6v10.2M17.8 3.2c-1.7 1.3-2.5 3.3-2.5 5.5s1 3.4 2.5 3.4v8.7"/>',
 livre:'<circle cx="12" cy="12" r="3.9"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/>',
 via:'<path d="M4.5 12h14M13.2 6.2 19.5 12l-6.3 5.8"/>',
 festa:'<path d="M4.5 20.8V12h15v8.8zM4.5 12a1.9 1.9 0 0 1 1.9-1.9h11.2A1.9 1.9 0 0 1 19.5 12M12 10V6.4M12 6.4a1.9 1.9 0 1 0-1.9-1.9A1.9 1.9 0 0 0 12 6.4Z"/>',
 pe:'<path d="M13.4 4.6a1.4 1.4 0 1 0 0-.1M10.6 20.8 12 16l3 2.4.5 2.4M6 13.8l3.4-2 1-4.4 2.9 2 2.9.5"/>',
 carro:'<path d="M5 16.4v2.2M19 16.4v2.2M3.2 16.4v-3.2l2-4.1h13.6l2 4.1v3.2z"/><circle cx="7.4" cy="16.4" r="1.1"/><circle cx="16.6" cy="16.4" r="1.1"/>',
 barco:'<path d="M3 18.2c1.5 1.3 3 1.3 4.5 0s3-1.3 4.5 0 3 1.3 4.5 0 3-1.3 4.5 0M5.2 14.2 6.2 9h11.6l1 5.2M12 9V3.8"/>',
 alerta:'<path d="M12 4.4 2.9 19.8h18.2zM12 10.2v4.1M12 17.1v.1"/>',
 seta:'<path d="M9.2 5.6 15.6 12l-6.4 6.4"/>'
};
const ico=n=>SV.replace('%',IC[n]||IC.livre);
const icoVia=m=>/pé/i.test(m)?'pe':/barco/i.test(m)?'barco':/avi|conex/i.test(m)?'voo':/uber|carro|van|transfer|táxi/i.test(m)?'carro':/ônibus|onibus/i.test(m)?'onibus':'via';

/* relógio */
const ehHora=h=>/^\d{1,2}:\d{2}$/.test(h||'');
const emMin=h=>ehHora(h)?(+h.split(':')[0])*60+(+h.split(':')[1]):null;
function durMin(t){
  if(!t) return null;
  const s=String(t).toLowerCase();
  let m=s.match(/(\d+)\s*h\s*(\d{1,2})?/);
  if(m) return +m[1]*60+(m[2]?+m[2]:0);
  m=s.match(/(\d+)\s*min/);
  if(m) return +m[1];
  return null;
}
const PAD={voo:90,onibus:120,hotel:35,passeio:75,jantar:75,livre:60,via:20,festa:150};
const ESC=.62, VAO_MAX=70, VAO_CORTE=46, ALT_MIN=74;

function planejar(d){
  const fila=[];
  d.i.forEach(it=>{
    if(it.mv){const p=it.mv.split('|');
      fila.push({tipo:'via',ini:emMin(p[3]),dur:durMin(p[0])||15,p,it});
    }else{
      fila.push({tipo:'par',ini:emMin(it.h),dur:durMin(it.g)||PAD[it.k||'livre']||60,it});
    }});
  let fim=null;
  return fila.map(n=>{
    let vao=null;
    if(n.ini!=null&&fim!=null){
      let g=n.ini-fim; if(g<0) g+=1440;
      if(g>4) vao=g;
    }
    if(n.ini!=null) fim=n.ini+n.dur;
    return {...n,vao};
  });
}
function alturaVao(g){
  if(g<=VAO_MAX) return Math.round(g*ESC);
  return VAO_CORTE;
}
function rotuloVao(g){
  const h=Math.floor(g/60), m=g%60;
  return (h?h+'h':'')+(m?(h?' ':'')+m+' min':'')+' sem compromisso';
}

function bloco(n){
  if(n.tipo==='via'){
    const p=n.p, alt=Math.max(Math.round(n.dur*ESC),34);
    return `<div class="linha via" style="--alt:${alt}px">
      <span class="hh">${esc(p[3]||'')}</span><span class="mk">${ico(icoVia(p[1]))}</span>
      <span><b>${esc(p[1])} · ${esc(p[0])}</b> · ${esc(p[2])}</span></div>`;
  }
  const it=n.it, k=it.k||'livre', alt=Math.max(Math.round(n.dur*ESC),ALT_MIN);
  return `<div class="linha par" style="--h:${HUE[k]??250};--alt:${alt}px">
    <span class="hh">${esc(it.h&&it.h!=='—'?it.h:'')}</span><span class="mk">${ico(k)}</span>
    <div class="cx"><div class="rot">${esc(it.g||ROT[k])}</div><h3>${esc(it.t)}</h3>
      ${it.x?`<p>${esc(it.x)}</p>`:''}
      ${it.cod?`<div class="cod"><b>${esc(it.cl||'Código')}</b>${esc(it.cod)}</div>`:''}
      ${it.av?`<div class="av">${ico('alerta')}<div>${esc(it.av)}</div></div>`:''}</div></div>`;
}
function anel(pc,tam,cor){
  const r=(tam-4)/2, c=2*Math.PI*r;
  return `<svg width="${tam}" height="${tam}" viewBox="0 0 ${tam} ${tam}" aria-hidden="true">
    <circle cx="${tam/2}" cy="${tam/2}" r="${r}" fill="none" stroke="var(--line2)" stroke-width="3"/>
    <circle cx="${tam/2}" cy="${tam/2}" r="${r}" fill="none" stroke="${cor}" stroke-width="3"
      stroke-linecap="round" stroke-dasharray="${c}" stroke-dashoffset="${c*(1-pc)}"
      transform="rotate(-90 ${tam/2} ${tam/2})"/></svg>`;
}

function folha(d,n){
  const plano=planejar(d);
  const paradas=plano.filter(x=>x.tipo==='par').length;
  const vias=plano.length-paradas;
  const minutos=plano.filter(x=>x.tipo==='via').reduce((a,b)=>a+b.dur,0);
  const inicio=plano.find(x=>x.ini!=null), ultimo=[...plano].reverse().find(x=>x.ini!=null);
  const janela=inicio?`${String(Math.floor(inicio.ini/60)).padStart(2,'0')}:${String(inicio.ini%60).padStart(2,'0')} → ${String(Math.floor((ultimo.ini+ultimo.dur)%1440/60)).padStart(2,'0')}:${String((ultimo.ini+ultimo.dur)%60).padStart(2,'0')}`:'dia aberto';
  const corpo=plano.map(x=>
    (x.vao?`<div class="linha"><span class="vao${x.vao>VAO_MAX?' corte':''}" style="--alt:${alturaVao(x.vao)}px">${esc(rotuloVao(x.vao))}</span></div>`:'')
    +bloco(x)).join('');
  return `<article class="folha" style="--rh:${rh(d)}">
    <div class="capa" data-n="${esc(d.d)}"><div class="l1">
      <div class="dt"><b>${esc(d.d)}</b><i>${esc(d.m)} · ${esc(d.sem)}</i></div>
      <span class="tag">Dia ${n+1} de ${D.length}</span></div>
      <h2>${esc(d.c)}</h2><p>${esc(d.r)}</p></div>
    <div class="medidas">
      <div><b>${paradas}</b><span>paradas</span></div>
      <div><b>${vias}</b><span>deslocamentos</span></div>
      <div><b>${Math.floor(minutos/60)}h${String(minutos%60).padStart(2,'0')}</b><span>em trânsito</span></div>
      <div><b>${janela}</b><span>janela do dia</span></div>
    </div>
    <div class="tl">${corpo}</div>
  </article>`;
}

let atual=0;
function pinta(n){
  atual=n;
  tela.innerHTML=folha(D[n],n);
  document.querySelectorAll('.chip').forEach((b,i)=>b.setAttribute('aria-current',i===n?'true':'false'));
  const c=rol.children[n]; if(c&&c.scrollIntoView) c.scrollIntoView({inline:'center',block:'nearest'});
  const a=D[n-1], z=D[n+1];
  passos.innerHTML=
   `<button type="button" data-ir="${n-1}" ${a?'':'disabled'}><span style="transform:rotate(180deg);display:flex">${ico('seta')}</span><span><b>Anterior</b><em>${a?esc(a.d)+'/'+mm(a)+' · '+esc(a.c):'—'}</em></span></button>`+
   `<button type="button" class="fim" data-ir="${n+1}" ${z?'':'disabled'}><span><b>Próximo</b><em>${z?esc(z.d)+'/'+mm(z)+' · '+esc(z.c):'—'}</em></span>${ico('seta')}</button>`;
  anel.innerHTML=anel_svg(n);
  sub.textContent=`${D[n].c} · dia ${n+1} de ${D.length}`;
  rota.innerHTML=desenhaRota(n);
  anima();
  try{history.replaceState(null,'','#dia-'+D[n].d+'-'+mm(D[n]))}catch(_){}
}
const anel_svg=n=>anel((n+1)/D.length,30,`oklch(55% .13 ${rh(D[n])})`);
function abrir(n,rolar){
  n=Math.max(0,Math.min(D.length-1,n));
  if(document.startViewTransition){document.startViewTransition(()=>pinta(n))}else{pinta(n)}
  if(rolar!==false) scrollTo({top:0,behavior:'instant'});
}

let grupos=[],ult=null;
D.forEach((d,i)=>{const c=d.c.split(' →')[0].split(' ·')[0];
  if(c!==ult){grupos.push({c,ds:[]});ult=c} grupos[grupos.length-1].ds.push(i)});
const hj=new Date(), ih=D.findIndex(d=>+d.d===hj.getDate()&&(d.m==='nov'?10:11)===hj.getMonth());
rol.innerHTML=D.map((d,i)=>`<button type="button" class="chip${i===ih?' hoje':''}" data-ir="${i}"
  style="--rc:oklch(60% .13 ${rh(d)})"><b>${esc(d.d)}/${mm(d)}</b><i>${esc(d.sem)}</i><u></u></button>`).join('');

/* índice e paleta */
const IX=[];
D.forEach((d,i)=>{
  IX.push({i,t:`${d.d}/${mm(d)} · ${d.c}`,s:d.r,d:`${d.d}/${mm(d)}`,b:`${d.d} ${d.c} ${d.r} ${d.sem}`.toLowerCase()});
  d.i.forEach(it=>{if(it.mv)return;
    IX.push({i,t:it.t,s:`${d.d}/${mm(d)} · ${d.c}${it.h&&it.h!=='—'?' · '+it.h:''}`,d:it.h&&it.h!=='—'?it.h:'',
      b:`${it.t} ${it.x||''} ${it.cod||''} ${d.c}`.toLowerCase()})})});
let sel=0, achados=[];
function buscar(v){
  v=(v||'').trim().toLowerCase();
  achados=v.length<2?IX.filter(x=>x.d.includes('/')).slice(0,23):IX.filter(x=>x.b.includes(v)).slice(0,12);
  sel=0; desenha();
}
function desenha(){
  saida.innerHTML=achados.length?achados.map((x,j)=>
    `<button type="button" class="it" data-ir="${x.i}" data-sel="${j===sel?1:0}">
      <span class="d">${esc(x.d)}</span><span><b>${esc(x.t)}</b><small>${esc(x.s)}</small></span></button>`).join('')
    :'<div class="vazio">Nada encontrado</div>';
}
function abrePal(){ov.classList.add('on');q.value='';buscar('');q.focus()}
function fechaPal(){ov.classList.remove('on')}
abrirPal.addEventListener('click',abrePal);
ov.addEventListener('click',e=>{if(e.target===ov)fechaPal()});
q.addEventListener('input',e=>buscar(e.target.value));
q.addEventListener('keydown',e=>{
  if(e.key==='ArrowDown'){e.preventDefault();sel=Math.min(sel+1,achados.length-1);desenha()}
  if(e.key==='ArrowUp'){e.preventDefault();sel=Math.max(sel-1,0);desenha()}
  if(e.key==='Enter'&&achados[sel]){abrir(achados[sel].i);fechaPal()}
  if(e.key==='Escape')fechaPal();
});
addEventListener('keydown',e=>{
  if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();abrePal();return}
  if(e.target===q) return;
  if(e.key==='Escape')fechaPal();
  if(e.key==='ArrowRight')abrir(atual+1);
  if(e.key==='ArrowLeft')abrir(atual-1);
});
addEventListener('click',e=>{const b=e.target.closest('[data-ir]');
  if(b&&!b.disabled){abrir(+b.dataset.ir);fechaPal()}});
let tx=0,ty=0;
addEventListener('touchstart',e=>{tx=e.changedTouches[0].clientX;ty=e.changedTouches[0].clientY},{passive:true});
addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx, dy=e.changedTouches[0].clientY-ty;
  if(Math.abs(dx)>80&&Math.abs(dy)<50) abrir(atual+(dx<0?1:-1),false)},{passive:true});
imp.addEventListener('click',()=>{tela.innerHTML=D.map(folha).join('');print()});
addEventListener('afterprint',()=>pinta(atual));

/* herói: números que sobem */
const totItens=D.reduce((a,d)=>a+d.i.filter(x=>!x.mv).length,0);
const totMin=D.reduce((a,d)=>a+planejar(d).filter(x=>x.tipo==='via').reduce((b,c)=>b+c.dur,0),0);
const cidades=new Set(D.map(d=>d.c.split(' →')[0].split(' ·')[0]));
nums.innerHTML=[[D.length,'dias'],[cidades.size,'cidades'],[totItens,'paradas'],
  [Math.round(totMin/60),'horas em trânsito']].map(([v,r])=>
  `<div><b data-ate="${v}">0</b><span>${r}</span></div>`).join('');
const partida=new Date(2026,10,11);
const dias=Math.ceil((partida-new Date())/864e5);
faltam.textContent=dias>0?dias+' dias':(dias===0?'hoje':'11 de novembro');
if(!calmo()){
  document.querySelectorAll('#nums b').forEach(el=>{
    const ate=+el.dataset.ate, t0=performance.now(), dur=900;
    const passo=t=>{const k=Math.min((t-t0)/dur,1), e=1-Math.pow(1-k,3);
      el.textContent=Math.round(ate*e); if(k<1) requestAnimationFrame(passo)};
    requestAnimationFrame(passo)});
}else{document.querySelectorAll('#nums b').forEach(el=>el.textContent=el.dataset.ate)}

/* mapa da rota */
function desenhaRota(n){
  const P=52, y0=44, L=D.length, larg=P*(L-1)+120;
  const pts=D.map((d,i)=>[60+i*P, y0+Math.sin(i*.78)*11]);
  const cam=pts.map((p,i)=>(i?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' ');
  const feito=pts.slice(0,n+1).map((p,i)=>(i?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' ');
  const nome=i=>D[i].c.split(' →')[0].split(' ·')[0];
  let cid='',ult=null;
  D.forEach((d,i)=>{const c=nome(i);
    if(c!==ult){cid+=`<text class="cid${c===nome(n)?' at':''}" x="${pts[i][0]-4}" y="100">${esc(c)}</text>`;ult=c}});
  return `<svg viewBox="0 0 ${larg} 120" preserveAspectRatio="xMinYMid meet" role="img" aria-label="Rota da viagem">
    <path class="fio" d="${cam}"/>
    <path class="fio feito" style="--L:${P*L*1.3}" d="${feito}"/>
    ${D.map((d,i)=>`<g class="no${i===n?' at':''}${i===ih?' hoje':''}" data-ir="${i}" tabindex="0" role="button"
        aria-label="Dia ${esc(d.d)} de ${mm(d)==='11'?'novembro':'dezembro'}">
        <circle cx="${pts[i][0]}" cy="${pts[i][1]}" r="5.5"/>
        <text x="${pts[i][0]}" y="${pts[i][1]-15}">${esc(d.d)}</text></g>`).join('')}
    ${cid}</svg>`;
}

/* revelação e paralaxe */
let io=null;
function anima(){
  const alvos=[...document.querySelectorAll('.tl .linha')];
  if(calmo()||!('IntersectionObserver' in window)){
    alvos.forEach(a=>a.classList.add('vis')); return;
  }
  if(io) io.disconnect();
  io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){
      const k=alvos.indexOf(e.target);
      e.target.style.transitionDelay=Math.min(k,6)*26+'ms';
      e.target.classList.add('vis'); io.unobserve(e.target);
    }}),{rootMargin:'0px 0px -8% 0px',threshold:.06});
  alvos.forEach(a=>io.observe(a));
}
let raf=0;
addEventListener('scroll',()=>{
  if(raf) return;
  raf=requestAnimationFrame(()=>{raf=0;
    const c=document.querySelector('.capa');
    if(c) c.style.setProperty('--par',Math.round(scrollY*.14)+'px');
  })},{passive:true});

const alvo=location.hash.match(/^#dia-(\d{2})-(\d{2})$/);
const iAlvo=alvo?D.findIndex(d=>d.d===alvo[1]&&mm(d)===alvo[2]):-1;
pinta(iAlvo>=0?iAlvo:(ih>=0?ih:0));
</script>
</body>
</html>
"""
