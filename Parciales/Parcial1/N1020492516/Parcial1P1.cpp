/* 
Juego de la vida de 2 sistemas biologicos
*/
#include <unistd.h>
#include <iostream>
#include <vector>
using namespace std;

//------------ La clase ------------//

class LifeGame 
{
public:  
	int N; // N Declara la dimensión de la matriz
	vector<vector<int> > Matrix; //Declara la matriz como un vector de vectores.

	//Atributos de la clase, se explican en sus definiciones
	void set_dim(int);
	vector<int> vecinos(int, int);
	void Evolution(int);

};

//-------------- Atributos de la clase --------------//

void LifeGame::set_dim(int n){  //Fija la dimensión de la matriz de evolución y la matriz nxn
/*
Aquí definimos la matriz inicial con 2 dimensiones más, es decir N=n+2, esto para ahorrar bastante código pues no tendremos el problema de tener esquinas y bordes con menos vecinos donde habrá que poner más condiciones. Ahora bien, para no incumplir ninguna regla, definimos todo el borde con números desconocido para nuestro universo de ceros, unos y dos, por ejemplo 5. Es decir, tomese el 5 como la barrera, algo que no tiene reglas, algo que está fuera del universo, nuestra nota del parcial reflejada en una maravillosa estrategia para ahorrar cómputo. 
Después de esto, graficamos y trabajamos sobre la matriz menor N-2 x N-2.
*/
	N = n+2;
	Matrix.resize(n+2, vector<int>(n+2));

	// Definiendo contornos para que no afecten las reglas:
	for (int i=0; i<N; i++){
		Matrix[0][i] = 5; Matrix[N-1][i] = 5; Matrix[i][0] = 5; Matrix[i][N-1] = 5; 
	}
	
	// Aqui se asignan las condiciones iniciales: Recordemos que las posiciones de los bordes NO se deben modificar, o se incumplirá la regla 1
	
	Matrix[2][1] = 0; Matrix[2][2] = 1; Matrix[2][3] = 1; Matrix[2][4] = 1; Matrix[2][5] = 2;
}

vector<int> LifeGame::vecinos(int i ,int j){ //Funcion para analizar vecinos:
/* Esta función recibe la posicion i,j y devuelve un vector cud (ceros unos dos) que tiene como elemento cero cud[0] el conteo de los vecinos que son cero, cud[1] cuántos vecinos son 1 y cud[2] cuántos son 2 */
 
  	vector<int> cud(3);  //definimos vector con los tres elementos, cero uno y dos.
   
  	for (int i1=i-1;i1<i+2;i1++){        //Estos dos for correran sobre los 9 elementos alrededor del i,j. Los vecinos
	  for (int j1=j-1;j1<j+2;j1++){      //de i-1 hasta <i+2 y lo mismo para j, y el if nos exceptua el elemento i,j
	    if (i1 != i or j1 != j){         //este if es para exeptuar el elemento i,j.
    		
	      if (Matrix[i1][j1] == 0){cud[0]+=1;}             //Si hay algun cero, sumele 1 al contador cud[0]
	      else if (Matrix[i1][j1] == 1){cud[1]+=1;}  //Si hay algun uno, sumele 1 al contador cud[1]
	      else if (Matrix[i1][j1] == 2){cud[2]+=1;}  //Si hay algun dos, sumele 1 al contador cud[2]
	    } //Cierre del if
	  }   //cierre del segundo for
	}     //cierre del primer for
	return cud; //que nos retorne el vector contador cud
}

void LifeGame::Evolution(int t) //Evolución de la matriz del juego de la vida
{
  vector<int> num,numcel;  /*num nos da el contador de 0's, 1's y 2's de cada celda. numcel es para mostrar en pantalla los vecinos de una celda especifica de nuestro interés e irla actualizando con la matriz.*/

  while ( t>0){ //t es el numero de pasos. Los pasos van de 1000 a cero.
    vector<vector<int> > Pseudo(N, vector<int>(N)); /*Aqui definimos una pseudomatriz para ir actualizando bajo las reglas
						      Establecidas. Esta matriz también debe tener la barrera de cincos */
    for (int i=0; i<N; i++){ //Contorno o barrera
      Pseudo[0][i] = 5; Pseudo[N-1][i] = 5; Pseudo[i][0] = 5; Pseudo[i][N-1] = 5;
    }

    for (int i=1; i<N-1; i++){//Del primer elemento DENTRO del contorno de filas, hasta el último dentro también.
      for (int j=1; j<N-1; j++){//Este corre sobre las columnas
	num = vecinos(i, j);//Corre sobre cada una de las celdas.
	numcel = vecinos(1,1);//Esta es nuestra celda de interés.

	if ( Matrix[i][j] == 0){ //Reglas si en la posicion i,j hay un 0:
	  if ( num[1] == 3 and num[0] >= 2 ) { Pseudo[i][j] = 1; }     //Regla 1
	  else if ( num[2]==4 and num[1] >= 1  ){ Pseudo[i][j] = 2; }   //Regla 2
	}
	
	else if ( Matrix[i][j] == 1 ){//Reglas si en la posicion i,j hay un 1:
	    if ( num[1]==2 or num[1]==3 ) { Pseudo[i][j] = 1; }         //Regla 3
	    else if (num[2] >= 4 and num[1] <= 1 ){ Pseudo[i][j] = 2; }//Regla 5
	    else if ( num[1] >= 5 ){ Pseudo[i][j] = 0; }                //Regla 7
				}
	
	else if ( Matrix[i][j] == 2 ){//Reglas si en la posicion i,j hay un 2:  
	  if ( num[2]==2 or num[2]==3 ) { Pseudo[i][j] = 2; }                          //Relga 4
	  else if ( (num[1] == 4 or num[1] == 5) and num[2] <= 2 ){ Pseudo[i][j] = 1; }//Regla 6
	  else if ( num[2] == 5 ){ Pseudo[i][j] = 0; }                                 //Regla 8
				}
	
	//----------Gráficar--------//
	
	cout <<" | " << Matrix[i][j]; /*Vamos a imprimir en terminal un | y después el número que hay en i,j sin cerrar la linea, notese que esto sigue dentro de el for de las filas*/
      }
      cout<<endl;//Cerramos las filas fuera del for
    }
    Matrix = Pseudo; //Actualizamos la matriz
    t-=1; //restamos un paso
    cout<< " " << endl;//Esto es para dejar una linea de espacio
    cout<<"Vecinos de casilla 1,1: " << "Ceros: " << numcel[0] <<" Unos: "<<numcel[1]<<" Dos: "<<numcel[2]<<endl;
    /*Mostramos los vecinos de nuestra celda de interés*/
    usleep(1500000);//Esperar un tiempo de 0.5 segundos
    system("clear");//Borrar lo que hay en panalla. Limpiar el sistema
    usleep(200000);//Esperar un tiempo de 0.2 segundos para ver las actualizaciones de matriz
  }
}

//-------------- El viejo main ---------------//

int main(){
  LifeGame Juego1;   //Llamamos juego 1
  int n, steps;      //definimos los enteros de la dimension y los pasos
  cout << "Porfavor ingrese un numero entero para las dimensiones de la matriz nxn" << endl;
  cin >> n;          //que reciba el n ingresado por el usuario
  Juego1.set_dim(n); //llamamos set dim para organizar las dimensiones
  steps = 1000; //1000 pasos que nos pide el ejercicio. Si las condiciones no son adecuadas, reducir estos pasos.
  Juego1.Evolution(steps); //llamamos evolution
    
  return 0;
}
//Listo.
