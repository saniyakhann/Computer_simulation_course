#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:34:01 2022

@author: saniyakhan
"""

from solarsystembody import solarsystembody
from solarsystemsimulation import solarsystemsimulation
import matplotlib.pyplot as pyploy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animation_tick(i, planets, ax):
    for planet in planets:
        planet.render(ax, i)
    

def output_to_file(kes, vs, timestep):
        with open ("energyofsystem.csv", "w") as file:  #opens file for energies of the system to show conservation
            file.write("t, total kinetic energy, total potential energy, sum\n")
            for i in range (0, len(kes)):
                file.write(str(i * timestep) + ", " + str(kes[i]) + ", " + str(vs[i]) + ", " + str(kes[i] + vs[i]) + "\n")

def main(): #creating a function to run the simulation 
    simulation = solarsystemsimulation()  
    Vs, KEs = simulation.simulation()  
    
    # Output KEs and Vs in file
    output_to_file(KEs, Vs, simulation.timestep)
    
    # Print orbital periods
    print("Orbital Periods:")
    for i in range(0, len(simulation.planets)):
        print(simulation.planets[i].name, simulation.planets[i].orbital_period / (24*60*60), "days")
    
    # Print Satelite journey time
    for planet in simulation.planets:
        if planet.is_satelite:
            print("The Satelite gets to mars after", planet.journey_time/(24*60*60), "days")
            if planet.return_time != 0:
                print("The Satelite returns to earth after ", planet.return_time/(24*60*60), "days")
            else:
                print("The Satellite does not return to Earth.")
    
    # Plot Energies
    fig, ax = plt.subplots()
    xs = np.linspace(0, len(Vs)*simulation.timestep, len(Vs))
    plt.plot(xs, Vs, label="Potential Energy")
    plt.plot(xs, KEs, label="Kinetic Energy")
    plt.plot(xs, Vs + KEs, label="Total Energy") #takes sum of the potential and kinetic energies from functions to plot total energy
    plt.legend()
    plt.show()
    
    # Plot animation
    fig, ax = plt.subplots() 
    #creates plane for animation
    def init():
        ax.set_xlim(-1e12, 1e12)
        ax.set_ylim(-1e12, 1e12)
        return ax,
    
    print("Generating animation...")
    ani = FuncAnimation(fig, animation_tick, frames=range(0, len(simulation.planets[0].history)), fargs=(simulation.planets,ax,),
                       init_func=init) 
    
    plt.show() 
    
    
    ani.save("output.gif", dpi=90) #saving animation as mp4 file to be able to reference previously generated animation
    print("... done.")

    

    
main()