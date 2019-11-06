#include <iostream>
#include <vector>
using namespace std;
#include <stdlib.h> //import rand
#include <time.h>
#define n 10 


class Estado
{
public:
  int Matriz[n][n]={{},{}};//Definicion del objeto
  int Copia[n][n]={{},{}}; //Copia de respaldo de la matriz para las iteraciones con el fin 

  //Metodos con las reglas
  int Regla1(int, int);
  int Regla2(int, int);
  int Regla3(int, int);
  int Regla4(int, int);
  int Regla5(int, int);
  int Regla6(int, int);
  int Regla7(int, int);
  int Regla8(int, int);

} e;//Creacion del primero Objeto



int Init() //Funcion Para dar los valores iniciales a la matriz
{
  srand (time(NULL)); //inicializacion de la semilla
    for (int i=0; i<n ; i++)
      {
	for (int j=0; j<n ; j++)
	  {
	    e.Matriz[i][j]= rand() % 3;//inicializacion aleatoria de los valores de la matriz 0 1 o 2
	    cout<<" " << e.Matriz[i][j];
	  }
	cout<< endl;
      }
  
}

int* Vecindad(int i, int j) //Retorna el estado de la vecindad, es decir, de cada uno de los vecinos de la variable que estamos estudiando, vale la pena aclarar que para este juego no se consideraron los bordes, es decir, los bordes no tienen vecinos.
{
  static int Vecinos[8]={e.Matriz[i-1][j-1],e.Matriz[i-1][j],e.Matriz[i-1][j+1],e.Matriz[i][j-1],e.Matriz[i][j+1],e.Matriz[i+1][j-1],e.Matriz[i+1][j],e.Matriz[i+1][j+1]};
  //cout << Vecinos[0] <<Vecinos[1] <<Vecinos[2]<<Vecinos[3] <<Vecinos[4] <<Vecinos[5] <<Vecinos[6] <<Vecinos[7] <<endl;
  return Vecinos;//Retorna un array con el estado de los vecinos del elemento ij
}


//Definicion de las Reglas
//Regla 1
int Estado::Regla1(int l, int m)
{
  if (e.Matriz[l][m]==0){int k=0,b=0;for(int h=0;h<8;h++)
      {if(Vecindad(l,m)[h]==1){k=k+1;} //Contador para saber cuantos 1 hay en el vecindario
      if(Vecindad(l,m)[h]==0){b=b+1;}  //Contador para saber cuantos 0 hay en el vecindario
      if(k==3 and b>1 ){e.Copia[l][m]=1;} //Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
      else {e.Copia[l][m]=0;}}} // Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion
  else {e.Copia[l][m];}} // Escribe en la copia el valor que tenia inicialmente el estado

//Regla 2

int Estado::Regla2(int l, int m)
{
  if (e.Matriz[l][m]==0){int k=0,b=0;for(int h=0;h<8;h++)
    {if(Vecindad(l,m)[h]==2){k=k+1;}//Contador para saber cuantos 2 hay en el vecindario
    if(Vecindad(l,m)[h]==1){b=b+1;}//Contador para saber cuantos 1 hay en el vecindario
    if(k==4 and b>0 ){e.Copia[l][m]=2;} //Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
    else {e.Copia[l][m];}}} // Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion
  else { e.Copia[l][m];}} // Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion

