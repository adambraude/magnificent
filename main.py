import random
import copy
import minimax
from MaxDec import *
from AllRandom import *

print ("Hello, and welcome to Splandor!")

verbose = 0
Rwinner = -1

colors = "W", "U", "G", "R", "B", "Y"

# color, points, white, blue, green, red, black
fresh_tier1Deck = [
(4, 0, 1, 1, 1, 1, 0),
(4, 0, 1, 2, 1, 1, 0),
(4, 0, 2, 2, 0, 1, 0),
(4, 0, 0, 0, 1, 3, 1),
(4, 0, 0, 0, 2, 1, 0),
(4, 0, 2, 0, 2, 0, 0),
(4, 0, 0, 0, 3, 0, 0),
(4, 1, 0, 4, 0, 0, 0),

(1, 0, 1, 0, 1, 1, 1),
(1, 0, 1, 0, 1, 2, 1),
(1, 0, 1, 0, 2, 2, 0),
(1, 0, 0, 1, 3, 1, 0),
(1, 0, 1, 0, 0, 0, 2),
(1, 0, 0, 0, 2, 0, 2),
(1, 0, 0, 0, 0, 0, 3),
(1, 1, 0, 0, 0, 4, 0),

(0, 0, 0, 1, 1, 1, 1),
(0, 0, 0, 1, 2, 1, 1),
(0, 0, 0, 2, 2, 0, 1),
(0, 0, 3, 1, 0, 0, 1),
(0, 0, 0, 0, 0, 2, 1),
(0, 0, 0, 2, 0, 0, 2),
(0, 0, 0, 3, 0, 0, 0),
(0, 1, 0, 0, 4, 0, 0),

(2, 0, 1, 1, 0, 1, 1),
(2, 0, 1, 1, 0, 1, 2),
(2, 0, 0, 1, 0, 2, 2),
(2, 0, 1, 3, 1, 0, 0),
(2, 0, 2, 1, 0, 0, 0),
(2, 0, 0, 2, 0, 2, 0),
(2, 0, 0, 0, 0, 3, 0),
(2, 1, 0, 0, 0, 0, 4),

(3, 0, 1, 1, 1, 0, 1),
(3, 0, 2, 1, 1, 0, 1),
(3, 0, 2, 0, 1, 0, 2),
(3, 0, 1, 0, 0, 1, 3),
(3, 0, 0, 2, 1, 0, 0),
(3, 0, 2, 0, 0, 2, 0),
(3, 0, 3, 0, 0, 0, 0),
(3, 1, 4, 0, 0, 0, 0)
    ]

fresh_tier2Deck = [
(4, 1, 3, 2, 2, 0, 0),
(4, 1, 3, 0, 3, 0, 2),
(4, 2, 0, 1, 4, 2, 0),
(4, 2, 0, 0, 5, 3, 0),
(4, 2, 5, 0, 0, 0, 0),
(4, 3, 0, 0, 0, 0, 6),

(1, 1, 0, 2, 2, 3, 0),
(1, 1, 0, 2, 3, 0, 3),
(1, 2, 5, 3, 0, 0, 0),
(1, 2, 2, 0, 0, 1, 4),
(1, 2, 0, 5, 0, 0, 0),
(1, 3, 0, 6, 0, 0, 0),

(0, 1, 0, 0, 3, 2, 2),
(0, 1, 2, 3, 0, 3, 0),
(0, 2, 0, 0, 1, 4, 2),
(0, 2, 0, 0, 0, 5, 3),
(0, 2, 0, 0, 0, 5, 0),
(0, 3, 6, 0, 0, 0, 0),

(2, 1, 3, 0, 2, 3, 0),
(2, 1, 2, 3, 0, 0, 2),
(2, 2, 4, 2, 0, 0, 1),
(2, 2, 0, 5, 3, 0, 0),
(2, 2, 0, 0, 5, 0, 0),
(2, 3, 0, 0, 6, 0, 0),

(3, 1, 2, 0, 0, 2, 1),
(3, 1, 0, 3, 0, 2, 1),
(3, 2, 1, 4, 2, 0, 2),
(3, 2, 3, 0, 0, 0, 3),
(3, 2, 0, 0, 0, 0, 5),
(3, 3, 0, 0, 0, 6, 0)
    ]

