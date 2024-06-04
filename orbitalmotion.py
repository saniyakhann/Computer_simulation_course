#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:08:24 2022

@author: saniyakhan
"""

import numpy as np 
import matplotlib.pyplot as plt 
from numpy.linalg import norm

class orbitalmotion(object):
    mars = []
    phobos = []
    
    def __init__(self, m1, m2, deltat, G, orbradius, n):
        self.m1 = m1 #mass of Mars
        self.m2 = m2 #mass of Phobos
        self.deltat = deltat
        self.n = n
        self.orbradius = orbradius
        self.G = G
     
        
    def getPositions(self):
        r1 = np.array([0, 0])
        r2 = np.array([self.orbradius, 0])
        r12 = np.array([self.orbradius, 0])
        r21 = np.array([-self.orbradius, 0])
        
        self.mars.append(np.array([0, 0]))
        self.phobos.append(np.array([self.orbradius, 0]))
        
        a1, a2 = np.array([0, 0]), np.array([0, 0])
        v1 = np.array([0, 0])
        v2 = np.array([0, (self.G * self.m1 / self.orbradius) ** (1/2)])
        
        for i in range (self.n): 
            print(r2)
            a1 = - self.G * self.m2 * r21 / (norm(r21) ** 3)
            a2 = - self.G * self.m1 * r12 / (norm(r12) ** 3)
            v1 = v1 + a1 * self.deltat
            v2 = v2 + a2 * self.deltat
            r1 = r1 + v1 * self.deltat
            r2 = r2 + v2 * self.deltat
            r12 = r2 - r1
            r21 = r1 - r2
            self.mars.append(r1)
            self.phobos.append(r2)
            #self.kineticenergyMars = (1/2)*m1*(v1)**2
            #self.kineticener
            
            
            
        return (self.mars, self.phobos)