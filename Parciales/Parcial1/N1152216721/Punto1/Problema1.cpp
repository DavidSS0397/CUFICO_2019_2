/* Descripción: Código que evoluciona un sistema de dos especies basado 
en el Juego de La Vida. Desarrollo basado en el uso de clases, métodos e 
instancias. Correspondiente al examen parcial 1 de Física Computacional I.
Autores:
Juan José León Gil
Andrés David Gómez Villegas
2019 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm> //para contar ocurrencias con std::count
#include<random> //para generar las entradas aleatorias de la matriz
#include<unistd.h> //para usar la función usleep(microseconds)

/* Variables iniciales */
//user_n: string ingresado por el usuario para el tamaño de la matriz
//user_iter: string ingresado por el usuario para cantidad de iteraciones
//n: valor entero al que será convertido user_n si es válido
//iter: valor entero al que será convertido user_iter si es válido
std::string user_n, user_iter;
int n, iter;

/* Definición de funciones */

//****NumInput****//
/* Función que recibe del usuario un número para usar en el programa, 
lo convierte de cadena de caracteres a entero y verifica las siguientes 
situaciones para evitar valores no útiles:
1. Fallo en ingreso, con std::cin.fail()
2. Fallo tipo "End Of File", con std::cin.eof()
3. Que "user_in" no tenga ninguno de los caracteres {0,1,2,3,4,5,6,7,8,9}, 
con user_in.find_first_not_of("0123456789") y std::string::npos (la igualdad 
o desigualdad decide si "user_in" tiene o no alguno de los caracteres)*/
int NumInput(std::string user_in)
{
  while( std::cin.fail() ||
	 std::cin.eof() ||
	 user_in.find_first_not_of("0123456789") != std::string::npos)
    {
      //Si user_in es una entrada no nula pero tiene un caracter diferente a
      //{0,1,2,3,4,5,6,7,8,9}, borrar la entrada antes de pedir el valor
      //nuevamente al usuario (limpiar el buffer con cin.clear y cin.ignore)
      if( user_in.find_first_not_of("0123456789") == std::string::npos)
	{
	  std::cin.clear();
	  std::cin.ignore(256,'\n');
	}

      //Aviso de entrada no válida y pedido de ingreso al usuario para recibir un número válido
      std::cout << "La entrada no es válida. Ingrese el valor nuevamente (0 para abortar la ejecución): ";
      std::getline(std::cin, user_in);
    }

  //Convertir user_in con la función std::stoi ("string to integer")
  n = std::stoi(user_in, nullptr);
  
  return(n);
} //fin de función NumInput


/* Clase que contiene al sistema y su evolución */
class World
{  
public: //ver las implementaciones después del main

  //Creación del escenario del mundo, matriz cuadrada de dimensión "Msize"
  std::vector<std::vector<int>> MatrixSetUp(int Msize);

  //Extracción de los "vecinos" del elemento en la fila r (row),
  //columna c (column),  de la matriz cuadrada M. Los vecinos
  //se guardan en un array llamado "neighb".
  std::vector<int> Neighbours(const std::vector<std::vector<int>>& M, int r, int c);

  //Condiciones de evolución del sistema
  int Evolution(int v, int k0, int k1, int k2);

  //Iteración del sistema
  void Iteration(std::vector<std::vector<int>> Curr, int iter);

}; //fin de class World

/* Inicio de ejecución */
int main()
{
  /* Descripción en pantalla */
  std::cout << std::string(64, '*') << std::endl;
  std::cout << "JUEGO DE LA VIDA CON DOS ESPECIES." << std::endl;
  std::cout << "Se creará una matriz cuadrada de tamaño ingresado por el" << std::endl;
  std::cout << "usuario, evolucionando el sistema una cantidad de iteraciones" << std::endl;
  std::cout << "también definida por el usuario. El estado inicial se genera" << std::endl;
  std::cout << "ubicando de manera aleatoria ambas especies y lugares vacíos." << std::endl;
  std::cout << "(Ejecutar preferiblemente en terminal de tamaño maximizado.)" << std::endl;
  std::cout << std::string(64, '*') << std::endl;

  /* Primera etapa: recibir la entrada del usuario por línea de comando,
  aceptando sólamente valores naturales (0 se usa como "flag" para
  terminar ejecución). Dicha entrada será el string "user_n", que de
  ser válida se convertirá a entero para ser guardada en "n". */

   //Recibir el string "user_n"
  std::cout << "\nIngrese el número natural que define el tamaño de la matriz (0 para abortar la ejecución): ";
  std::getline(std::cin, user_n);

  //Convertir el string a entero
  n = NumInput(user_n);

  //Si la entrada es 0 abortar la ejecución. En caso contrario continuar
  if (n == 0)
    {
      std::cout << "Ejecución abortada. " << std::endl;
      return(0);
    }

  /* Segunda etapa: creación del "mundo" y establecimiento de condiciones
 iniciales */
  World GameOfLife;

  //Matriz
  std::vector<std::vector<int>> Matrix = GameOfLife.MatrixSetUp(n);

  //Caso de mundo trivial: una matriz 1x1 permanecerá igual
  if (n == 1)
    {
      std::cout << "La evolución del sistema es trivial. " << std::endl;
      return(0);
    }

  /* Tercera etapa: definición de la cantidad de iteraciones */
  //Recibir el string "user_iter"
  std::cout << "\nIngrese el número natural que define la cantidad de iteraciones (0 para abortar la ejecución): ";
  std::getline(std::cin, user_iter);

  //Convertir el string a entero
  iter = NumInput(user_iter);

  //Si la entrada es 0 abortar la ejecución. En caso contrario continuar
  if (iter == 0)
    {
      std::cout << "Ejecución abortada. " << std::endl;
      return(0);
    }

  /*Última etapa: iteración */
  GameOfLife.Iteration(Matrix, iter);

  std::cout << "Fin de la ejecución." << std::endl;
  
  return(0);
} //fin de main


