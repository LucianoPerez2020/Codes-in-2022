//Ver el codigo ascii de un conjunto de caracteres deseados.

#include <iostream>
using namespace std;

int ascii (char letra);
//Prototipo de funcion || Devuelve un valor entero (ascii) y necesita recibir un char (letra).
char letra; //Variable para los caracteres a ingresar.
int enter; //Variable para terminar con el bucle "do while".
int letras; //Variable para contar la cantidad de letras y usar esta dentro de otra variable con vetores (letra_ascii[]).
int letra_ascii[15]; //Variable para guardar el valor de el caracter a ingresar.
int valor_ascii; //EL valor ascii de la variable tipo char.

int main (){

    cout<<"Ingrese sus caracateres: ";

    do{   
        letras ++; //El contador "letras" suma +1 a su valor actual.
        cin>>letra; //Le pido que ingrese la letra.
        ascii(letra); //Llamo a la funcion para hacer la conversion de "char" a "int" (letra a ascii).
        letra_ascii[letras] == valor_ascii; 
        //El valor de la posicion de la varibale "letra_ascii" va a ser igual al valor convertido ("valor_ascii").
    
        /*
            UN CICLO DO WHILE PARA:
            1_ Al presionar ENTER se agarren todos los carcateres y sean convertidos en ascii uno por uno.
            2_ A medida que se van ingresando los caracteres ya los conviertan y los dejen guardados en una
            variable de tipo "int" para despues ser mostrados.
        */

        // < - - - - - - - - - - - - - - - - - - - - >
        // do{        
        //     letras ++;
        //     cin>>letra;
        //     ascii(letra);
        //     letra_ascii[letras] == valor_ascii; 
        // }while ();
        // < - - - - - - - - - - - - - - - - - - - - >

    }while (enter >= 13); //Si apreto ENTER finaliza el "do";

    cout<<"hola";

    // for (int letras_ascii = 0; letras_ascii; letras_ascii++){
    //     cout<<letras_ascii[1]; //Porque error???
    // }

    return 0;
}

int ascii (char letra){ 
    int valor_ascii = letra; //Ahora el valor de "valor_ascii" es el mismo que el de "letra".
    return valor_ascii; //Y que me retorne ese mismo valor hacia donde este la funcion.
}

//Separar las letras para convertirlas una por una