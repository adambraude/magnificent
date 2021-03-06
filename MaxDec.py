##########################
######   MaxDec     ######
##########################

#Code based on a minimax algorithm found at https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/
#And the Maximum Decision Algorithm in the AI textbook in section 5.5

# Each player is trying to reach the terminal state that gives them the highest score. The boardstate has
# an eval for each player, and the player will pick the node that has the highest score.

# The list of players should be in their turn order, with players[0] being the first player, and players[3]
#being the last one

class MaxDec:
    #The player list should be ordered by the player's turn order
    def __init__(self, boardState, depth, players, startingPlayer, evalFunc):
        self.boardState = boardState# The current boardstate
        self.currentNode = None     # GameNode
        self.successors = []        # List of GameNodes
        self.cap = depth            # How many levels to go down
        self.currentDepth = 0       # The current level of minimax  
        self.players = players
        self.startingPlayer = startingPlayer    #This should be a number
        self.evalFunc = evalFunc
        return

    # returns the node of the best move
    def maxdec(self):
        currentPlayer = self.players[self.startingPlayer]
        # first, find the max value
        self.currentNode = self.boardState
        best_moves = self.multi_max(self.currentNode, self.startingPlayer)

        bestBoard = best_moves[1]
        # return that best value that we've found
        return bestBoard

    # returns a value matrix for a move
    # should probably be tweaked to grab the best value for the CURRENT player

    #returns a 2 element list, first elem is score, second is the parent node
    def multi_max(self, node, playerNum):
        if self.isTerminal(node):
            return [self.getUtility(node, self.currentDepth), node]

        self.currentDepth += 1
        currentPlayer = self.players[playerNum]
        nextPlayerNum = (playerNum + 1) % len(self.players)
        next_nodes = self.boardState.children()

        infinity = float('inf')
        currentBest = -infinity
        bestValues = []
        bestNode = None
        
        for state in next_nodes:
            oldvalues = self.multi_max(state, nextPlayerNum)
            valvec = oldvalues[0]
            max_value = valvec[playerNum]
            if max_value > currentBest:
                currentBest = max_value
                bestValues = valvec
                bestNode = state

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
