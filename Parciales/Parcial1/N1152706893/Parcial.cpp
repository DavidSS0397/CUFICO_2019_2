/*Estudiantes: 
Luisa Fernanda Vargas Restrepo
C.C 1.152.706.893

Julian Andres Montoya Carvajal
C.C 1.247.279.27
*/

#include <iostream>
#include <stdlib.h> //libreria que contiene prototipos de funciones para gestion de memoria dinamica, control de procesos y otras 
#include <string> //libreria cadena de textos
#include <vector>
#include <cstdlib> //esta incluida en la libreria estandar y la pusimos para el rand()
#include <ctime> //libreria para numeros aleatorios
#include <unistd.h> //la pusimos para el size

using namespace std;

class JuegoDeLaVida {
    private:
        vector< vector<int> > tablero;
        int x,y,nc;
    public:
        JuegoDeLaVida(int tamanoTablero, int numeroEspecies){
            srand(time(0)); // inicializamos el generador de numeros aleatorios
            tablero.resize(tamanoTablero); //le digo al vector que se ajuste al valor ingresado
            for(int i =0; i< tablero.size(); i++){
                tablero[i].resize(tamanoTablero); //dimensiona los elementos internos de la matriz
            }
            //inicializo el tablero en 0
            for(int a = 1; a < tablero.size(); a++){
                for(int b = 1; b < tablero.size(); b++){
                    tablero[a][b]=0;
                }
            }
            nc = numeroEspecies;
            //TODO: Cambiar ciclo por funcion random que genere las especies.
            for(int i=0;i<nc;i++){
	        x = ( rand() % ( tamanoTablero-1 ) + 1); //ubica las especies en los elementos de la matriz de manera aleatoria
                y = ( rand() % ( tamanoTablero-1 ) + 1);
                int especie =  ( rand() % ( 2 ) + 1); //genera las especies 1 o 2 aleatoriamente
                tablero[x][y] = especie; //representa una especie
                pintarTablero();
                clearScreen();
            }
        }

        void pintarTablero();
        void determinarEstado();
        void clearScreen(void);
};

int main(){

    int tamanoTablero; // Tamaño del tablero al iniciar
    int numeroEspecies;
    string iniciar;

    cout << " JUEGO DE LA VIDA - en C++ " << endl;
    cout << endl;
    cout << "Ingrese el tamaño de la matriz: ";
    cin >> tamanoTablero;

    cout << "Ingrese el numero de Especies: ";
    cin >> numeroEspecies;
    if(numeroEspecies > (tamanoTablero*tamanoTablero)){ //la cantidad de especies (1 o 2) no puede superar los elementos nxn de la matriz
        cout << "El numero de especies es mayor a tamano del tablero";
        return 0;
    }

    tamanoTablero++; //Le incrementamos en uno porque sino me muestra una matriz de n-1*n-1
    JuegoDeLaVida juego(tamanoTablero, numeroEspecies);
    cout << endl;

    cout << "Configuracion completa. Iniciar el juego? (s/n)" << endl;
    juego.pintarTablero();

    cin >> iniciar;
    if( iniciar == "s" || iniciar == "S" ){ //no importa si el usuario escribe s en minuscula o mayuscula
        for(int x = 0; x <  1000; x++){
            juego.pintarTablero();
            juego.determinarEstado();
	    cout << endl;
	    cout << "Iteracion Nro: " << x ;
	    cout << endl;
	    usleep(1000000); // ejecuta la iteracion cada segundo
	    //cout << "Presiona enter para habilitar las iteraciones";
	    //cin.get(); Esto me permite que el enter habilite las iteraciones
	    juego.clearScreen(); 
          }
      } else{
        return 0;
    }
}

void JuegoDeLaVida::clearScreen(void) {
  system("clear"); //limpia la pantalla
}

void JuegoDeLaVida::pintarTablero(){
    for(int a = 1; a < tablero.size(); a++){
        for(int b = 1; b < tablero.size(); b++){
            if(tablero[a][b] == 0){
                cout << " 0 ";
            }
            else{
                cout << " " << tablero[a][b] << " ";
            }
            if(b == tablero.size()-1){
                cout << endl;
            }
        }
    }
}