/* Definición de las implementaciones de la clase World */

//****MatrixSetUp****//
//Entrada: tamaño de la matriz, "Msize"
//Salida: Matriz "Matrix"
std::vector<std::vector<int>> World::MatrixSetUp(int Msize)
{
  //Semilla para generar aleatoriamente el estado inicial de la matriz
  srand( (unsigned int) time(NULL) );

  //Matriz cuadrada creada como vector de "Msize" vectores de tamaño
  //"Msize", inicialmente con todos sus valores iguales a 0
  std::vector<std::vector<int>> Matrix(Msize, std::vector<int>(Msize));

  //Doble ciclo for que inserta valores en cada entrada de la matriz
  for (int i = 0; i < Msize; i++)
    {
      for (int j = 0; j < Msize; j++)
        {
	  Matrix[i][j] = rand()%3; //módulo 3: sólo {0,1,2} posibles
        } 
    } 

  return(Matrix);
} //fin de World::MatrixSetUp


//****Neighbours****//
//Entrada: Matriz "M", ubicación en fila (r) y en columna (c)
//Salida: vector "neighb" que contiene a los vecinos de M[r][c]
std::vector<int> World::Neighbours(const std::vector<std::vector<int>>& M, int r, int c)
{
  //En este caso (matriz cuadrada), M.size() da el número de filas,
  //igual al número de columnas.
  int n = M.size();

  //Vector en el que se almacenarán los vecinos del elemento (i, j)
  std::vector<int> neighb;

  if ( r == 0 )
    { //recorrido por fila superior
      if ( c == 0 )
	{
	  neighb = {M[0][1], M[1][0], M[1][1]};
	} //caso esquina superior izquierda: M[0][0]

      else if ( c > 0 && c < n-1 )
	{
	  neighb = {M[0][c-1], M[0][c+1], M[1][c-1], M[1][c], M[1][c+1]};
	} //caso fila superior, no esquina: M[0][0 < c < n-1]

      else if ( c == n-1 )
	{
	  neighb = {M[0][n-2], M[1][n-2], M[1][n-1]};
	} //caso esquina superior derecha: M[0][n-1]
    } //fin recorrido por fila superior

  else if ( r > 0 && r < n-1 )
    { //recorrido por filas intermedias
      if ( c == 0 )
	{
	  neighb = {M[r-1][0], M[r-1][1], M[r][1], M[r+1][0], M[r+1][1]};
	} //caso columna izquierda, no esquina: M[0 < r < n-1][0]

      else if ( c > 0 && c < n-1 )
	{
	  neighb = {M[r-1][c-1], M[r-1][c], M[r-1][c+1], M[r][c-1], M[r][c+1], M[r+1][c-1], M[r+1][c], M[r+1][c+1]};
	} //caso intermedio, ni esquina ni bordes: M[0 < r < n-1][0 < c < n-1]

      else if ( c == n-1 )
	{
	  neighb = {M[r-1][n-2], M[r-1][n-1], M[r][n-2], M[r+1][n-2], M[r+1][n-1]};
	} //caso columna derecha, no esquina: M[0 < r < n-1][n-1]
    } //fin recorrido por filas intermedias

  else if ( r == n-1 )
    { //recorrido por fila inferior
      if ( c == 0 )
	{
	  neighb = {M[n-2][0], M[n-2][1], M[n-1][1]};
	} //caso esquina inferior izquierda: M[n-1][0]

      else if ( c > 0 && c < n-1 )
	{
	  neighb = {M[n-2][c-1], M[n-2][c], M[n-2][c+1], M[n-1][c-1], M[n-1][c+1]};
	} //caso fila inferior, no esquina: M[n-1][0 < c < n-1]

      else if ( c == n-1 )
	{
	  neighb = {M[n-2][n-2], M[n-2][n-1], M[n-1][n-2]};
	} //caso esquina inferior derecha: M[n-1][n-1]
    } //fin recorrido por fila inferior

  return(neighb);
} //fin de World::Neighbours


