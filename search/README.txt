In this project, my Pacman agent finds paths through his maze world, both to reach a particular location and to collect food efficiently. I built a general search algorithms and applied them to Pacman scenarios.

For the following, the commands provided show the execution of my implementations.

Part 1: Finding a Fixed Food Dot using Depth First Search
python pacman.py -l bigMaze -z .5 -p SearchAgent
python autograder.py -q q1

Part 2: Breadth First Search
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python eightpuzzle.py
python autograder.py -q q2

Part 3: Varying the Cost Function
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
python autograder.py -q q3

Part 4: A* Search
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python autograder.py -q q4

Part 5: Finding All The Corners
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python autograder.py -q q5

Part 6: Corners Problem: Heuristic
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
python autograder.py -q q6

Part 7: Eating All The Dots
python pacman.py -l trickySearch -p AStarFoodSearchAgent
python autograder.py -q q7

Part 8: Suboptimal Search
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
python autograder.py -q q8
