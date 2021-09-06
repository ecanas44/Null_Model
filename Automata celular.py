# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:59:23 2019

@author: esteban
"""
#AUTOMATA CELULAR: TIEMPO DISCRETO, ESPACIO DISCRETO, ESTADOS DISCRETOS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from Dominio import Dominio
from Celda import Celda
from Regla import Regla
#from Ambiente import Interactor_Ambiental

#%%       
#DEFINICION AUTOMATA CELULAR
#CA = (A(dx,L,dt,T),F,sigma,f_init,u,O)
#A = dominio:
##dx = tamaño de las celdas
##L = area del dominio
##dt = paso de tiempo
##T = tiempo final (T/dt = numero de iteraciones)
#F = estados
#sigma = regla de actualizacion = PCB
##P = Operador de propagacion
##C = Operador de colision
##B = Condicion de borde
#f_init = estado inicial
#u = colector de de informacion externa entre el CA y el ambiente
#O = observador

class Automata:
    def __init__(self, dominio, estados, regla, estado_inicial = 'vacia', interactor_ambiental = None, observador = None):
        self._dominio = dominio
        self._estados = estados
        self._regla = regla
        self._estado_inicial = estado_inicial
        self._interactor_ambiental = interactor_ambiental
        self._observador = observador
        self._tiempo = 0
        
        self.inicializar_dominio(dominio, estado_inicial)
        
        self.inicializar_variables_estado()
        
    @property
    def dominio(self):
        return self._dominio
    @property
    def estados(self):
        return self._estados
    @property
    def regla(self):
        return self._regla
    @property
    def estado_inicial(self):
        return self._estado_inicial
    @property
    def interactor_ambiental(self):
        return self._interactor_ambiental
    @property
    def observador(self):
        return self._observador
    def matar(self, x,y):
        self._dominio.set_celda(Celda([x,y]), self._estado_inicial)
        
    # =============================================================================
    #PARTES DEL MODELO
    # =============================================================================
    def inicializar_dominio(self, dominio, estado_inicial):
        for i in range(dominio.dimensiones[0]):
            for j in range(dominio.dimensiones[1]):
                self._dominio.grid[i][j] = Celda([i,j])
    
    #Podria inicializar con metodos especficos como nucleacion o aleatorio        
    def inicializar_variables_estado(self):
        #Por ahora empieza con 1 estado en cada esquina
        self._dominio.set_celda(2, 2, 'especie1')
        self._dominio.set_celda(2, 6, 'especie2')
        self._dominio.set_celda(6, 2, 'especie3')
        self._dominio.set_celda(-2, 2, 'especie1')
        self._dominio.set_celda(-2, 6, 'especie2')
        self._dominio.set_celda(-6, 2, 'especie3')
        self._dominio.set_celda(6, -6, 'especie1')
        self._dominio.set_celda(2, -6, 'especie2')
        self._dominio.set_celda(2, -2, 'especie3')
        self._dominio.set_celda(-2, -2, 'especie1')
        self._dominio.set_celda(-2, -4, 'especie2')
        self._dominio.set_celda(-4, -4, 'especie3')
        
    def simular(self):
        cmap = colors.ListedColormap(['white', 'purple', 'blue', 'green'])
        bounds = [0,10,20,30,40]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        plt.title('t = 0')
        plt.imshow(self.dominio.print_grid, cmap, norm)
        plt.pause(0.5)
        
        while self._tiempo <= self._dominio.tiempo_total:
            self._tiempo += self._dominio.step
            self.regla.delimitar(self.dominio)
            self.regla.propagacion(self.dominio)
            plt.title(f't = {self._tiempo}')
            plt.imshow(self.dominio.print_grid, cmap, norm)
            plt.pause(0.5)
    
#%%
#CODIGO PARA CUADRICULA DE COLORES ESPECIFICOS
data = np.random.rand(10, 10) * 30

# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue', 'white'])
bounds = [0,10,20,30]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-.5, 10, 1));
ax.set_yticks(np.arange(-.5, 10, 1));

plt.show()

#%%
# =============================================================================
# PARA CORRER EL AUTOMATA
# =============================================================================
D = Dominio(1, [50,50], 1, 50)
estados = ['especie1','especie2','especie3','vacia']
regla = Regla()
CA = Automata(D, estados, regla)

#%%
CA.simular()