fresh_tier3Deck = [
(4, 3, 3, 3, 5, 3, 0),
(4, 4, 0, 0, 0, 7, 0),
(4, 4, 0, 0, 3, 6, 3),
(4, 5, 0, 0, 0, 7, 3),

(1, 3, 3, 0, 3, 3, 5),
(1, 4, 7, 0, 0, 0, 0),
(1, 4, 6, 3, 0, 0, 3),
(1, 5, 7, 3, 0, 0, 0),

(0, 3, 0, 3, 3, 5, 3),
(0, 4, 0, 0, 0, 0, 7),
(0, 4, 3, 0, 0, 3, 6),
(0, 5, 3, 0, 0, 0, 7),

(2, 3, 5, 3, 0, 3, 3),
(2, 4, 0, 7, 0, 0, 0),
(2, 4, 3, 6, 3, 0, 0),
(2, 5, 0, 7, 3, 0, 0),

(3, 3, 3, 5, 3, 0, 3),
(3, 4, 0, 0, 7, 0, 0),
(3, 4, 0, 3, 6, 3, 0),
(3, 5, 0, 0, 7, 3, 0)
    ]

fresh_nobles = [
(0, 0, 3, 3, 3),
(3, 3, 3, 0, 0),
(3, 3, 0, 0, 3),
(0, 3, 3, 3, 0),
(3, 0, 0, 3, 3),
(4, 4, 0, 0, 0),
(0, 4, 4, 0, 0),
(0, 0, 4, 4, 0),
(4, 0, 0, 0, 4),
(0, 0, 0, 4, 4)
    ]



