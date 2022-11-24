#include <iostream>
#include <conio.h>
//Uso bibliotecas

using namespace std;

int mayor_numero(int numero1, int numero2); //Para que la variable funcione voy a necesitar dos numeros.
int n1, n2, Nmax;
//Creo un para de variables.

int main(){

    cout<<"Ingrse dos numeros: ";
    cin>>n1>>n2;

    mayor_numero(n1, n2);
    //Le digo que haga lo que este dentro de la funcion mayor_numero.

    if(Nmax != 12345){
        cout<<"El número mas grande de los dos es: "<<Nmax;
    }
    else{
        cout<<"Los dos numeros son iguales";
    }

    return 0;
}

int mayor_numero(int n1, int n2){ //Le digo lo que va a hacer mi funcion (en este caso solo comparar numeros).

    if(n1 > n2){
        return Nmax = n1;
    }
    else if(n1 == n2){
        return Nmax = 12345;
    }
    else{
        return Nmax = n2;
    }
}