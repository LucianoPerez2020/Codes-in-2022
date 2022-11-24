//Ver el codigo ascii de un caracter deseado.

#include <iostream>
using namespace std;

int ascii (char letra);
char letra;

int main (){

    cout<<"Ingrese su caracater: ";
    cin>>letra;
    cout<<ascii(letra);

    return 0;
}

int ascii (char letra){
    int valor_ascii = letra;
    return valor_ascii;
}