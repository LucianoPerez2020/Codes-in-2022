#include <iostream>
using namespace std;

char asterisco(char texto[15]);

int main(){

    string username, password;

    cout<<"- - - INICIO DE SESION - - -"<<endl;
    cout<<"Username: ";
    cin>>username;
    cout<<"Password: ";
    cin>>password;

    return 0;
}

// char asterisco(char texto[50]){
//     int i = 0;
//     while(texto[i] != 0){
//         //El valor del vector de texto ahora se le va a sumar -10.
//         texto[i] = texto[i] - 10;
//         i++;
//     }
// }

//Como hago para que antes de que me muestre lo que ingrese ya me devuelva un asterisco???