#include <iostream> //Allows the use of inputs and outpus
#include <vector> //We will be using vectors for creating the grid where the game of life will take place

using namespace std; //lets us use, for example, cout instead of std::cout 



// Class for a being on the game of life.

class being{
public:
  int species; // species attribute, has 3 possible values: 1-species 1, 2-species 2, 0-dead being
  int x,y; // position of the being on the grid

  int neighbors[3]; // number of each type of neighbors. Pos[0]: num of 0 (dead) neighbors, Pos[1]: num of species 1 neighbors, Pos[2]: num of species 2 neighbors

  // int next_state; // attribute that sets the next state of the being in the next itaration

  void create(int i, int j, int k); //Prototype function used for creating a being with certain position (i,j) and state (k)

  void reset_neighbors(void); //Prototype function for reseting the neighbors count to 0
  void set_state(void); //Prototype function for setting the stated that a being will have in the next iteration 

  
};

//--------------------------------------------------------------------------------------------------------
// member functions of class being

// function to create a being with certain position and species
void being::create(int i, int j,int k){
  x = i; //sets x value equals to i
  y = j; //sets y value equals to j
  species = k; //sets species value equal to k
}

// function to reset the states of the neighbors of the being
void being::reset_neighbors(void){ // 
  for (int i=0; i<3; i++){ // The neighbors array is of size 3 (each item corresponding to a species)
    neighbors[i] = 0; //Sets the count for each species as 0
  }
}

// funtion to set the state of the being on the next iteration
void being::set_state(void){ 
  switch (species){ // cases that depend on the species of the being
  case 0: // if the being is dead
    if (neighbors[1] == 3 && neighbors[0] >= 2){ // if it has 3 neighbors of species 1 and 2 or more of species 0
      species = 1; //then it transforms to species 1
    }
    else if (neighbors[2] == 4 && neighbors[0] >= 1){ // if it has 4 neighbors of species 2 and one or more neighbors with value 1
      species = 2;//then it transforms to species 2
    }
    else { //if the last two conditionals aren't true
      species = 0; //then the being keeps being dead
    }
    break; //breaks the switch method

  case 1: // if the being is of species 1
    if (neighbors[1] == 2 || neighbors[1] == 3){ //if it has 2 or 3 neighbors of species 1 
      species = 1; //then it keeps being of species 1
    }
    else if (neighbors[2] >= 4 && neighbors[1] <= 1){ // if it has 4 or more neighbors of species 2 and less than 1 neighbor of species 1
      species = 2; //it transforms into species 2
    }
    else if (neighbors[1] >= 5){ //if it has 5 or more neighbors of species 1
      species = 0; //It dies
    }
    else { //if none of the conditionals are true
      species = 1; //it keeps being of species one
    }
    break; //breaks the switch method

  case 2: // if the being is of species 2
    if (neighbors[2] == 2 || neighbors[2] == 3){ //if it has 2 or neighbors of species 2
      species = 2; //then if keeps being of species 2
    }
    else if ((neighbors[1] == 4 || neighbors[1] == 5) && neighbors[2] <= 1 ){ //if it has 4 or 5 neighbors of species 1 and less than one neighbor of species 2
      species = 1; //Then it becomes of species 1
    }
    else if (neighbors[2] == 5){ //if it has 5 neighbors of species 2
      species = 0; //then it dies
    }
    else { //else
      species = 2; //it keeps being of species 2
    }
    break; //breaks the switch method
  }
}


// ------------------------------------------------------------------------------------------------------
// Class for the system in the game of life
// The system contains all the beings
class board{ //it is named board as system has conflicts with C++ compilator
public:
  int N; //As the system will be a square array, there is no need of defining lenght and height. N is the dimention of the grid

  board(){ //Constructor for the board class
    cout << "Input the dimention of the array: "; //asks for the dimention to be used
    cin >> N; //Assigns said value to N
  }
  
  vector<vector<being>> grid; //Creates a vector of vectors containing instances of being class


  void create_grid(void); //Prototype function for filling the grid with beings

  void update_grid(void); //Prototype function for updating the grid in each iteration
  void print_grid(void);  //Prototype function for printing the grid in screen

};



