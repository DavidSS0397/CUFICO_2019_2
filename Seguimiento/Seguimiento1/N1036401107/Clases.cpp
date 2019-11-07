// Movimiento de una partícula en un campo magnético. 

#include <iostream>
using namespace std;

// Definimos la clase paartícula donde vamos a definir los "atributos" y los métodos (funciones).

class Particula
{
  public                          // Definimos atributos publicos para poder usarlos en cualquier parte del código.
    int Carga;
    float X, Y, Z, VX, VY, VZ;
    float M;
    
    // Defino los métodos (funciones) de la clase.
    
    void SetValues (float, float, float, float, float, float, float, int);   // Ingreso el tipo de variables que va a recibir el método.
    float Pos_evol (float, float, float, float);
    float Vel_evol (float, float, float, float);
    void print_pos();
} Particula1;                             //Defino una instancia global para mi partícula.

// Utilizo el método SetValues que está en la clase Patricula.

void Particula::SetValues(float x, float y, float z, float vx, float vy, float vz, float m, int q)
{
  X = x;
  Y = y;
  Z = z;
  VX = vx;
  VY = vy:
  Vz = vz;
  M = m;
  Carga = q;
}

// Utilizo el método Pos_evol que está en la clase Particula.

float Particula::Pos_evol(float ax, float ay, float az, float t)
{
  int Bz = 10;               // Campo magnético en la dirección z. Esto significa que solo habrá aceleración en las direcciones x y y.
  ax = Carga*VY*Bz/M;        // Aceleración en x de acuerdo a  -> a = F/m = (q*(vxB))/m
  ay = -1.0*Carga*VX*Bz/M;
  az = 0;
  X = X + (VX*t) + (0.5*ax*t*t);            // Posiciones de la partícula en un campo magnético.
  Y = Y + (VY*t) + (0.5*ay*t*t);
  Z = Z + (VZ*t) + (0.5*az*t*t);  
}

float Particula::Vel_evol(float ax, float ay, float az, float t)
{
  VX = (VX*t) + (ax*t);                  // Velocidades de la partícula.
  VY = (VY*t) + (ay*t);
  VZ = (VZ*t) + (az*t);
}

void Particula::print_pos()
{
  cout << "x = " << X << "y = " << Y << "z = " << Z << endl;   //Muestra en pantalla los valores de la posición.
}

int main()
{
  Particula1.SetValues(0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 10.0, 1);   // Defino los valores de las posiciones y velocidades iniciales con los de carga y masa.
  int i;
  while (i<1000)           
  {
    i+=1
    Particula1.Pos_evol(0.0, 0.0, 0.0, 1);  // Cambia la posición de la partícula en el tiempo. 
    Particula1.print_pos();                 // Muestra en pantalla los valores de la posición.
  }
  return 0;
}