class GameState:
    
    def __init__(self):
        self.nobles = []
        self.cards = [[],[],[]]
        # white, blue, green, red, black, yellow
        self.gemsAvailable = [7, 7, 7, 7, 7, 5]
        self.players = []
        self.turn = 1
        self.playerTurn = 0
        self.childrenL = []
        self.name = "start of game"
        self.strippedCopy = None

    #advance the game by one step and return the new state
    def gameStep(self):
        self.restockCards()
        self.childrenL = []
        self.strippedCopy = None
        if (verbose): self.printState()
        win = self.checkWinner()
        if (win != -1):
            print("The winner is Player", win+1, "with a score of", self.players[win].points, "points")
            Rwinner = win
            return
        if (verbose): print("Player", self.playerTurn+1, "turn:")
        return self.players[self.playerTurn].playerFunction(self)

    def checkWinner(self):
        if (self.playerTurn == 0):
            highestScore = 0
            numPlayers = 0
            numPlayer = 0
            for i in range(len(self.players)):
                pts = self.players[i].points
                if (pts > highestScore):
                    highestScore = pts
                    numPlayer = i
                    numPlayers = 0
                if (pts == highestScore):
                    numPlayers += 1
            if highestScore >= 15:
                if numPlayers == 1:
                    return numPlayer
                else:
                    #In ties, the player with the fewest development cards wins
                    #This is a fairly clunky way to do it, but should work
                    winningPlayer = 0
                    fewestCards = len(tier1Deck)+len(tier2Deck)+len(tier3Deck)+1
                    for j in range(len(self.players)):
                        currentPlayer = self.players[i]
                        if (highestScore == currentPlayer.points):
                            playerCards = sum(currentPlayer.cardsOwned)
                            if (playerCards < fewestCards):
                                fewestCards = playerCards
                                winningPlayer = i
                return winningPlayer
        return -1

    #run this on the very first GameState
    def setupNewGame(self, decks, ndeck):
        l = len(self.players)+1
        for i in range(len(self.gemsAvailable)-1):
            if (l == 3): self.gemsAvailable[i] -= 3
            if (l == 4): self.gemsAvailable[i] -= 2
        for i in range(l):
            noble = random.choice(ndeck)
            self.nobles.append(noble)
            ndeck.remove(noble)
        for j in range(len(decks)):
            for i in range(4):
                card = random.choice(decks[j])
                self.cards[j].append(card)
                decks[j].remove(card)
        self.decks = decks
        if (verbose):
            self.printState()
            print("Player", self.playerTurn+1, "turn:")
        self.players[self.playerTurn].playerFunction(self)
        self.children()

    #refills any open card slots
    def restockCards(self):
        for j in range(len(self.cards)):
            while (len(self.cards[j]) < 4 and len(self.decks[j]) > 0):
                card = random.choice(self.decks[j])
                self.cards[j].append(card)
                self.decks[j].remove(card)

    #get all children of this node
    def children(self):
        #if children have already been generated, don't regenerate them
        if (len(self.childrenL) > 0): return self.childrenL
        #take 2
        for i in range(len(self.gemsAvailable)-1):
            if self.gemsAvailable[i] >= 4:
                new = self.copyMe()
                new.gemsAvailable[i] -= 2
                new.players[self.playerTurn].gemsOwned[i] += 2
                new.name = "take 2" + colors[i]
                if (sum(new.players[self.playerTurn].gemsOwned) > 10):
                    #self.childrenL.extend(self.discardGems([new], 0))
                    pass
                else:
                    self.childrenL.append(new)
        #take 1 from up to 3 different places
        for i in range(len(self.gemsAvailable)-1):
            for j in range(i+1, len(self.gemsAvailable)-1):
                for k in range(j+1, len(self.gemsAvailable)-1):
                    if self.gemsAvailable[i] >= 1 or self.gemsAvailable[j] >= 1 or self.gemsAvailable[k] >= 1:
                        new = self.copyMe()
                        new.name = "take "
                        if self.gemsAvailable[i]:
                            new.gemsAvailable[i] -= 1
                            new.players[self.playerTurn].gemsOwned[i] += 1
                            new.name += colors[i]
                        if self.gemsAvailable[j]:
                            new.gemsAvailable[j] -= 1
                            new.players[self.playerTurn].gemsOwned[j] += 1
                            new.name += colors[j]
                        if self.gemsAvailable[k]:
                            new.gemsAvailable[k] -= 1
                            new.players[self.playerTurn].gemsOwned[k] += 1
                            new.name += colors[k]
                        if (sum(new.players[self.playerTurn].gemsOwned) > 10):
                            #self.childrenL.extend(self.discardGems([new], 0))
                            pass
                        else:
                            self.childrenL.append(new)
        #buy card
        for i in range(len(self.cards)):
            for j in range(len(self.cards[i])):
                card = self.cards[i][j]
                if (self.canAfford(card)):
                    new = self.copyMe()
                    self.buyCard(new, card)
                    new.cards[i].remove(card)
                    new.name = "buy " + str(i*4+j+1)
                    self.takeNobles(new)
                    self.childrenL.append(new)
        r = self.players[self.playerTurn].reserve
        #buy card from reserve
        for i in range(len(r)):
            if (self.canAfford(r[i])):
                new = self.copyMe()
                self.buyCard(new, r[i])
                new.players[self.playerTurn].reserve.remove(r[i])
                new.name = "buy reserve " + str(i+1)
                self.takeNobles(new)
                self.childrenL.append(new)
        #reserve a card
        if len(r) < 3:
            for i in range(len(self.cards)):
                for j in range(len(self.cards[i])):
                    card = self.cards[i][j]
                    new = self.copyMe()
                    new.cards[i].remove(card)
                    p = new.players[self.playerTurn]
                    if new.gemsAvailable[len(self.gemsAvailable)-1]:
                        p.gemsOwned[len(self.gemsAvailable)-1] += 1
                        new.gemsAvailable[len(self.gemsAvailable)-1] -= 1
                    p.reserve.append(card)
                    new.name = "reserve " + str(i*4+j+1) 
                    if (sum(new.players[self.playerTurn].gemsOwned) > 10):
                        self.childrenL.extend(self.discardGems([new], 0))
                    else:
                        self.childrenL.append(new)
        if (len(self.childrenL) == 0):
            new = self.copyMe()
            new.name = "pass"
            self.childrenL.append(new)
        return self.childrenL

    #discards down to 10 gems if over
    #returns a list of states
    def discardGems(self, states, gemind):
        out = []
        for s in states:
            ps = s.players[self.playerTurn]
            if (sum(ps.gemsOwned) > 10):
                if (gemind == len(self.gemsAvailable)-1):
                    continue
                newStates = []
                for i in range(min(ps.gemsOwned[gemind], sum(ps.gemsOwned) - 10)+1):
                    newState = copy.deepcopy(s)
                    if (i > 0):
                        newState.name += "return" + str(i) + colors[gemind]
                    p = newState.players[self.playerTurn]
                    p.gemsOwned[gemind] -= i
                    newState.gemsAvailable[gemind] += i
                    newStates.append(newState)
                out.extend(self.discardGems(newStates, gemind+1))
            else:
                out.append(s)
        return out

    #purchase a card
    def buyCard(self, state, card):
        wild = 0
        p = state.players[self.playerTurn]
        for k in range(len(state.gemsAvailable)-1):
            kcost = card[k+2] - p.cardsOwned[k]
            if kcost < 0: kcost = 0
            state.gemsAvailable[k] += min(kcost, p.gemsOwned[k])
            p.gemsOwned[k] -= kcost
            if p.gemsOwned[k] < 0:
                wild += p.gemsOwned[k]
                p.gemsOwned[k] = 0
        p.gemsOwned[len(state.gemsAvailable)-1] += wild
        state.gemsAvailable[len(state.gemsAvailable)-1] += -wild
        p.cardsOwned[card[0]] += 1
        p.points += card[1]

    #check if a card is affordable
    def canAfford(self, card):
        wild = 0
        p = self.players[self.playerTurn]
        for k in range(len(self.gemsAvailable)-1):
            kcost = card[k+2] - p.cardsOwned[k]
            if kcost < 0: kcost = 0
            if p.gemsOwned[k] - kcost < 0:
                wild += p.gemsOwned[k] - kcost
        if p.gemsOwned[len(self.gemsAvailable)-1] >= -wild:
            return 1
        return 0

    #checks if nobles are available, takes one if possible.
    #simplification: if multiple nobles are available, take a random one
    def takeNobles(self, state):
        p = state.players[self.playerTurn]
        random.shuffle(state.nobles)
        for n in state.nobles:
            nyes = 1
            for i in range(len(p.cardsOwned)-1):
                if p.cardsOwned[i] < n[i]:
                    nyes = 0
                    break
            if nyes:
                state.nobles.remove(n)
                p.points += 3
                break

    #Returns a score for the highest fraction of a noble a player has
    #If player doesn't have noble, return (the highest percentage of nobles
    #on board)/(3). If player already has a noble, return zero.
    def fracOfNobles(self, player, state):
        total = 0
        for noble in state.nobles:
            nobleTotal = 0
            playerTotal = 0
            for i in range(len(player.cardsOwned)-1):
                if player.cardsOwned[i] >= noble[i]:
                    nobleTotal += noble[i]
                    playerTotal += noble[i]

                if player.cardsOwned[i] < noble[i]:
                    nobleTotal += noble[i]
                    playerTotal += player.cardsOwned[i]

            playerPercent = (playerTotal/nobleTotal)
            total += playerPercent

        return (total/3)

    #Modified allEval2 that gives scaling points for how close a player is to a
    #noble
    def modifiedEval(self, numTurns, node):
        utilVec = [0]*(len(node.players))
        counter = 0
        for player in node.players:
            #winlose = 100*player.wonloss    #this should be a player held variable,
                                        #1 if the player won, -1 if they lost,
                                        #0 otherwise
            score = 1.5*player.points
            nobles = self.fracOfNobles(player, node)
            prestige = sum(player.cardsOwned)
            gems = sum(player.gemsOwned)
            val = score + prestige + gems + nobles #+ winlose
            expDecay = .9**numTurns
            utilVec[counter] = val*expDecay
            counter += 1
        return utilVec
    
    #The heuristic from the thesis.
    #This heuristic also uses a function of .9^NumTurns in the future this is from.
    #The exponential decay is to help evaluate the uncertainty of the board state in
    # the future.
    #Commenting out the noble section until nobles are implemented
    def allEval2(self, numTurns, node):
        utilVec = [0]*(len(node.players))
        counter = 0
        for player in node.players:
            #winlose = 100*player.wonloss    #this should be a player held variable,
                                        #1 if the player won, -1 if they lost,
                                        #0 otherwise
            score = 1.5*player.points
            #nobles = 2.5*player.noble       #should be 1 if has noble, 0 otherwise
            prestige = sum(player.cardsOwned)
            gems = sum(player.gemsOwned)
            val = score + prestige + gems #+ nobles + winlose
            expDecay = .9**numTurns
            utilVec[counter] = val*expDecay
            counter += 1
        return utilVec
    
    #creates a copy of the state and advances it to the next turn
    def copyMe(self):
        if self.strippedCopy == None:
            self.strippedCopy = copy.deepcopy(self)
            self.strippedCopy.childrenL = []
        out = copy.deepcopy(self.strippedCopy)
        out.strippedCopy = None
        out.playerTurn += 1
        if (out.playerTurn == len(out.players)):
            out.playerTurn=0
            out.turn += 1
        return out

    #prints a representation of the current state
    def printState(self):
        print("\n--- Turn", self.turn, "---")
        state = "Gems Available:"
        for i in range(len(self.gemsAvailable)):
            state += " " + str(self.gemsAvailable[i])+ colors[i]
        print(state)
        state = "Nobles Available:"
        count = 1
        for n in self.nobles:
            state += " [" + str(count) + "]:"
            count += 1
            for i in range(len(n)):
                if n[i] > 0:
                    state += " " + str(n[i])+ colors[i]
        print(state)
        count = 1
        print("Cards: ")
        for i in range(len(self.cards)):
            state = ""
            for j in range(len(self.cards[i])):
                for k in range(len(self.cards[i][j])):
                    if k == 0:
                        state += "{" + colors[self.cards[i][j][k]]
                    elif k == 1:
                        state += str(self.cards[i][j][k]) + "}:"
                    elif self.cards[i][j][k] > 0:
                        state += " " + str(self.cards[i][j][k])+ colors[k-2]
                state += " [" + str(count) + "]\n"
                count += 1
            print(state)
        for i in range(len(self.players)):
            self.players[i].printState()
    pass

