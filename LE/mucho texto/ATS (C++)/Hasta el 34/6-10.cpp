// 6 ==> Expreciones.
// 7 ==> Expreciones.
// 8 ==> Expreciones.
// 9 ==> Expreciones.
// 10 ==> Expreciones.

#include <iostream>
#include <cmath>

using namespace std;

int main(){
   
    cout<<"----------Video 06----------\n";
   
    //cout.precision(x); ==> Números despues de la coma
   
    float a1 = 0;
    float b1 = 0;
    float c1 = 0;
    float d1 = 0;
    float resultado1 = 0;
   
    cout<<"Ingrese 4 valores para hacer el calculo (a1 + b1) / ( c1 + d1)\n";
    cout<<"\nValor 1: "; cin>>a1;
    cout<<"Valor 2: "; cin>>b1;
    cout<<"Valor 3: "; cin>>c1;
    cout<<"Valor 4: "; cin>>d1;
   
    resultado1 = (a1 + b1) / ( c1 + d1);
   
    //cout.precision(2); ==> ¿COMO LO PUEDO USAR?
   
    cout<<"\nSu resultado es: " <<resultado1;
   
    cout<<"\n\n----------Video 07----------\n";
    
    float a2 = 0;
    float b2 = 0;
    float c2 = 0;
    float d2 = 0;
    float resultado2 = 0;
   
    cout<<"Ingrese 4 valores para hacer el cálculo\n";
    
    cout<<"\nValor 1: "; cin>>a2;
    cout<<"Valor 2: "; cin>>b2;
    cout<<"Valor 3: "; cin>>c2;
    cout<<"Valor 4: "; cin>>d2;
    
    resultado2 = a2 + (b2 / (c2 - d2) );
    
    cout<<"\nResultado: " <<resultado2;
   
    cout<<"\n\n----------Video 08----------\n";
   
    float alumno1 = 0;
    float alumno2 = 0;
    float alumno3 = 0;
    float alumno4 = 0;
    float media = 0;
    
    cout<<"Ingrese las 4 notas de los alumnos\n";
    
    cout<<"\nNota del alumno 1: "; cin>>alumno1;
    cout<<"Nota del alumno 2: "; cin>>alumno2;
    cout<<"Nota del alumno 3: "; cin>>alumno3;
    cout<<"Nota del alumno 4: "; cin>>alumno4;
    
    media = (alumno1 + alumno2 + alumno3 + alumno4) / 4;
    
    cout<<"\nNota media: " <<media;
   
    cout<<"\n\n----------Video 09----------\n";
   
    float cateto1 = 0;
    float cateto2 = 0;
    float hipotenusa = 0;
    
    cout<<"Ingrese sus dos catetos\n";
    
    cout<<"\nIngrese su cateto 1: "; cin>>cateto1;
    cout<<"Ingrese su cateto 2: "; cin>>cateto2;
    
    hipotenusa = cateto1 * cateto1 + cateto2 * cateto2;
    hipotenusa = sqrt(hipotenusa);
    
    cout<<"\nValor de la hipotenusa: " <<hipotenusa;
    
    //#include<cmath> + sqrt (variable) ==> Raiz de la variable
   
    cout<<"\n\n----------Video 10----------\n";
   
    float a = 0;
    float b = 0;
    float c = 0;
    float x1 = 0;
    float x2 = 0;

    cout<<"Ingrese a, b y c\n";
    cout<<"\nA: "; cin>> a;
    cout<<"B: "; cin>> b;
    cout<<"C: "; cin>> c;
 
    x1 = -b - sqrt((b * b) -4 *(a * c)) / (2 * a);
    x2 = -b + sqrt((b * b) -4 *(a * c)) / (2 * a);
 
    cout<<"\nResultados: \n";
    cout<<"X1: " <<x1;
    cout<<"\nX2: " <<x2;
   
    return 0;
}

