#include <iostream>
#include <fstream>

using namespace std;

void archivo_bat(void);

int main(){

    archivo_bat();

    return 0;
}

void archivo_bat(){
    ofstream archivo;

    archivo.open("archivo_bat.bat",ios::out); //El ios::out es para mandar o recibir datos de los archivos.

    if(archivo.fail()){
        cout<<"Hubo un error en el programa :(";
        exit(1);
    }

    archivo<<"@echo off\nstart MicrosoftEdge";
    archivo.close();
}