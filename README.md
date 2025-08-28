# Computer_simulation_course
# Computer Simulation Course

This repository contains code implementations and assignments from my Computer Simulation course at the University of Edinburgh. The coursework covers a diverse range of computational physics and simulation techniques, from quantum algorithms to celestial mechanics.

## Course Overview

This course explores fundamental concepts and practical implementations of computer simulation techniques, including:
- Quantum computing algorithms (Grover's search, Shor's factorization)
- Traffic flow simulation using cellular automata
- Orbital mechanics and N-body gravitational simulations
- Solar system dynamics and satellite trajectory modeling
- Energy conservation analysis in physical systems

## Repository Structure

```
Computer_simulation_course/
├── README.md
├── codewithanimation.py        # Quantum algorithms (Grover's & Shor's)
├── cp4.py                      # Traffic simulation checkpoint
├── cp5.py                      # Orbital motion checkpoint
├── orbitalmotion.py            # Two-body orbital mechanics
├── solarsystembody.py          # Solar system object definitions
├── solarsystemsimulation.py    # Main solar system simulation engine
├── solarsystemanimation.py     # Animation utilities (incomplete)
├── test.py                     # Main simulation runner and visualization
└── dataforsolarsystem.txt      # Planet data (mass, position, color, etc.)
```

## Technologies Used

- **Python 3** - Primary programming language
- **NumPy** - Numerical computations and array operations
- **Matplotlib** - Data visualization and animation
- **FuncAnimation** - Real-time simulation visualization
- **Mathematical Libraries** - For physics calculations and algorithms

## Key Implementations

### 1. Quantum Computing Algorithms (`codewithanimation.py`)
- **Grover's Search Algorithm**: Quantum search in unordered databases with O(√N) complexity
- **Shor's Factorization Algorithm**: Quantum integer factorization
- Animated visualizations showing probability amplitudes during quantum operations
- Demonstrates quantum superposition and amplitude amplification

### 2. Traffic Flow Simulation (`cp4.py`, `Checkpoint4.py`)
- Cellular automata model for traffic flow
- Configurable parameters: number of cells, iterations, and car density
- Real-time visualization of traffic patterns and flow dynamics

### 3. Orbital Mechanics (`orbitalmotion.py`, `cp5.py`)
- Two-body orbital simulation (Mars-Phobos system)
- Numerical integration using Euler and Verlet methods
- Gravitational force calculations and orbital stability analysis

### 4. Solar System Simulation (`solarsystemsimulation.py`, `solarsystembody.py`, `test.py`)

**Main Features:**
- Complete N-body gravitational simulation
- Beeman integration algorithm for improved numerical stability
- Real-time energy conservation monitoring (kinetic + potential)
- Animated visualization of planetary motions

**Experiments Implemented:**
- **Experiment 1**: Orbital period calculations for all planets
- **Experiment 2**: Energy conservation analysis with CSV output
- **Experiment 3**: Satellite trajectory from Earth to Mars with return journey analysis

**Key Capabilities:**
- Reads planetary data from external file (`dataforsolarsystem.txt`)
- Supports satellite launches with custom initial velocities
- Calculates orbital periods, journey times, and energy conservation
- Generates animated GIF output of the entire simulation

## Getting Started

### Prerequisites
```bash
pip install numpy matplotlib scipy
```

### Running the Simulations

1. **Solar System Simulation** (Main Project):
```bash
python test.py
```
This runs the complete solar system simulation with:
- Animated visualization of planetary orbits
- Energy conservation plots
- Orbital period calculations
- Satellite mission analysis

2. **Quantum Algorithms**:
```bash
python codewithanimation.py
```
Demonstrates Grover's search and Shor's factorization with animations.

3. **Traffic Simulation**:
```bash
python cp4.py
```
Interactive traffic flow simulation with user-defined parameters.

### Input Files
- `dataforsolarsystem.txt`: Contains planetary data in format:
  ```
  Name Mass(kg) Radius(km) X-position(m) Y-position(m) Color
  ```

## Simulation Results

### Solar System Analysis
- **Orbital Periods**: Calculated for all planets and compared with real values
- **Energy Conservation**: Total energy remains constant within numerical precision
- **Satellite Missions**: Earth-to-Mars trajectory optimization

### Output Files
- `energyofsystem.csv`: Time-series data of kinetic, potential, and total energy
- `output.gif`: Animated visualization of the solar system simulation

## Mathematical Methods

### Numerical Integration
- **Beeman Algorithm**: Used for planetary motion integration with superior stability
- **Verlet Integration**: Applied in orbital mechanics calculations
- **Euler Method**: Basic integration for simple systems

### Physics Implementations
- **Newton's Law of Gravitation**: F = G(m₁m₂)/r²
- **Conservation Laws**: Energy and momentum conservation verification
- **Orbital Mechanics**: Kepler's laws and orbital element calculations

## Key Learning Outcomes

- Implementation of advanced numerical integration methods
- Understanding of quantum computing algorithms and their complexity advantages
- Practical experience with N-body gravitational simulations
- Energy conservation principles in computational physics
- Real-time animation and data visualization techniques
- Object-oriented design for complex physical systems

## Experiments and Analysis

### Experiment 1: Orbital Period Verification
Calculated orbital periods match theoretical predictions within 1-2% accuracy.

### Experiment 2: Energy Conservation
Demonstrated conservation of total energy in the N-body system with < 0.1% drift over simulation time.

### Experiment 3: Interplanetary Mission Design
Successfully modeled Earth-to-Mars satellite trajectory with:
- Launch velocity optimization
- Journey time calculation
- Return trajectory analysis

## Physics Accuracy

The simulations incorporate real astronomical data:
- Actual planetary masses and initial positions
- Realistic gravitational constant (G = 6.67 × 10⁻¹¹ m³/kg⋅s²)
- Appropriate time steps for numerical stability
- Conservation law verification

---

*Repository reflects coursework completed during the 2022-2023 academic year at the University of Edinburgh.*

**Note**: Some animation files may be incomplete as they were part of ongoing development during the course.
