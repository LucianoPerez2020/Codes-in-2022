#include <iostream>
#include <conio.h> //getch

using namespace std;

string username, password;

int main(){

    cout<<"- - - INICIO DE SESION - - -"<<endl;
    cout<<"Username: ";
    cin>>username;
    cout<<"Password: ";
    cin>>password;

    //- VER COMO FUNCIONAN LOS ASTERISCOS -
    // char caracter;
    // caracter = getch();

    // password = "";

    // while(caracter =! 13){
    //     password.push_back(caracter);
    //     cout<<"*";
    //     caracter = getch();
    // }

    if(username == "luperez" && password == "lu123"){
        cout<<"-username and paswword correct-"<<endl;
    }
    else{
        cout<<"-username and/or paswword incorrect-"<<endl;
    }

    return 0;
}