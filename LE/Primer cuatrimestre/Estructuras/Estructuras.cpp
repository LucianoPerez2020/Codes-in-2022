#include<iostream>
#include<conio.h>

using namespace std;

struct mallas{ 
//Creo una estructura que se llama mallas y le digo los tipos y nombres de las variables que voy a usar.
    char marca[10];
    float precio;
    char talle[5];
    char fechadecompra[20];
}
Malla1 = {"Arena",20000, "LX", "03/06/2022"}, //Creo una variable con los valores asignados.
Malla2; //Creo una variable pero sin llenar los datos.

int main(){
    cout << "---Caracteristicas de la malla 1---" << endl;
    cout << "Marca: " << Malla1.marca << endl;
    cout << "Precio: " << Malla1.precio << endl;
    cout << "Talle: " << Malla1.talle << endl;
    cout << "Fecha de compra: " << Malla1.fechadecompra << endl;
    //Asi se imprimen los valores de ciertas partes de la estructura con la variable asignada.

    cout << "---Ingrese las aracteristicas de la malla 2---" << endl;
    cout << "Marca: ";
    cin >> Malla2.marca;
    cout << "Precio: ";
    cin >> Malla2.precio;
    cout << "Talle: ";
    cin >> Malla2.talle;
    cout << "Fecha de compra: ";
    cin >> Malla2.fechadecompra;
    //Asi se imprimen los valores de ciertas partes de la estructura con la variable asignada.

    //Averiguar como crear mas variables si es que el usuario desea ingresar mas.

    getch();
    return 0;
}