#include <iostream>
#include <conio.h>

using namespace std;

/*
 &n = La direccion de n
 *n = La variable cuya direccion esta almacenada en n
*/

int numero1, *direccion_de_numero1; //Creo un puntero con el nombre direccion_de_numero1.

int main(){

    numero1 = 10;
    direccion_de_numero1 = &numero1; //Digo que la variable sea igual a la direccion de numero1.

    cout<<"Numero: "<<*direccion_de_numero1<<endl;
    //Le digo que me muestre la direccion que tiene de almacenamiento la vairable.
    cout<<"Direccion de memoria: "<<direccion_de_numero1;
    //Le digo que me muestre la direccion de la variable.

    return 0;
}