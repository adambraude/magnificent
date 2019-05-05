##########################
######   MINI-MAX   ######
##########################

#Code based on a minimax algorithm found at https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/

# I'm pushing all of the board evaluating functionality (such as evaluating the board and finding vlaid moves
# to a as of yet unmade 'boardState' class
# This is probably equivalent to what the 'game_tree' is

class MiniMax:
    def __init__(self, boardState, depth):
        self.boardState = boardState  # GameTree
        self.currentNode = None     # GameNode
        self.successors = []        # List of GameNodes
        self.cap = depth            # How big of a search to do
        self.currentDepth = 0
        return

    # Currently doesn't keep track of both the best node and best value, just the best value. Should
    # change this probably
    def minimax(self):
        # first, find the max value
        currentNode = Node(boardState)
        best_val = self.max_value(currentNode) # should be root node of tree

        # second, find the node which HAS that max value
        #  --> means we need to propagate the values back up the
        #      tree as part of our minimax algorithm
        successors = self.getSuccessors(currentNode)
        # find the node with our best move
        best_move = None
        for elem in successors:   # ---> Need to propagate values up tree for this to work
            if elem.value == best_val:
                best_move = elem
                break

        # return that best value that we've found
        return best_move


    def max_value(self, node):
        if self.isTerminal(node):
            return self.getUtility(node)

        depth += 1
        infinity = float('inf')
        max_value = -infinity

        successors_states = self.getSuccessors(node)
        for state in successors_states:
            max_value = max(max_value, self.min_value(state))
        return max_value

    def min_value(self, node):
        if self.isTerminal(node):
            return self.getUtility(node)

        infinity = float('inf')
        min_value = infinity

        successor_states = self.getSuccessors(node)
        for state in successor_states:
            min_value = min(min_value, self.max_value(state))
        return min_value

    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes...
    def getSuccessors(self, node):
        assert node is not None
        return node.children

    # return true if the node has NO children (successor states) OR we reach the maximum depth
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        assert node is not None
        return ((len(node.children) == 0) or (depth > cap))

    def getUtility(self, node):
        assert node is not None
        return node.value
