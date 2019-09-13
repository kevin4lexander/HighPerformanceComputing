# Multiplicación de Matrices (Procesos VS Hilos)

_Comparar los tiempos de ejecución de la multiplicación de matrices mediante el algoritmo tradicional utilizando procesos vs utilizando hilos._


### Pre-requisitos 📋

_Es necesario instalar previamente la libreria matplotlib de python para graficar los tiempos de ejecución obtenidos_

```
pip install matplotlib
```

### Uso 🔧

_Puedes modificar los valores del array 'val_N' en el archivo scriptProcess.sh para definir los valores de N de las matrices NxN_

```
val_N=(100 250 500 1000 1500 2000)
```

_Para ejecutar el programa, el script recibe por parámetro el nombre del archivo "matrizProcess" (sin .cpp)_

```
./scriptProcess.sh matrizProcess
```

_El archivo graficar2.py lee los tiempos de ejecución del archivo timesProcess.txt para graficar los promedios de los tiempos. Para ver de nuevo las gráficas después de obtener los tiempos, se pasan los valores del array 'val_N' al archivo graficar2.py_

```
python2 graficar.py 100 250 500 1000 1500 2000
```

_Sin usar el script, para compilar los archivo matrizProcess.cpp ejecute_

```
g++ -g -o matrizProcess.out matrizProcess.cpp -lm
```

_Para ejecutar el archivo matrizProcess.out es necesario pasar por parámetro los tamaños N de las matrices NxN a multiplicar, por ejemplo_

```
./matrizProcess.out 100 250 500 1000 1500 2000
```

## Autores ✒️

* **Kevin Alexander Moreno** - [kevin4lexander](https://github.com/kevin4lexander)
* **Cristian Camilo Holguin** - [cristianHolguin](#fulanito-de-tal)
* **Edward Narvaez** - [edwardNarvaez](#fulanito-de-tal)

  _High Performance Computing (HPC)_</br>
  _Ingeniería de Sistemas y Computación_</br>
  _Universidad Tecnológica de Pereira_
