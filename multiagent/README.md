# Multi-Agent Search Project

This project implements various adversarial and probabilistic search agents for the classic version of Pacman. The implementations include minimax and expectimax search algorithms, along with custom evaluation functions.

## Project Components

### 1. Reflex Agent
A basic agent that uses state evaluation heuristics to make decisions.
```bash
# Run the reflex agent on the test classic layout
python pacman.py -p ReflexAgent -l testClassic

# Test the implementation
python autograder.py -q q1
```

### 2. Minimax Agent
Implementation of the minimax algorithm for adversarial search.
```bash
# Test the implementation
python autograder.py -q q2
```

### 3. Alpha-Beta Pruning
An optimized version of minimax that prunes unnecessary branches.
```bash
# Run the agent on a small classic layout with depth 3
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

# Test the implementation
python autograder.py -q q3
```

### 4. Expectimax Agent
Handles probabilistic behavior in adversaries.
```bash
# Run the agent on the minimax classic layout with depth 3
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3

# Test the implementation
python autograder.py -q q4
```

### 5. Evaluation Function
Custom state evaluation function for better agent performance.
```bash
# Test the implementation
python autograder.py -q q5
```

## Key Files

- `multiAgents.py`: Contains all agent implementations
- `pacman.py`: Main game logic
- `game.py`: Game rules and mechanics
- `ghostAgents.py`: Ghost behavior implementations
- `util.py`: Utility functions and data structures

## Testing

Run all tests using:
```bash
python autograder.py
```

Or test specific questions using:
```bash
python autograder.py -q qN
```
where N is the question number (1-5).

## Project Resources

For more detailed information about the project specifications and requirements, visit:
[Project Description](https://classes.cs.uoregon.edu/24F/cs471/programming-projects/project2.html) 