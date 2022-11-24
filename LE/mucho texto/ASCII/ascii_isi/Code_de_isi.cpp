#include <iostream>

using namespace std;
int main(){

    system("cls");
    int cant, i = 0;
    char caracteres[25];

    cout<<"Ingrese su texto: ";
    cin.getline(caracteres, 25, '\n'); //Me toma todos los caracteres hasta que haga un salto de linea (ENTER).

    cout<<"Ascii: ";

    while(caracteres[i]!=0){
        cout<< "-" <<(int)(caracteres[i++]);
    }

    return 0;
}