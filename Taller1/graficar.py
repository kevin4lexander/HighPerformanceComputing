from io import open
from pylab import *
import numpy as np
import re
import sys
import multiprocessing as mp


# obtener tiempos de ejecucion hilos del archivo times.txt
def tiempos_hilos(expresionHilos):
    for linea in texto:
        match = expresionHilos.search(linea)
        if match:
            algoritmo = str(match.groupdict()['algoritmo'])
            # verificar si el tiempo corresponde a datos de hilos (Threads)
            if algoritmo == 'T':
                tipoTime = str(match.groupdict()['tipoTime'])
                if tipoTime == 'W':  # obtener tiempos de reloj
                    tamano = int(match.groupdict()['tamano'])
                    for i in range(len(val_N)):
                        if tamano == val_N[i]:
                            valor = (float(match.groupdict()['valor']))
                            tiempos_reloj_Hilos[i].append(valor)
                if tipoTime == 'C':  # obtener tiempos de cpu
                    tamano = int(match.groupdict()['tamano'])
                    for i in range(len(val_N)):
                        if tamano == val_N[i]:
                            valor = (float(match.groupdict()['valor']))
                            tiempos_cpu_Hilos[i].append(valor)
            # verificar si el tiempo corresponde a datos secuenciales (Seq)
            if algoritmo == 'S':
                tipoTime = str(match.groupdict()['tipoTime'])
                if tipoTime == 'W':  # obtener tiempos de reloj
                    tamano = int(match.groupdict()['tamano'])
                    for i in range(len(val_N)):
                        if tamano == val_N[i]:
                            valor = (float(match.groupdict()['valor']))
                            tiempos_reloj_Seq[i].append(valor)
                if tipoTime == 'C':  # obtener tiempos de cpu
                    tamano = int(match.groupdict()['tamano'])
                    for i in range(len(val_N)):
                        if tamano == val_N[i]:
                            valor = (float(match.groupdict()['valor']))
                            tiempos_cpu_Seq[i].append(valor)


# calcular promedio para tiempos de reloj hilos
def promedio_tiempos(tiempos):
    tiempo_medio = []
    for i in range(len(tiempos)):
        suma = 0.0
        for valor in tiempos[i]:
            suma += valor
        if suma > 0:
            tiempo_medio.append(suma/len(tiempos[i]))
    return tiempo_medio


# mostrar los tiempos promedio
def imprimir_tiempo_medio(listaTiempos, val_N):
    for i in range(len(listaTiempos)):
        print('N:{} - Time: {}'.format(val_N[i], listaTiempos[i]))


# graficar con matplotlib los tiempos obtenidos
def graficar(tm_cpuHilos, tm_relojHilos, tm_cpuSeq, tm_relojSeq, val_N):
    figure(num=1, facecolor='w', edgecolor='w')
    xlabel('Valor N Matriz')
    ylabel('Tiempo (s)')
    title(r'Multiplicacion Matrices - Hilos vs Secuencial')

    plot(val_N, tm_relojHilos, label=r'Hilos - Reloj Time',
         color='Green')  # ver tiempo de rejos hilos
    plot(val_N, tm_relojSeq, label=r'Sec - Reloj Time',
         color='Red')  # ver tiempo de reloj secuencial
    # plot(val_N, tm_cpuHilos, linestyle='--', label=r'Hilos - CPU Time',
    #      color='Blue')  # ver tiempo de cpu hilos
    # plot(val_N, tm_cpuSeq, linestyle='--', label=r'Sec - CPU Time',
    #      color='Black')  # ver tiempo de reloj secuencial

    # for i, j in zip(tm_cpuHilos, val_N):
    #     value = round(i, 2)  # redondear valor
    #     annotate(str(value), xy=(i, j))  # mostrar valores en la grafica
    # for i, j in zip(tm_cpuSeq, val_N):
    #     value = round(i, 2)  # redondear valor
    #     annotate(str(value), xy=(i, j))  # mostrar valores en la grafica

    legend(loc='upper left')
    show()
    draw()


if __name__ == '__main__':
    # valores de N para las matrices - val_N = [100 250 500 1000 1500 2000 2500 3000 4000 5000 7000]
    val_N = []

    if(len(sys.argv) > 1):
        for p in range(1, len(sys.argv)):
            try:
                val_N.append(int(sys.argv[p]))
            except:
                print("Oops!", sys.exc_info()[0], "ocurred.")
                print("Parametro incorrecto")
    else:
        print("Faltan parametros")
        sys.exit()

    # array's para guardar los tiempos obtenidos del archivo times.txt
    tiempos_reloj_Hilos = []
    tiempos_cpu_Hilos = []
    tiempos_reloj_Seq = []
    tiempos_cpu_Seq = []
    for i in range(len(val_N)):
        tiempos_reloj_Hilos.append([])
        tiempos_cpu_Hilos.append([])
        tiempos_reloj_Seq.append([])
        tiempos_cpu_Seq.append([])

    # abrir fichero para lectura
    fichero = open('times.txt', 'r')
    texto = fichero.readlines()

    # expresion regular para leer los tiempos en el archivo times.txt
    leer_tiempos = re.compile(
        '''
        \[
        (?P<algoritmo>
            T|S
        )
        .*
        (?P<tipoTime>
            W|C
        )
        .*N.*\=
        (?P<tamano>
            [0-9]+
        )
        \s:\s
        (?P<valor>
            [0-9]+.[0-9]+
        )
        $
        ''',
        re.VERBOSE)

    tiempos_hilos(leer_tiempos)

    tmedio_cpu_Hilos = promedio_tiempos(tiempos_cpu_Hilos)
    tmedio_reloj_Hilos = promedio_tiempos(tiempos_reloj_Hilos)
    tmedio_cpu_Seq = promedio_tiempos(tiempos_cpu_Seq)
    tmedio_reloj_Seq = promedio_tiempos(tiempos_reloj_Seq)

    print("\nPromedio Tiempos de Reloj - Hilos")
    imprimir_tiempo_medio(tmedio_reloj_Hilos, val_N)

    print("\nPromedio Tiempos de CPU - Hilos")
    imprimir_tiempo_medio(tmedio_cpu_Hilos, val_N)

    print("\nPromedio Tiempos de Reloj - Secuencial")
    imprimir_tiempo_medio(tmedio_reloj_Seq, val_N)

    print("\nPromedio Tiempos de CPU - Secuencial")
    imprimir_tiempo_medio(tmedio_cpu_Seq, val_N)

    # se crea un proceso para evitar desbordamiento de la memoria porque la
    # libreria matplotlib no libera automaticamente la memoria al graficar
    # cuando termina el proceso se libera la memoria
    proc = mp.Process(target=graficar(tmedio_cpu_Hilos, tmedio_reloj_Hilos,
                                      tmedio_cpu_Seq, tmedio_reloj_Seq, val_N))
    proc.daemon = True
    proc.start()
    proc.join()
