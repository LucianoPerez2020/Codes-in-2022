// 11 ==> Condicionales simple y dobles (if / else).
// 12 ==> Condicionales multiples (switch).
// 13 ==> Ejercicios.
// 14 ==> Ejercicios.
// 15 ==> Ejercicio para tener en cuenta.

#include <iostream>
using namespace std;

int main(){

    cout<<"----------Video 11----------\n";
    
/*
    if (condicion){
        instruccion1;
    }
    else {
        instruccion2;
    }
password
    = (igual que...)
    != (diferente de...)
    < (menor que...)
    > (mayor que...)
    <= (menor o igual que...)
    >= (mayor o igual que...)
*/
    int password;
    cout<<"Ingrese la contraseña: ";
    cin>>password;

    if(password == 123){
        cout<<"Contaseña correcta";
    }
    else{
        cout<<"Contraseña incorrecta";
    }

    cout<<"\n\n----------Video 12----------\n";

    /*
        switch(expresion){
            case literal1:
            instrucciones1;
            break;

            case literal2:
            instrucciones1;
            break;

            case literalN:
            instruccionesN;
            break;

            default:
            instrucciones de default;
            break;
        }
    */
    
    int n1, n2, suma;
    cout<<"Ingrese dos numeros para hacer una suma\n";
    cout<<"Numero 1: ";
    cin>>n1;
    cout<<"Numero 2: ";
    cin>>n2;
    suma = n1 + n2;
    
    switch(suma){
    case 2:
    cout<<"La suma de 2";
    break;

    case 4:
    cout<<"La suma de 4";
    break;

    case 6:
    cout<<"La suma de 6";
    break;

    default:
    cout<<"La suma no esta en el rango 2-4-6";
    break;
    }

    /*
    
    cout<<"\n\n----------Video 13----------\n";

    1) Escriba un programa que lea dos números y determine cuál de ellos es el mayor.
    2) Escriba un programa que lea tres números y determine cuál de ellos es el mayor.

    cout<<"\n\n----------Video 14----------\n";
    
    1) Realice un programa que lea un valor entero y determine si se trata de un número par o impar.
    2) Comprobar si un número digitado por el usuario es positivo o negativo.
    
    */

    cout<<"\n\n----------Video 15----------\n";
    
    char letra;
    cout<<"Ingrese un caracter: ";
    cin>>letra;
    
    switch(letra){
        case 'a':
        cout<<"La letra ¨a¨ es una vocal.";
        break;
        
        case 'e':
        cout<<"La letra ¨e¨ es una vocal.";
        break;
        
        case 'i':
        cout<<"La letra ¨i¨ es una vocal.";
        break;
        
        case 'o':
        cout<<"La letra ¨o¨ es una vocal.";
        break;
        
        case 'u':
        cout<<"La letra ¨u¨ es una vocal.";
        break;
        
        default:
        cout<<"La letra ";
        cout<<letra;
        cout<<" no es una vocal.";
        break;
    }

    return 0;
}