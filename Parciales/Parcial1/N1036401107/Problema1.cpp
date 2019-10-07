/* 
Parcial 1
Elizabeth Jiménez Gómez 1036401107
Samuel Quitian Gallego 1152222545
*/


#include <iostream> //Se incluye libreria para entrada y salida de datos
#include <vector> //Se incluye libreria para manejo de vectores
#include <unistd.h> // Se incluye libreria que define constantes, tipos y funciones.
#include <cstdlib>  // Se incluye libreria estandar de propósito general de C. 
using namespace std; //Esta linea sirve para no tener que llamar cada vez a iostream

class Matriz   //Defino la clase Matriz, que va a ser la encargada de generar la matriz nxn.
{
public:         // Definimos las cantidades de la clase, que en este caso son públicas para tener acceso a ellas desde cualquier otro lugar.
  int filas;    // Definimos las filas de la matriz como un número entero.
  int columnas; // Definimos las columnas de la matriz como un número entero. 
  int vecinos0; // Definimos los vecinos que tienen valor 0.
  int vecinos1; // Definimos los vecinos que tienen valor 1.
  int vecinos2; // Definimos los vecinos que tienen valor 2.
  
  vector<vector<int> > matriz; // Definimos el vector que se va a convertir en la matriz nxn.

  void MkMatriz(int, int);            //Defino la matriz donde sus entradas son f=filas, c=columnas.
  int analizarvecinos0(int posf,int posc);  //Función entera que analiza los vecinos con valor 0 para una posicion (posf,pos)       
  int analizarvecinos1(int posf, int posc); //Función entera que analiza los vecinos con valor 1 para una posicion (posf,posc)
  int analizarvecinos2(int posf, int posc);//Función entera que analiza los vecinos con valor 2 para una posicion (posf,posc)
  void Mostrar();                  //Definimos una función que muestre en pantalla la organización de las células.
  void ciclo();                    //Definimos una función que hace evolucionar el sistema.
};

void Matriz::MkMatriz(int f, int c)  // Creamos una instancia de la clase que forme una matriz de números aleatorios.
{
  filas = f;              // Redefinimos el nombre de las filas.
  columnas = c;           // Redefinimos el nombre de las columnas.
  matriz.resize(filas);   // Al vector que habia creado anteriormente le doy la longitud de las filas de la matriz por lo que ahora tengo
                          // un vector matriz = [x1,x2,...,xn].
  for (int i=0; i<matriz.size(); i++)  // Hacemos un for para agregar las columnas a la matriz.
    {
      matriz[i].resize(columnas);      // Aquí es donde juntamos las columnas con las filas para obtener la matriz nxn
    }

  for (int f=0; f<filas; f++)          // Hacemos un for sobre las filas para variar los posibles valores de las posiciones.
    {
      for (int c=0; c<columnas; c++)   // Hacemos un for sobre las columnas para variar los posibles valores de las posiciones.
	{
	  matriz[f][c] = rand()%3;      //Agrego un valor aleatorio a cada elemento de la matriz, números aleatorios entre 0 y 2.
	}
    }
}

void Matriz::Mostrar()                 // Creamos una instancia de la clase que muestra en pantalla la forma de la matriz
{
  for (int a=0; a<filas; a++)          // Ciclo que recorre las filas.
    {
      for (int b=0; b<columnas; b++)     // Ciclo que recorre las columnas.
	{
	  if (matriz[a][b] == 1)       // Si esta viva una célula de la especie 1
	    {
	      cout << "0";            // Muestre en pantalla "*"
	    }
	  else if (matriz[a][b] == 2)       // Si esta viva una célula de la especie 2
	    {
	      cout << " # ";            // Muestre en pantalla "#"
	    }
	  else                         // Si la célula esta muerta
	    {
	      cout << " - ";             // Muestre en pantalla "-"
	    }
	}
      cout << endl;                    // Deje un espacio a la hora de mostrar en pantalla.
    }
}

// Hasta aquí hemos definido la clase que contiene la matriz nxn. En lo que sigue definiremos los métodos que la hacen evolucionar
// de acuerdo a las reglas estipuladas.

