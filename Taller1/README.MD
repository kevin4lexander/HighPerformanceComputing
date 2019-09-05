# Multiplicación de Matrices (Secuencial VS Hilos)

_Comparar los tiempos de ejecución de la multiplicación de matrices mediante el algoritmo tradicional de forma secuencial vs utilizando hilos._


### Pre-requisitos 📋

_Es necesario instalar previamente la libreria matplotlib de python para graficar los tiempos de ejecución obtenidos_

```
pip install matplotlib
```

### Uso 🔧

_Puedes modificar los valores del array 'val_N' en el archivo script.sh para definir los valores de N de las matrices NxN_

```
val_N=(100 250 500 1000 1500 2000)
```

_Para ejecutar el programa, el script recibe por parámetro los nombres del archivo "matrizSeq" (sin .cpp) y el archivo "matrizThreads" (sin .cpp)_

```
./script.sh matrizThreads matrizSeq
```

_El archivo graficar.py lee los tiempos de ejecución del archivo times.txt para graficar los promedios de los tiempos. Para ver de nuevo las gráficas después de obtener los tiempos, se pasan los valores del array 'val_N' al archivo graficar.py_

```
python2 graficar.py 100 250 500 1000 1500 2000
```

_**Recuerde eliminar el archivo times.txt antes de ejecutar el script para obtener el gráfico únicamente con los datos de la última ejecución_

</br>

_Sin usar el script, para compilar los archivo matrizThreads.cpp y matrizSeq.cpp ejecute_

```
g++ -g -o matrizThreads.out matrizThreads.cpp -lpthread -lm
g++ -g -o matrizSeq.out matrizSeq.cpp
```

_Para ejecutar los archivo matrizThreads.out y matrizSeq.out es necesario pasar por parámetro los tamaños N de las matrices NxN a multiplicar, por ejemplo_

```
./matrizThreads.out 100
./matrizSeq.out 250
```

## Autores ✒️

* **Kevin Alexander Moreno** - [kevin4lexander](https://github.com/kevin4lexander)
* **Cristian Camilo Holguin** - [cristianHolguin](#fulanito-de-tal)
* **Edward Narvaez** - [edwardNarvaez](#fulanito-de-tal)

  _High Performance Computing (HPC)_</br>
  _Ingeniería de Sistemas y Computación_</br>
  _Universidad Tecnológica de Pereira_
