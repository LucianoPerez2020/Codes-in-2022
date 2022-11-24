#include<iostream>
using namespace std;

// * = valor
// & = direccion

int main(){

    cout<<"\t- - - Ejercicio 1 - - -\n";

    //Creo las variables que necesito con un puntero
    int numero, *dir_numero1;

    cout<<"Ingrese un numero: ";
    cin>>numero;

    //Ahora "dir_numero" tiene el valor de la dirección de memoria de "numero".
    dir_numero1 = &numero;

    //Si el valor al que apunta mi puntero da de resto 0 al dividirlo por 2…
    if(*dir_numero1 %2 == 0){
        cout<<"El numero "<<*dir_numero1<<" es par.\n";
        cout<<"Direccion de memoria: "<<dir_numero1;
    }
    //Si no...
    else{
        cout<<"El numero "<<*dir_numero1<<" es impar.\n";
        cout<<"Direccion de memoria: "<<dir_numero1;
    }

    return 0;
}