# Rota Zenodo — como mintir o DOI (5 minutos, quando o senhor decidir)

1. Acesse https://zenodo.org e faça login com a conta GitHub (mesma: BlackYuriJDU).
2. Em account → GitHub, ative o repositório `dcj-lito` (toggle ON).
3. No GitHub: Releases → "Draft a new release" → tag `v1.0.0-preprint` → Publish.
4. O Zenodo cria automaticamente um DOI para o release (e um conceitual p/ todas versões).
5. Copie o badge DOI gerado no README.en.md e atualize o CITATION.cff (`doi:` + `date-released`).

**Quando fazer**: junto do envio ao bioRxiv (o preprint pede "code availability";
DOI de repositório é padrão esperado). Tornar o repo PÚBLICO no mesmo dia.
