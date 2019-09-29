/*
! ==================================================================================
! problema1.cpp
! ==================================================================================
! 
* Juego de la vida. Se tienen tres estados posibles para cada una de las casillas:
* celula de tipo 1 (1), celula de tipo 2 (2) y ninguna celula (0). El sistema 
* evoluciona segun ocho reglas estipuladas en el documento y se imprime su evolucion
* en pantalla. El usuario ingresa la dimension del tablero.
* Para evitar programacion especial en los bordes del tablero, se le pone un marco
* de numeros 5.
* 
!     Carolina Herrera Segura, carolina.herreras@udea.edu.co    
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co
!
! Up to date: 29 septiembre 2019            
*/

#include <cstdlib> // Libreria estandar de C. Se usa para numeros aleatorios
#include <iostream> // Libreria para input y output
#include <vector> // Libreria para usar vectores
#include <ctime> // Libreria para medir el tiempo del sistema

// Para no tener que escribir std::
using namespace std;


// Definicion clase GameOfLife
class GameOfLife
{
    // Atributos publicos de la clase
    public:
        
        int n; // Entero n que indica tamaño del tablero
        vector<vector<int>> board; // El tablero, que es un vector de vectores
        void set_values(int); // Metodo que define el valor de n
        void initialize(); // Metodo que incializa el tablero
        void evolution(); // Metodo que evoluciona el sistema
        void print(); // Metodo que imprime el tablero

}gameoflife; // Definimos un objetos de clase GameOfLife


// Metodo que define el valor de n con input del usuario
void GameOfLife::set_values(int N)
{
    n = N+2; // Al tamaño del tablero se le suma 2 para incluir un marco de 5s
}


// Metodo que inicializa el tablero de forma aleatoria
void GameOfLife::initialize()
{
    srand(time(NULL)); // Reinicia la semilla del generador de numero aleatorios

    // Ciclo que recorre filas de la matriz, que son vectores
    for (int i=0; i<n; i++)
    { 
        // Se crea vector rows para ser inicializado y agregado al vector de vectores board
        vector<int> row;
        
        // Ciclo que agrega entradas a vector row, correspondientes a las columnas
        for (int j=0; j<n; j++) 
        {
            // Si estamos en los bordes del tablero, agregar un 5
            // Esto crea un marco de 5s para el tablero
            if(i==0 or j==0 or i==n-1 or j==n-1) row.push_back(5);
            
            // Si no se esta en los bordes, agregar un numero aleatorio entre 0 y 2
            else
            {
                row.push_back(rand()%3); // Genera el numero aleatorio
            }
        }
        
        // Agregamos vector row a vector de vectores board
        board.push_back(row);
    }
}


