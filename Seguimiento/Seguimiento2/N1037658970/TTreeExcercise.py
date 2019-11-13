"""
! ===========================================================================
! TTreeExercise.py
! ===========================================================================
!
!
!     Valentina Roquemen Echeverry, valentina.roquemen@udea.edu.co

! Up to date: 7 noviembre de 2019			
"""
# Librerias
import ROOT
from ROOT import gROOT 
from array import array
from random import randint
import numpy as np

# Definicion del arbol
MyTree = ROOT.TTree( 'tree1', 'tree para un par de dados y un float' )

# Definicion del tipo de variables que tendra el arbol
dado1 = array( 'i', [ 0 ] )
dado2 = array( 'i', [ 0 ] )
infiltrado = array( 'f', [0] )

# Asignacion de las variables a las ramas
MyTree.Branch( 'dado 1', dado1, 'dado1/I' )
MyTree.Branch( 'dado 2', dado2, 'dado2/I' )
MyTree.Branch( 'infiltrado', infiltrado, 'infiltrado/F' )

# Se llena de datos aleatorios el arbol
for i in range(1000):
  dado1[0] = randint(1,6)
  dado2[0] = randint(1,6)
  np.random.seed(dado2[0]) # Se usa el dato del dado 2 como semilla
  infiltrado[0] = np.random.random()
  MyTree.Fill()

# Grafica de los datos de la rama con datos tipo float
c1 = ROOT.TCanvas( 'c1', 'Canvas', 200, 10, 700, 900 )
c1.SetFillColor( 18 )
MyTree.Draw("infiltrado>>h1(5,0,1)")
c1.Update()
gROOT.GetListOfCanvases().Draw()
raw_input()