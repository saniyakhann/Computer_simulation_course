#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:19:01 2022


Animation file 

@author: saniyakhan
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


    def patches (self,i): #creating patches for the planets
        for i in range (0,len(self.planets)): 
            self.patch.append(self.bodies[i].name) 
    
    
    def animate(self, i): #animatinf the patches as a circle with the specified centers
        for j in range (0,len(self.patch)): 
            self.patch[j].center = (self.pos[i][0], self.pos[i][1])
            
            return (self.patch.center)
    
    def display(self): #displays the patch animation
        fig = plt.figure()
        ax = plt.axes()
        
        for i in range(0,len(self.patch)): 
            self.patch.center[i].append(plt.circle(self.patch[0][0], self.patch[0][1], .5e6, colour = 'r', animated = True ))
            ax.add_patch(self.patch[i]) #setting how the patches will appear 
            
        ax.set_xlim(-10e6, 10e6)
        ax.set_ylim(-10e6, 10e6)
        
        numFrames = len(self.mars) #accounts for range to be only till mars
        self.anim = FuncAnimation(fig, self.animate, numFrames, repeat = False, interval = 20, blit = True)
        plt.show()

