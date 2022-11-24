#include <iostream>
#include <conio.h>
using namespace std;

char letra[15]; //Variable "char" con 16 "espacios".

int main (){

    cout<<"Ingrese sus caracateres: ";

    letra[0] = getchar(); //La posicion del vector 0 es el valor del primer caracter ingresado.
    letra[1] = getchar(); //La posicion del vector 1 es el valor del segundo caracter ingresado.

    /*
        La funcion "getchar()" es para conseguir la etnrada de caracteres uno a uno.
    */

    cout<<"Caracateres ingresados: "<<letra;

    return 0;
}

//NO ME SIRVE PARA LO QUE QUIERO.