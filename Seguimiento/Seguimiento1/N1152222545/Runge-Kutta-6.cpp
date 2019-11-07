#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;



float F(float xn,float yn)
  {
    return xn-yn;

  }
float f(float x, float y)
{
  return x-1+2*exp(-x);
}
  

float RK6(float xn,float yn,float h)

{

 float k1 = F(xn,yn);
  float k2 = F(xn + h/3.,yn + h/3.*k1);
  float k3 = F(xn + h*3./4.,yn + h*((123./256.)*k1 + (315./256.)*k2));
  float k4 = F(xn + h/5.,yn + h*((193./750.)*k1 + (189./1250.)*k2 + (176./1875.)*k3));
  float k5 = F(xn + h*2/3,yn + h*((26./81.)*k1 + (7./15.)*k2 + (304./4455.)*k3 + (175/297)*k4));
  float k6 = F(xn + h, yn + h*((151./150.)*k1 + (351./250.)*k2 + (304./4125.)*k3 + (5/77)*k4 + (243./175.)*k5));
 return yn + h*(k1/24 + (125./336.)*k4 + (27./56.)*k5 + (5./48.)*k6);			     
			       
}

int main()

{
 float y0=1.0;
  float x0=0.0;
  float xf=5.0;
  int Num[4] = {10,100,1000,10000};
  int d=sizeof(Num)/sizeof(*Num);
  float h[d];

  ofstream ofs ("RK6.csv",ofstream::out);


  ofs<<"X"<<" "<<"Y"<<" "<<"YE"<<" "<<"Diff"<<endl;
for (int j =0; j<d;j++)
    {
  h[j]= (xf-x0)/Num[j];
   float X[Num[j]]={x0};
  float Y[Num[j]]={y0};
  float Diff[Num[j]]={0};


  ofs << X[0]<< " "<< Y[0]<<" "<<X[0]-1+2*exp(-X[0])<<" "<<Diff[0]<<endl;

for (int i = 0; i<Num[j]; i++)
    {

        X[i+1]=X[i]+ h[j];
      Y[i+1]=RK6(X[i],Y[i],h[j]);
      Diff[i+1]=fdim(Y[i+1], X[i]-1+2*exp(-X[i]));

      ofs << X[i+1]<< " "<< Y[i+1]<<" "<<X[i]-1+2*exp(-X[i])<<" "<<Diff[i+1]<<endl;


      
	//cout<<X[i+1]<< " "<<Y[i+1]<<endl;
      
	
     
    }


    }


 ofs.close();
   
 return 0;
}