void board::create_grid(void){ //Defining the function that fills the grid

  grid.resize(N); //sets the number of rows for the grid vector as N
  for (int i = 0; i < N; i++){ //for used to set the number of columns for each row of grid vector
    grid[i].resize(N); //sets the number of columns for the i-th row as N
  }
  
  for (int i = 0; i < N; i++){ //Iterates over each row of grid vector

   
    for (int j = 0; j < N; j++){ //Iterates over each column of the corresponding row
      int random = rand() % 3; //Creates a random number from 0 to 2, it will be the species of the being with coordinates (i,j)
      grid[i][j].create(i,j,random); //creates a being with pos = (i,j) and species = random
    }
  }
}


void board::update_grid(void){ //Function used to update the state of each cell on the grid and thus of the whole board
  for (int i = 0; i < N; i++){ //Iterates over each row of the grid
    for (int j = 0; j < N; j++){ //Iterates over each column of the corresponding row
      //if the cell is a corner, then it only has 3 neighbors
      if ( (i == 0 && j == 0) || (i == 0 && j == (N-1)) || (i==(N-1) && j==0) || (i==(N-1) && j==(N-1))){
	int neh[] = {grid[i + 1 - 2*i/(N-1)][j].species, grid[i][j + 1 - 2*j/(N-1)].species, grid[i + 1 - 2*i/(N-1)][j + 1 - 2*j/(N-1)].species};
	//The formula 1 - 2*l(N-1) is 1 when l == 0 and -1 when l == N-1 (l = i,j). This avoids the use of a contional for each corner
	//it fills the array neh with the 3 neighbors that each corner has

	for (int k = 0; k < 3; k++){ //Iterating over the neh array
	  switch(neh[k]){ //neh has entries {N1,N2,N3..,} where Ni is a species
	  case 0: //the value for the i-th component of neh is 0
	    grid[i][j].neighbors[0] += 1; //adds +1 to the counter of neighbors of species 0 to the cell of pos(i,j)
	    break; //breaks the switch method

	  case 1: //the value for the i-th component of neh is 1
	    grid[i][j].neighbors[1] += 1; //adds +1 to the counter of neighbors of species 1 to the cell of pos(i,j)
	    break;//breaks the switch method
	    
	  case 2: //the value for the i-th component of neh is 1
	    grid[i][j].neighbors[2] += 1; //adds +1 to the counter of neighbors of species 2 to the cell of pos(i,j)
	    break;//breaks the switch method
	  }
	}
      }

      //if the cell lies on a limiting column (except for corners!)
      else if ( (j == 0) || (j == (N-1))){
	int neh[] = {grid[i + 1][j - 2*j/(N-1) + 1].species, grid[i][j - 2*j/(N-1) + 1].species, \
		     grid[i - 1][j - 2*j/(N-1) + 1].species, grid[i+1][j].species, grid[i-1][j].species};
	//The formula 1 - 2*l(N-1) is 1 when l == 0 and -1 when l == N-1 (l = i,j). This avoids the use of a contional for each limiting column
	//it fills the array neh with the 5 neighbors that each cell has
	for (int k = 0; k < 5; k++){ //iterates over neh
	  switch(neh[k]){  //neh has entries {N1,N2,N3..,} where Ni is a species
	  case 0://the value for the i-th component of neh is 0
	    grid[i][j].neighbors[0] += 1;//adds +1 to the counter of neighbors of species 0 to the cell of pos(i,j)
	    break;//breaks the switch method
	    
	  case 1://the value for the i-th component of neh is 1
	    grid[i][j].neighbors[1] += 1;//adds +1 to the counter of neighbors of species 1 to the cell of pos(i,j)
	    break;//breaks the switch method
	    
	  case 2://the value for the i-th component of neh is 2
	    grid[i][j].neighbors[2] += 1;//adds +1 to the counter of neighbors of species 2 to the cell of pos(i,j)
	    break;//breaks the switch method

	  }
	}
      }
      
      //if the cell lies on a limiting row (except for corners!)
      else if ( (i == 0) || (i == (N-1))){

	int neh[] = {grid[i - 2*i/(N-1) + 1][j + 1].species, grid[i - 2*i/(N-1) + 1][j].species, \
		     grid[i - 2*i/(N-1) + 1][j - 1].species, grid[i][j - 1].species, grid[i][j + 1].species};
	//The formula 1 - 2*l(N-1) is 1 when l == 0 and -1 when l == N-1 (l = i,j). This avoids the use of a contional for each limiting column
	//it fills the array neh with the species of the 5 neighbors that each cell has
	
	for (int k = 0; k < 5; k++){ //iterates over neh
	  switch(neh[k]){  //neh has entries {N1,N2,N3..,} where Ni is a species
	  case 0: //the value for the i-th component of neh is 0
	    grid[i][j].neighbors[0] += 1;//adds +1 to the counter of neighbors of species 0 to the cell of pos(i,j)
	    break;//breaks the switch method
	    
	  case 1: //the value for the i-th component of neh is 1
	    grid[i][j].neighbors[1] += 1;//adds +1 to the counter of neighbors of species 1 to the cell of pos(i,j)
	    break;//breaks the switch method
	    
	  case 2: //the value for the i-th component of neh is 2
	    grid[i][j].neighbors[2] += 1;//adds +1 to the counter of neighbors of species 2 to the cell of pos(i,j)			 
	    break;//breaks the switch method
	    
	  }
	}
      }
      //else, if the cell is a inner cell i.e it doesn't lie on a corner of a limiting row/column
      else {

	int neh[] = {grid[i][j+1].species, grid[i][j-1].species, grid[i+1][j].species, grid[i-1][j].species, \
		     grid[i+1][j+1].species, grid[i+1][j-1].species, grid[i-1][j+1].species, grid[i-1][j-1].species};
	//it fills the neh array of each inner cell with the species of the 8 neighbors that each cell has
	for (int k = 0; k < 8; k++){//Iterates over neh
	  switch(neh[k]){  //neh has entries {N1,N2,N3..,} where Ni is a species
	  case 0: //the value for the i-th component of neh is 0
	    grid[i][j].neighbors[0] += 1; //adds +1 to the counter of neighbors of species 0 to the cell of pos(i,j)
	    break;//breaks the switch method
	    
	  case 1: //the value for the i-th component of neh is 1
	    grid[i][j].neighbors[1] += 1; //adds +1 to the counter of neighbors of species 1 to the cell of pos(i,j)
	    break;//breaks the switch method
	    
	  case 2: //the value for the i-th component of neh is 2
	    grid[i][j].neighbors[2] += 1;//adds +1 to the counter of neighbors of species 2 to the cell of pos(i,j)			 
	    break;//breaks the switch method

	  }
	}
      }
    }
  }

  for (int i=0; i<N; i++){ //iterates over each row of the grid
    for (int j=0; j<N; j++){ //iterates over each column of the corresponding row
      grid[i][j].set_state(); //updates the state of each cell based on its neighbors
    }
  }

  for (int i=0; i<N; i++){ //Iterates over each row
    for (int j=0; j<N; j++){ //Iterates over each column of the corresponding row
      grid[i][j].reset_neighbors(); //resets the count of the neighbors of each cell to 0
    }
  }
  
}



void board::print_grid(void){ //Function used for printing the current grid on screen
  for (int i = 0; i < N; i++){ //iterates over each row
    for (int j = 0; j < N; j++){  //iterates over each column of the corresponding row
      if (j == N -1){ //if it is the las element of the row
	cout << grid[i][j].species << endl; //prints and goes to a new line
      }

      else { //if it is any other element
	cout << grid[i][j].species << " "; //prints but doesn't go to a new line
      }
    }
  }
}

 
int main(){ //Creating the main function

  board Game; //Creates a board called Game
  

  Game.create_grid(); //Creates the grid

  system("clear"); //Clears the terminal, only works for bash terminal, use system("CLS") if using cmd
  
  for (int i=0; i<1000; i++){ //Iterates 1000 times
    Game.print_grid(); //prints the current grid
    Game.update_grid(); //updates the grid
    system("sleep 0.3"); //waits for 300 ms
    system("clear"); //Clears the terminal once again
  }
  return 0; //returns a value of 0 
}
