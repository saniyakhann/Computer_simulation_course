#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:26:23 2022

Simulation File
@author: saniyakhan
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm 
from solarsystembody import solarsystembody
from matplotlib.animation import FuncAnimation
import math
import sys
import matplotlib.pyplot as plt 



class solarsystemsimulation(object): #class for iterations in the simulation
    def __init__(self): 
        self.timestep = 300000   #timestep
        self.G= 6.67e-11 #constant value of G used in formulae
        self.N = 200   #the number of iterations
        self.planets = []  #creating a list of planets to store multiple items in different variables
        self.patches = [] #creating a list for the spheres that will represent the planets in the simulation 
    #iterating over lines in the text file 
        filein = open("dataforsolarsystem.txt", "r") #reads the data from the mentioned data file for properties of planets
        for line in filein.readlines(): 
            line= line.split() 
            name = line[0]
            m = int(float(line[1]))
            radius = int(float((line[2])))
            x = float(line[3])
            y = float(line[4])
            c = line[5] 
            self.planets.append(solarsystembody(m,c,radius, x, y, name))
     
    #calculates acceleration of planets in current timestep   
    def compute_current_accelerations(self):
        for a in self.planets:
            a.previous_acceleration = a.current_acceleration
            a.current_acceleration = np.array([0, 0])
            for b in self.planets: #creates loop for each iteration
                if a == b: continue;

                r = a.position - b.position #displacement of planet position
                mag = math.sqrt(r[0]**2 + r[1]**2) #magnitude of r gives distance

                if mag == 0: #ignores the case when distance equals 0
                    continue

                a.current_acceleration = a.current_acceleration-self.G*(b.m * r)/(mag**3) #Beeman's integral formualae
                
    #calculates acceleration of planets in next timestep
    def compute_next_acceleration(self):
        for a in self.planets:
            a.next_acceleration = np.array([0, 0])

            for b in self.planets: #creates loop for each iteration
                if a == b: continue; 

                r = a.next_position - b.next_position #displacement of planet position
                mag = math.sqrt(r[0]**2 + r[1]**2) #magnitude of r gives distance

                if mag == 0: #ignores the case when distance equals 0 
                    continue

                a.next_acceleration = a.current_acceleration -self.G*(b.m * r)/(mag**3) #Beeman's integral formulae

    def compute_next_positions(self): #gets positions of planets form their acceleration
        self.compute_current_accelerations()
        
        # Finds next position
        for planet in self.planets:
            planet.next_position = planet.position + planet.velocity * self.timestep + (1/6)*(4*planet.current_acceleration-planet.previous_acceleration)*self.timestep**2
        
    def compute_velocities(self): #uses Beeman's integral for velocity of planets
        for planet in self.planets:
            planet.velocity = planet.velocity + (1/6)*(2*planet.next_acceleration + 5*planet.current_acceleration - planet.previous_acceleration) * self.timestep


    def simulation(self): 
        
        history_Vs = [] #stores potential energy data as history
        history_KEs = [] #stores kinetic energy data as history
        print ("Simulating...")
    
        
        for i in range(self.N):

            history_Vs.append(self.compute_total_V()) #calls potential energy function from history stored
            history_KEs.append(self.compute_total_KE()) #calls kinetic energy function from history stored
             
            self.compute_next_positions()
            self.compute_next_acceleration()
            self.compute_velocities()
        
            for planet in self.planets:
                planet.position = planet.next_position # Apply positions
                planet.append_history() # Keep track of all positions for visualisation
                
            self.check_for_period(i) #running the orbital period
            self.check_satellite_return(i) 
            self.check_satellite_journey(i) #running the journey time of the satellite
            
        print("Done")
        return (np.array(history_Vs), np.array(history_KEs))
    
    #Experiment 1
    def check_for_period(self, cur_frame): #finds time taken to complete one orbit
        for planet in self.planets:
            if (planet.position[1] < 0 and planet.orbital_period == 0):
                planet.orbital_period = 2*(cur_frame * self.timestep) #the time taken for y coordinate to be negative, then multiplying that by 2 = orbital period
               
    #Experiment 3
    def check_satellite_return(self, cur_frame):
        satelite = None
        earth = None
        for planet in self.planets:
            if planet.is_satelite: #checks if orbital object is satellite
                satelite = planet
            elif planet.name == "Earth":
                earth = planet
                
        if (satelite == None or earth == None):
            raise "Could not find earth or satelite in planets array"
             
        r = satelite.position - earth.position #calculates distance of satellite from Earth
        distance = math.sqrt(r[0]**2 + r[1]**2) 
    
        if (distance < 1e12 and cur_frame > 100):
            satelite.return_time = cur_frame * self.timestep
            
    #Experiment 3        
    def check_satellite_journey(self, cur_frame):
        satelite = None
        mars = None
        for planet in self.planets:
            if planet.is_satelite:
                satelite = planet
            elif planet.name == "Mars": #setting condiiton for when satellite reaches mars
                mars = planet
                
        if (satelite == None or mars == None):
            raise "Could not find mars or satelite in planets array"
            
        r = satelite.position - mars.position #calculates distance of satellite from Mars
        distance = math.sqrt(r[0]**2 + r[1]**2)
    
        if (distance < 1e12):
            satelite.journey_time = cur_frame * self.timestep #calculates the time taken for satellite to reach mars
            
        
   #Experiment 2
    def compute_total_V (self):         #calculates potential energy for each planet
        total_V = 0
        for a in self.planets:
            V = 0
            for b in self.planets: 
                if a == b:
                    continue; 
                
                
                r = a.position - b.position
                mag = math.sqrt(r[0]**2 + r[1]**2) #distance between the two planets the potential energy is being calculated of
                
                if (mag == 0): continue; #skips to avoid division by 0 
                
                V = V + (-(self.G*a.m*b.m)/mag) #sums up all potential energies
            total_V += V/2 #divides potential energy by 2 to avoid double counting
            
        return total_V
            
    #Experiment 2        
    def compute_total_KE(self): #calculates kinetic energy of each planet
        KE = 0
        for planet in self.planets:
            speed = math.sqrt(planet.velocity[0]**2 + planet.velocity[1]**2) #magnetitude of velocity to get speed
            KE = KE + (0.5)*(planet.m)*(speed)**2 #kinetic energy formula
        return KE 
    
  
            
        