class Player:
    def __init__(self, playerFunction):
        self.playerFunction = playerFunction
        self.gemsOwned = [0,0,0,0,0,0]
        self.reserve = []
        self.points = 0
        self.cardsOwned = [0,0,0,0,0,0]
        self.id = 0

    def printState(self):
        print("\n--- Player", self.id+1, "---", self.points, "points")
        state = "Gems Owned:"
        for i in range(len(self.gemsOwned)):
            state += " " + str(self.gemsOwned[i]) + "(+" +str(self.cardsOwned[i]) + ")" + colors[i]
        print(state)
        count = 1
        print("Cards in Reserve: ", len(self.reserve))
        for i in range(len(self.reserve)):
            state = ""
            for k in range(len(self.reserve[i])):
                if k == 0:
                    state += "{" + colors[self.reserve[i][k]]
                elif k == 1:
                    state += str(self.reserve[i][k]) + "}:"
                elif self.reserve[i][k] > 0:
                    state += " " + str(self.reserve[i][k])+ colors[k-2]
            print(state)
    pass

class PlayerFunctions:
    def human(boardState):
        valid = 0
        while(not valid):
            command = input("Please enter a command: ")
            if (command == "help"):
                for s in boardState.children():
                    print(s.name, " ")
            else:
                for s in boardState.children():
                    if (s.name == command):
                        return s
        
    def ai_random(boardState):
        if len(boardState.children()):
            out = random.choice(boardState.children())
            if (verbose): print(out.name)
            return out
        else:
            print("Error: no legal moves")
            return cs
     
    def md(boardState):
        depth = 1
        ai = MaxDec(boardState, depth, boardState.players, boardState.playerTurn, boardState.allEval2)
        out = ai.maxdec()
        if (verbose): print(out.name)
        return out

    def allR(boardState):
        depth = 0
        samples = 10
        playerList = boardState.players
        startingPlayer = boardState.playerTurn
        ai = AllRandom(boardState, playerList, startingPlayer, depth, samples, boardState.modifiedEval)
        out = ai.outer_ran()
        if (verbose): print(out.name)
        return out

