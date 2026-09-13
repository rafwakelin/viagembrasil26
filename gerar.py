# -*- coding: utf-8 -*-
"""Gera dados.json, o HTML público e o arquivo privado de códigos.

Uso:
  python3 gerar.py                       -> HTML sem nenhum código de reserva
  python3 gerar.py --senha "sua frase"   -> HTML com os códigos cifrados (AES-GCM)
"""
import base64, hashlib, json, os, sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from dados_a import DIAS_A
from dados_b import DIAS_B, PEND
from template import HTML

ITER = 250000
senha = None
if "--senha" in sys.argv:
    senha = sys.argv[sys.argv.index("--senha") + 1]
elif os.environ.get("SENHA"):
    senha = os.environ["SENHA"]

D = DIAS_A + DIAS_B
dados = {"PEND": PEND, "D": D}
json.dump(dados, open("dados.json", "w"), ensure_ascii=False, indent=1)   # privado, não commitar

# --- arquivo privado com todos os códigos, para o bolso e para impressão ---
linhas = ["# Códigos de reserva — Roteiro Brasil 2026", "",
          "Arquivo privado. Não subir para o GitHub.", ""]
for d in D:
    cods = [i for i in d["i"] if i.get("cod")]
    if not cods:
        continue
    linhas.append(f"## {d['d']}/{'12' if d['m']=='dez' else '11'} — {d['c']}")
    for i in cods:
        linhas.append(f"- **{i['t']}** · {i.get('cl','Código')}: `{i['cod']}`")
    linhas.append("")
open("codigos-privado.md", "w").write("\n".join(linhas))

# --- público: remove ou cifra cada código ---
pub = json.loads(json.dumps(dados, ensure_ascii=False))
n = 0
if senha:
    salt = os.urandom(16)
    chave = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt, ITER, 32)
    aes = AESGCM(chave)
    for dia in pub["D"]:
        for it in dia["i"]:
            if it.get("cod"):
                iv = os.urandom(12)
                ct = aes.encrypt(iv, it["cod"].encode(), None)
                it["cod"] = base64.b64encode(iv + ct).decode()
                it["cf"] = 1
                n += 1
    pub["CRIPTO"] = {"salt": base64.b64encode(salt).decode(), "iter": ITER}
else:
    for dia in pub["D"]:
        for it in dia["i"]:
            it.pop("cod", None)
            it.pop("cl", None)
            n += 0

open("roteiro-brasil-2026.html", "w").write(HTML.replace("__PAYLOAD__", json.dumps(pub, ensure_ascii=False)))
open(".gitignore", "w").write("codigos-privado.md\ndados.json\n")
print(f"dias: {len(D)} | itens: {sum(len(x['i']) for x in D)} | códigos cifrados: {n}"
      f" | modo: {'senha' if senha else 'sem códigos'}")
