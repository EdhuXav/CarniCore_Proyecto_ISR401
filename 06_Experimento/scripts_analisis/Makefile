.PHONY: all clean install

all:
	python3 run_all.py

install:
	pip install -r requirements.txt

clean:
	rm -f clasificaciones_detector.csv
	rm -f ../resultados/dataset_consolidado.csv
	rm -f ../resultados/kappa_resultados.json
	rm -f ../resultados/matriz_confusion_prf1.json
	rm -f ../resultados/tabla_confusion.csv
	rm -f ../resultados/bootstrap_ic95.json
	@echo "Archivos generados eliminados. etiquetas_expertos.csv (dato crudo real) NO se toca."
