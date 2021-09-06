#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:55:46 2020

@author: esteban
"""

from scipy.stats import skewnorm
import numpy as np

#sigma = regla de actualizacion = PCB
##P = Operador de propagacion
##C = Operador de colision
##B = Condicion de borde
class Regla:
    def __init__(self, paradigma = None):
        self._paradigma = paradigma
        
    @property
    def paradigma(self):
        return self._paradigma
        
    #Operador de borde
    def delimitar(self,dominio):
        self.reproducirse(dominio)
        self.brotar(dominio)
        
    #Operador de propagacion
    def propagacion(self, dominio):
        for i in range(dominio.dimensiones[0]):
            for j in range(dominio.dimensiones[1]):
                celda = dominio.grid[i][j]
                if not self.envejecer(celda):
                    dominio.set_celda(i, j, 'vacia')
        
    
    #Funcion de envejecer para cada celda
    def envejecer(self, celda):
        celda._edad += 1
        if celda.edad <= celda.rasgos['longevidad']:
            return True
        else:
            return False
        
    #Funcion de dispersion y reproduccion
    def reproducirse(self, dominio):
        for i in range(dominio.dimensiones[0]):
            for j in range(dominio.dimensiones[1]):
                celda = dominio.grid[i][j]
                if celda.estado != 'vacia':
                    vecindario = dominio.vecindario(i,j,celda.rasgos['rango_dispersion'])           
                    for vecino in vecindario:
                        if vecino.estado == 'vacia':
                            coef_brotacion = np.random.randint(0,100)
                            if celda.estado == 'especie1':
                                vecino.brotacion['especie1'] = skewnorm.rvs(0, size=100)[coef_brotacion]
                            elif celda.estado == 'especie2':
                                vecino.brotacion['especie2'] = skewnorm.rvs(0, size=100)[coef_brotacion]
                            elif celda.estado == 'especie3':
                                vecino.brotacion['especie3'] = skewnorm.rvs(0, size=100)[coef_brotacion]
    
    #Funcion de nuevos individuos
    def brotar(self, dominio):
        for i in range(dominio.dimensiones[0]):
            for j in range(dominio.dimensiones[1]):
                celda = dominio.grid[i][j]
                if celda.estado == 'vacia':
                    especie1 = celda.brotacion['especie1']
                    especie2 = celda.brotacion['especie2']
                    especie3 = celda.brotacion['especie3']
                    vacia = skewnorm.rvs(0, size=1)
                    m = max(especie1,especie2,especie3, vacia)
                    if m == vacia:
                        pass
                    elif m == especie1:
                        dominio.set_celda(i,j,'especie1')
                    elif m == especie2:
                        dominio.set_celda(i,j,'especie2')
                    elif m == especie3:
                        dominio.set_celda(i,j,'especie3')
                    
            
