# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:59:23 2019

@author: esteban
"""
#AUTOMATA CELULAR: TIEMPO DISCRETO, ESPACIO DISCRETO, ESTADOS DISCRETOS
import os
import matplotlib.pyplot as plt
import imageio
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
        filenames = []
        count_empty = []
        count_sp1 = []
        count_sp2 = []
        count_sp3 = []
        cmap = colors.ListedColormap(['white', 'purple', 'blue', 'green'])
        bounds = [0,10,20,30,40]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        plt.title('t = 0')
        plt.imshow(self.dominio.print_grid, cmap, norm)
        filename = 't0.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.pause(0.5)
        
        while self._tiempo <= self._dominio.tiempo_total:
            self._tiempo += self._dominio.step
            self.regla.delimitar(self.dominio)
            self.regla.propagacion(self.dominio)
            plt.title(f't = {self._tiempo}')
            plt.imshow(self.dominio.print_grid, cmap, norm)
            filename = f't{self._tiempo}.png'
            
            # last frame of each viz stays longer
            if (self._tiempo == self._dominio.tiempo_total):
                for i in range(15):
                    filenames.append(filename)
            else:
                for i in range(3):
                    filenames.append(filename)
            
            empty, sp1, sp2, sp3 = self.dominio.count_values()
            
            count_empty.append(empty)
            count_sp1.append(sp1)
            count_sp2.append(sp2)
            count_sp3.append(sp3)
            
            plt.savefig(filename)
            plt.pause(0.5)
            
        # build gif
        with imageio.get_writer('simulacion.gif', mode='I') as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
                
        # Remove files
        for filename in set(filenames):
            os.remove(filename)
            
        time = [i  for i in range(0,51)]
        plt.plot(time, count_empty, label='empty')
        plt.plot(time, count_sp1, label='sp1')
        plt.plot(time, count_sp2, label='sp2')
        plt.plot(time, count_sp3, label='sp3')
        plt.xlabel('time step')
        plt.ylabel('count')
        plt.title('Count of states per time step')
        plt.legend()
        plt.show()
            
        plt.close()
    
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