int Matriz::analizarvecinos0(int posf,int posc)         // Función que analiza si los vecinos tienen valor 0                                
{
  vecinos0 = 0;               // Para inicializar los vecinos que tengan valor 0.                                                              
  if(posf-1 >=0 and posc-1 >= 0) //Se mira si el vecino que esta en la posicion (posf-1,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc-1] == 0) //Se ve si el vecino en esa pocision tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
  if(posf-1 >= 0) //Se mira si el vecino que esta en la posición (posf-1,posc) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc] == 0) //Se ve si el vecino en esa pocisión tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
  if(posf-1 >= 0 and posc+1 <= columnas-1)//Se mira si el vecino que esta en la posición (posf-1,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc+1] == 0) //Se ve si el vecino en esa pocisión tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
  if(posc-1 >= 0)//Se mira si el vecino que esta en la posición (posf,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf][posc-1] == 0)  //Se ve si el vecino en esa pocision tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
  if(posc+1 <= columnas -1)//Se mira si el vecino que esta en la posicion (posf,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf][posc+1] == 0) //Se ve si el vecino en esa pocision tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
   if(posf+1 <= filas-1 and posc-1 >= 0)//Se mira si el vecino que esta en la posicion (posf+1,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc-1] == 0) //Se ve si el vecino en esa pocision tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
  if(posf+1 <= filas-1)//Se mira si el vecino que esta en la posicion (posf+1,posc) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc] == 0) //Se ve si el vecino en esa pocision tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
  if(posf+1 <= filas-1 and posc+1 <= columnas-1)//Se mira si el vecino que esta en la posicion (posf+1,pos+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc+1] == 0) //Se ve si el vecino en esa pocision tiene valor 0
        {
          vecinos0++; //Si tiene valor de 0 se añade uno al contador
        }
    }
  return vecinos0;        //Devielve en número de vecinos con valor 0.
}


int Matriz::analizarvecinos1(int posf,int posc)         // Funcion entera que analiza si los vecinos tienen valor 1
{
  vecinos1 = 0;               // Para inicializar los vecinos que tengan valor 1.
  if(posf-1 >=0 and posc-1 >= 0)//Se mira si el vecino que esta en la posicion (posf-1,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc-1] == 1)//Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;    // Si tiene valor de 1 se añade uno al contador.
	}
    }
  if(posf-1 >= 0)//Se mira si el vecino que esta en la posicion (posf-1,posc) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc] == 1) //Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;//Si tiene valor de 1 se añade uno al contador
	}
    }
  if(posf-1 >= 0 and posc+1 <= columnas-1)//Se mira si el vecino que esta en la posicion (posf-1,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc+1] == 1)//Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;//Si tiene valor de 1 se añade uno al contador
	}
    }
  if(posc-1 >= 0)//Se mira si el vecino que esta en la posicion (posf,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf][posc-1] == 1)//Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;//Si tiene valor de 1 se añade uno al contador
	}
    }
  if(posc+1 <= columnas -1)//Se mira si el vecino que esta en la posicion (posf,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf][posc+1] == 1)//Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;//Si tiene valor de 1 se añade uno al contador
	}
    }
  if(posf+1 <= filas-1 and posc-1 >= 0)//Se mira si el vecino que esta en la posicion (posf+1,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc-1] == 1)//Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;//Si tiene valor de 1 se añade uno al contador
	}
    }
  if(posf+1 <= filas-1)//Se mira si el vecino que esta en la posicion (posf+1,posc) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc] == 1)//Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;//Si tiene valor de 1 se añade uno al contador
	}
    }
  if(posf+1 <= filas-1 and posc+1 <= columnas-1)//Se mira si el vecino que esta en la posicion (posf+1,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc+1] == 1)//Se ve si el vecino en esa pocision tiene valor 1
	{
	  vecinos1++;//Si tiene valor de 1 se añade uno al contador
	}
    }
  return vecinos1;   // Devielve el número de vecinos con valor 1.
}

int Matriz::analizarvecinos2(int posf, int posc) //Se define una funcion entera que analiza si los vecinos tienen valor 2 
{
  vecinos2 = 0;               // Para inicializar los vecinos que tengan valor 2.                                                              
  if(posf-1 >=0  and posc-1 >= 0)//Se mira si el vecino que esta en la posicion (posf-1,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc-1] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
        }
    }
  if(posf-1 >= 0)//Se mira si el vecino que esta en la posicion (posf-1,posc) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
        }
    }
  if(posf-1 >= 0 and posc+1 <= columnas-1)//Se mira si el vecino que esta en la posicion (posf-1,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf-1][posc+1] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
	}
    }
  if(posc-1 >= 0)//Se mira si el vecino que esta en la posicion (posf,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf][posc-1] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
        }
    }
  if(posc+1 <= columnas -1)//Se mira si el vecino que esta en la posicion (posf,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf][posc+1] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
        }
    }
  if(posf+1 <= filas-1 and posc-1 >= 0)//Se mira si el vecino que esta en la posicion (posf+1,posc-1) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc-1] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
        }
    }
  if(posf+1 <= filas-1)//Se mira si el vecino que esta en la posicion (posf+1,posc) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
        }
    }
  if(posf+1 <= filas-1 and posc+1 <= columnas-1)//Se mira si el vecino que esta en la posicion (posf+1,posc+1) esta dentro de la matriz (existe)
    {
      if(matriz[posf+1][posc+1] == 2)//Se ve si el vecino en esa pocision tiene valor 2
        {
          vecinos2++;//Si tiene valor de 2 se añade uno al contador
        }
    }
  return vecinos2;   // Devuelve el número de vecinos con valor 2.

}

