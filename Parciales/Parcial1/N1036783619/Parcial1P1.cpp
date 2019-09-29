/*#include <iostream> 
#include <vector> 


#include <cstdlib> 
#include <ctime> */

#include <iostream>//libreria base
#include <cstdlib>// librerias para generar numeros aleateorios
#include <vector>// libreria para trabajar con vectores
#include <unistd.h>// necesario para el funionamiento de la funcio usleep()
#include<ctime>// incializa los numeros aleateorios
#include<fstream>

using namespace std;


class Estado // Definos estado de un sistema en un tiempo estatico t
{
public:
  int fil; // definimos el numero de filas
  int col; // definimos el numero de columnas
  int vecinos1; // definimos el numero de vecinos de la especie 1 para una celula 
  int vecinos2; // definimos el numero de vecinos de la especei 2 para una celula 
  int vecinos0; // definimos
  int vivos1; // contiene la informacion de cuantos vivos hay por ciclo de la especie 1
  int vivos2; // contiene la informacion de cuantos vivos hay por ciclo de la especie 2
  vector<vector<int> > estado; // definimos la matriz que contiene la informacion de la evulucion  

  Estado(int f, int c); // funcion que produce las condiciones iniciales
  void dibujar(); // funcion que permite imprimir en pantalla la evoluvion del estado
  int analizarVecinos1(int posf, int posc); // funcion que evalua las conciones en la localidad de cada celula para encontrar celulas de la especie 1
  int analizarVecinos2(int posf, int posc); // funcion que evalua las conciones en la localidad de cada celula para encontrar celulas de la especie 2  
  //int analizarVecinos0(int posf, int posc); // funcion que evalua las conciones en la localidad de cada celula para encontrar celulas muertas
  void ciclo(); // esta funcion calcula la evolucion temporal del estado
};

Estado::Estado(int f, int c) // Esta funcion sirve para pintar el mapa por primera vez y darle valores iniciales aleatorios a cada entrada
{

  vivos1 = 0; // indicamos que no hay seres vivos de la especie 1 en la primera instancia
  vivos2 = 0; // indicamos  que  no hay serser vivos de la especie 2 en la primera instancia
  fil = f; // ingresamos el numero de filas
  col = c; // ingresamos el numero de columnas
  estado.resize(fil); // redefinimos el numero de filas 

  for(int i=0; i<estado.size(); i++) // inicializamos el cambio del numero de columnas, a partir del nuevo numero de filas
  {
    estado[i].resize(col); // redefinimos el numero de columnas 
  }

  for(int f=0; f<fil; f++) // iniciamos la lectura de la fila f
  {
    for(int c=0; c<col; c++) // iniciamos la lectura de los elementos de la fila f, corremos sobre las columnas en la fila f
    {
      estado[f][c] = rand()%3; // generamos entradas de la matriz con numeros aleatorios entre 0 y 2
      if (estado[f][c] == 1) // buscamos seres vivos de la especie 1
        vivos1++; // esta linea cuenta el numero de seres vivos de la especie 1
      if (estado[f][c] == 2) // buscamos serer vivos de la especie 2
        vivos2++; // esta linea cuenta el numero de seres vivos de la especie 2
    }
  }
}

void Estado::dibujar() // esta funcion permite mostrar en pantalla el estado de forma grafica
{
  for(int f=0; f<fil; f++) // iniciamos la lectura de las filas, para su representacion grafica
  {
    for(int c=0; c<col; c++) // iniciamos la lectura de los elementos de las filas, para su representacion grafica
    {
      if(estado[f][c] == 1) // seleccionamos celulas vivas de la especie 1
        cout << "o"; // representa celulas vivas de la especie 1
      else if(estado[f][c] == 2) // seleccionamos celulas vivas de la especie 2
        cout << "*"; // representa celulas vivas de la especie 2
      else  // buscamos espacios sin celulas vivas
        cout << "."; // representa celulas muertas
    }
    cout << "\n"; // terminamos la lectura y la escritura de la fila
  }
}

