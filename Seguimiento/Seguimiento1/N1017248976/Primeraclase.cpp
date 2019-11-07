#include <iostream>
using namespace std;

//Creacion clase
class Particle
{

public:
  int Carga;
  float X,Y,Z;
  float VX ,VY,VZ;
  float M;
  void Setvalues(float,float,float,float,float,float,float,int);//metodo funcion dentro de la clase
  float Pos_evol(float,float,float,float);//creacionde una funcion vacia, solo le digo cuantas y que tipo de variables va a recibir pero nada mas
  

} ;
void Particle::Setvalues(float x ,float y, float z, float vx, float vy, float vz, float m, int carga)
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

float Particle::Pos_evol(float Bx,float By, float Bz, float dt) //Funcion de la dinamica de la particula sometida a un campo magnetico constante
{
  for (int i=0;i<1e5;i++)
    {
  //Aceleracion
  float ax=(Carga/M)*(VY*Bz-VZ*By);
  float ay=(Carga/M)*(VZ*Bx-VX*Bz);
  float az=(Carga/M)*(VX*By-VY*Bx);
  
  //Velocidad
  VX=VX+ax*dt;
  VY=VY+ay*dt;
  VZ=VZ+az*dt;
  
  //Posicion
  X=X+(VX*dt)+(0.5*ax*(dt*dt));
  Y=Y+(VY*dt)+(0.5*ay*(dt*dt));
  Z=Z+(VZ*dt)+(0.5*az*(dt*dt));
    }
}



int main()
{
  
  Particle Particula;
  Particula.Setvalues(0.0,0.0,0.0,-1.0,2.0,5.0,4.0,1);//inicializacion de los valores
  //Valores iniciales
  cout <<"\n Valores iniciales: \n"<<"Velocidades(Vx,Vy,Vz): "<<Particula.VX <<" "<< Particula.VY<< " " <<Particula.VZ<<"\n" <<"Carga: "<<Particula.Carga <<"\n"<<"Posicion(X,Y,Z):" << Particula.X << " "<< Particula.Y << " "<<Particula.Z << " "<< endl;

  //Evolucion de la particula
  // Componenetes campo magnetico
  float B_x=-3.0;
  float B_y=0.0;
  float B_z=1.0;
  Particula.Pos_evol(B_x,B_y,B_z,0.00001);
 
  cout <<"\n Evolucion de la particula:\n"<<"Posicion(X,Y,Z): "<< Particula.X << " "<< Particula.Y << " "<<Particula.Z << " "<<"\n"<<"Valocidades(Vx,Vy,Vz): "<< Particula.VX <<" " << Particula.VY << " "<< Particula.VZ << " "<<"\nCampo magnetico:" <<B_x<<" "<<B_y<<" "<<B_z<<" "<< endl;

 //Particula de prueba
 /* Con la particula de prueba comprobaremos si los resultados obtenidos numericamente tienen sentido fisico, para esto escogeremos una configuracion inicial sencilla, cuya dinamica conozcamos de antemano.
Si tomamos que la particula se encuentra inicialmente con velocidad en una unica direccion (i.e Vx=!0 Vy=Vz=0) y ademas tenemos el campo solo en direccion z, esperaremos que la fuerza genere una desviacion en la trayectoria tal que la velocidad en x disminuya y empiece a existir una componenete en la velocidad en y negativa mientras que la velocidad en z permanezca constante.*/
 
  Particle ParticuladePrueba;
  ParticuladePrueba.Setvalues(0.0,0.0,0.0,1.0,0.0,0.0,1.0,1);//inicializacion de los valores velocidad solo en x
  //Valores iniciales
  cout <<"\n Particula de Prueba:\n "<<"Valores iniciales: \n"<<"Velocidades(Vx,Vy,Vz): "<<ParticuladePrueba.VX <<" "<< ParticuladePrueba.VY<< " " <<ParticuladePrueba.VZ<<"\n " <<"Carga: "<<ParticuladePrueba.Carga <<"\n "<<"Posicion(X,Y,Z):" << ParticuladePrueba.X << " "<< ParticuladePrueba.Y << " "<<ParticuladePrueba.Z << " "<< endl;

  //Evolucion de la particula
  ParticuladePrueba.Pos_evol(0.0,0.0,1.0,0.00001);//campo con componenetes unicamente en el eje z
 
 cout <<"\n Evolucion de la particula de prueba:\n"<<"Posicion(X,Y,Z): "<< ParticuladePrueba.X << " "<< ParticuladePrueba.Y << " "<<ParticuladePrueba.Z << " "<<"\n"<<"Valocidades(Vx,Vy,Vz): "<< ParticuladePrueba.VX <<" " << ParticuladePrueba.VY << " "<< ParticuladePrueba.VZ << " "<< endl;
  


 


 return 0;
}
