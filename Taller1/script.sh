#!/bin/bash

file_threads=$1
file_seq=$2

shift # pull off first arg

threads=${file_threads} # archivo cpp hilos
sequencial=${file_seq} # archivo cpp secuencial

# Array con los valores de N para la matriz NxN
# val_N=(100 250 500 1000 1500 2000 2500 3000 4000 5000 7000)
val_N=(100 200 300 400)

repeat_from=1
repeat_to=3

while [ $repeat_from -le $repeat_to ]
do
    for (( i=0; i<${#val_N[*]}; i++ ))
    do
        echo -e "\nN:${val_N[i]} x$repeat_from"

        # compilar
        g++ -g -o $file_threads.out $threads.cpp -lpthread -lm

        # echo $?
        if [[ $? -eq 0 ]]; then
        ./$threads.out ${val_N[i]} # correr ejecutable
        fi

        g++ -g -o $file_seq.out $sequencial.cpp -lm

        if [[ $? -eq 0 ]]; then
        ./$sequencial.out ${val_N[i]}
        fi
    done
    (( repeat_from++ ))
done

# echo `date` >> hora_fin.txt

# graficar los tiempos de ejecucion
python2 graficar.py ${val_N[@]}

exit