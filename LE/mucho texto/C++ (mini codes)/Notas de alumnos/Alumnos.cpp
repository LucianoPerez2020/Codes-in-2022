#include <iostream>

using namespace std;

int main(){

   int n, nota;
   int max = 0;
   int cont = 0;

   do{
      cout<<"\nIngrese la cantidad de alumnos: ";
      cin>>n;
   
      if(n <= 1){
         cout<<"Tiene que haber por lo menos dos alumnos."<<endl;
      }
   }while(n < 2); //Mientras n sea mas chico que 2 cumplime esto.

   for(int i = 0; i < n; ++i){

      do{
         cout<<"\nNota #"<<i<<": ";
         cin>>nota;
         
         if(nota < 0 || nota > 20){
            cout<<"La nota tiene que ser >= 0 y <= 20"<<endl;
         }
      }while(nota < 0 || nota > 20);
      
      if(nota >= max){

         if(nota > max){
            max = nota;
            cont = 1;
         }
         else{
            ++cont;
         }

      }
   }
   
   cout<<"La maxima nota es: "<<max<<endl;
   cout<<"Cantidad de alumnos que la obtuvieron: "<<cont<<endl;

	return 0;
}