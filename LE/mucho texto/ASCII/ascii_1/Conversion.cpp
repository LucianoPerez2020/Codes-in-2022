//Demostracion de como pasar de un caracter a codigo ascii y viceversa.
#include <iostream>
using namespace std;

int ascii1 (char letra); //De caracter a ascii
char ascii2 (char numero); //De ascii a caracter

int main (){

//  72 - 111 - 108 - 97
    cout<<ascii1('H')<<endl; //72
    cout<<ascii1('o')<<endl; //111
    cout<<ascii1('l')<<endl; //108
    cout<<ascii1('a')<<endl; //97

//  Hola
    cout<<ascii2(72);  //H
    cout<<ascii2(111); //o
    cout<<ascii2(108); //l
    cout<<ascii2(97);  //a

    return 0;
}

int ascii1 (char letra){
    int valorASCII1 = letra;
    return valorASCII1;
}

char ascii2 (char numero){
    char valorASCII2 = numero;
    return valorASCII2;
}