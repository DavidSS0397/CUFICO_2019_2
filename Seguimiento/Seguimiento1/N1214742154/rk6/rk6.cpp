#include <iostream>
//#include <tuple> //Allows returning more than one value from functions by using std::make_tuple
#include <vector>

using namespace std;


//Giving values to the constants

float c1 = 0, c2 = 1./3., c3 = 3./4., c4 = 1./5., c5 = 2./3., c6 = 1.; //The C values
float b1 = 1./24., b2 = 0, b3 = 0, b4 = 125./336., b5 = 27./56., b6 = 5./48., b7 = 0; //the B values

float a11 = 0;
float a21 = 1/3, a22 = 0;
float a31 = 123/256, a32 = 315/256, a33 = 0;
float a41 = 193/750, a42 = 189/1250, a43 = 176/1875, a44 = 0;
float a51 = 26/81, a52 = 7/15, a53 = 304/4455, a54 = 175/297, a55 = 0;
float a61 = 151/150, a62 = 351/250, a63 = 304/4125, a64 = 5/77, a65 = 243/175, a66 = 0;


//defining the function
float myFunc(float xn, float yn) //The function that equals y'
{
  return xn-yn;
}


//defining values
float x0 = 0;//initial x
float xf = 5;//final x
float y0 = 99.001;//the initial height
float NumPuntos = 10000;//number of points
float h = (xf-x0)/NumPuntos;//the step size. MIGHT PRODUCE ERRORS DUE TO FLOAT-INT DIVISION 


/*
struct valPair // a structure to return from the rungekuta method
{
  float val1;
  float val2;
}
*/

vector<float> rungeKutta(float xn, float yn, float h, float (*func)(float xn, float yn))// The RungeKutta method, returns a tupple
{
  float xnPlus1 = xn + h;

  float k1 = func(xn,yn);
  //cout << "k1: " << k1 << "=?" << func(xn,yn)  << endl;
  
  float k2 = func(xn+h*c2, yn+h*(a21*k1));
  //cout << "k2: " << k2 << "=?" << func(xn+h*c2, yn+h*(a21*k1))  << endl;

  float k3 = func(xn+h*c3, yn+h*(a31*k1+a32*k2));
  //cout << "k3: " << k3 << "=?" << func(xn+h*c3, yn+h*(a31*k1+a32*k2))  << endl;

  float k4 = func(xn+h*c4, yn+h*(a41*k1+a42*k2+a43*k3));
  //cout << "k4: " << k4 << "=?" << func(xn+h*c4, yn+h*(a41*k1+a42*k2+a43*k3))  << endl;

  float k5 = func(xn+h*c5, yn+h*(a51*k1+a52*k2+a53*k3+a54*k4));
  //cout << "k5: " << k5 << "=?" << func(xn+h*c5, yn+h*(a51*k1+a52*k2+a53*k3+a54*k4))  << endl;

  float k6 = func(xn+h*c6, yn+h*(a61*k1+a62*k2+a63*k3+a64*k4+a65*k5));
  //cout << "k6: " << k6 << "=?" <<  func(xn+h*c6, yn+h*(a61*k1+a62*k2+a63*k3+a64*k4+a65*k5))  << endl;
  
  //cout << "yn: " << yn << endl;

  //cout << "h: " << h << endl;
  
  //cout << "to add: " << h*(b1*k1+b2*k2+b3*k3+b4*k4+b5*k5+b6*k6) << endl;

  //cout << "second factor: " << (b1*k1+b2*k2+b3*k3+b4*k4+b5*k5+b6*k6) << endl;
  
  //cout << "y_n+1: " << yn + h*(b1*k1+b2*k2+b3*k3+b4*k4+b5*k5+b6*k6) << endl;


  
  /*
  cout << "b1: " << b1 << " k1:" << k1  << endl;
  cout << "b1*k1: " << b1*k1 << endl;

  cout << "b2: " << b2 << " k2:" << k2  << endl;
  cout << "b2*k2: " << b2*k2 << endl;

  cout << "b3: " << b3 << " k3:" << k3  << endl;
  cout << "b3*k3: " << b3*k3 << endl;

  cout << "b4: " << b4 << " k4:" << k4  << endl;
  cout << "b4*k4: " << b4*k4 << endl;

  cout << "b5: " << b5 << " k5:" << k5  << endl;
  cout << "b5*k5: " << b5*k5 << endl;

  cout << "b6: " << b6 << " k6:" << k6  << endl;
  cout << "b6*k6: " << b6*k6 << endl;
  */


  /*
  cout << "c1: " << c1 << endl;
  cout << "c2: " << c2 << endl;
  cout << "c3: " << c3 << endl;
  cout << "c4: " << c4 << endl;
  cout << "c5: " << c5 << endl;
  cout << "c6: " << c6 << endl;
  */
  
  float ynPlus1 = yn + h*(b1*k1+b2*k2+b3*k3+b4*k4+b5*k5+b6*k6);
  

  vector<float> toReturn = {xnPlus1, ynPlus1};
  
  return toReturn; //makes a tuple and returns two values    
}


int main(void)
{
  
  vector<float> xValues;//vector to store the x coordinates
  vector<float> yValues;//vector to store the y coordinates

  xValues.push_back(x0);
  yValues.push_back(y0);

  vector<float> auxVector; //auxiliar tuple
  
  for (int i = 0; i < NumPuntos; i++)//Fills the vectors with the points coordinates of the numerical solution
    {
      auxVector = rungeKutta(xValues.at(i), yValues.at(i), h, myFunc);
      xValues.push_back(auxVector.at(0)); //Gets the value out of the tuple into the vector
      yValues.push_back(auxVector.at(1)); //Gets the value out of the tuple into the vector
      
    }
  

  for (int i = 0; i < xValues.size(); i++)
    {
      cout <<  xValues.at(i) << "," << yValues.at(i) << endl;
    }
  
  return 0;
}
