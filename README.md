# Maze Escape Game (PS No. 44)

A console-based Maze Escape Game developed in Python 3 for B.Tech CSE (First Semester) at **Rungta International Skills University**.

## Features
- **5x5 2D Grid Maze:** Represents open paths (`.`), walls (`#`), player position (`P`), and exit (`E`).
- **Interactive Navigation:** Move using `W` (Up), `A` (Left), `S` (Down), and `D` (Right) with boundary checks, wall collision detection, and valid move counting.
- **Shortest Path Finder (BFS):** Uses Breadth-First Search (`collections.deque`) to compute the minimum number of steps required to reach the exit (`10 steps`).

## How to Run
```bash
python python_code.py
