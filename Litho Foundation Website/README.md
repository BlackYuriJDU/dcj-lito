# Lithos Foundation — Website

Site institucional (placeholder v1) do laboratório aberto de doenças priônicas.
Estático puro: `index.html` + `styles.css` + `app.js`. Zero dependências, zero build.

## Idiomas

PT-BR e EN via dicionário em `app.js` (`I18N`). O idioma padrão é detectado do
navegador (`pt*` → PT, senão EN) e a escolha fica salva no `localStorage`
(chave `lithos-lang`). Fase 2 (multi-página): migrar para rotas `/en/` com hreflang.

## Rodar local

```bash
cd "Litho Foundation Website"
npx serve .          # ou python3 -m http.server
```

## Deploy (Vercel)

O projeto já está Vercel-ready (estático + `vercel.json` com `cleanUrls`).

**Rota A — CLI (mais rápido):**
```bash
npm i -g vercel
vercel login
cd "Litho Foundation Website"
vercel --prod        # primeiro deploy pede link: criar projeto novo, sem framework
```

**Rota B — Git (contínua):** conectar o repositório GitHub em vercel.com/new e
definir **Root Directory = `Litho Foundation Website`** (o repo raiz contém dados
de pesquisa que NÃO devem ser servidos — o root directory isola o site).

## Estrutura

| Arquivo | Papel |
|---|---|
| `index.html` | página única; conteúdo default em PT-BR; chaves `data-i18n*` |
| `styles.css` | tokens (knobs `--dsd-*`), layout responsivo, motion |
| `app.js` | dicionário PT/EN, seletor de idioma, menu, reveal |
| `vercel.json` | cleanUrls + cache de assets |

## Identidade

- Azul-petróleo `#17657F` (institucional) + laranja-crail `#D97757` (faceta de
  destaque; variante profunda `#A85B3F` para fundos com texto branco).
- Marca provisória: gema lapidada (o registro que fica), faceta laranja.
- Tipografia: Oswald (display) + IBM Plex Sans (corpo) + IBM Plex Mono (dados).

## Ética

Nenhum dado de paciente individual. Conteúdo informativo — decisão clínica é dos
médicos assistentes. Todas as afirmações apontam para fonte primária.
