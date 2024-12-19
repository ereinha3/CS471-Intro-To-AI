# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        This evaluation function considers the proximity to food and ghosts, aiming to
        increase Pacman's score while avoiding ghosts.
        """
        # Generate the successor game state for the action
        # Add 1 to ensure no divide by 0
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()

        score = successorGameState.getScore()

        # Linearly combining score based on food distances
        foodDists = [manhattanDistance(newPos, food) for food in newFood.asList()]
        nearestFood = min(foodDists) if foodDists else 0
        score += 10 / (nearestFood+1) if nearestFood > 0 else 0

        # Linearly combining score based on ghost distances
        ghostDistances = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        closestGhost = min(ghostDistances) if ghostDistances else float('inf')

        if closestGhost > 1:
            score += 10 / (closestGhost + 1)
        else:
            score -= 500

        return score
    

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """

        # Start recursion for Pacman (agentIndex=0)
        _, bestAction = self.handleRecursion(gameState, 0, 0)
        return bestAction

    def handleRecursion(self, state: GameState, depth, agentIndex):
        # Check if terminal state or maximum depth reached
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state), None

        # Determine whether Pacman or Ghost
        if agentIndex == 0:  # Pacman's turn
            return self.maxValue(state, depth,)
        else:  # Ghosts' turn
            return self.minValue(state, depth, agentIndex)

    def maxValue(self, state: GameState, depth):
        value = float('-inf')
        bestAction = None

        # Iterate over all Pacman's possible actions
        for action in state.getLegalActions(0):
            successor = state.generateSuccessor(0, action)
            successorValue, _ = self.handleRecursion(successor, depth, 1)

            # Update the best value
            if successorValue > value:
                value = successorValue
                bestAction = action


        return value, bestAction

    def minValue(self, state: GameState, depth, agentIndex):
        value = float('inf')
        bestAction = None

        # Compute the next agent index and depth
        numAgents = state.getNumAgents()
        nextAgentIndex = (agentIndex + 1) % numAgents
        nextDepth = depth + 1 if nextAgentIndex == 0 else depth

        # Iterate over all ghost actions
        for action in state.getLegalActions(agentIndex):
            successor = state.generateSuccessor(agentIndex, action)
            successorValue, _ = self.handleRecursion(successor, nextDepth, nextAgentIndex)

            if successorValue < value:
                value = successorValue
                bestAction = action

        return value, bestAction
    
        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        # Start alpha-beta recursion for Pacman
        _, bestAction = self.handleRecursion(gameState, 0, 0, float('-inf'), float('inf'))
        return bestAction

    def handleRecursion(self, state: GameState, depth, agentIndex, alpha, beta):
        # Check if terminal state or maximum depth reached
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state), None

        # Determine whether Pacman or Ghost
        if agentIndex == 0:  # Pacman's turn
            return self.maxValue(state, depth, alpha, beta)
        else:  # Ghosts' turn
            return self.minValue(state, depth, agentIndex, alpha, beta)

    def maxValue(self, state: GameState, depth, alpha, beta):
        value = float('-inf')
        bestAction = None

        # Iterate over all Pacman's possible actions
        for action in state.getLegalActions(0):
            successor = state.generateSuccessor(0, action)
            successorValue, _ = self.handleRecursion(successor, depth, 1, alpha, beta)

            if successorValue > value:
                value = successorValue
                bestAction = action

            # Update alpha
            alpha = max(alpha, value)
            # Prune if the current value is greater than beta
            if value > beta:
                return value, bestAction

        return value, bestAction

    def minValue(self, state: GameState, depth, agentIndex, alpha, beta):
        value = float('inf')
        bestAction = None

        # Compute the next agent index and depth
        numAgents = state.getNumAgents()
        nextAgentIndex = (agentIndex + 1) % numAgents
        nextDepth = depth + 1 if nextAgentIndex == 0 else depth

        # Iterate over all ghost actions
        for action in state.getLegalActions(agentIndex):
            successor = state.generateSuccessor(agentIndex, action)
            successorValue, _ = self.handleRecursion(successor, nextDepth, nextAgentIndex, alpha, beta)

            # Update the best value
            if successorValue < value:
                value = successorValue
                bestAction = action

            # Update beta
            beta = min(beta, value)
            # Prune if the current value is less than alpha
            if value < alpha:
                return value, bestAction

        return value, bestAction


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        # Start expectimax recursion for Pacman
        _, bestAction = self.expectimax(gameState, 0, 0)
        return bestAction

    def expectimax(self, state: GameState, depth, agentIndex):
        # Check if terminal state or maximum depth reached
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state), None

        # Determine whether Pacman or Ghost
        if agentIndex == 0:  # Pacman's turn
            return self.maxValue(state, depth)
        else:  # Ghosts' turn
            return self.expValue(state, depth, agentIndex)

    def maxValue(self, state: GameState, depth):
        value = float('-inf')
        bestAction = None

        # Iterate over Pacman's possible actions
        for action in state.getLegalActions(0):
            successor = state.generateSuccessor(0, action)
            successorValue, _ = self.expectimax(successor, depth, 1)

            if successorValue > value:
                value = successorValue
                bestAction = action

        return value, bestAction

    def expValue(self, state: GameState, depth, agentIndex):
        value = 0
        actions = state.getLegalActions(agentIndex)

        # Compute the next agent index and depth
        numAgents = state.getNumAgents()
        nextAgentIndex = (agentIndex + 1) % numAgents
        nextDepth = depth + 1 if nextAgentIndex == 0 else depth

        # No actions available = return evaluation
        if not actions:
            return self.evaluationFunction(state), None

        # Assuming probabilities are equal (random actions)
        probability = 1 / len(actions)

        # Iterate over all ghost's possible actions and average the results
        for action in actions:
            successor = state.generateSuccessor(agentIndex, action)
            successorValue, _ = self.expectimax(successor, nextDepth, nextAgentIndex)
            value += probability * successorValue

        return value, None

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: 
    Takes into account food, scared ghosts, and capsule distances
    Does not take into account regular ghosts as pacman knows to avoid them when they are right next to him (encourages exploration)
    Highest priority to scared ghosts as they give score and reduce danger
    Second highest to capsules as they make ghosts scared and give points
    Lowest priority to food as priority goal is staying alive
    """

    pos = currentGameState.getPacmanPosition()
    pellets = currentGameState.getFood().asList()
    ghosts = currentGameState.getGhostStates()
    capsules = currentGameState.getCapsules()
    currentScore = currentGameState.getScore()
    
    score = 0
    
    # Add scaled min food distance (10 / (minDist + 1))
    score += 10 / (min([manhattanDistance(pos, pellet) for pellet in pellets]) + 1) if pellets else 0

    # Add scaled ghost distance from each scared ghost (incentivizes chasing scared ghosts and eating them) and penalizes getting close to not scared ghosts
    for ghost in ghosts:
        ghostPos = ghost.getPosition()
        distanceToGhost = manhattanDistance(pos, ghostPos)
        if ghost.scaredTimer > 0:
            # If ghost is scared, it's beneficial to be close to it for extra points
            score += 20 / (distanceToGhost + 1)
        else:
            # If ghost is active, apply a penalty if too close to encourage avoidance
            if distanceToGhost < 2:
                score -= 200  # High penalty if too close to an active ghost
            
    # Add scaled capsule distance (15 / (minDist + 1))
    score += 15 / (min(manhattanDistance(pos, cap) for cap in capsules) + 1) if capsules else 0

    # Add current game score
    score += currentScore
    
    return score

# Abbreviation
better = betterEvaluationFunction