numPlayers = 0

#while numPlayers < 2 or numPlayers > 4:
#    numPlayers = int(input("How many players? (2-4)"))
#    if (numPlayers < 2 or numPlayers > 4):
#        print("invalid player count:", numPlayers)
winners = [0,0]

for i in range(10):
    
    tier1Deck = copy.deepcopy(fresh_tier1Deck)
    tier2Deck = copy.deepcopy(fresh_tier2Deck)
    tier3Deck = copy.deepcopy(fresh_tier3Deck)
    nobles = copy.deepcopy(fresh_nobles)

    cs = GameState()

    print ("Tier 1 deck initialized with", len(tier1Deck), "cards")
    print ("Tier 2 deck initialized with", len(tier2Deck), "cards")
    print ("Tier 3 deck initialized with", len(tier3Deck), "cards")
    print ("Noble deck initialized with", len(nobles), "tiles")

    cs.players.append(Player(PlayerFunctions.md))
    cs.players.append(Player(PlayerFunctions.ai_random))
    cs.players.append(Player(PlayerFunctions.ai_random))
    cs.players.append(Player(PlayerFunctions.ai_random))

    for i in range(len(cs.players)):
        cs.players[i].id = i

    cs.setupNewGame([tier1Deck, tier2Deck, tier3Deck], nobles)

    while cs != None:
        cs = cs.gameStep()

    winners[Rwinner] += 1

print("Minimax win rate:", winners[0]/sum(winners))