void Matriz::ciclo()       // Aquí definimos las reglas estipuladas.
{
  vector <vector<int> > nuevo (matriz);    // Definimos una nueva matriz para que pueda evolucionar.
    for (int i=0; i<filas; i++)           // Ciclo que recorre todas las filas.
      {
	for (int j=0; j<columnas; j++)    // Ciclo que recorre todas las columnas.
	  {
	    int n_vecinos0 = analizarvecinos0(i,j);  // Se define los nuevos vecinos con valor 0 llamando la función anterior.
	    int n_vecinos1 = analizarvecinos1(i,j);  // Se define los nuevos vecinos con valor 1 llamando la función anterior.
	    int n_vecinos2 = analizarvecinos2(i,j); // Se define los nuevos vecinos con valor 2 llamando la función anterior.
	    if(matriz[i][j] == 0)               // Elemento con valor 0
	      {
		if(n_vecinos1 == 3 && n_vecinos0 >= 2)  // Condición de que si hay 3 vecinos con valor 1 y 2 o más con valor 0. Regla 1
		  {
		    nuevo[i][j] = 1;                // Su valor cambia a 1.
		  }
		else if(n_vecinos2 == 4 && n_vecinos1 >= 1)  // Condición de que si hay 4 vecinos con valor 2 y 1 o más vecinos con valor 1. Regla 2
		  {
		    nuevo[i][j] = 2;                // Su valor cambia a 2.
		  }
	      }
	    if (matriz[i][j] == 1)                 // Elemento con valor 1.
	      {
		if(n_vecinos1 == 2 || n_vecinos1 == 3) // Condición de que si tiene 2 o 3 vecinos con valor 1
		  {
		    nuevo[i][j] = 1;               // conserve su valor de 1.
		  }
		else   //Si no se cumple alguna condicion anterior pasa a esta
		  {
		    if(n_vecinos2 >=4 and n_vecinos1 <= 1)  // Condición de que si tiene al menos 4 vecinos con valor dos y 1 vecino con valor 1
		      {
			nuevo[i][j] = 2;               // Su valor cambia a 2.
		      }
		    else if(n_vecinos1 >=5)                   // Condición de que si tiene al menos 5 vecinos con valor 1
		      {
			nuevo[i][j] = 0;               // Su valor cambia a 0.
		      }
		  }
	      }
	    if (matriz[i][j] == 2)                 // Elemento con valor 2.
	      {
		if(n_vecinos2 == 2 || n_vecinos2 == 3) // Condición de que si tiene 2 o 3 vecinos con valor 2
		  {
		    nuevo[i][j] = 2;               // Conserve su valor 2.
		  }
		else //Si no se cumple alguna condicion anterior pasa a esta
		  {
		    if(n_vecinos1 == 4 || n_vecinos1 == 5 && n_vecinos2<=1) // Condición de tener 4 o 5 vecinos con valor 1 y uno con valor 2.
		      {
			nuevo[i][j] = 1;               // Su valor cambia a 1.
			
		      }
		    else if(n_vecinos2 == 5)                  // COndición de tener 5 vecinos con valor de 2
		      {
			nuevo[i][j] = 0;               // Su valor cambia a 0
		      }
		  }
	      }
	  }
      }
    matriz = nuevo; //Actualiza la matriz a su nuevo estado 
}


int main()        // Comienza la función principal
{
  srand(time(NULL));  // Hace uso del reloj interno del computador para cambiar el valor inicial para generar una secuancia de nÃºmeros
                      // enteros semi-aleatorios.
  int N ; //Se inicia la variable N que es el tamaño que tendra la matriz
  cout << "Ingrese el tamaño de la matriz : " << endl; //En la pantalla muestra un mensaje pidiendo que ingrese el tamaño de la matriz
 cin >> N; //Se lee el valor ingresado como N 
  
  Matriz A; //Inicia la clase Matriz para la variable A
A.MkMatriz(N,N); // Le da el tamaño a la matriz con el valor que ingresemos.

 int t=0;  // Empezamos el tiempo en 0.
	
   while(t<= 1000)  //Siempre que dibuje la matriz, espera un tiempo, borra y dibuja una nueva configuración.
    {
      A.Mostrar();   // Muestra en pantalla una matriz que consta de "#", "-", "*"
      //usleep(1000000);
        sleep(1);   // Controla el tiempo
      system("clear");  // Limpia una salida para poder mostrar la otra.
      A.ciclo();        // Llamamos la función que le da la evolución a la matriz.
      t++;                // Aumenta el contador de tiempo.
    }

}
