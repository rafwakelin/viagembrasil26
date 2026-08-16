# Roteiro Brasil 2026

Pagina estatica com o roteiro dia a dia. Sem dependencias e sem build.

## Arquivos

- `index.html` - estrutura da pagina
- `style.css` - todo o estilo
- `app.js` - dados do roteiro e logica de navegacao

## Publicar no GitHub Pages

1. Crie um repositorio e envie os tres arquivos na raiz.
2. Abra **Settings** e depois **Pages**.
3. Em *Source*, escolha **Deploy from a branch**.
4. Selecione a branch `main` e a pasta `/ (root)`. Salve.
5. O endereco sai em poucos minutos, no formato
   `https://SEU-USUARIO.github.io/NOME-DO-REPO/`.

## Editar o roteiro

Os dados ficam na primeira linha do `app.js`, na constante `DADOS`.

- `D` e a lista de dias. Cada dia tem `d` (dia), `m` (mes), `s` (dia da
  semana), `c` (cidade), `r` (resumo) e `i` (lista de itens).
- Cada item tem `h` (hora), `k` (tipo: `voo`, `bus`, `hotel`, `passeio`,
  `jantar` ou `livre`), `g` (rotulo), `t` (titulo) e `x` (descricao).
  Opcionalmente tem `mv`, o deslocamento no formato `duracao|meio|rota`,
  e `av`, um aviso destacado.
- `PEND` e a lista de pendencias.
- `CIDADES` alimenta a pagina inicial com clima e descricao.

## Aviso

Esta e a versao publica. Numeros de reserva, PIN, localizadores de voo,
bilhetes e vouchers foram removidos de proposito. Nao adicione esses
dados a um repositorio publico.

## Fontes

Inter e IBM Plex Mono vem do Google Fonts. Sem internet a pagina continua
funcionando com as fontes do sistema.
