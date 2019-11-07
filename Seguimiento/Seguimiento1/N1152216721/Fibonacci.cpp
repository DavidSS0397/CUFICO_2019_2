/*
Program to generate a certain number N of numbers belonging to
the Fibonacci sequence, printing only the even ones.
*/

#include<iostream>

int main()
{
  /*
  List of variables:
  N: quantity of Fibonacci numbers to be generated
  counter_tot: counter to be iterated
  counter_even: counter of even Fibonacci numbers
  prev: a_{n-2} term of the Fibonacci sequence
  current: a_{n-1} term of the Fibonacci sequence
  next: a_n term of the Fibonacci sequence
  */

  int N, counter_tot, counter_even;
  unsigned long long int prev, current, next; //unsigned long long int: 0 to 18,446,744,073,709,551,615

  /*Variables initialization. 
  N = 100 to avoid extremely large numbers.
  counter_tot starts at 2 because the first Fibonacci numbers
  are not generated but given: a_0 = 1, a_1 = 1.
  */
  N = 100; counter_tot = 2; counter_even = 0; //N = 100, not 1000 because of digits overflow
  prev = 1; current = 1;


  //The following lines print the first two Fibonacci numbers.
  //std::cout << "1 is the 1st fib number" << std::endl;
  //std::cout << "1 is the 2nd fib number" << std::endl;


  //For loop to iterate from counter_tot = 3 to the given limit N.
  for (counter_tot = 3; counter_tot < N; counter_tot++)
    {
      //Fibonacci recursive formula
      next = current + prev;

      //For odd numbers, just print the number and its place on the sequence
      /*
      if (next % 2 != 0)
	{
	  std::cout << next << " is the " << counter_tot << "th fib number" << std::endl;
	}
      */
      

      //For even numbers print the number, its position on the sequence and its position
      //between the even numbers of the sequence
      //else if (next % 2 == 0)
      if (next % 2 == 0)
	{
	  counter_even += 1;
	  std::cout << next << " is the " << counter_tot << "th Fibonacci number and the " << counter_even << "th even." << std::endl;
	}
      
      //Variables replacement for next loop cycle
      prev = current;
      current = next;
    }
    
  return 0;
}
