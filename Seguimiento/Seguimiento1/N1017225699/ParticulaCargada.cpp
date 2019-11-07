#include<iostream>
#include <fstream>
using namespace std;


class Particle
{
	public:
	int Carga;
	float X,Y,Z;
	float VX, VY, VZ;
	float M;
	void SetValues(float,float,float,float,float,float,float,int);
	float Avanzar(float);
	//void time_slice_print();
};


void Particle::SetValues(float x,float y,float z,float vx,float vy,float vz,float m,int Car)
{
	X=x;
	Y=y;
	Z=z;
	VX=vx;
	VY=vy;
	VZ=vz;
	M=m;
	Carga=Car;
}


float Particle::Avanzar(float delta)
{
	
	float fx = Carga*VY*10.0;
	float fy= -Carga*VX*10.0;
	float fz=0;	

	
	VX=VX+ fx*delta/M;
	VY=VY+ fy*delta/M;
	VZ=VZ+ fz*delta/M;

	X=X + VX*delta;
	Y=Y + VY*delta;
	Z=Z + VZ*delta;
}

int main()
{
		int j;
		Particle Particula1;

		Particula1.SetValues(1,0,0,0,-1,0,10,1);
		
		ofstream myfile;
  		myfile.open ("posicion.txt");
  		
  		

		for(j=1; j<10000; j=j+1){
			//cout << j << endl;
			float delta=0.001;	
			Particula1.Avanzar(delta);
			myfile << Particula1.X << " " <<Particula1.Y << " " << Particula1.Z <<endl;
			cout << Particula1.X <<" "<<Particula1.Y << " " << Particula1.Z << endl;
	   	}
		myfile.close();
		return 0;

}

