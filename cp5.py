#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:48:30 2022

@author: saniyakhan
"""

import math 
from Checkpoint5 import Orbit

def main(): 
    
    m_mars = float(input("Mass of Mars:")) 
    mars_rix = float(input("intial position  x of Mars:"))
    mars_riy = float(input("initial position y of mars:"))
    mars_vix  = float(input("initial velocity  x of mars:")) 
    mars_viy = float(input("initial velocity y of mars"))
    
    m_phobos = float(input("Mass of phobos:")) 
    phobos_rix = float(input("intial position  x of phobos:"))
    phobos_riy = float(input("initial position y of phobos:"))
    phobos_vix  = float(input("initial velocity  x of phobos:")) 
    phobos_viy = float(input("initial velocity y of phobos"))
    
    
    timestep = float(input("input timestep for system:"))
     
    
main()