// 16 ==> Ejercicio.
// 17 ==> Ejercicio.
// 18 ==> Ejercicio.
// 19 ==> Ciclos o bucles (while).
// 20 ==> Ciclos o bucles (do while).
// 21 ==> Ciclos o bucles (for).

#include <iostream>

using namespace std;

main (){

  cout << "----------Video 16----------\n";
  
  int edad;
  cout<<"Ingrese su edad para el registro (solo personas de 18 a 25 años): ";
  cin>>edad;
  
  if (edad >= 18 && edad <= 25){
      cout<<"Registro*";
  }
    else{
      cout<<"Usted no tiene la edad permitida.";
  }
  
  cout << "\n\n----------Video 17----------\n";
  
    // Cambiar un número entero con el mismo valor pero en romanos.
    // Mostrar los meses del año, pidiéndole al usuario un número entre (1-12), y mostrar el mes al que corresponde.
  
  cout << "\n\n----------Video 18----------\n";
  
    // Hacer un programa que simule un cajero automático con un saldo inicial de 1000 Dólares.
  
  cout << "\n\n----------Video 19----------\n";
  
  /*
    while(condicion){
     conjunto de instrucciones;
    }
  */
  
  int vidas;
  vidas = 3;
  
    while(vidas > 0){
        cout<<"Acabas de pereder una vida, ahora tienes ";
        cout<<vidas;
        cout<<" vida/s.\n";
        vidas--;
    }
  
  cout << "\n----------Video 20----------\n";
  
  /*
    do{
        conjunto de instrucciones;
    } while ();
  */

    int lifes;
    lifes = 3;
    
    do{
        cout<<"Acabas de pereder una vida, ahora tienes ";
        cout<<lifes;
        cout<<" vida/s.\n";
        lifes--;
    } while (lifes > 0);
    
    cout << "----------Video 21----------\n";
  
  /*
    for(condicion inicial; hasta cuando se ejecuta; modificaion de la variable de inicion){
        instrucciones;
    }
  */
  
  int i;
  for(i=1; i<=5; i++){
    cout<<i;
    cout<<"\n";
  }

  return 0;
}
