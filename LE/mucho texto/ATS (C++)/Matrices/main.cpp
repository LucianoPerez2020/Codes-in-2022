#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){

    int matriz[2][3] = {{1,2,3} , {4,5,6}};
/*
    (tipo_de_variable) (nombre_de_variable) [N_de_filas][N_de_columnas] = (valor1,valor2);
*/

    /*
        (columnas)
        | 1 | 2 | 3 |
(filas)
        | 4 | 5 | 6 |
    */

    cout<<matriz[0][0];

    return 0;
}