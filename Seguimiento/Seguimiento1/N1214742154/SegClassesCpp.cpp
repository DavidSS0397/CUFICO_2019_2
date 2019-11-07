
#include <iostream>
#include <cmath>
using namespace std;

//Physical constants
float G = 0.0; //Constante gravitacional
float k_e = 8000000000; //Constante de Coulomb

//Physical values of the problem
float B_x = 0;//
float B_y = 0;//
float B_z = 10;//Unica componente no nula del campo magnetico



class Particle //The class that will be instanced to create particles
//This creates a type called "Particle" so this is the type that goes into the methods arguments
{
public:
  float Carga;
  float X,Y,Z;
  float VX,VY,VZ;
  float M;


  //Methods
  void SetValues(float,float,float,float,float,float,float,int);
  void Pos_evol(float,float,float,float);
  float calc_B_force(float, float, float);
  float calc_f_e(Particle);
  float calc_net_f(Particle);
  float force_by_axis(Particle,float, float, float);
  float calc_acc(Particle,float,float,float);
  float calc_rel_pos(Particle);


  
}P1,P2;//Instancing of two particles

void Particle::SetValues(float x, float y, float z, float vx, float vy, float vz, float m, int carga)
//Sets values for the particles
{
  X = x;
  Y = y;
  Z = z;
  VX = vx;
  VY = vy;
  VZ = vz;
  M = m;
  Carga = carga;
}

float Particle::calc_rel_pos(Particle other)
//Calculates relative position respect to other particle
//PARECE FUNCIONAR
{
  float x_rel = X-other.X;
  float y_rel = Y-other.Y;
  float z_rel = Z-other.Z;

  //cout << x_rel << " " << y_rel << " " << z_rel << endl;

  float to_return[3] = {x_rel, y_rel, z_rel};
  
  return * to_return;
  
}

float Particle::calc_B_force(float B_x, float B_y, float B_z)
//NOT TESTED
//Calculates magnetic force experienced due to other particle
{
  float B_force_x = Carga*( VY*B_z - VZ*B_y );
  float B_force_y = Carga*( -VX*B_z + VZ*B_x );
  float B_force_z = Carga*( VY*B_x - VX*B_y );

  cout << B_force_x << " " << B_force_y << " " << B_force_z << "H" <<endl;//NO BORRAR,

  
  float to_return[3] = {B_force_x, B_force_y, B_force_z};
  
  return * to_return;

}

float Particle::calc_f_e(Particle other)
//USING CLASS AS ARGUMENT MIGHT CAUSE ERROR
//Calculates electrical force experienced due to other particle
{
  float x_rel, y_rel, z_rel = calc_rel_pos(other);

  
  float r = sqrt( pow(x_rel, 2) + pow(y_rel, 2) + pow( z_rel, 2));//PUEDE DAR ERRORES POR NOTACIÓN PYTHON

  /*
  cout << x_rel << " " << y_rel << " " << z_rel << endl;
  cout << r << endl;

  cout << k_e << " " << Carga << " " << other.Carga << endl;
  
  */
  float f_e = (k_e*Carga*other.Carga); //pow(r, 2.0);//PUEDE DAR ERRORES POR NOTACIÓN PYTHON


  cout << f_e << endl; //BIEN
  return f_e;
}


float Particle::calc_net_f(Particle other) //BIEN
//USING CLASS AS ARGUMENT MIGHT CAUSE ERROR
{
  float e_f = calc_f_e(other);
  //float g_f = calc_f_g(other);

  //float net_f = e_f+g_f;
  
  float net_f = e_f;

  cout << net_f << endl;// BIEN
  return net_f;
}

float Particle::force_by_axis(Particle other,float B_x, float B_y, float B_z)
//Returns the net force on each axis.
{
  float net_f = calc_net_f(other);
  float x_rel,y_rel,z_rel = calc_rel_pos(other);

  float r = sqrt(pow(x_rel, 2)+pow(y_rel, 2)+pow(z_rel, 2));
  float F_z = net_f*(z_rel/r);
  float F_y = net_f*( sqrt( pow(r, 2) - pow(z_rel, 2)) / r ) * ( y_rel / sqrt( pow(r, 2) - pow(z_rel, 2)) );
  float F_x = net_f*( sqrt( pow(r, 2) - pow(z_rel, 2)) / r ) * ( x_rel / sqrt( pow(r, 2) - pow(z_rel, 2)) );



  float B_force_x, B_force_y, B_force_z = calc_B_force(B_x,B_y,B_z);

  F_x = F_x + B_force_x;
  F_y = F_y + B_force_y;
  F_z = F_z + B_force_z;

  cout << F_x << " " << F_y << " " << F_z << "PAPAYA" <<  endl;//NaN

  float to_return[3] = {F_x, F_y, F_z};
  
  return * to_return;

}
        

float Particle::calc_acc(Particle other,float B_x,float B_y,float B_z)
// Calculates acceleration in each axis
{
  float F_x, F_y, F_z = force_by_axis(other,B_x,B_y,B_z);
  float acc_x = F_x/M;
  float acc_y = F_y/M;
  float acc_z = F_z/M;
  

  cout << acc_x << acc_y << acc_z << endl;//BIEN

  
  float to_return[3] = {acc_x, acc_y, acc_z};
  
  return * to_return;
  

}




void Particle::Pos_evol(float ax, float ay, float az, float t)
//Updates the positions of the particle
{
  X = X + (VX*t)+(0.5*ax*t*t);
  Y = Y + (VY*t)+(0.5*ay*t*t);
  Z = Z + (VZ*t)+(0.5*az*t*t);
}
 

int main(){

  cout << "----------------------" << endl;
  //Setting initial values
  P1.SetValues(0,0,0,0,0,0,1,-422);
  P2.SetValues(1,0,0,0,0,0,1,422);

  //oat acc_x, acc_y, acc_z = P1.calc_acc (P2,B_x,B_y,B_z);

  //cout << acc_x  << " " << acc_y  << " " << acc_z << endl; 

  int i = 0;
    while (i <= 10000)
    {

     float ax_p1, ay_p1, az_p1 = P1.calc_acc (P2,B_x,B_y,B_z);

     P1.Pos_evol(ax_p1,ay_p1,az_p1,0.01);

     
     float ax_p2, ay_p2, az_p2 = P1.calc_acc (P2,B_x,B_y,B_z);

     
     P2.Pos_evol(ax_p2,ay_p2,az_p2,0.01);

     cout << P1.X   << " " << P1.Y      << " " << P1.Z     << endl;

     cout << P2.X  << " " <<    P2.Y << " " << P2.Z     << endl;

     i++;
    }

  
  return 0;
}
