#include <iostream>
#include <string.h> 

using namespace std;

string user, password;
string new_user, new_password;
int menu;

//Prototipos de funciones
void iniciar_sesion (string, string);
void crear_cuenta (string, string);

int main (){

    cout<<"--------------------"<<endl;
    cout<<"\tMENU"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"(1) Iniciar sesion"<<endl;
    cout<<"(2) Crear cuenta"<<endl;
    cout<<"(3) Apagar pc"<<endl;

    cout<<"Numero de opcion: ";
    cin>>menu;

    switch (menu){
        case 1:
            cout<<" Iniciar sesion:"<<endl;
            iniciar_sesion (user, password);
            break;

        case 2:
            crear_cuenta (new_user, new_password);
            break;

        case 3:
            return -1;
            break;

        default:
            cout<<"ERROR";
            break;
    }

    return 0;
}

void iniciar_sesion (string user, string password){
    cout<<"Username: ";
    cin>>user;
    cout<<"Paswword: ";
    cin>>password;

    if(user == "luperez" && password == "lu123"){
        cout<<"-username and paswword correct-"<<endl;
    }
    else{
        cout<<"-username and/or paswword incorrect-"<<endl;
    }
}

void crear_cuenta (string new_user, string new_password){
    
}