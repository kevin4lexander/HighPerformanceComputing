#!/bin/bash

file_process=$1

shift # pull off first arg

process=${file_process} # archivo cpp procesos (multiplicacion matrices)

# Array con los valores de N para la matriz NxN
val_N=(100 250 500 1000 1500 2000 2500 3000 4000 5000 7000)
# val_N=(100 250 500 1000)

repeat_from=1
repeat_to=6

while [ $repeat_from -le $repeat_to ]
do
    for (( i=0; i<${#val_N[*]}; i++ ))
    do
        echo -e "\nN:${val_N[i]} x$repeat_from"

        # compilar
        g++ -g -o $file_process.out $process.cpp -lm

        # echo $?
        if [[ $? -eq 0 ]]; then
        ./$process.out ${val_N[i]} # correr ejecutable de multiplicacion matrices procesos
        fi
    done
    (( repeat_from++ ))
done

# echo `date` >> hora_fin.txt

# graficar los tiempos de ejecucion
# python2 graficar.py ${val_N[@]}

exit
