#include <iostream> //Allows using coutfor printing in screen with cout, getting input with cin, and ending lines with endl
#include <vector> //Allows using vectors to store data, specifically 2D vectors
#include <stdlib.h>//Allows putting comands directly into the terminal with std::system(); and use std::rand() to generate random numbers
#include <time.h> //The time library to give time as a seed for the randomizer
using namespace std; //Allows stop writing std:: for every standard function
int usrInput(void) //A function to ask for user input (For this case, the size of the grid)
{
  int n; //the height and width of the grid
  cout << "Please enter the size of the grid for the simulation: "; //Prints in screen this text
  cin >> n; //puts the usr input into the n variable
  cout << "The grid will have dimension " << n << "x" << n << endl; //confirms the size of the grid
  return n; //Returns the value to be used in-code
}

class matrix //A matrix class where the game will ocour
{
public://The atributes and methods that can be used in all the code
  int N; //height and lenght of the matrix
  vector< vector<int> > entries; //The actual matrix
  void gridCreator(int); //A functions that creaters the matrix
  void gridPrint(void); //prints the matrix
  vector< vector<int> > getNeigh(int,int);//a function that returns the 3x3 neighbourhood with the ij entry at it's centre
  vector<int> studyNeigh(int,int);//returns the value of the ij entry, and how many 0,1 and 2 neighbours it has
  int newVal(int,int); //studies to wich value would the ij entry evolve to
  vector< vector<int> > getEvo(void); //Returns the next evolution of the grid
  void EVOLVE(void); //EVOLVES
} grid1; //Creates an instance of a matrix called "grid1"

void matrix::EVOLVE(void)//EVOLVES
{
  entries = getEvo();//uses the function getEvo() to update the next iteration of the grid into "entries"
}

vector< vector<int>  > matrix::getEvo(void)//a method that returns the state of a matrix after an itertion
{
  vector< vector<int> > evo; //A vector of vectors to store the new state of the grid  
  int nV; //an int to store the new value of the cell
  for (int i = 0; i < N; i++)//iterates over each row of the matrix
    {
      vector<int> row; //a row to store values before passing them to "evo"
      for (int j = 0; j < N; j++)//iterates over each column of the matrix
	{
	  nV = newVal(i,j);//Stores the new value of the ij cell in nV
	  row.push_back(nV);//Puts the new value of the cell at the end of the vector
	}
      evo.push_back(row);//adds the updated row to the "evo" grid
    }
  return evo;//returns the evolved grid
}

int matrix::newVal(int i, int j)//returns the value a cell would evolve to after an iteration
{
  vector<int> nInf = studyNeigh(i,j);//put's the neighborhood's info in nInf
  int nV; //the new value for the cell in the middle
  if ( nInf[0] == 0 )//Checks if the value in the cell is zero
    {
      if ( (nInf [2] == 3) && (nInf[1] >= 2 ) )//Checks if the first rule is met
	{
	  nV = 1;//sets the new value of the cell to 1
	}
      else if ( (nInf [3] == 4) && (nInf[1] >= 1 ) )//Checks if the second rule is met
	{
	  nV = 2;//sets the new value of the cell to 2
	}
      else//acts if no condition is met
	{
	  nV = nInf[0];//sets the new value of the cell to the original one
	}
    }
  if ( nInf[0] == 1 )//Checks if the value in the cell is one
    {
      if ( (nInf [2] == 3) || (nInf [2] == 2) )//Checks if the third rule is met
	{
	  nV = 1;//sets the new value of the cell to 1
	}
      else if ( (nInf [3] >= 4) && (nInf[2] <= 1 ) )//cheks if the fifth rule is met
	{
	  nV = 2;//sets the new value of the cell to 2
	}
      else if (nInf [2] >= 5)//Checks if the seventh rule is met
	{
	  nV = 1;//sets the new value of the cell to 1
	}
      else//acts if no condition is met
	{
	  nV = nInf[0];//sets the new value of the original one
	}
    }
  if ( nInf[0] == 2 )//Checks if the value in the cell is two
    {
      if ( (nInf [3] == 3) || (nInf [3] == 2) )//Checks if the fourth rule met
	{
	  nV = 2;//sets the new value of the cell to 2
	}
      else if ( ( (nInf [2] == 4) || (nInf[2] == 5) ) && (nInf[3] <= 1) )//checks if the sixth rule is met
	{
	  nV = 1;//sets the new value of the cell to 1
	}
      else if (nInf [3] >= 5)//checks if the eight rule is met
	{
	  nV = 0;//sets the new value of the cell to 0
	}
      else//acts if no condition is met
	{
	  nV = nInf[0];//sets the new value of the cell to it's original
	}
    }
  return nV; //Returns the new value for the cell
}

vector<int> matrix::studyNeigh(int i,int j)//returns a vector with the ij cell value, and the number of 0,1 and 2 neighbours
{
  vector<int> toReturn;//To return, it has the (i,j) value, and the number of 0, 1, and 2 neighbours on that order
  vector< vector<int> > neigh = getNeigh(i,j); //Gets the 3x3 neighborhood centered at ij
  toReturn.push_back(neigh[1][1]); //puts the center value into the first entry of the vector to return
  toReturn.push_back(0);//Adds a zero to the end of the vector
  toReturn.push_back(0);//Adds a zero to the end of the vector
  toReturn.push_back(0);//Adds a zero to the end of the vector 
  for (int c1 = 0; c1 < 3; c1++)//Iterares trough the rows of the 3x3 neighborhood
    {
      for (int c2 = 0; c2 < 3; c2++)//iterates trough the columns of the neighborhood
	{
	  if ( (c1 != 1) || (c2 != 1) )//checks if the cell is diferent to the one in the middle
	    {
	      if(neigh[c1][c2] == 0)//checks if the value of the cell is 0
	       {
		 toReturn[1] +=1;//adds 1 to the count of neighbours valued 0
	       }
	     if(neigh[c1][c2] == 1)//checks if the value of the cell is 1
	       {
		 toReturn[2] +=1;//adds 1 to the count of neighbours valued 1
	       }
	     if(neigh[c1][c2] == 2)//checks if the value of the cell is 2
	       {
		 toReturn[3] +=1;//adds 1 to the count of neighbours valued 2
	       }
	    }
	}
    }
  return toReturn;//Returns the vector with the count of the neighbours and the value in the center
}