//Regla 3
int Estado::Regla3(int l, int m)
{
  if (e.Matriz[l][m]==1){int k=0;for(int h=0;h<8;h++)
     {if(Vecindad(l,m)[h]==1){k=k+1;} //Contador para saber cuantos 1 hay en el vecindario
      if(k==2 or k==3 ){e.Copia[l][m]=1;} //Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
      else{e.Copia[l][m]=rand() % (0,3);} //En caso de no cumplirse la condicion se cambia el estado de la variable
      }}
  else { e.Copia[l][m];}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion

//Regla 4
int Estado::Regla4(int l, int m)
{
  if (e.Matriz[l][m]==2){int k=0;for(int h=0;h<8;h++)
     {if(Vecindad(l,m)[h]==2){k=k+1;} //Contador para saber cuantos 2 hay en el vecindario
      if(k==2 or k==3 ){e.Copia[l][m]=2;}//Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
      else {e.Copia[l][m]=rand() % (0,2);}}}//En caso de no cumplirse la condicion se cambia el estado de la variable
  else { e.Copia[l][m];}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion

//Regla 5
int Estado::Regla5(int l, int m)
{
  if (e.Matriz[l][m]==1){int k=0,b=0;for(int h=0;h<8;h++)
     {if(Vecindad(l,m)[h]==1){k=k+1;} //Contador para saber cuantos 1 hay en el vecindario
      if(Vecindad(l,m)[h]==2){b=b+1;} //Contador para saber cuantos 2 hay en el vecindario
      if(k<2 & b>3 ){e.Copia[l][m]=2;}//Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
      else {e.Copia[l][m]=1;}}}//En caso de no cumplirse la condicion permanece invariante el estado de la variable y es puesto asi en la copia
  else { e.Copia[l][m];}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion

//Regla 6
int Estado::Regla6(int l, int m)
{
  if (e.Matriz[l][m]==2){int k=0, b=0;for(int h=0;h<8;h++)
     {if(Vecindad(l,m)[h]==1){k=k+1;}//Contador para saber cuantos 1 hay en el vecindario
      if(Vecindad(l,m)[h]==2){b=b+1;}//Contador para saber cuantos 2 hay en el vecindario
      if(k<4 or k>5){e.Copia[l][m]=2;}//Si se cumple la condicion permanece igual el estado
      else if((k==4 or k==5) & b<2 ){e.Copia[l][m]=1;}//Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
       else {e.Copia[l][m]=2;}}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion
  else {e.Copia[l][m];}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion

//Regla 7
int Estado::Regla7(int l, int m)
{
  if (e.Matriz[l][m]==1){int b=0;for(int h=0;h<8;h++)
     {if(Vecindad(l,m)[h]==1){b=b+1;}//Contador para saber cuantos 1 hay en el vecindario
      if( b>4 ){e.Copia[l][m]=0;}//Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
      else {e.Copia[l][m]=2;}}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion
  else { e.Copia[l][m];}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion

//Regla 8
int Estado::Regla8(int l, int m)
{
  if (e.Matriz[l][m]==2){int b=0;for(int h=0;h<8;h++)
     {if(Vecindad(l,m)[h]==2){b=b+1;}//Contador para saber cuantos 2 hay en el vecindario
      if( b==5 ){e.Copia[l][m]=0;}//Si se cumple la condicion se cambia el valor estipulado en la copia de la matriz
      else {e.Copia[l][m]=2;}}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion
  else { e.Copia[l][m];}}// Escribe en la copia el valor que tenia inicialmente el estado en caso de no cumplir la condicion


  int main()
  {
   
    cout<<"Ingrese la dimension n de la matriz"<<endl;
    int m;
    cin >> m;
    #define n m
    //inicio del ciclo
    cout<<"Condiciones Iniciales:"<<endl;
    Init(); //Funcion que fija las condiciones iniciales
    for(int t=0;t<1000;t++){//numero de iteraciones 1000
    for (int p=1;p<n-1;p++)
      {for (int q=1;q<n-1;q++){
	  
	  e.Copia[p][q]=e.Matriz[p][q]; //Copiamos el estado en una matriz auxiliar con el fin de no sobreescribir los datos y que la modificacion de una regla no afecte la evaluacion de la siguiente regla
	  //Evaluacion de las reglas
	  e.Regla1(p,q);
	  e.Regla2(p,q);
	  e.Regla3(p,q);
	  e.Regla4(p,q);
	  e.Regla5(p,q);
	  e.Regla6(p,q);
	  e.Regla7(p,q);
	  e.Regla8(p,q);

	  e.Matriz[p][q]=e.Copia[p][q]; //Redefinimos el estado como las modificaciones hechas por las reglas y actualizamos su valor con el fin de evolucionar el sistema
	  
	}

	
      }
    cout<<"-----------------------"<<endl; 
    for (int i=0; i<n ; i++)
      {
	for (int j=0; j<n ; j++)
	  {
	    cout<<" " << e.Matriz[i][j]; // Output de la salida de la matriz en cada paso de tiempo
	  }
	cout<< endl;}
	
      }

    return 0;


  }
