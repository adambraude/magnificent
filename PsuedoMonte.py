import random
#An algorithm based on random moves
#Currently has a runTime of numSamples^(depth). Could decrease this with some sort of
#decay operation for the number of samples taken at deeper levels.
class PsuedoMonte:
    def __init__(self, boardState, startingPlayer, depth, samples, evalFunc):
        self.boardState = boardState
        self.startingPlayer = startingPlayer
        self.currentDepth = 0
        self.maxDepth = depth #Note that starting with a depth of zero is just a greedy search
        self.evalFunc = evalFunc
        self.samples = samples

    #Checks an inputted amount of random paths for each child, takes the average, and returns
    # the move with the highest average score
    def outer_monte(self):
        bestMove = None
        infinity = float('inf')
        bestScore = -infinity
        numSamples = self.samples

        nextNodes = self.boardState.children()
        counter = 0
        bestAverage = 0
        bestMove = None
        
        for state in nextNodes:
            score = 0
            while counter < self.samples:
                counter+= 1
                stateVal = self.monte(state, self.samples)
                score += stateVal[self.startingPlayer]

            moveAverage = (score/self.samples)
            if moveAverage > bestAverage:
                bestAverage = moveAverage
                bestMove = state

        return bestMove

    #For a given random child for a parent, what is the average score of its children
    #This doesn't find the best move, it finds the average score for making this move
    def monte(self, state, numSamples):
        if self.isTerminal(state):
            return self.getUtility(state, self.currentDepth)

        self.currentDepth += 1
        
        nextNodes = self.boardState.children()
        ranMove = random.choice(nextNodes)
        counter = 0

        totalScore = [0] * len(state.players)
        averageScore = [0]*len(state.players)
        
        nextSamples = self.samples
        while counter < numSamples:
            counter += 1
            sampleVal = self.monte(ranMove, nextSamples)

            for i in range(len(state.players)):
                totalScore[i] += sampleVal[i]

        for i in range(len(state.players)):
                averageScore[i] = (totalScore[i]/numSamples)
        
        return averageScore


    #                     #
    #   UTILITY METHODS   #
    #                     #

    def isTerminal(self, node):
        assert node is not None
        return ((self.currentDepth > self.maxDepth) or len(node.children()) == 0)

    def getUtility(self, node, numTurns):
        assert node is not None
        return self.evalFunc(numTurns, node)
