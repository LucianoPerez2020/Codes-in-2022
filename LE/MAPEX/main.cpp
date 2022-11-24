#include<iostream>
using namespace std;

//Creo dos prototipos para dos funciones. Una para encriptar y la otra para desencriptar.
int encriptacion(char texo[50]);
int desencriptacion(char texto[50]);

int main(){
    system("cls");
    
    char texto[50];
    cout<<"Ingrese su texto: ";
    //"cin.getline" me toma todos los valores diferentes hasta que de el ENTER.
    cin.getline(texto,50);

    encriptacion(texto);
    cout<<"Texto encriptado: "<<texto;

    desencriptacion(texto);
    cout<<"\nTexto desencriptado: "<<texto;

    return 0;
}

/*
Me va a devolver un valor entero y para eso necesita los
valores tipo char de "texto".
*/
int encriptacion(char texto[50]){
    //Creo una variable local (i) y la igualo a "0" para hacer la conversion
    int i = 0;
    //Mientras que el valor del vector texto sea diferente de "0"...
    while(texto[i] != 0){
        //El valor del vector de texto ahora se le va a sumar +10.
        texto[i] = texto[i] + 10;
        //Corro la "casilla" donde esta el valor del vector.
        i++;
    }
}

int desencriptacion(char texto[50]){
    int i = 0;
    while(texto[i] != 0){
        //El valor del vector de texto ahora se le va a sumar -10.
        texto[i] = texto[i] - 10;
        i++;
    }
}