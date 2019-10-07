#include<iostream>
#include<vector>
using namespace std;

int rows; //filas
int cols; //columnas

class Matrix
{
public:
    Matrix(int rows, int cols); //se define el metodo que fijará la dimension de la matriz
    int CellState_evol(int,int); //metodo que hara evolucionar la matriz
    int mRows; //filas maximas
    int mCols; //columnas maximas
    std::vector<int> mData; //Vector que definirá la matriz
    
};
Matrix::Matrix(int rows, int cols) //funcion que fija las filas y columnas de la matriz
: mRows(rows),
  mCols(cols),
  mData(rows * cols)
{
}

void SumaAlPrimero(int a, int b)
{ a = a+b;
}

int Matrix::CellState_evol(int neighborst1, int neighborst2)
{
  int t=0;
  int deltat=1; //de esta manera fijamos el paso del tiempo discreto (turnos)
  SumaAlPrimero(t,deltat); //aumenta el tiempo
  int neighbors1=0;
  int neighbors2=0;
  int neighborsdead=0;
  //para actualizar cada termino de la matriz donde esta cada celular debemos considerar el estado de los 8 vecinos de su alrededor
  for (int mRows; mRows<mData.size(); mRows++)
{
}
  return 0;
}

// se pueden declarar instancias aca;

int main()
{
int n=0; //dimensiones n de la matriz cuadrada
cout << "ingrese las dimensiones de la matriz nxn" << endl; //imprime en la terminal
cin >> n; // entrada por linea de comando de la dimension de la matriz
Matrix matrixofspc(n,n); //llamamos una instancia de la clase Matrix para definir la matriz para el juego de la vida

cout << "n ha sido asignado como:" << matrixofspc.mRows << endl;
cout << "dimension nxn: " << matrixofspc.mData.size() << endl;
//cout << matrix[0][0] << endl;
}
