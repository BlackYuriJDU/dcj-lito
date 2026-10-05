.PHONY: install test simulacoes gwas clean

install:
	pip install -r requirements.txt --break-system-packages

test:
	python3 -m pytest tests/ -v

simulacoes:
	python3 pipeline/scripts/simulacao_prion.py
	python3 pipeline/scripts/varredura_blindagem.py
	python3 pipeline/scripts/simulacao_calibrada.py

gwas:
	python3 pipeline/scripts/qc_gwas_gcst90001389.py
	python3 pipeline/scripts/clumping_descoberta.py
	python3 pipeline/scripts/coloc_stx6_eqtl.py
	python3 pipeline/scripts/coloc_meta_stx6.py

# O alvo `relatorios` foi removido em 2026-10-05: montava o dossie privado
# (MEMORIA.md, contexto do caso, cartas), que nao faz parte da face publica
# do projeto. O script continua no disco, apenas nao e versionado.

clean:
	rm -f pipeline/data/eqtl_*.tsv
