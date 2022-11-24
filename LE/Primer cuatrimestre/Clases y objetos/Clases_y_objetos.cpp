#include <iostream>
#include <stdlib.h>

using namespace std;

class persona{
    private: //Atributos 
    //NO me permite usarlo fuera de esta funcion.
        int edad;
        string nombre;
    public: //Metodos 
    //SI me permite usarlo fuera de esta funcion.
        persona(int,string); //Prototipo de constructor.
        //Para construir el objeto de la persona necesito esto.
        void leer ();
        void correr();
        //Más funciones.
};

//Inicialización del constructor que nos sirve para iniciar los atributos.
//nombre_de_la_clase::prototipo_del_constructor
persona::persona(int _edad,string _nombre){ //Con el :: le digo que tome los atributos de class persona.
    this->edad = _edad;
    this->nombre = _nombre;
    /*
    Con el this-> yo le estoy indicando que ESA variable de ESE atributo sea el _edad o el _nombre
    de esa persona, de esta forma los nombres y edades de demas class (osea personas) no se mezclen.
    */
}

void persona::leer(void){ //Creo una funcion que se llama persona con los atributos de leer.
    cout<<"Soy "<<this->nombre<<" y estoy programando"<<endl;
}

void persona::correr(void){ //Creo una funcion que se llama persona con los atributos de correr.
    cout<<"Soy "<<this->nombre<<",estoy corriendo y tengo "<<this->edad<<" años"<<endl;
}

int main (){

    persona p1(28,"Isi"); //Esto...
    persona p2(17,"Luciano"); //... y esto son objetos.

    p1.leer(); //Esto es el metodo leer.
    p2.correr(); //Esto es el metodo correr.
    //"LAS CLASES QUE ESTAN DENTRO DE LOS METODOS SE LES DICE METODOS"

    return 0;
}