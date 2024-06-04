#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:34:07 2022

Body file 

Computer Simulation Project 
Saniya Khan
@author: saniyakhan
"""

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from numpy.linalg import norm
import math


class solarsystembody(object):
    
    def __init__(self, m, c, radius, x, y, name): #properties of the planets 
        self.m = m    #mass of the planets
        self.c = c   #colour of the planets
        self.name = name   #planet name
        self.radius = radius #radius of the planet
        self.G= 6.67e-11
        
        self.position = np.array([x, y])  #initial position of the planet before any calculuations are made 
        self.next_position = np.array([x, y])
        self.previous_acceleration = np.array([0,0])
        self.current_acceleration = np.array([0,0])
        self.next_acceleration = np.array([0,0])

        self.orbital_period = 0

        self.history = [] #stores position of planets as a list 
        self.patch = None #defines the null value
        
        self.is_satelite = self.name == "Satellite"
        
        self.return_time = 0 #starting the time from 0 since quantity is scalar
        self.journey_time = 0 #starting the time from 0 since quantity is scalar
        
        #conditions for satellite launch
        if self.position[0] == 0:
           self.velocity = np.array([0, 0], dtype = float)
        elif self.is_satelite:
            self.velocity = np.array([0.0, 12000.0]) #initial velocity the satellite is launched with
        else:
            self.velocity = np.array([0, (self.G*1.9e30 / self.position[0])**(1/2)], dtype = float) 

            

    def append_history(self):
        self.history.append(self.position)  #adds final input position in list that is stored 
        
   #removes patch and reproduces in the new position
    def render(self, ax, i):
        if (self.patch != None):
            self.patch.remove()
        self.patch = plt.Circle((self.history[i][0], self.history[i][1]), .3e11, color=self.c ) #use of the history function to simulate where the patch will show up
        ax.add_patch(self.patch)


                            
                            
                            
                            