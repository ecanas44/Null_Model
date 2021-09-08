#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 09:47:35 2020

@author: esteban
"""

import numpy as np

# =============================================================================
# Clase DOMINIO
#Paremetros:
    #Tamaño de las celdas
    #Dimensiones del dominio
    #Extensión de los pasos de tiempo
    #Tiempo total
# =============================================================================

class Dominio:
    def __init__(self, tamano_celda, dimensiones, step, tiempo_total):
        self._tamano_celda = tamano_celda
        self._dimensiones = dimensiones
        self._step = step
        self._tiempo_total = tiempo_total
        self._grid = np.zeros(dimensiones, dtype=object)
        self._print_grid = np.zeros(dimensiones, dtype=int)
        
    def __repr__(self):
        return f"""
                Dominio:
                    Tamaño de la celda: {self.tamano_celda}
                    Dimensiones del dominio: {self.dimensiones}
                    Paso de tiempo: {self.step}
                    Tiempo total: {self.tiempo_total}                    
            """
    @property
    def tamano_celda(self):
        return self._tamano_celda
    
    @property
    def dimensiones(self):
        return self._dimensiones
    
    @property
    def step(self):
        return self._step
    
    @property
    def tiempo_total(self):
        return self._tiempo_total
    
    @property
    def grid(self):
        return self._grid
    
    @property
    def print_grid(self):
        return self._print_grid
    
    def set_celda(self, x, y, estado):
        celda = self.grid[x][y]
        self.grid[celda.posicion[0]][celda.posicion[1]].cambiar_estado(estado)
        if estado == 'especie1':
            self.print_grid[x][y] = 15
        elif estado == 'especie2':
            self.print_grid[x][y] = 25
        elif estado == 'especie3':
            self.print_grid[x][y] = 35
        else:
            self.print_grid[x][y] = 5
    
    def vecindario(self,i,j,distancia):
        vecinos = []
        for a in range(- distancia, distancia + 1):
          for b in range(- distancia, distancia + 1):
              if (a!=0 or b!=0) and i+a>=0 and i+a<self.dimensiones[0] and j+b>=0 and j+b<self.dimensiones[1]:
                  vecinos.append(self.grid[i+a][j+b])
        return vecinos
    
    def count_values(self):
        empty = np.count_nonzero(self.print_grid == 5)
        sp1 = np.count_nonzero(self.print_grid == 15)
        sp2 = np.count_nonzero(self.print_grid == 25)
        sp3 = np.count_nonzero(self.print_grid == 35)
        return empty, sp1, sp2, sp3
        
