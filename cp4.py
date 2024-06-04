#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:09:29 2022

@author: saniyakhan
"""
from Checkpoint4 import newtraffic

def main():
    C = int(input("Enter the number of cells:"))
    n = int(input("Enter the number of iterations:"))
    p = float(input("Enter the number density:"))
    t = newtraffic(C, n, p)
    t.carset(0, False)
    t.printGrid()
    t.plotGridAndGraph()
main()

 
