#include <iostream>
/*iostream es un componente de la biblioteca estándar (STL) del lenguaje de programación C++ que 
es utilizado para operaciones de entrada/salida. Su nombre es un acrónimo de Input/Output Stream.*/

#include <stdlib.h>
//Sirve para convertir un entero a cadena de caracteres.

#include <fstream>
/*ifstream es una clase que permite crear la instancia fich para leer de un 
fichero. En este caso, se abre un fichero para lectura llamado "ejemplo. dat".*/

using namespace std; //Para no poner std:: en todos los cout.

void prueba_de_archivo(void); //Creo una funcion que se llama prueba_de_archivo.
//Entre los () tengo que poner lo que va a recibir.

int main(){

    prueba_de_archivo(); //Llamo a la funcion prueba_de_archivo para que ahga lo que este dentro de la funcion.

    return 0;
}

void prueba_de_archivo(){ //Le digo que cosas va a ser cunado llame a la funcion prueba_de_archivo.
    ofstream archivo; //Le

    archivo.open("nombre_de__archivo.txt",ios::out); 
    //Le pongo nombre y formato a mi archivo con el .open("");.
    //El ios::out es para mandar o recibir datos de los archivos.

    if(archivo.fail()){
        cout<<"Hubo un error en el programa :(";
        exit(1);
    } //Si por alguna razon no se pudo abrir el archivo se va a mostrar el cout en pantalla.

    archivo<<"\n---Esto tendria que estar dentro de nombre_de__archivo---"; //Le digo que cosa quiero que este dentro del archivo.
    archivo.close(); //Despues de que haga todo lo anterior le digo que el archivo se cierre.
}