// Metodo que evoluciona el tablero
void GameOfLife::evolution()
{
    int new_board[n][n]; // Declaramos una matriz new_board para almacenar nuevo tablero
    int neighbour[8]; // Declaramos arreglo de 8 entradas para almacenar el valor que tienen los vecinos
    int count[] = {0,0,0}; // Declaramos arreglo count para almacenar numero de vecinos con valor 0, 1 y 2 
    
    // Ciclo que recorre filas de las matrices board y new_board
    for (int i=0; i<n; i++)
        {
            // Ciclo que recorre las columnas de las matrices board y new board
            for (int j=0; j<n; j++)
            {
                // Este if aplica solo para las entradas que no estan en los bordes
                if(i!=0 and j!=0 and j!=n-1 and i!=n-1)
                {
                    // Se reinician los valores del arreglo count a cero
                    count[0] = count[1] = count[2] = 0;
                    
                    // Se almacena el valor de los ocho vecinos en el arreglo neighbour
                    neighbour[0] = board[i][j+1];
                    neighbour[1] = board[i][j-1];
                    neighbour[2] = board[i+1][j];
                    neighbour[3] = board[i-1][j];
                    neighbour[4] = board[i+1][j+1];
                    neighbour[5] = board[i+1][j-1];
                    neighbour[6] = board[i-1][j+1];
                    neighbour[7] = board[i-1][j-1];
                    
                    // Ciclo que recorre el arreglo neighbour
                    for (int k=0; k<8; k++)
                    {
                        if(neighbour[k]==0) {count[0] += 1;} // Si el valor de neibhbour es 0, se suma 1 a la primera entrada de count
                        else if(neighbour[k]==1) {count[1] += 1;} // Si el valor de neibhbour es 1, se suma 1 a la segunda entrada de count
                        else if(neighbour[k]==2)  {count[2] += 1;} // Si el valor de neibhbour es 2, se suma 1 a la tercera entrada de count
                    }
                    
                    // Las ocho reglas definidas en el documento para evolucionar el sistema
                    // El nuevo valor se almacena en la matriz new_board, para que no afecte valores originales de board
                    if(board[i][j]==0 and count[1]==3 and count[0]>=2){new_board[i][j]=1;}
                    else if(board[i][j]==0 and count[2]==4 and count[1]>=1){new_board[i][j]=2;}
                    else if(board[i][j]==1 and (count[1]==3 or count[1]==2)){new_board[i][j]=board[i][j];}
                    else if(board[i][j]==2 and (count[2]==3 or count[2]==2)){new_board[i][j]=board[i][j];}
                    else if(board[i][j]==1 and count[2]>=4 and count[1]<=1){new_board[i][j]=2;}
                    else if(board[i][j]==2 and (count[1]==4 or count[1]==5) and count[2]<=1){new_board[i][j]=1;}
                    else if(board[i][j]==1 and count[1]>=5){new_board[i][j]=0;}
                    else if(board[i][j]==2 and count[2]==5){new_board[i][j]=0;}
                    else {new_board[i][j]=board[i][j];} // Si no se cumple ninguna regla, la casilla queda con su mismo valor
                }
            }
        }
        
        // Luego de haber definido todo new_board, se actualizan los valores de la matriz board
        // Ciclo que recorre filas
        for (int i = 0; i < n; ++i)
        {
            // Ciclo que recorre columnas
            for (int j = 0; j < n; ++j)
            {
                // Actualizamos entradas de board para que correspondan a new_board
                board[i][j] = new_board[i][j];
            }
        }
}


// Metodo que imprime en pantalla el tablero, primero borrando lo que había en la terminal
void GameOfLife::print()
{
    // Se usa comando 'clear' para limpiar la terminal antes de imprimir
    system("clear");
    
    // Cico que recorre filas
    for (int i = 0; i < n; ++i)
    {
        // Ciclo que recorre columnas
        for (int j = 0; j < n; ++j)
        {
            // Contenido del if aplica solo para valores que no esten en los bordes
            if(i!=0 and j != 0 and j!= n-1 and i!= n-1)
            {
                // Se imprime valor de la entrada (i, j) de board
                cout << board[i][j] << " ";
            }
        }
        // Salto de linea cuando se termina de imprimir una fila
        cout << endl;
    }
}


// Main del programa
int main()
{
    int steps = 1000; // Definimos numero de pasos para la evolucion
    int N; // Declaramos la variable donde se guardara la dimension del tablero

    // Mensaje que le pide al usuario que ingrese n
    cout << "Ingrese la dimension del tablero:" << endl;  
    cin >> N; // El valor de n es ingresado

    gameoflife.set_values(N); // Define valor de n
    gameoflife.initialize(); // Inicializa tablero de forma aleatoria
    gameoflife.print(); // Imprime estado actual del tablero. En este caso, inicializacion
    
    // Ciclo que cuenta numero de pasos
    for (int t=0; t<steps; t++)
    {   
        system("sleep 1"); // Comando para que espere un segundo y vea la evolucion
        gameoflife.evolution(); // Evoluciona el sistema
        gameoflife.print(); // Imprime el resultado de la evolucion
    }
    
    // Si todo sale bien, el main retorna 0
    return 0;
}
