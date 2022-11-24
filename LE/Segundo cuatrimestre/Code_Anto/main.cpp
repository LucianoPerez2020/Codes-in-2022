#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define CANT 10

int cantAprobados (int *, int, int);

int main (int argc, char* argv[])
    {
        srand (time(NULL));
        int nota = 0;
        int notas [CANT];
        //nota = (int)argv[1][0] - '0'; 

        if (argc != 2 || atoi(argv[1])<0 || atoi(argv[1])>10) 
        {
            printf("¡¡¡CUIDADO!!! \n");
            printf("USO CORRECTO --> [./ejecutable] [0-10] \n");
            return(0);
        }

        nota = argv[1][0] & 0x0F; //mascara 0000 1111

        for(int i = 0; i<CANT; i++)
        {
            notas[i] = rand() % 11;
            printf("Nota [%d] = [%d] \n", i, notas[i]);
        }

        printf("Aprobados con [%d] = [%d] \n", nota, cantAprobados (notas, CANT, nota));

        return(0);
    }

int cantAprobados (int *notas, int cantidad, int limite)
    {
        int aprob = 0;

        for (int j = 0; j<cantidad; j++)
        {
            if(*(notas+j) >= limite)
            aprob++;
        }
        return(aprob);
    }

    //Revisar porque no funciona.