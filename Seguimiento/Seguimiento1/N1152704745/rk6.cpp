  #include <iostream>
#include <math.h>

// runge kutta coeffitients
double a_2 = 1.0/3.0;
double a_3[]={123.0/256.0, 315.0/256.0}, a_4[]={193.0/750.0, 189.0/1250.0, 176.0/1875.0}, a_5[]={26.0/81.0, 7.0/15.0, 304.0/4455.0, 176.0/297.0}, a_6[]={151.0/150.0, 351.0/250.0, 304.0/4125.0, 5.0/77.0, 243.0/175.0};
double c[]={1.0/3.0, 3.0/4.0, 1.0/5.0, 2.0/3.0, 1.0}, b[]={1.0/24.0, 0.0, 0.0, 125.0/336.0, 27.0/56.0, 5.0/48.0};


// runge kutta 6 method
double rk6(double xn, double yn, double h, double (*f_prime)(double, double)){

  double k1 = f_prime(xn, yn);
  double k2 = f_prime(xn + h*c[0], yn + h*(a_2*k1));
  double k3 = f_prime(xn + h*c[1], yn + h*(a_3[0]*k1 + a_3[1]*k2));
  double k4 = f_prime(xn + h*c[2], yn + h*(a_4[0]*k1 + a_4[1]*k2 + a_4[2]*k3));
  double k5 = f_prime(xn + h*c[3], yn + h*(a_5[0]*k1 + a_5[1]*k2 + a_5[2]*k3 + a_5[3]*k4));
  double k6 = f_prime(xn + h*c[4], yn + h*(a_6[0]*k1 + a_6[1]*k2 + a_6[2]*k3 + a_6[3]*k4 + a_6[4]*k5));

  double k[]={k1, k2, k3, k4, k5, k6};
  double bk=0;

  for (int i=0; i<6; i++){
    bk += b[i]*k[i];
  }

  return yn + h*bk;
}


// ODE
double y_prime(double x,double y){

  return x - y;
}

// Exact solution
double exact_sol(double x){
  // with initial values (0,0)

  return 2*exp(-x) + x - 1.;
}

//---------------------------------------------------------------------

int main(){

  // Initial value of x
  double x_i=0., y=1.;

  int num_points[4]={10,100,1000,10000};
  double x_f = 5.;

  for (int i=0; i<4; i++){

    // print first solution pair (x,y) printed
    std::cout << x_i << "," << y << "," << exact_sol(x_i) << std::endl;

    // step for runge kutta
    double h = (x_f - x_i)/num_points[i];

    double x = x_i;
    
    for (int j=1; j<num_points[i]; j++){
      y = rk6(x, y, h, y_prime);
      x += h;
      std::cout << x << "," << y << "," << exact_sol(x) << std::endl;
    }

    y = 1.;
  }
  
  return 0;
}
