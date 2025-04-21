# Search Project

This project implements various search algorithms to help Pacman navigate through maze environments. The goal is to find efficient paths to reach specific locations and collect food dots.

## Implementation Overview

The project implements the following search algorithms:
- Depth First Search (DFS)
- Breadth First Search (BFS)
- Uniform Cost Search
- A* Search with custom heuristics

## Running the Project

### 1. Finding a Fixed Food Dot using DFS
```bash
python pacman.py -l bigMaze -z .5 -p SearchAgent
python autograder.py -q q1
```

### 2. Breadth First Search
```bash
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python eightpuzzle.py
python autograder.py -q q2
```

### 3. Uniform Cost Search
```bash
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
python autograder.py -q q3
```

### 4. A* Search
```bash
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python autograder.py -q q4
```

### 5. Finding All Corners
```bash
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python autograder.py -q q5
```

### 6. Corners Problem: Heuristic
```bash
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
python autograder.py -q q6
```

### 7. Eating All Dots
```bash
python pacman.py -l trickySearch -p AStarFoodSearchAgent
python autograder.py -q q7
```

### 8. Suboptimal Search
```bash
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
python autograder.py -q q8
```

## Key Files

- `search.py`: Contains the core search algorithms
- `searchAgents.py`: Implements various search-based agents
- `pacman.py`: Main game logic
- `game.py`: Game rules and mechanics
- `util.py`: Utility functions and data structures

## Testing

Each component can be tested using the autograder:
```bash
python autograder.py
```

Or test specific questions using:
```bash
python autograder.py -q qN
```
where N is the question number (1-8). 