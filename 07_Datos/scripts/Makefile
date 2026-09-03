.PHONY: all clean install figuras

all:
	python3 run_all.py

figuras:
	python3 05_generar_figuras.py
	python3 06_analisis_potencia.py

install:
	pip install -r requirements.txt

clean:
	rm -f clasificaciones_detector.csv
	rm -f ../resultados/dataset_consolidado.csv
	rm -f ../resultados/kappa_resultados.json
	rm -f ../resultados/matriz_confusion_prf1.json
	rm -f ../resultados/tabla_confusion.csv
	rm -f ../resultados/bootstrap_ic95.json
	rm -f ../resultados/analisis_potencia.json
	rm -f ../../07_Publicacion/figuras/figura_0*.png
	rm -f ../../07_Publicacion/figuras/figura_0*.pdf
	rm -f ../../07_Publicacion/tablas/tabla_01_resultados_detector.tex
	rm -f ../../07_Publicacion/tablas/tabla_03_confusion_prf1.tex
	rm -f ../../07_Publicacion/tablas/tabla_04_acuerdo_interevaluador.tex
	rm -f ../../07_Publicacion/tablas/tabla_05_potencia.tex
	@echo "Artefactos generados eliminados."
	@echo "etiquetas_expertos.csv (dato crudo real) NO se toca."
