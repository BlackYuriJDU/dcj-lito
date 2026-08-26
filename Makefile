.PHONY: install test simulacoes gwas relatorios clean

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

relatorios:
	python3 pipeline/scripts/monta_arquivo_completo.py

clean:
	rm -f pipeline/data/eqtl_*.tsv
