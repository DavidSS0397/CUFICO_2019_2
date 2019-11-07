#include <iostream>
#include <cmath>

/*
 * sixth order Runge-Kutta
 * 
 * By: Carolina Herrera
 * Last update: september 18, 2019
 * 
 * */


// ODE
double function(double x, double y)
{
    return x - y;
} 


// Exact solution of ODE
double exact_solution(double x)
{
    return x - 1 + 2*exp(-x);
}


// 6th order Runge-Kutta
// Assigns y_(n+1) to yn variable
void RK6(double xn, double& yn, double h, double func(double, double))
{
    double k1, k2, k3, k4, k5, k6;
    
    double a21 = 1.0/3;
    double a31 = 123.0/256, a32 = 315.0/256;
    double a41 = 193.0/750, a42 = 189.0/1250, a43 = 176.0/1875;
    double a51 = 26.0/81, a52 = 7.0/15, a53 = 304.0/4455, a54 = 176.0/297;
    double a61 = 151.0/150, a62 = 351.0/250, a63 = 304.0/4125, a64 = 5.0/77, a65 = 243.0/175;
    
    double b1 = 1.0/24, b2 = 0.0, b3 = 0.0;
    double b4 = 125.0/336, b5 = 27.0/56, b6 = 5.0/48;
    
    double c2 = 1.0/3, c3 = 3.0/4;
    double c4 = 1.0/5, c5 = 2.0/3, c6 = 1.0;
    
    k1 = func(xn, yn);
    k2 = func(xn+h*c2, yn+h*a21*k1);
    k3 = func(xn+h*c3, yn+h*(a31*k1+a32*k2));
    k4 = func(xn+h*c4, yn+h*(a41*k1+a42*k2+a43*k3));
    k5 = func(xn+h*c5, yn+h*(a51*k1+a52*k2+a53*k3+a54*k4));
    k6 = func(xn+h*c6, yn+h*(a61*k1+a62*k2+a63*k3+a64*k4+a65*k5));
    
    yn += h*(b1*k1+b2*k2+b3*k3+b4*k4+b5*k5+b6*k6);
}


int main(void)
{
    int i, steps;
    
    // Initial conditions and parameters
    double x0 = 0.0, xf = 5.0;
    double y0 = 1.0;
    double xn = x0, yn = y0;
    
    double h, y_exact, diff;
    
    // Receives steps through input
    std::cin >> steps;
    
    // Step size
    h = (xf-x0)/steps;
    
    std::cout << "#x, y_rk6, y_exact, difference" << std::endl;
    std::cout << x0 << "," << y0 << "," << y0 << "," << 0.0 << std::endl;
    
    // Solution calculation
    for(i=1;i<=steps;i++)
    {   
        // yn is updated
        RK6(xn, yn, h, function);
        
        y_exact = exact_solution(xn);
        diff = std::abs(yn-y_exact);
        
        xn += h;
        
        std::cout << xn << "," << yn << "," << y_exact << "," << diff << std::endl;
    }
    
    return 0;
}

