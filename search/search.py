# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def graphSearch(problem, frontier):
    """ Sources: Book, chapter 3- page 77 psuedocode
        General description of graph-search algorithm
        Returns a soltion or failure
        As mentioned in description, we can use this generic search method with different DS for the other search problems
    """

    # initialize the frontier using problem start state and empty set
    frontier.push((problem.getStartState(), []))
    visited = []
    # check if start state = goal state
    # if problem.getStartState() == problem.isGoalstate():
    #     return []
    while True:
        if frontier.isEmpty():
            return []
        # choose a leaf node and remove it from the frontier
        state, actions = frontier.pop()
        # if the node contains a goal state return the solution
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            # add the node is not in the explored
            visited.append(state)
            # expand the chosen node, adding the result
            sucessors = problem.getSuccessors(state)
            # nodes that is not in the explored to the frontier
            for successor, action, stepCost in sucessors:
                if successor not in visited:
                    next_actions = actions + [action]
                    successor_node = (successor, next_actions)
                    frontier.push(successor_node)

    return []




def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    # first attempt before creating graphSearch. after realizing the other funcs are same structure
    from util import Stack

    print ("Start: ") + str(problem.getStartState)
    print ("Goal: ") + str(problem.isGoalState)

    stackSol = Stack()
    visitedStates = []  # Visited states
    path = []  # Every state keeps it's path from the starting state
    # See if goal == start state, then you are finished
    if problem.isGoalState(problem.getStartState()):
        return []
    # Start from the beginning and find a solution, path is an empty list #
    stackSol.push((problem.getStartState(), []))
    # If stack is empty, there isn't a start state
    if stackSol.isEmpty():
        return []

    while (True):  # will run indefinitely unless returned
        # get position and path for the current state
        xy, path = stackSol.pop()
        visitedStates.append(xy)
        if problem.isGoalState(xy):
            print("path: ") + str(path)
            return path
        # get successor from the current state
        successors = problem.getSuccessors(xy)
        # Add new states in stack and fix their path #
        if successors:
            for item in successors:
                #print ("sucessor: ") + str(item)
                if item[0] not in visitedStates:
                    newPath = path + [item[1]]  # Calculate new path
                    stackSol.push((item[0], newPath))

    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    Resource: Book chp 3- pg 85 Psuedocode
    """
    # utilize queue and our graph search algorithm
    # we only need actions, cost not important
    def costFunction((state, actions)):
        return len(actions)

    frontier = util.PriorityQueueWithFunction(costFunction)
    frontier.push((problem.getStartState(), []))
    return graphSearch(problem, frontier)



def uniformCostSearch(problem):
    """Search the node of least total cost first.
    By changing the cost function, we can encourage Pacman to find different paths.
    """
    # similar to BFS, but we need to factor in cost
    def costFunction((state, actions)):
        return problem.getCostOfActions(actions)

    # use priority queue and our graphSearch function
    frontier = util.PriorityQueueWithFunction(costFunction)
    return graphSearch(problem, frontier)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    # similar structure as before, but we want to add heuristics to search
    def costFunction((state, actions)):
        return problem.getCostOfActions(actions) + heuristic(state, problem)

    frontier = util.PriorityQueueWithFunction(costFunction)
    return graphSearch(problem, frontier)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