//****Evolution****//
//Entrada:
//  v: estado inicial de la celda
//  k0: cantidad de elementos tipo 0 aledaños
//  k1: cantidad de elementos tipo 1 aledaños
//  k2: cantidad de elementos tipo 2 aledaños
//Salida:
//  w: nuevo valor de la celda
int World::Evolution(int v, int k0, int k1, int k2)
{
  int w;
  if (v == 0) //Si no hay ninguna especie
    {
      if (k0 >= 2 and k1 == 3) {w = 1;}
      else if (k1 >= 1 and k2 == 4) {w = 2;}
      else {w = 0;} //Si no se cumple ninguna anterior
    }
  
  else if (v == 1) //Si la especie es de tipo 1
    {
      if (k1 == 2 or k1 == 3) {w = 1;}
      else if (k1 <= 1 and k2 >= 4) {w = 2;}
      else if (k1 >= 5) {w = 0;}
      else {w = 0;} //Si no se cumple ninguna anterior
    }
  
  else if ( v == 2) //Si la especie es de tipo 2
    {
      if (k2 == 2 or k2 == 3) {w = 2;}
      else if ((k1 == 4 or k1 == 5) and k2 <= 1) {w = 1;}
      else if (k2 == 5) {w = 0;}
      else {w = 0;} //Si no se cumple ninguna anterior
    }
  
  return(w);
} //fin de World::Evolution


//****Iteration****//
//InitM: matriz que contiene el estado inicial
//CurrM: matriz que contiene el estado actual
//iter: número de iteraciones
//NextM: matriz que contiene el estado siguiente
void World::Iteration(std::vector<std::vector<int>> InitM, int iter)
{
  //Primer estado: matriz actual = matriz inicial
  std::vector<std::vector<int>> CurrM = InitM;
  int Msize = CurrM.size(); //Tamaño de la matriz del estado actual
  
  //Matriz en la que guardar el estado siguiente
  std::vector<std::vector<int>> NextM(Msize, std::vector<int>(Msize));
  
  //Impresión de primera generación
  system("clear"); //limpiar la pantalla
  std::cout << "Generación: 0" << std::endl;
  for (int i = 0; i < Msize; i++)
    {
      for (int j = 0; j < Msize; j++)
	{
	  if (CurrM[i][j] == 0)
	    {
	      std::cout << " " << " ";
	    } //Imprimir un espacio en vez de 0, para claridad visual
	  else
	    {
	      std::cout << CurrM[i][j] << " ";
	    }
	}
      std::cout << std::endl; //salto de línea para separar filas
    }
  
  usleep(125000); //esperar 0.125 segundos
  system("clear"); //limpiar la pantalla
  
  //Evolución de cada generación iterando "iter" veces
  for (int gen = 1; gen <= iter; gen++)
    {
      std::cout << "Generación: " << gen << std::endl;
      
      //Conversión de cada especie. Doble ciclo for que observa cada elemento
      for (int row = 0; row < Msize; row++)
	{
	  for (int col = 0; col < Msize; col++)
	    { 
	      //Neighb contiene los vecinos del elemento (row, col) del estado actual
	      std::vector<int> Neighb = World::Neighbours(CurrM, row, col);

	      //oc0, oc1 y oc2: ocurrencia de 0, 1 y 2 entre los vecinos
	      int oc0 = std::count( Neighb.begin(), Neighb.end(), 0 );
	      int oc1 = std::count( Neighb.begin(), Neighb.end(), 1 );
	      int oc2 = std::count( Neighb.begin(), Neighb.end(), 2 );
	      
	      //Evolución de acuerdo a las reglas definidas en "Evolution"
	      NextM[row][col] = World::Evolution(CurrM[row][col], oc0, oc1, oc2);
	      
	    } //fin del ciclo for para las columnas "col"
	} //fin del ciclo for para las filas "row"

      //Impresión en pantalla de la generación número "gen"
      for (int iprint = 0; iprint < Msize; iprint++)
	{
	  for (int jprint = 0; jprint < Msize; jprint++)
	    {
	      if (NextM[iprint][jprint] == 0)
		{
		  std::cout << " " << " ";
		} //Imprimir un espacio en vez de 0, para claridad visual
	      else
		{
		  std::cout << NextM[iprint][jprint] << " ";
		}
	    }
	  std::cout << std::endl; //salto de línea para separar las filas
	}

      usleep(125000); //esperar 0.125 segundos
      system("clear"); //limpiar la pantalla
      CurrM = NextM; //Reemplazar estado siguiente de la iteración
      
    } //fin de la iteración "iter" veces sobre las generaciones "gen"
  
} //fin de World::Iteration
