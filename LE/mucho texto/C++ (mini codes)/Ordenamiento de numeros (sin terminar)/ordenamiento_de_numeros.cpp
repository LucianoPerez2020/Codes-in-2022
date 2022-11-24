#include <iostream>
#include <conio.h>

using namespace std;

int cantidad_de_numeros;

int main (){

    cout<<"Cuantos numeros quiere ingresar?: ";

    cin>>cantidad_de_numeros;

    while (cantidad_de_numeros <= 1){
        cout<<"Tienen que ser minimamente dos numeros.";
        cin>>cantidad_de_numeros;
    }

    int numeros1[cantidad_de_numeros];

    cout<<numeros1[0]<<numeros1[1]<<numeros1[2];

        // cout<<"Ingrese los numeros que quiere ordenar: \n";

        // for(int i = 0; i < cantidad_de_numeros; i++){
        // cin>>numeros1[i];
        // }

    return 0;
}




    // cout<<"Quiere ordenar los numeros de  menor a mayor (1) o de mayor a menor(2)?: ";
    // cin>>ordenamiento;

    //     if(ordenamiento == 1){
    //     cout<<"\nOrdenamiento de menor a mayor: ";
        
    //     for( i = 0; i < cantidad_de_numeros; i++){
    //         for(numeros1){

    //         }
    //     }
        
    //     }

    //     else{
    //     cout<<"Ordenamiento de mayor a menor: ";
    //     for(){

    //     }
    //     }

    //     cout<<"---TICKET DE SALIDA---";
    //     cout<<"Numeros ingresados: ";
    //     cout<<"Seleccion de ordenamiento: ";
    //     cout<<"Numeros ordenados: ";
    // }