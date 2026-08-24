#!/usr/bin/env bash
# tavily_search.sh — busca padrão do projeto DCJ - Lito via API Tavily.
# Uso: ./tavily_search.sh "consulta" [max_resultados] [profundidade: basic|advanced]
# Saída: JSON bruto da Tavily em stdout; erros em stderr.
set -euo pipefail

QUERY="${1:?Uso: tavily_search.sh \"consulta\" [max_results] [depth]}"
MAX="${2:-5}"
DEPTH="${3:-basic}"

# Chave lida de ~/.config/dcj-lito/ (FORA da árvore do projeto — auditoria de
# utilidade 2026-08-24: chave dentro da árvore = risco de vazamento em git/zip).
KEY_FILE="${TAVILY_KEY_FILE:-$HOME/.config/dcj-lito/tavily_key}"
if [[ -f "$KEY_FILE" ]]; then
  KEY="$(cat "$KEY_FILE")"
else
  echo "ERRO: $KEY_FILE não encontrado." >&2
  exit 1
fi

curl -s -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d "$(jq -n --arg q "$QUERY" --arg d "$DEPTH" --argjson m "$MAX" \
        '{query:$q, max_results:$m, search_depth:$d}')"