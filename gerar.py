# -*- coding: utf-8 -*-
"""Gera dados.json e roteiro-brasil-2026.html."""
import json
from dados_a import DIAS_A
from dados_b import DIAS_B

D = DIAS_A + DIAS_B
dados = {"PEND": __import__("dados_b").PEND, "D": D}

json.dump(dados, open("dados.json", "w"), ensure_ascii=False, indent=1)

PAYLOAD = json.dumps(dados, ensure_ascii=False)

from template import HTML

open("roteiro-brasil-2026.html", "w").write(HTML.replace("__PAYLOAD__", PAYLOAD))
print("dias:", len(D), "| itens:", sum(len(x["i"]) for x in D), "| pendências:", len(dados["PEND"]))