void JuegoDeLaVida::determinarEstado(){ //voy a comprobar las 8 posiciones de cada uno de los elementos del array
    int vecinos0= 0;
    int vecinos1= 0;
    int vecinos2= 0;
    int tableroSize =  tablero.size();
    for(int a = 1; a < tableroSize; a++){
        for(int b = 1; b < tableroSize; b++){
            //Comprobacion de Vecinos
                if( a-1 > 0 ){
                        if(tablero[a-1][b] == 0){
                            vecinos0++;
                        }
                        if(tablero[a-1][b] == 1){
                            vecinos1++;
                        }
                        if(tablero[a-1][b] == 2){
                            vecinos2++;
                        }

                       if( b-1 > 0 ){
                            if(tablero[a-1][b-1] == 0){
                                vecinos0++;
                            }
                            if(tablero[a-1][b-1] == 1){
                                vecinos1++;
                            }
                            if(tablero[a-1][b-1] == 2){
                                vecinos2++;
                            }

                        if( b+1 < tablero.size() ){
                            if(tablero[a-1][b+1] == 0){
                                vecinos0++;
                            }
                            if(tablero[a-1][b+1] == 1){
                                vecinos1++;
                            }
                            if(tablero[a-1][b+1] == 2){
                                vecinos2++;
                            }
                       }
                    }
                }
                if( b-1 > 0 ){
                    if(tablero[a][b-1] == 0){
                            vecinos0++;
                        }
                        if(tablero[a][b-1] == 1){
                            vecinos1++;
                        }
                        if(tablero[a][b-1] == 2){
                            vecinos2++;
                        }

                }
                if( (a+1) < tablero.size() ){
                    if(tablero[a+1][b] == 0){
                        vecinos0++;
                    }
                    if(tablero[a+1][b] == 1){
                        vecinos1++;
                    }
                    if(tablero[a+1][b] == 2){
                        vecinos2++;
                    }
                    if( b+1 < tablero.size() ){
                            if(tablero[a+1][b+1] == 0){
                                vecinos0++;
                            }
                            if(tablero[a+1][b+1] == 1){
                                vecinos1++;
                            }
                            if(tablero[a+1][b+1] == 2){
                                vecinos2++;
                            }
                    }
                    if( b-1 > 0 ){
                        if(tablero[a+1][b-1] == 0){
                            vecinos0++;
                        }
                        if(tablero[a+1][b-1] == 1){
                            vecinos1++;
                        }
                        if(tablero[a+1][b-1] == 2){
                            vecinos2++;
                        }
                    }
                }
                if( (b+1) < tablero.size() ){
                    if(tablero[a][b+1] == 0){
                        vecinos0++;
                    }
                    if(tablero[a][b+1] == 1){
                        vecinos1++;
                    }
                    if(tablero[a][b+1] == 2){
                        vecinos2++;
                    }
                }

                // Reglas de Valor 0
                if(tablero[a][b] == 0){
                    if(vecinos1 == 3 && vecinos0 >=2 ){
                        tablero[a][b] = 1;
                    }
                    if(vecinos2 == 4 && vecinos1 >=1 ){
                        tablero[a][b] = 1;
                    }
                }

                // Reglas de Valor 1
                if(tablero[a][b] == 1){
                    if(vecinos1 == 2 || vecinos1 == 3 ){
                        tablero[a][b] = 1;
                    }
                    if(vecinos2 >= 4 && vecinos1 == 1 ){
                        tablero[a][b]=2;
                    }
                    if(vecinos1 >= 5 ){
                        tablero[a][b]=0;
                    }
                }

                // Reglas de Valor 2
                if(tablero[a][b] == 2){
                    if(vecinos2 == 2 || vecinos2 == 3 ){
                        tablero[a][b] = 2;
                    }
                    if((vecinos1 == 4 || vecinos1 == 5) && vecinos2 == 1 ){
                        tablero[a][b]=1;
                    }
                    if(vecinos2 == 5 ){
                        tablero[a][b]=0;
                    }
                }

		//cout << endl;
		//cout << "x: " << a << " Y:" << b << " Vecinos 0: "  << vecinos0 << "Vecinos 1: " << vecinos1 << " Vecinos 2: " << vecinos2;
	        //cout << "X:" << a << " Y:" << b << "Tablero en la posicion [a][b]" << tablero[a][b];
		vecinos0= 0;
                vecinos1= 0;
                vecinos2= 0;
        }
    }
}

