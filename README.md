# Catan Simulation in Python

A Settlers of Catan simulator for AI agents written in Python.

## Overview

This repository contains a Python-based simulator for the board game Settlers of Catan. It is designed to test and refine AI agents in a simulated environment. Users can execute predefined agents, as well as introduce their own custom agents into the game.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. The simulation is compatible with Python 3.x.

### Adding Your Agents

1. Navigate to the `Agents` folder.
2. Place your custom agent module or Python file in this folder.
3. Ensure your agent class is correctly defined within the module.

### Running the Simulator

To run the simulator, use the `main` module. Specify the agents to be executed and the number of games to be played. Each agent should be referenced by the module or file name, followed by a dot, and then the class name (e.g., `MyModule.MyClass`).

### Results

After each game, the result is displayed in the console and the game trace is saved in JSON format in the `Traces` folder.

## Visualizing Results

To visualize game results:
1. Open the `index.html` file located in the `Visualizer` folder.
2. Load a JSON trace file by clicking on the three-dot icon located in the controls below the right side of the Catan board.

<img src="assets/visualizer_screenshot.png" width="900" alt="Screenshot of the visualizer">

## Sistema de coordenadas

Se basa en el sistema de coordenadas axiales descrito en el blog de red blob games: https://www.redblobgames.com/grids/hexagons/

En el siguiente enlace se pueden ver los sistemas de coordenadas para cada uno de los elementos del grid (Tile, Vertex, Edge) y las relaciones entre estos: https://www.redblobgames.com/grids/parts/#hexagon-relationships

Asi pues se propone crear una clase que permita recorrer cualquiera de los elementos del tablero, saltando de unos a otros etc. Ademas debera de comprobar los limites del mapa y permitir asignar un diccionario con atributos a cada elemento (si un vertex tiene un pueblo o ciudad, que probabilidad y recurso tiene un tile etc.)

Se entiende un tile como un par de coordenadas (q, r)

Se entiende un edge como un par de tiles ((q1,r1),(q2,r2)) que cumple restricciones de adyacencia (todo). Para movernos de un edge a otro adyacente lo que hacemos es sustituir uno de los tiles por otro que cumpla adyacencia con los dos originales.

Se entiende un vertex como una tripleta de tiles que cumplen restricciones de adyacencia todos con todos. Para movernos de un vertex a otro lo que hacemos es sustituir un tile por otro que cumpla adyacencia con los otros dos. 

Definimos adyacencia del tile (q,r) como cualquiera de las siguientes opciones:
    (1,0) => (q+1, r)
    (-1, +1) => (q-1, r+1)
    (0, +1) => (q, r+1)
    (0, -1) => (q, r-1)
    (+1, -1) => (q+1, r-1)
    (-1, 0) => (q-1, 0)

O dicho de otro modo, considerará adyacente cualquier tupla (iq,ir) tal qu: iq,ir in [-1,0,1] & iq!=ir

Esto permite calcular la distancia entre dos elementos del mismo tipo como el número de incrementos que hay que hacer en cualquiera de sus tiles para llegar desde A hasta B.

## Contributing

Contributions to the Catan Simulation in Python are welcome! Please feel free to make changes and submit pull requests.
