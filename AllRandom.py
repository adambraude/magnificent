import random
#An algorithm based on random moves
#Currently has a runTime of numSamples^(depth+1). Could decrease this with some sort of
#decay operation for the number of samples taken at deeper levels.

#The idea of this ai is that it takes an inputted amount of samples, generates the
#numPaths amount of random moves from that sample, then returns the sample that has the
#highest possible value for a path.
#This is basically a random greedy algorithm.
class AllRandom:
    def __init__(self, boardState, startingPlayer, depth, samples, numPaths, evalFunc):
        self.boardState = boardState
        self.startingPlayer = startingPlayer
        self.currentDepth = 0
        self.maxDepth = depth
        self.evalFunc = evalFunc
        self.samples = samples
        self.numPaths = numPaths

    def outer_ran(self):
        bestMove = None
        
        infinity = float('inf')
        
        bestMoveVal = -infinity
        sampleMoves = self.samples
        counter = 0
        innerLoop = 0

        possNodes = self.boardState.children()
        
        while counter < sampleMoves:
            counter += 1
            sampleNode = random.choice(possNodes)
            sampleVal = -infinity
            while innerLoop < self.numPaths:
                innerLoop += 1
                ranPathVec = self.ran_path(sampleNode)
                sampleScore = ranPathVec[self.startingPlayer]
                if sampleScore > sampleVal:
                    sampleVal = sampleScore

            if sampleVal > bestMoveVal:
                bestMoveVal = sampleVal
                bestMove = sampleNode

        return bestMove

    #Each step generates a random node and generates a random path for that node, so
    #pick the node that gets the best score
    def ran_path(self, state):
        if self.isTerminal(state):
            return self.getUtility(state, self.currentDepth)

        self.currentDepth += 1
        
        nextNodes = state.children()
        ranMove = random.choice(nextNodes)
        checks = 0

        return self.ran_path(ranMove)


    #                     #
    #   UTILITY METHODS   #
    #                     #

    def isTerminal(self, node):
        assert node is not None
        return ((self.currentDepth > self.maxDepth) or len(node.children()) == 0)

    def getUtility(self, node, numTurns):
        assert node is not None
        return self.evalFunc(numTurns, node)