int Estado::analizarVecinos1(int posf, int posc) // cuenta el numero de vecinos vivos de la especie 1 que tiene alrededor
{
  vecinos1 = 0; // contador de celulas de la especie 1


// ubicandonos en una zona local correspondiente a una cuadricula 3x3, estudiamos el ambiente de una celula en el centro 

  if(posf-1 >=0 and posc-1 >=0) // 1. cuadro superior izquierdo de la cuadricula 
    if(estado[posf-1][posc-1] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1


  if(posf-1 >=0) // 2. cuadro superior central de la cuadricula 
    if(estado[posf-1][posc] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1
    
  if(posf-1 >= 0 and posc+1 <= col-1) // 3. cuadro superior derecho de la cuadricula 
    if(estado[posf-1][posc+1] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1
    
  if(posc-1 >=0) // 4. cuadro medio izquierdo 
    if(estado[posf][posc-1] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1
    
  if(posf+1 <= col-1) // 5. cuadro medio derecho
    if(estado[posf][posc+1] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1
    
  if(posf+1 <= fil-1 and posc-1 >= 0) // 6. cuadro inferior izquierdo
    if(estado[posf+1][posc-1] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1
   

  if(posf+1 <= fil-1) // 7. cuadro inferior central
    if(estado[posf+1][posc] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1
    

  if(posf+1 <= fil-1 and posc+1 <= col-1) // 8. cuadro inferior derecho
    if(estado[posf+1][posc+1] == 1) // verificamos si es una celula de la especie 1
      vecinos1++; // aumentamos el numero de celulas de la especie 1
    
  return vecinos1; // retorna el numero total de celulas de la especie 1 alrededor de nuestra celula

}

int Estado::analizarVecinos2(int posf, int posc) // cuenta el numero de vecinos vivos de la especie 2 que tiene al rededor
{
  vecinos2 = 0; // contador de celulas de la especie 2


// ubicandonos en una zona local correspondiente a una cuadricula 3x3, estudiamos el ambiente de una celula en el centro 

  if(posf-1 >=0 and posc-1 >=0) // 1. cuadro superior izquierdo de la cuadricula 
    if(estado[posf-1][posc-1] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2


  if(posf-1 >=0) // 2. cuadro superior central de la cuadricula 
    if(estado[posf-1][posc] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2
    
  if(posf-1 >= 0 and posc+1 <= col-1) // 3. cuadro superior derecho de la cuadricula 
    if(estado[posf-1][posc+1] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2
    
  if(posc-1 >=0) // 4. cuadro medio izquierdo 
    if(estado[posf][posc-1] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2
    
  if(posf+1 <= col-1) // 5. cuadro medio derecho
    if(estado[posf][posc+1] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2
    
  if(posf+1 <= fil-1 and posc-1 >= 0) // 6. cuadro inferior izquierdo
    if(estado[posf+1][posc-1] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2
   

  if(posf+1 <= fil-1) // 7. cuadro inferior central
    if(estado[posf+1][posc] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2
    

  if(posf+1 <= fil-1 and posc+1 <= col-1) // 8. cuadro inferior derecho
    if(estado[posf+1][posc+1] == 2) // verificamos si es una celula de la especie 2
      vecinos2++; // aumentamos el numero de celulas de la especie 2
   
  return vecinos2; // retorna el numero total de celulas de la especie 2 que rodean a nuestra celula

}

void Estado::ciclo() // Esta funcion calcula el valor de cada entrada de la matriz para el paso siguiente de tiempo
{  
  vector<vector<int> > nueva_conf = estado; // Guarda la nueva forma del estado
  vivos1 = 0; // se reinicia el contador de vivos de la especie 1 para recalcularse
  vivos2 = 0; // se reinicia el contador de vivos de la especie 2 para recalcularse

  for (int f=0; f<fil; f++) // se inicia la lectura de las filas
    {
      for(int c=0; c<col; c++) // se leen los elementos de las filas, al correr sobre las columnas
        {
	  int n_vecinos1 = analizarVecinos1(f, c); // calculamos el numero de vecinos de la especie 1 al rededor de (f,c)
	  int n_vecinos2 = analizarVecinos2(f, c); // calculamos el numero de vecinos de la especie 2 al rededor de (f,c)
	  int vecinos0 = 8-(vecinos1 + vecinos2); //calculamos el numero de vecinos muertos al rededor de (f,c)

	// (a) Si un elemento tiene como valor 0 y tiene 3 vecinos con valor 1 y dos o más vecinos con valor 0, transforma su valor a 1.
    // (b) Si un elemento tiene como valor 0 y tiene 4 vecinos con valor 2 y uno o más vecinos con valor 1, transforma su valor a 2.
    if(estado[f][c] == 0) // se evalua el entorno cuando la celula esta muerta
            {
	      if(vecinos1 == 3 and vecinos0 >= 2) // aplicamos (a)
		    nueva_conf[f][c] = 1;// valor en para el nuevo estado del sistema
	      else if(vecinos2 == 4 and vecinos1 >= 1) // aplicamos (b)
		    nueva_conf[f][c] = 2;//  valor en para el nuevo estado del sistema
	      else 
		    nueva_conf[f][c] = 0; // sino es un una celula muerta
	           }
    // (c) Si un elemento tiene como valor 1 y tiene 2 o 3 vecinos con valor 1, conserva su valor de 1.
    // (d) Si un elemento tiene como valor 1 y tiene al menos 5 vecinos valor 1, transforma su valor a 0.
    // (e) Si un elemento tiene como valor 1 y tiene al menos 4 vecinos con valor 2 y máximo un vecino 1 transforma su valor a 2.         
	  if (estado[f][c] == 1)// se evalua el entorno cuando la celula es la especie 1
            { 
          vivos1++; // aumenta el numero de  celulas vivas de la especie 1
	      if(vecinos1== 2 || vecinos1== 3)//aplicamos (c)
        nueva_conf[f][c] = 1;// valor para el nuevo estado del sistema
	      else if(vecinos2 >= 4 and vecinos1 <= 1)// aplicamos (e)
		    nueva_conf[f][c] = 2; // valor para el nuevo estado del sistema
	      else if(vecinos1 >=5)// aplicamos (d)
		    nueva_conf[f][c] = 0;// valor para el nuevo estado del sistema
	      else 
		    nueva_conf[f][c] = 0;// de lo contrario se toma como una celula muerta
            }

    // (f) Si un elemento tiene como valor 2 y tiene 2 o 3 vecinos con valor 2, conserva su valor de 2.
    // (g) Si un elemento tiene como valor 2 y tiene 4 o 5 vecinos con valor 1 y máximo un vecino 2 transforma su valor a 1.
    // (h) Si un elemento tiene como valor 2 y tiene 5 vecinos valor 2, transforma su valor a 0.
  
    if (estado[f][c] == 2)// se evalua el entorno cuando la celula es la especie 1
	       {
	 vivos2++; // aumenta el numero de celulas de la especie 2 
	      if (vecinos2 == 2 || vecinos2 == 3)// se aplica (f)
		nueva_conf[f][c] = 2;// valor para el nuevo estado del sistema
	      else if(vecinos1 == 4 || vecinos1 == 5 and vecinos2 <= 1) // seaplica (g)
		nueva_conf[f][c] = 1;// valor para el nuevo estado del sistema
	      else if(vecinos2 == 5)// se aplica (h)
		nueva_conf[f][c] = 0;// valor para el nuevo estado del sistema
	      else 
		nueva_conf[f][c] = 0;//de lo contrario se toma como celula muerta
		
	       }
      }
    } 
  estado = nueva_conf; // se guardan las nuevas condiciones iniciales
}


int main()
{
 int n; // representa las dimensiones de la matriz nxn

 cout << "ingrese el tamaño de la matriz: \n"; // le pide al usuario 3que ingrese manualmente el tamaño de la matriz
 cin >> n; // se ingresa de forma manual el valor de n



 srand(time(NULL)); // iniciamos el generador de evolucion temporal
 Estado estado(n, n); //dfinimos las dimensiones de nuestra matriz


 while(1) 
  {
    estado.dibujar(); //dibujamos el estado actual 
    usleep(100000); // damos un delay al paso del sistema
    system("clear"); //
    estado.ciclo(); // aplicamos la evolucion del sistema
  }

  return 0;

}
