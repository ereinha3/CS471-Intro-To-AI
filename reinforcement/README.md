# Reinforcement Learning Project

This project implements various reinforcement learning algorithms and applies them to Gridworld, a simulated robot controller (Crawler), and Pacman environments. The implementations include value iteration, Q-learning, and approximate Q-learning.

## Project Components

### 1. Value Iteration
Implementation of the Bellman equation for optimal value function computation in MDPs.
```bash
# Run value iteration on Gridworld
python gridworld.py -a value -i 100 -k 10

# Test the implementation
python autograder.py -q q1
```

### 2. Policy Analysis
Exploration of different policies under varying discount, noise, and reward parameters.
```bash
# Run with custom parameters
python gridworld.py -g DiscountGrid -a value --discount [DISCOUNT] --noise [NOISE] --livingReward [LIVING_REWARD]

# Test the implementation
python autograder.py -q q2
```

### 3. Q-Learning
Model-free learning implementation that learns from experience.
```bash
# Run Q-learning on Gridworld
python gridworld.py -a q -k 5 -m

# Test the implementation
python autograder.py -q q3
```

### 4. Epsilon Greedy
Implementation of exploration vs exploitation strategy.
```bash
# Run with epsilon-greedy strategy
python gridworld.py -a q -k 100 --noise 0.0 -e 0.1

# Test the implementation
python autograder.py -q q4

# Try the crawler simulation
python crawler.py
```

### 5. Q-Learning and Pacman
Application of Q-learning to the Pacman environment.
```bash
# Train Pacman with Q-learning
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid 

# Test the implementation
python autograder.py -q q5
```

### 6. Approximate Q-Learning
Implementation of Q-learning with function approximation.
```bash
# Train Pacman with approximate Q-learning
python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid 

# Test the implementation
python autograder.py -q q6
```

## Key Files

- `valueIterationAgents.py`: Value iteration implementation
- `qlearningAgents.py`: Q-learning implementations
- `learningAgents.py`: Base classes for learning agents
- `environment.py`: Environment interface
- `gridworld.py`: Gridworld environment implementation
- `crawler.py`: Crawler robot simulation
- `featureExtractors.py`: Feature extraction for approximate Q-learning

## Testing

Run all tests using:
```bash
python autograder.py
```

Or test specific questions using:
```bash
python autograder.py -q qN
```
where N is the question number (1-6).

## Environments

The project includes three main environments:
1. **Gridworld**: A simple grid-based environment for testing basic RL concepts
2. **Crawler**: A physics-based robot simulation for testing continuous state spaces
3. **Pacman**: The classic Pacman game for testing in a complex environment 