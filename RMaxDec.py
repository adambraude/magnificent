##########################
######   RMaxDec     ######
##########################

#Code based on a minimax algorithm found at https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/
#And the Maximum Decision Algorithm in the AI textbook in section 5.5

#This is an adaptation of Rminimax, designed by Silvia Garcia Diez, Jerome Laforge, and Marco Saerens

# Each player is trying to reach the terminal state that gives them the highest score. The boardstate has
# an eval for each player, and the player will pick the node that has the highest score.

# The list of players should be in their turn order, with players[0] being the first player, and players[3]
#being the last one

import math
import random

class RMaxDec:
    #The player list should be ordered by the player's turn order
    def __init__(self, boardState, depth, startingPlayer, evalFunc, theta):
        self.boardState = boardState# The current boardstate
        self.currentNode = None     # GameNode
        self.successors = []        # List of GameNodes
        self.cap = depth            # How many levels to go down
        self.currentDepth = 0       # The current level of minimax  
        self.players = boardState.players
        self.startingPlayer = startingPlayer    #This should be a number
        self.evalFunc = evalFunc
        self.theta = theta             #a real number indicating the amount of entropy. lower is more entropic
        return

    # returns the node of the best move
    def Rmaxdec(self):
        currentPlayer = self.players[self.startingPlayer]
        # first, find the max value
        self.currentNode = self.boardState
        best_moves = self.Rmulti_max(self.currentNode, self.startingPlayer)

        bestBoard = best_moves[1]
        # return that best value that we've found
        return bestBoard

    # returns a value matrix for a move
    # should probably be tweaked to grab the best value for the CURRENT player

    #returns a 2 element list, first elem is score, second is the parent node
    def Rmulti_max(self, node, playerNum):
        if self.isTerminal(node):
            node.z = [1,1,1,1]
            return [self.getUtility(node, self.currentDepth), node]

        self.currentDepth += 1
        currentPlayer = self.players[playerNum]
        nextPlayerNum = (playerNum + 1) % len(self.players)
        next_nodes = self.boardState.children()

        infinity = float('inf')
        currentBest = -infinity
        bestValues = []
        bestNode = None
        node.z = [0,0,0,0]
        weights = []
        for state in next_nodes:
            oldvalues = self.Rmulti_max(state, nextPlayerNum)
            valvec = oldvalues[0]
            max_value = valvec[playerNum]
            state.value = max_value
            for i in range(4):
                node.z[i] += math.exp(self.theta*max_value)*oldvalues[1].z[i]
            if max_value > currentBest:
                currentBest = max_value
                bestValues = valvec
                bestNode = state

        if self.currentDepth == 1:
            for state in next_nodes:
                weights.append((state.z[playerNum]/node.z[playerNum])*math.exp(self.theta*state.value))
            return [node.z[playerNum],random.choices(next_nodes, weights)[0]]

        
        self.currentDepth -= 1
        return [bestValues, bestNode]

    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes...
    def getSuccessors(self, node):
        assert node is not None
        return node.children()

    # return true if the node has NO children (successor states) OR we reach the maximum depth
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        assert node is not None
        return ((self.currentDepth > self.cap) or len(node.children()) == 0)

    #Will need to spit out a vector that has value for each player
    def getUtility(self, node, numTurns):
        assert node is not None
        return self.evalFunc(numTurns, node)
