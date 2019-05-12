import random
#An algorithm based on random moves
#Currently has a runTime of numSamples^(depth+1). Could decrease this with some sort of
#decay operation for the number of samples taken at deeper levels.

#The idea of this ai is that it takes an inputted amount of samples, generates that number of
#possible moves from the current state, then generates a random path from the random sample
#for a given depth. It then returns the highest scoring path found this way.
#This is a random greedy algorithm.
class AllRandom:
    def __init__(self, boardState, players, startingPlayer, depth, samples, evalFunc):
        self.boardState = boardState
        self.players = players
        self.startingPlayer = startingPlayer
        self.currentDepth = -1  #If started at 0, if the user gave a depth of zero, the is
                                #isTerminal check would only run on the initial boardState
                                #without looking at any of the children nodes
        self.maxDepth = depth
        self.evalFunc = evalFunc
        self.samples = samples

    def outer_ran(self):
        bestMove = None
        infinity = float('inf')
        bestScore = -infinity
        numSamples = self.samples
        counter = 0
        
        while counter < numSamples:
            counter += 1
            possMove = self.ran_path(self.boardState, self.samples, self.startingPlayer)
            sampleVec = possMove[0]
            if sampleVec[self.startingPlayer] > bestScore:
                bestScore = sampleVec[self.startingPlayer]
                bestMove = possMove[1]

        return bestMove

    #Each step generates a random node and generates a random path for that node, so
    #pick the node that gets the best score
    def ran_path(self, state, numSamples, playerNum):
        if self.isTerminal(state):
            return [self.getUtility(state, self.currentDepth), state]

        self.currentDepth += 1
        
        nextNodes = self.boardState.children()
        ranMove = None
        checks = 0

        infinity = float('inf')
        bestMoveVal = -infinity
        bestMoveVec = None
        bestPlayerMove = None
        
        nextSamples = self.samples
        while checks < numSamples:
            nextPlayerNum = (playerNum + 1) % len(self.players)
            ranMove = random.choice(nextNodes)
            sampleVal = self.ran_path(ranMove, nextSamples, nextPlayerNum)
            checks += 1
            
            sampleVec = sampleVal[0]
            if bestMoveVal < sampleVec[playerNum]:
                bestMoveVal = sampleVec[playerNum]
                bestMoveVec = sampleVec
                bestPlayerMove = ranMove

        return [bestMoveVec, bestPlayerMove]


    #                     #
    #   UTILITY METHODS   #
    #                     #

    def isTerminal(self, node):
        assert node is not None
        return ((self.currentDepth > self.maxDepth) or len(node.children()) == 0)

    def getUtility(self, node, numTurns):
        assert node is not None
        return self.evalFunc(numTurns, node)

