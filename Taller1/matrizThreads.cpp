#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h> //strerror
#include <pthread.h>
#include <time.h>
#include <sys/time.h>
#include <fstream>
using namespace std;

int NTHREADS = 1;
int **puntero_matriz1,**puntero_matriz2,**puntero_matriz3;
int filA,colA,filB,colB,filC,colC;

void llenarMatriz(int);
void *multiplicacion(void *args);
void mostrarMatriz(int **,int,int);
double get_wall_time();
double get_cpu_time();
void guardarTiempos(int,double, double);

int main(int argc, char *argv[])
{
    int tamano = 0; //tamano matrices NxN
    if (argc >= 2){
        tamano = stoi(argv[1]);
    }
    else {
        printf("ERROR: missing parameters\n");
        return 0;
    }

    srand(time(NULL));
    llenarMatriz(tamano); //llenar matriz con numeros aleatorios
    NTHREADS = filA; // cantidad de hilos

    pthread_t threads[NTHREADS];
    int rc;
    int idHilos[NTHREADS];

    // iniciar temporizadores
    double wall0 = get_wall_time(); //////////////
    double cpu0  = get_cpu_time(); ////////////

    //Creamos los hilos
    for(int t=0;t<NTHREADS;t++){
        //cout<<"Valor de t: "<<t<<endl;
        idHilos[t] = t;
        rc = pthread_create(&threads[t], NULL, multiplicacion, &idHilos[t]);
        if (rc){
            printf("ERROR: return code from pthread_create() is %d\n", rc);
            printf("Code %d= %s\n",rc,strerror(rc));
            exit(-1);
        }
   }

    for (int h = 0; h < NTHREADS; h++)
        pthread_join(threads[h], NULL);

    // detener temporizadores
    double wall1 = get_wall_time();
    double cpu1  = get_cpu_time();

    // mostrarMatriz(puntero_matriz1,filA,colA);
    // mostrarMatriz(puntero_matriz2,filB,colB);
    // mostrarMatriz(puntero_matriz3,filC,colC);

    // tiempos de ejecución
    double wallTime = wall1 - wall0;
    double cpuTime = cpu1 - cpu0;
    guardarTiempos(tamano,wallTime, cpuTime);

    // mostrar temporizadores
    printf("\n");
    cout << "\033[0m[Threads] N=" << tamano << " Wall Time : " << wallTime << " seconds \033[0m" << endl;
    cout << "\033[0;32m[Threads] N=" << tamano << " CPU Time  : " << cpuTime  << " seconds \033[0m" << endl;

    //Liberar la memoria utiliza en matriz1
    for(int i=0;i<filA;i++){
        delete[] puntero_matriz1[i];
    }
    delete[] puntero_matriz1;

    //Liberar la memoria utiliza en matriz2
    for(int i=0;i<filB;i++){
        delete[] puntero_matriz2[i];
    }
    delete[] puntero_matriz2;

    //Liberar la memoria utiliza en matriz3
    for(int i=0;i<filC;i++){
        delete[] puntero_matriz3[i];
    }
    delete[] puntero_matriz3;

    return 0;
}

void llenarMatriz(int t)
{
    filA=t; filB=t; colA=t; colB=t;

    //Reservar memoria para la primera matriz
    puntero_matriz1 = new int*[filA]; //Reservar memoria para las filas
    for(int i=0;i<filA;i++){
        puntero_matriz1[i] = new int[colA]; //Reservar memoria para las columnas
    }

    for (int i = 0; i < filA; i++)
        for (int j = 0; j < colA; j++)
            *(*(puntero_matriz1+i)+j) = rand()%11;

    //Reservar memoria para la segunda matriz
    puntero_matriz2 = new int*[filB]; //Reservar memoria para las filas
    for(int i=0;i<filB;i++){
        puntero_matriz2[i] = new int[colB]; //Reservar memoria para las columnas
    }

    for (int i = 0; i < filB; i++)
        for (int j = 0; j < colB; j++)
            *(*(puntero_matriz2+i)+j) = rand()%11;

    filC = filA;
    colC = colB;

    //Reservar memoria para la primera matriz
    puntero_matriz3 = new int*[filC]; //Reservar memoria para las filas
    for(int i=0;i<filC;i++){
        puntero_matriz3[i] = new int[colC]; //Reservar memoria para las columnas
    }
}

void *multiplicacion(void *threadid)
{
    int idHilo = *(int *) threadid;
    //cout<<"Verificar idHilo: "<<idHilo<<endl;

    int j;
    if(colA==filB){//para que se puedan multiplicar dos matrices
        for(j=0;j<colB;j++){
            for(int k=0;k<colA;k++){
                *(*(puntero_matriz3+idHilo)+j) += *(*(puntero_matriz1+idHilo)+k) * *(*(puntero_matriz2+k)+j);
            } //puntero_matriz3[idHilo][j] += puntero_matriz1[idHilo][k] * puntero_matriz2[k][j];
        }
    } pthread_exit(NULL);
}

void mostrarMatriz(int **matriz, int nFilas,int nCol)
{
    printf("\nMatriz: \n");
    for(int i=0;i<nFilas;i++){
        for(int j=0;j<nCol;j++){
            cout << *(*(matriz+i)+j) << " ";
        }
        printf("\n");
    }
}

double get_wall_time(){
    struct timeval time;
    if (gettimeofday(&time,NULL)){
        //  Handle error
        return 0;
    }
    return (double)time.tv_sec + (double)time.tv_usec * .000001;
}

double get_cpu_time(){
    return (double)clock() / CLOCKS_PER_SEC;
}

void guardarTiempos(int tamanoMatriz,double wallTime, double cpuTime)
{
    ofstream fileTime; // archivo
    fileTime.open("times.txt",ios::app); //crea el archivo si no existe - sobreescribe (out), aniade datos (app)

    if(fileTime.fail()){
        printf("ERROR: fail creating the file\n");
        exit(1);
    }

    //fileTime << wallTime << endl;
    fileTime << "[Threads Wall Time] N=" << tamanoMatriz << " : " << wallTime << endl;
    fileTime << "[Threads CPU Time] N=" << tamanoMatriz << " : " << cpuTime << endl;

    fileTime.close();
}
