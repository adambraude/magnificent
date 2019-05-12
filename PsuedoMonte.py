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
    def outer_monte(self, numSamples):
        bestMove = None
        infinity = float('inf')
        bestScore = -infinity

        nextNodes = self.boardState.children()
        counter = 0
        bestAverage = 0
        bestMove = None
        
        for state in nextNodes:
            score = 0
            while counter < self.samples:
                counter+= 1
                stateVal = monte(state, self.samples)
                sampleVec = stateVal[0]
                score += sampleVec[self.startingPlayer]

            moveAverage = (score/self.samples)
            if moveAverage > bestAverage:
                bestAverage = moveAverage
                bestMove = state

        return bestMove

    #For a given random child for a parent, what is the average score of its children
    #This doesn't find the best move, it finds the average score for making this move
    def monte(self, state, numSamples):
        if self.isTerminal(node):
            return self.getUtility(node, self.currentDepth)

        currentDepth += 1
        
        nextNodes = self.boardState.children()
        ranMove = random.choice(nextNodes)
        ccounter = 0

        totalScore = [0] * len(self.players)
        averageScore = [0]*len(self.players)
        
        nextSamples = self.samples
        while counter < numSamples:
            counter += 1
            sampleVal = monte(self, ranMove, nextSamples)

            for i in range(len(self.players)):
                totalScore[i] += sampleVal[i]

        for i in range(len(self.players)):
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
