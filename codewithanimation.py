#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 22:18:27 2023

@author: saniyakhan
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# creating an unordered list of n elements 
def create_database(n):
    return np.random.randint(0, 2, size=(n))

# Oracle function to check if x == a
def oracle(x, a):
    return x == a

# Diffuser function to amplify the amplitude of the desired state
def diffuser(n):
    H = np.ones((2 ** n, 1)) / np.sqrt(2 ** n)
    I = np.eye(2 ** n)
    D = 2 * np.outer(H, H) - I
    return D

# Grover's algorithm to search for a in an unordered list of size 2^n
def grover_search(a, n):
    N = 2 ** n
    database = create_database(N)
    print("Database:", database)

    # Initialize superposition of all states
    s = np.ones(N) / np.sqrt(N)

    # Define number of iterations of Grover's algorithm
    num_iterations = int(np.round(np.pi/4 * np.sqrt(N)))

    # Create a figure for the animation
    fig, ax = plt.subplots()

    # Define a function to update the plot for each frame of the animation
    def update(i):
        nonlocal s
        nonlocal ax

        # Apply the oracle
        oracle_mask = np.array([oracle(x, a) for x in database])
        s = 2 * oracle_mask * s - s

        # Apply the diffuser
        D = diffuser(n)
        s = D.dot(s)

        # Update the plot
        ax.clear()
        ax.bar(range(N), s ** 2)
        ax.set_title("Grover's algorithm for searching an unordered list")
        ax.set_xlabel("Database element")
        ax.set_ylabel("Probability")

    # Create the animation
    anim = FuncAnimation(fig, update, frames=range(num_iterations))

    # Display the animation
    plt.show()

# Shor's algorithm to factorize a number N
def shor_algorithm(N):
    # Step 1: Choose a random integer a between 1 and N-1
    a = np.random.randint(1, N)
    print("Random integer a:", a)

    # Step 2: Compute the greatest common divisor of a and N
    gcd = np.gcd(a, N)
    if gcd != 1:
        # If the gcd is not 1, we have found a nontrivial factor of N
        print("Factor found:", gcd)
        return gcd

    # Step 3: Compute the period r of the function f(x) = a^x mod N
    for r in range(1, N):
        if pow(a, r, N) == 1:
            break
    print("Period r:", r)

    # Step 4: Use the period r to find factors of N
    if r % 2 == 0:
        factor1 = np.gcd(pow(a, r//2, N) + 1, N)
        factor2 = np.gcd(pow(a, r//2, N) - 1, N)
        print("Factors found:", factor1, factor2)
        return factor1, factor2
    else:
        # If r is odd, we need to try again with a different random integer a
        print("Odd period, trying again...")
        return shor_algorithm(N)

#
grover_search(1, 3)
shor_algorithm(15)
