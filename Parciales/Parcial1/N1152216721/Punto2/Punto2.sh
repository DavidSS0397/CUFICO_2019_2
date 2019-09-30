#!/bin/bash
echo Compilación y ejecución del Punto 2 del Parcial.
echo El siguiente código soluciona dos ecuaciones diferenciales acopladas por los métodos de RK4 y Euler.
echo El Usuario visualizará las gráficas de las soluciones numéricas para diferentes números de puntos en el dominio de integración.
echo Finalmente se presenta el comportamiento del error relativo maximo para cada uno de los métodos vs. el número de puntos en el dominio.
echo "Recomendación: visualizar las gráficas en modo pantala completa."

python EcuDifAco.py


echo "********************************************************************************"
echo CONCLUSIÓN DE LAS PRUEBAS HECHAS PRE-ENTREGA:
echo los dos métodos se comportan de manera similar respecto al error relativo máximo.
echo El comportamiento de error relativo nos muestra que la soluciones convergen.
echo "********************************************************************************"
