#include<iostream>
using namespace std;

int main(){

    cout<<"\t- - - Ejercicio 3 - - -\n";

    int espacio;

    cout<<"Cantidad de espacio: ";
    cin>>espacio;
    int numeros[espacio];

    cout<<"Ingrese sus valores: ";
    cin>>numeros[espacio];

    for(int i = 0; i < espacio; i++){
        cout<<numeros[espacio];
    }

    return 0;
}