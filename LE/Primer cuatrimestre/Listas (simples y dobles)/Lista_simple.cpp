#include <iostream>

using namespace std;

struct Nodo{
    int dato;
    Nodo *siguiente;
};

void instertarLista(Nodo *&, int);

int main(){
    Nodo *lista = NULL;

    int dato;

    cout<<"Digame un numero";
    cin>>dato;
    instertarLista(lista, dato);
    
    cout<<"Digame un numero";
    cin>>dato;
    instertarLista(lista, dato);

    cout<<"Digame un numero";
    cin>>dato;
    instertarLista(lista, dato);

    return 0;
}

void instertarLista(Nodo *&lista, int n){
    Nodo *nuevo_nodo = new Nodo ();
    nuevo_nodo -> dato = n;

    Nodo *aux1 = lista;
    Nodo *aux2;

    while((aux1 != NULL) && (aux1->dato < n)){
        aux2 = aux1;
        aux1 = aux1->siguiente;
    }

    if(lista == aux1){
        lista = nuevo_nodo;
    }
    else{
        aux2->siguiente = nuevo_nodo;
    }

    nuevo_nodo->siguiente = aux1;

    cout<<"\tElemento "<<n<<" instertado a lista correctamente\n.";
}