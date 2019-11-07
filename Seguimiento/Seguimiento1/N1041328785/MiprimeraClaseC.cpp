#include <iostream>


using namespace std;


//#############################################

// ESTRUCTURAS: generalizacion de tipos de datos.
struct campos
{
  float X;
  float Y;
  float Z;
} E, B;//instancias de las clases.


//CLASES: publico: en cualquier momento se puede acceder.
class particle
{
public:
  int Carga;
  float X, Y, Z;
  float VX, VY, VZ;
  float M;
  
  //metodos
  //estos reciben solo el tipo de variables
  //no poseen cuerpo definido
  void setvalues( float, float, float, float, float, float, float, int);
  float pos_evol( float, float, float, float);
  float vel_evol( float, float, float, float);
  //float acl_evol(float, float, float, float, float, float)
} p1, p2;

// VALORES DE LAS PROPIEDADES DE LA PARTICULA
void particle::setvalues(float x, float y, float z, float vx, float vy, float vz, float m, int carga)
{
  X=x;
  Y=y;
  Z=z;
  VX=vx;
  VY=vy;
  VZ=vz;
  M=m;
  Carga=carga;
}
//  EVOLUCION DE LAS POSICIONES
float particle::pos_evol(float ax, float ay, float az, float t)
{
  X=X+(VX*t)+(0.5*ax*t*t);
  Y=Y+(VY*t)+(0.5*ay*t*t);
  Z=Z+(VZ*t)+(0.5*az*t*t);
  return t;
}
// EVOLUCION DE LAS VELOCIDADES
float particle::vel_evol(float ax, float ay, float az, float t)
{
  VX = VX + ax*t;
  VY = VY + ay*t;
  VZ = VZ + az*t;

  return t;
}


//#############################################


int main()
{

//SE DEFINEN LOS CAMPOS ELECTRICO Y MAGNETICO
  //elctrico
  E.X=9.0;
  E.Y=0.0;
  E.Z=0.0;

  //magnetico
  B.X=0.0;
  B.Y=0.0;
  B.Z=10.0;


// SE DEFINE LA PARTICULA 
    particle particula4;

    particula4.setvalues(1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 1.0, 1);

//PARAMETROS TEMPORALES
      float t = 0.0; // tiempo global de la simulacion
      float dt = 0.01; // resolucion del intervalo de tiempo
    //int i = 0; auxiliar progresion de estados

//SIMULACION DE MOVIMIENTO EN UN INTERVALO t
cout << "pocisiones x y z" << endl;
   while ( t <= 1 )
   {
    //se hace el estudio componentea a componente de la fuerza de lorentz para calcular 
    //la aceleracion a partir de la segunda ley de newton donde las masa del electron es
    // tomada como 1 y su carga 1.

    //la simulacion fue hecha estudiando solo las magnitudes de las componentes vectoriales
    //velocidad, aceleracion, posicion, campo electrico, campo magnetico y fuerza de lorentz.

    //SE REDEFINEN LAS COMPONENTES DE LA ACELERACION TRANSCURRIDO UN DEL ESTADO ACTUAL.
    float AX = particula4.Carga * (E.X + particula4.VY * B.Z - B.Y * particula4.VZ) / particula4.M;
    float AY = particula4.Carga * (E.Y - particula4.VX * B.Z + B.X * particula4.VZ) / particula4.M;
    float AZ = particula4.Carga * (E.Z + particula4.VX * B.Y - B.X * particula4.VY) / particula4.M; 
    //cout << AX << " " << AY << " " << AZ << endl; //imprime los valores de la aceleracion


//ESTE BLOQUE IMPRIME EN PANTALLA LOS VALOES DE POCISION Y VELOCIDAD DE LA PARTICULA EN EL ESTADO ACTUAL.
    //cout << "pocisiones" << " " << i << endl;
    cout << particula4.X << " " << particula4.Y << " " << particula4.Z << endl; // ESTA LINEA PUEDE SER COMENTADA SI SE DESEA.

    //cout << "velocidades" << " " << i << endl;
    //cout << particula4.VX << " " << particula4.VY << " " << particula4.VZ << endl;

//LAS SIGUIENTES LINEAS DAN LA TRANSICION A LAS NUEVAS COORDENADAS DESPUES DE PASAR UN dt. 
    particula4.pos_evol(AX, AY, AZ, dt);
    particula4.vel_evol(AX, AY, AZ, dt);
     
//    i = i + 1; progresion de estados
    t = t + dt;
   }
   
  return 0;

}
