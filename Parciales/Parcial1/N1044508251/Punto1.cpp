/*------------------------------------------------------
Se construyo un codigo que crea una matriz y la llena de forma aleatoria
con tres tipos de estados y muestra su evolucion en pantalla 
------------------------------------------------------*/

//Se importan la librerias 

#include <iostream> //Flujo entrada y saida de datos en patanlla
#include <vector>   //Uso de vectores                    
#include <ctime>    //Se usa para generar diferentes valores aleatorios
#include <unistd.h> //Acceso a controlar el sistema (pantalla)

using namespace std; //Usa los metodos se de la libreria STD sin llamarla

//Se creo la clase Cell que posee diferentes metodos para crear, imprimir y evolucionar el sistema segun ciertas reglas de acuerdo a los estados
class Cell{
  
public: //Determina los atributos que son publicos

  //Atributos
  int n; //Tamaño de la matriz cuadradas
  int iter; //Iteraciones a las que va a ser sometida la matriz

  //Metodos
  std::vector<int> BuildMatriz(int); //Construye la matriz nxn y la llena en posiciones aleatorias los valores 0, 1, 2
  void PrintMatriz(std::vector<int>&, int); //Imprime en pantalla la matriz construida
  std::vector<int> Vecinos(int, int, std::vector<int>&, int); //Metodo que encuentra los vecinos de cada celda
  void Rules(int, int, std::vector<int>&, std::vector<int>&, std::vector<int>&, int); //Reglas que rigen la interaccion entre las especies
  void Evolution(int, int); //Evoluciona el sistema generado aleatoriamente
};

//METODO PARA GENERAR LA MATRIZ 
std::vector<int> Cell::BuildMatriz(int n){ //Metodo de tipo vector de enteros y recibe el tamano de la matriz
  
  std::vector<int> matriz(n*n, 0); //Crea un vector de tamano nxn
  srand(time(0)); //Cambia la generacion de los numeros aleatorias cada vez se que corra el codigo
  for( int i=0; i<matriz.size(); i++){//Ciclo para poner los valores de forma aleatoria
    matriz[i]=rand() % 3; //La funcion rand()%3 genera un numero aleatorio entre 0, 1, 2. Se asigna a cada posicion de la matriz
  }
  
  return matriz; //Devuelve un vector (matriz) con valores de forma aleatoria
}

//METODO PARA IMPRIMIR LA MATRIZ
void Cell::PrintMatriz(std::vector<int>& matriz, int n){//Funcion que no devuelve nada. Recibe un vector y un entero
  for(int i=0; i<n; i++){ //Ciclo para imprimir filas
    for(int j=0; j<n; j++){ //Ciclo para imprimir columnas
      cout << matriz[i*n+j] << " "; //Salida a pantalla con un espacio " " entre valores
    }
    cout<<"\n"; //Salida a pantalla de los saltos de fila (linea)
  }
}

//FUNCION PARA ENCONTRAR VECINDADES
std::vector<int> Vecindad(int ef, int ff, int d, int u, int row, int col, std::vector<int>& matriz, int n, int l){ //Funcion usada en el metodo VECINOS. Recibe primero dos enteros de hasta donde se van a iterar las filas y columnas, dos enteros que las inicializan, la fila, la columna, la matriz, el lado y la cantidad de posiciones del vector de vecinos 
  
  std::vector<int> vec(l); //Crea un vector donde guarda los valores de lo vecinos
  
  int i=0;                //Entero que hace referencia a la posicion para guardar los valores de lso vecinos            
  int e=d;                //d inicializa e para la posicion de la filas e corre para las posiciones -1, 0, 2
  while(e<ef){            //Loop para la evolucion de filas 
    int f=u;              //u inicializa f para la posicion de la filas e corre para las posiciones -1, 0, 2  
    while(f<ff){          //Loop para la evolucion de columnas 
      
      if((row+(e))*n==row*n && (col+(f))==col){ //Condicion para no escribir la celda que se esta analizando
      }
      else{
	vec[i] = matriz[(row+(e))*n+(col+(f))]; //Escribe los valores de los vecinos excepto el propio
	i+=1;                                   //Avanzar la posicion del vector para llenarlo   
      }
      
      f+=1;                                     //Avanzar en la columna
    }
    e+=1;                                       //Avanzar en la fila
    
  }
  
  return vec;  //Devuelve el vector de vecinos
}

