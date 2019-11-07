#include<iostream>

  /* Program to compute the dynamics of a particle of mass m 
and charge q, with initial position (x0, y0, z0), and initial 
velocity (vx0, vy0, vz0), immersed in an electromagnetic
field (Ex, Ey, Ez) and (Bx, By, Bz).

ADDITIONAL VARIABLES:
T: total time of interaction
N: Number of iterations
Tstep: time step for evolution of the system ( = T/N)
  */

//**FUNCTIONS NEEDED FOR COMPUTATIONS

//ith-component of the Cross Product of vectors (Ui, Uj, Uk) and (Vi, Vj, Vk)
double CP(double Uj, double Uk, double Vj, double Vk)
{
  double cp_i = Uj * Vk - Uk * Vj;
  return(cp_i);
}

//ith-component of the Lorentz force on a particle of
//charge parCh and velocity (parVi, parVj, parVk) due to the
//fields (Ei, Ej, Ek) and (Bi, Bj, Bk)
double LorentzForce(float ParCh,
		    double parVj, double parVk,
		    double Ei, double Bj, double Bk)
{
  double LF = ParCh * (Ei + CP(parVj, parVk, Bj, Bk));
  return(LF);
}

//**Class associated to the interacting particle
class Particle
{
public:

  float mass, charge;
  double posx, posy, posz;
  double velx, vely, velz;
  
  void SetValues(float,float,
		 double,double,double,
		 double,double,double);

  double Acel_Evol(double); //Acceleration = [Force] / mass

  double Vel_Evol(double, double); //Velocity = [V0] + [A]t

  double Pos_Evol(double, double, double) //Position = [P0] + [V0]t + (1/2)[A]t^2
};

//Setting values for the properties of the particle
void Particle::SetValues(float Mass, float Charge,
			 double Posx, double Posy, double Posz,
			 double Velx, double Vely, double Velz)
{
  mass = Mass;
  charge = Charge;
  posx = Posx;
  posy = Posy;
  posz = Posz;
  velx = Velx;
  vely = Vely;
  velz = Velz;
}

//Acceleration of the particle in terms of the force exerted on it
double Particle::Acel_Evol(double Force)
{
  Ax = LorentzForce(float ParCh,
		    double parVy, double parVz,
		    double Ex, double By, double Bz) / Particle.mass;
  Ay = LorentzForce(float ParCh,
		    double parVz, double parVx,
		    double Ey, double Bz, double Bx) / Particle.mass;
  Az = LorentzForce(float ParCh,
		    double parVx, double parVy,
		    double Ez, double Bx, double By) / Particle.mass;
}


int main(void)
{
  Particle Particle1;
  
  float q, m;
  double x0, y0, z0, vx0, vy0, vz0;
  double Ex, Ey, Ez, Bx, By, Bz;
  float T, Tstep;
  int N;

  //System parameters
  q = 1.; m = 1.;

  x0 = 0.0; y0 = 0.0;  z0 = 0.0;
  vx0 = 1.0; vy0 = 1.0; vz0 = 1.0;
  
  Ex = 1.0; Ey = 2.0; Ez = 3.0;
  Bx = 4.0; By = 5.0; Bz = 6.0;

  //Computation parameters
  T = 1.0; N = 1000;
  Tstep = T / N;

  /* Test of the function for cross product
  std::cout << CP(2., 3., 2., 1.) << std::endl;
  std::cout << CP(3., 1., 1., 3.) << std::endl;
  std::cout << CP(1., 2., 3., 2.) << std::endl;
  */
  return(0);
}