vector< vector<int> > matrix::getNeigh(int i, int j) //a function that returns que 3x3 matrix with the ij entry at it's centre
{
  vector<int> row1 = {404,404,404};//the row above the entry being studied, 404 is a filler value in case a neighbour cannot be added
  vector<int> row2 = {404,404,404};//the row above the entry being studied, 404 is a filler value in case a neighbour cannot be added
  vector<int> row3 = {404,404,404};//the row above the entry being studied, 404 is a filler value in case a neighbour cannot be added
  vector< vector<int> > toReturn; //A vector to store row1, row2 and row3
  if ( (i-1 >= 0) && (j-1 >= 0) )//checks if upper left neighbour is within bounds
    {
    row1[0] = entries[i-1][j-1];//Adds upper left neighbour to the top row
    }
  if ( i-1 >= 0)//checks if upper neighbour is within bounds
    {
      row1[1] = entries[i-1][j];//adds the top neighbour to th top row
    }
  if ( (i-1 >= 0) && (j+1 < N) )//checks if upper right neighbour is within bounds
    {
      row1[2] = entries[i-1][j+1];//adds upper right neighbour to the top row
    }
  if ( j-1 >= 0)//checks if left neihgbour is within bounds
    {
      row2[0] = entries[i][j-1];//adds the left neightbour to the row of the middle
    }
  row2[1] = entries[i][j]; //Adds the entry whose neighbours are being studied to the middle row
  if ( j+1 < N)//checks if the right neighbour is within bounds
    {
      row2[2] = entries[i][j+1];//adds the right neighbour to the middle row
    }
  if ( (i+1 < N) && (j-1 >= 0) )//checks if bottom left neighbour is within bounds
    {
      row3[0] = entries[i+1][j-1];//adds bottom left neighbour to the bottom row
    }
  if ( i+1 < N)//checks if bottom neighbour is within bounds
    {
      row3[1] = entries[i+1][j];//Adds bottom neighbour to the bottom row
    }
  if ( (i+1 < N) && (j+1 < N) )//checks if the bottom right neighbour is within bounds
    {
      row3[2] = entries[i+1][j+1];//Adds bottom right neighbour to the bottoms row
    }
  toReturn.push_back(row1);//puts the upper neighbours' row into the matrix to return
  toReturn.push_back(row2);//puts the side neighbours' row into return
  toReturn.push_back(row3);//puts the bottom neighbours' row into the matrix to return
  return toReturn;//returns the 3x3 neighborhood with the entry being studied in it's centre
}

void matrix::gridCreator(int n) // A function that returns a n by n matrix of zeroes
{
  N = n;//gives the atribute N the value height and width of the matrix
  int entry; // a variable to store the value of an entry of the matrix
  vector< vector<int> > grid; //Creates vector of vectors of integres; the vector have undefined sizes
  for (int i = 0; i < n; i++) //iterates over the rows of the matrix
    {
      vector<int> row; //a vector to be used as a row
      for (int j = 0; j < n; j++)//iterates over columnns of the matrix
	{
	  entry = rand() %3; //Stores a random value between 0 and 2 in "entry"
	  row.push_back(entry); //adds the random value to the row
	}
      grid.push_back(row); //appens a vector of zeroes of lenght n to the end of the "grid" vector
    }

  entries = grid; //Uses "grid" as the entries for the instance
}

void matrix::gridPrint(void) //a function that prints the entries of an instance changing numbers of other charachters
{
  int n = entries.size();// gets the values for the
  for(int i = 0; i < n; i++)//iterates over the rows of the matrix
  {
    for(int j = 0; j < n; j++)//iterates over the columns of the matrix
      {
	if (entries[i][j] == 0)//checks if the entry has a zero on it
	  {
	    cout << " " << " "; //prints a dotted circle instead of a 0
	  }
	if (entries[i][j] == 1)//checks if the entry value is 1
	  {
	    cout << "■" << " ";//prints asquare instead of a one
	  }
	if (entries[i][j] == 2)//checks if the entry value is 2
	  {
	    cout << "●" << " ";//prints a circle instead of a 2
	  }
      }
    cout << endl;//ends the row
  }
  cout << endl;//ends the final row
}

int main(void) // The main code to be executed
{
  int n = usrInput(); //Asks the user for the dimension of the matrix
  srand(time(NULL));//seeds the randomizer 
  grid1.gridCreator(n);//creates the grid for the game
  system("sleep 2");//asks bash to wait for two seconds
  system("clear");//asks bash to clear the screen
  grid1.gridPrint();//prints the initial state of the game
  for (int i = 0; i < 10000; i++)//iterates over 10000 states of the game
    {
      system("sleep .1");//asks bash to wait a moment
      system("clear");//asks bash to clear the screen
      grid1.EVOLVE();//evolves the grid to the next state
      grid1.gridPrint();//prints the state of the grid
    } 
  return 0; // returns 0 in  main()
}
