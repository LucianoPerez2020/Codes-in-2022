#include <iostream>
#include <string.h>

using namespace std;

string user, password;
char iniciar_sesion;

int main (){

    cout<<"Log in? (y/n) ";
    cin>>iniciar_sesion;

    switch (iniciar_sesion){
        case 's':
            cout<<"Inicio sesion";
            break;

        case 'n':
            cout<<"No inicio sesion";
            break;

        default:
            cout<<"ERROR";
            break;
    }

    cout<<"Pasos siguientes: ";

    // cout<<"Enter your username and password: ";
    // cin>>user;
    // cin>>password;

    return 0;
}