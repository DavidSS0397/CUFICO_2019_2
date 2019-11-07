#include <iostream>

using namespace std;

// 

int main()

{

int numero = 1;
int numeroant = 0;
int paso; //esta variable contiene la informacion del numero actual

for (int i=0; i<1000; i++)
{
    if (numero%2 == 0)
    {
        std::cout << numero << std::endl; // solo se imprimen los numeros pares de la sucesion
    }
    paso = numero;
    numero +=numeroant;
    numeroant = paso;
}



    return 0;
}
