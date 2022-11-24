#include <iostream>
#include <conio.h>

using namespace std;

int main (){

//Video 30: Presentacion de vectores

  cout <<"\n\n----------Video 31----------\n";

  int numero[] = { 1, 2, 3, 4, 5 };
  int suma = 0;

  for (int i = 0; i < 5; i++){
      suma = suma + numero[i];	//Pongo "i" porque es la posicion (valor) que va cambiando.
    }

  cout << suma;

  cout << "\n\n(ejercicio)\n";

  int numero2[] = { 1, 2, 3, 4, 5 };
  int multiplicacion = 1;

  for (int i = 0; i < 5; i++){
      multiplicacion = multiplicacion * numero2[i];
    }

  cout << multiplicacion;

  cout <<"\n\n----------Video 32----------\n";

  /*Escribe un programa que lea de la entrada estándar un vector
  de números y muestre en la salida estándar los números del vector
  con sus índices asociados.*/

  /*Escribe un programa que defina un vector de números y muestre
  en la salida estándar el vector en orden inverso—del último al
  primer elemento.*/
  
  cout << "\n\n----------Video 33----------\n";

  

  return 0;
}
