#An algorithm based on random moves
#Currently has a runTime of numSamples^(depth+1). Could decrease this with some sort of
#decay operation for the number of samples taken at deeper levels.
class PsuedoMonte:
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

    def outer_monte(self, numSamples):
        bestMove = None
        infinity = float('inf')
        bestScore = -infinity
        
        while counter < numSamples:
            possMove = monte(self.boardState, self.samples, self.startingPlayer)
            if possMove[1] > bestScore:
                bestScore = possMove[1]
                bestMove = possMove[0]

        return bestMove

    def monte(self, state, numSamples, playerNum):
        if self.isTerminal(node):
            return [self.getUtility(node, self.currentDepth), node]

        currentDepth += 1
        
        nextNodes = self.boardState.children()
        ranMove = random.choice(nextNodes)
        checks = 0
        average = 0
        nextSamples = self.samples
        while checks < numSamples:
            nextPlayerNum = (playerNum + 1) % len(self.players)
            ranMove = random.choice(nextNodes)
            sampleVal = monte(self, ranMove, nextSamples, nextPlayerNum)
            valVec = sampleVal[1]
            average += valVec[playerNum]

        return [ranMove, (average/numSamples)]


    #                     #
    #   UTILITY METHODS   #
    #                     #

    def isTerminal(self, node):
        assert node is not None
        return ((self.currentDepth > self.maxDepth) or len(node.children()) == 0)

    def getUtility(self, node, numTurns):
        assert node is not None
        return self.evalFunc(numTurns, node)
