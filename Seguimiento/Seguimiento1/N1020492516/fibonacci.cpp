//Brayan Alexander Muñoz Barrara - 1020492516
//Por favor informarme si hay un error o algo

#include <iostream>

int main()
{
  int fi1=0;
int fi2=1;
for(int i=0; i<1000; i++)
  {fi2 = (fi2 + fi1);
    fi1 = (fi2 - fi1);
    //std::cout << fi2 << std::endl;
    if (fi2%2 == 0)
      { 
    std::cout << "Numero de Fibonacci" << i << "=" << fi2 << std::endl;
      }
  }
return 0;
}

  