//METODO QUE ENCUENTRA LOS VECINOS DE CADA CELDA
std::vector<int> Cell::Vecinos(int row, int col, std::vector<int>& matriz, int n){//Metodo tipo vector de enteros. Recibe la fila, columna, la matriz y el tamano de la matriz
  
  std::vector<int> vec; //Crea un vector para guardar los vecinos

  //Se esciben condiciones para los diferentes lugares de la matriz 
  
  if(row>0 && row<(n-1) && col>0 && col<(n-1)){ //Para ningun extremo o lado
    int l=8;  //Hay ocho vecinos
    int d=-1; //Se inicializa en posicion fila-1
    int u=-1; //Se inicializa en posicion columna-1
    vec = Vecindad(2, 2, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+1 y columna+1
  }
  else if(row==0 && col==0){ //Esquina superior izquierda
    int l=3; //Hay tres vecinos
    int d=0; //Se inicializa en fila+0
    int u=0; //Se inicializa en columna+0
    vec = Vecindad(2, 2, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+1 y columna+1
  }
  else if(row==0 && col==(n-1)){ //Esquina superior derecha
    int l=3; //Hay tres vecinos
    int d=0; //Se inicializa en fila+0
    int u=-1;//Se inicializa en columna-1
    vec = Vecindad(2, 1, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+1 y columna+0
  }
  else if(row==0 && col==(n-1)){ //Esquina inferior izquierda
    int l=3; //Hay tres vecinos
    int d=0; //Se inicializa en fila+0
    int u=-1;//Se inicializa en columna-1
    vec = Vecindad(2, 1, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+1 y columna+0
  }
  else if(row==(n-1) && col==(n-1)){ //Esquina inferior derecha
    int l=3; //Hay tres vecinos
    int d=-1;//Se inicializa en fila-1
    int u=-1;//Se inicializa en columna-1
    vec = Vecindad(1, 1, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+0 y columna+0
  }
  else if(row==0 && col>0 && col<(n-1)){ //Fila superior (excepto las esquinas)
    int l=5;  //Hay cinco vecinos
    int d=0;  //Se inicializa en fila+0
    int u=-1; //Se inicializa en columna-1
    vec = Vecindad(2, 2, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+1 y columna+1
  }
  else if(row==(n-1) && col>0 && col<(n-1)){ //Fila inferior
    int l=5; //Hay cinco vecinos
    int d=-1;//Se inicializa en fila-1
    int u=-1;//Se inicializa en columna-1
    vec = Vecindad(1, 2, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+0 y columna+1
  }  
  else if(col==0 && row>0 && row<(n-1)){ //Columna izquierda
    int l=5; //Hay cinco vecinos
    int d=-1;//Se inicializa en fila-1
    int u=0; //Se inicializa en fila-1
    vec = Vecindad(2, 2, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+0 y columna+1
  }
  else if(col==(n-1) && row>0 && row<(n-1)){ //Columna derecha
    int l=5; //Hay cinco vecinos
    int d=-1;//Se inicializa en fila-1
    int u=-1;//Se inicializa en columna-1
    vec = Vecindad(2, 1, d, u, row, col, matriz, n, l); //La funcion vencindad busca hasta fila+0 y columna+0
  }
  
  return vec; //Devuelve el vector con los diferentes vecinos
}

//METODO PARA USAR LAS REGLAS DE INTERACCION ENTRE LOS ESTADOS 
void Cell::Rules(int row, int col, std::vector<int>& vec, std::vector<int>& matriz, std::vector<int>& M, int n){//Metodo tipo vector de enteros. Recibe la fila, la columna, el vector de vecinos, la matriz original, una matriz tipo copia y el tamano del lado de la matriz.
  
  int n0 = 0, n1 = 0, n2 = 0; //Enteros que guardan la cantidad de valores del vector que tiene 0, 1 o 2
  
  for(int i=0; i<vec.size(); i+=1){ //Loop para seleccionar los vecinos
    
    if(vec[i] == 0){ //Condicion para valores del vector igual a 0
      n0=n0+1;} //Se anade 1 si hay un valor igual a 0
    else if(vec[i] == 1){ //Condicion para valores del vector igual a 0
      n1=n1+1;} //Se anade 1 si hay un valor igual a 1
    else if(vec[i] == 2){ //Condicion para valores del vector igual a 0
      n2=n2+1;} //Se anade 1 si hay un valor igual a 2
  }
  
  int status = matriz[row*n+col]; //Se define una variable para el valor de la celda a analizar
  
  if(status == 0 && n1 == 3 && n0>=2){ //Regla #1
    M[row*n+col] = 1; //Añade el valor si cumple Regla 1
  }
  else if(status == 0 && n2 == 4 && n1>=1){ //Regla #2
    M[row*n+col] = 2; //Añade el valor si cumple Regla 2
  }
  else if(status == 1 && n1==2 || n1==3){ //Regla #3
    M[row*n+col] = 1; //Añade el valor si cumple Regla 3
  }
  else if(status == 2 && n2==2 || n2==3){ //Regla #4
    M[row*n+col] = 2; //Añade el valor si cumple Regla 4
  }
  else if(status == 1 && n2>=4 && n1<=1){ //Regla #5
    M[row*n+col] = 2; //Añade el valor si cumple Regla 5
  }
  else if(status == 2 && n1==4 || n1==5 && n2<=2){ //Regla #6
    M[row*n+col] = 1; //Añade el valor si cumple Regla 6
  }
  else if(status == 1 && n1>=5){ //Regla #7
    M[row*n+col] = 0; //Añade el valor si cumple Regla 7
  }
  else if(status == 2 && n2>=5){ //Regla #8
    M[row*n+col] = 0; //Añade el valor si cumple Regla 8
  }

}

//METODO QUE EVOLUCIONA EL SISTEMA
void Cell::Evolution(int iter, int n){ //Recibe la cantidad de iteraciones y el tamano de la matriz

  std::vector<int> M = BuildMatriz(n); //Crea un vector en el cual se genera la matriz con el metodo de la clase Cell
  
  for(int t=0; t<iter+1; t++){ //Se hace un loop para evolucionar las matrices segun las reglas 
    
    usleep(100000);          //Funcion para dejar la pantalla esperando mientras se ve la matriz
    system("clear");         //Limpia la pantalla para empezar a imprimir las matrices
    
    PrintMatriz(M, n);       //Se imprime la matriz generada
    
    std::vector<int> N = M;  //Se crea una copia de la matriz y para ser modificada
    //Loop para correr las celdas por posicion (fila, columna)
    for(int fila=0; fila<n; fila++){ //Loop para las filas
      for(int col=0; col<n; col++){  //Loop para las columnas
	std::vector<int> V = Vecinos(fila, col, M, n); //Se sacan los vecinos para cada celda
	Rules(fila, col, V, M, N, n); //Se aplican el metodo de RULES ingresando la fila, columna, vecinos, la matriz original y la copia y el tamaño de la matriz 
      }
    }
    
    M=N; //Se actualiza el valor de la matriz original para cada iteracion
}

  
}

int main(){ //Funcion principal
  
  int n;   //Variable entera para el tamano de la matriz n*n
  cout << "Ingrese el valor n de una matriz n*n: ";
  cin >> n; //Se ingresa el tamano n*n
  
  Cell J;   //Se crea el objeto de la clase Cell

  J.Evolution(1000, n);  //Se evoluciona el objeto
  
  return 0; //No retorna nada
}

