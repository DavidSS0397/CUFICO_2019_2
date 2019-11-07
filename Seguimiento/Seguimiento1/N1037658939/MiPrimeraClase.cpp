#include <iostream>
using namespace std;

/*
 * Charged particle in a magnetic field.
 * 
 * By: Carolina Herrera S.
 * Updated: Sept 5, 2019
 * 
 * */


struct Force
{
    float X, Y, Z;
};


class Particle
{
    public:
        int Charge;
        float X, Y, Z;
        float VX, VY, VZ;
        float M;
        
        void SetValues(float, float, float, float, float, float, float, int);
        void Pos_evol(const Force&, float);
} Particle1;


void Particle::SetValues(float x, float y, float z, float vx, float vy, float vz, float m, int charge)
{
    X = x;
    Y = y;
    Z = z;
    VX = vx;
    VY = vy;
    VZ = vz;
    M = m;
    Charge = charge;
}


// Receives Force structure by reference
void Particle::Pos_evol(const Force& force, float dt)
{
    float ax, ay, az;
    
    ax = force.X/M;
    VX += ax*dt;
    X += (VX*dt)+(0.5*ax*dt*dt);
    
    ay = force.Y/M;
    VY += ay*dt;
    Y += (VY*dt)+(0.5*ay*dt*dt);
    
    az = force.Z/M;
    VZ += az*dt;
    Z += (VZ*dt)+(0.5*az*dt*dt);
}


// Lorentz force. No electric field
// Receives class Particle object and Force structure by reference
void Lorentz_force(const Particle& Particle1, Force& force)
{
    float Bz = 10.0;
    
    force.X = Particle1.Charge*Particle1.VY*Bz;
    force.Y = -Particle1.Charge*Particle1.VX*Bz;
    force.Z = 0;
}


int main()
{
    float x = 0.0, y = 0.0, z = 0.0;
    float vx = 1.0, vy = 1.0, vz = 0.0;
    float m = 2.0;
    float dt = 0.001;
    int q = 1;
    int i, steps = 10000;
    Force lorentz_force;
    
    // Set values for particle
    Particle1.SetValues(x, y, z, vx, vy, vz, m, q);
    
    // Evolution
    for(i=0; i<steps; i++)
    {
        // Update force components
        Lorentz_force(Particle1, lorentz_force);
        
        // Evolution given force
        Particle1.Pos_evol(lorentz_force, dt);
        
        // Uncomment to print X, Y, Z values each step
        //cout << Particle1.X << " " << Particle1.Y << " " << Particle1.Z << endl;
    }
    
    return 0;
}

