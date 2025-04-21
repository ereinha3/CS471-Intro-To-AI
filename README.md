# CS471: Introduction to Artificial Intelligence

This repository contains projects completed for CS471 Intro to AI, taken under Professor Thanh Nguyen. The course is modeled after UC Berkeley's AI course and covers fundamental concepts in artificial intelligence including search algorithms, multi-agent systems, and reinforcement learning.

## Project Overview

### 1. Search Algorithms
Located in [`search/`](./search)

Implements various search algorithms to help Pacman navigate through maze environments:
- **Depth First Search (DFS)**: Explores paths to their deepest level before backtracking
- **Breadth First Search (BFS)**: Explores all paths of the same length before moving deeper
- **Uniform Cost Search**: Finds the shortest path by considering path costs
- **Greedy Search**: Makes decisions based on estimated cost to goal
- **A* Search**: Combines path cost and heuristic estimates for optimal pathfinding
  - Implementation with pre-defined heuristics
  - Development of custom optimized heuristics

### 2. Multi-Agent Search
Located in [`multiagent/`](./multiagent)

Focuses on game theory and adversarial search in zero-sum games:
- **Reflex Agent**: Uses basic state evaluation heuristics
- **Minimax Agent**: Implements adversarial search
  - Alpha-Beta Pruning optimization for efficient tree traversal
- **Expectimax Agent**: Handles probabilistic behavior in adversaries
- **Advanced Evaluation Functions**: Enables recursive state evaluation

### 3. Reinforcement Learning
Located in [`reinforcement/`](./reinforcement)

Explores fundamental concepts in reinforcement learning:
- **Value Iteration**: Implementation of the Bellman equation for optimal value function computation
- **Policy Management**: Development of explicit state-action policies
- **Q-Learning**: Model-free learning from experience
  - Epsilon-Greedy exploration strategy
- **Approximate Q-Learning**: Function approximation using linear and neural network approaches

## Getting Started

Each project directory contains its own README with specific instructions for running the implementations. The projects use Python and include various test cases and autograders for verification.

## Dependencies

- Python 3.x
- Additional dependencies are listed in each project's directory

## Course Information

- **Course**: CS471 - Introduction to Artificial Intelligence
- **Institution**: University of Oregon
- **Professor**: Thanh Nguyen
- **Term**: Fall 2024
	
