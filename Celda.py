#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:06:25 2020

@author: esteban
"""
# =============================================================================
# CA con rasgos vs CA sin rasgos
# =============================================================================

#r1 = densidad de la madera
#r2 = sindrome de dispersion
#r3 = capacidad fotosintetica
#r4 = longevidad


class Celda:
    def __init__(self, posicion):
        self._posicion = posicion
        self.cambiar_estado('vacia')
            
    def cambiar_estado(self, estado):
        if estado == 'especie1':
            self._rasgos = {
                'densidad': 1, 
                'rango_dispersion': 5,
                'capacidad_fotosintetica': 3,
                'longevidad': 10
                }
        elif estado == 'especie2':
            self._rasgos = {
                'densidad': 1, 
                'rango_dispersion': 5,
                'capacidad_fotosintetica': 3,
                'longevidad': 10
                }
        elif estado == 'especie3':
            self._rasgos = {
                'densidad': 1, 
                'rango_dispersion': 5,
                'capacidad_fotosintetica': 3,
                'longevidad': 10
                }
        elif estado == 'vacia':
          self._rasgos = {
              'densidad': 0, 
              'rango_dispersion': 0,
              'capacidad_fotosintetica': 0,
              'longevidad': 0
              }
          self.brotacion = {
             'especie1': float('-inf')   ,      
             'especie2': float('-inf'),
             'especie3': float('-inf'),
             'vacia': float('-inf')
             }
        else:
            raise Exception(f"No hay estado {estado}")
        self._estado = estado
        self._edad = 0
            
    def __repr__(self):
        descripcion = f'''
            Especie: {self.estado}
            Posicion en dominio: {self.posicion}
            Edad: {self.edad}
            
            Rasgos:
                Densidad: {self.rasgos['densidad']}
                Rango de dispersion: {self.rasgos['rango_dispersion']}
                Capacidad fotosintetica: {self.rasgos['capacidad_fotosintetica']}
                Longevidad: {self.rasgos['longevidad']}
        '''
        if self._estado == 'vacia':
            return 'Celda vacia'
        else:
            return descripcion
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def densidad(self):
        return self._densidad
    
    @property
    def posicion(self):
        return self._posicion
    
    @property
    def rasgos(self):
        return self._rasgos