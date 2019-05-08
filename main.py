import random
import copy
print ("Hello, and welcome to Splandor!")

verbose = 1

colors = "W", "U", "G", "R", "B", "Y"

# color, points, white, blue, green, red, black
tier1Deck = [
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

tier2Deck = [
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

(2, 1, 3, 0, 2, 2, 1),
(2, 1, 2, 3, 0, 0, 2),
(2, 2, 4, 2, 0, 0, 2),
(2, 2, 0, 5, 3, 3, 0),
(2, 2, 0, 0, 5, 5, 0),
(2, 3, 0, 0, 6, 6, 0),

(3, 1, 2, 0, 0, 2, 1),
(3, 1, 0, 3, 0, 2, 1),
(3, 2, 1, 4, 2, 0, 2),
(3, 2, 3, 0, 0, 0, 3),
(3, 2, 0, 0, 0, 0, 0),
(3, 3, 0, 0, 0, 6, 0)
    ]

tier3Deck = [
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

nobles = [
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

    def gameStep(self):
        self.restockCards()
        if (verbose): self.printState()
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
                    print("The winner is Player", numPlayer+1, "with", highestScore, "points")
                else:
                    print("TIE")
                return
        
        if (verbose): print("Player", self.playerTurn+1, "turn:")
        self.players[self.playerTurn].playerFunction(self)

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
        self.printState()
        print("Player", self.playerTurn+1, "turn:")
        self.players[self.playerTurn].playerFunction(self)
        self.children()

    def restockCards(self):
        for j in range(len(self.cards)):
            while (len(self.cards[j]) < 4):
                card = random.choice(self.decks[j])
                self.cards[j].append(card)

    def take(self,gems):
        if sum(gems) > 3 or len(gems) > len(self.gemsAvailable)-1:
            print("illegal move")
            return
        for i in range(len(gems)):
            self.gemsAvailable[i] -= gems[i]
            self.players[self.playerTurn].gemsOwned[i] += gems[i]
        self.gameStep()

    def makeMove(self, move):
        cs = move
        cs.gameStep()

    def children(self):
        if (len(self.childrenL) > 0): return self.childrenL
        for i in range(len(self.gemsAvailable)-1):
            if self.gemsAvailable[i] >= 4:
                new = self.copyMe()
                new.gemsAvailable[i] -= 2
                new.players[self.playerTurn].gemsOwned[i] += 2
                new.name = "take 2" + colors[i]
                self.childrenL.append(new)
        for i in range(len(self.gemsAvailable)-3):
            for j in range(i+1, len(self.gemsAvailable)-2):
                for k in range(i+j+1, len(self.gemsAvailable)-1):
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
                        self.childrenL.append(new)
        for i in range(len(self.cards)):
            for j in range(len(self.cards[i])):
                card = self.cards[i][j]
                if (self.canAfford(card)):
                    new = self.copyMe()
                    self.buyCard(new, card)
                    new.cards[i].remove(card)
                    new.name = "buy " + str(i*4+j)
                    self.childrenL.append(new)
        r = self.players[self.playerTurn].reserve
        for i in range(len(r)):
            if (self.canAfford(r[i])):
                new = self.copyMe()
                self.buyCard(new, r[i])
                new.players[self.playerTurn].reserve.remove(r[i])
                new.name = "buy reserve" + str(i)
                self.childrenL.append(new)
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
                    self.childrenL.append(new)
            
        return self.childrenL

    def buyCard(self, state, card):
        wild = 0
        p = state.players[self.playerTurn]
        for k in range(len(state.gemsAvailable)-1):
            kcost = card[k+2] - p.cardsOwned[k]
            if kcost < 0: kcost = 0
            p.gemsOwned[k] -= kcost
            if p.gemsOwned[k] < 0:
                wild += p.gemsOwned[k]
                p.gemsOwned[k] = 0
        p.gemsOwned[len(state.gemsAvailable)-1] += wild
        p.cardsOwned[card[0]] += 1
        p.points += card[1]

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

    def copyMe(self):
        out = copy.deepcopy(self)
        out.childrenL = []
        out.playerTurn += 1
        if (out.playerTurn == len(out.players)):
            out.playerTurn=0
            out.turn += 1
        return out

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

cs = GameState()

print ("Tier 1 deck initialized with", len(tier1Deck), "cards")
print ("Tier 2 deck initialized with", len(tier2Deck), "cards")
print ("Tier 3 deck initialized with", len(tier3Deck), "cards")
print ("Noble deck initialized with", len(nobles), "tiles")

numPlayers = 0

while numPlayers < 2 or numPlayers > 4:
    numPlayers = int(input("How many players? (2-4)"))
    if (numPlayers < 2 or numPlayers > 4):
        print("invalid player count:", numPlayers)

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
        print("Cards in Reserve: ")
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
        print("Please enter a command")
    def ai_random(boardState):
        if len(boardState.children()):
            out = random.choice(boardState.children())
            if (verbose): print(out.name)
            cs.makeMove(out)
        else: print("Error: no legal moves")

for i in range(numPlayers):
    cs.players.append(Player(PlayerFunctions.ai_random))
    cs.players[i].id = i

cs.setupNewGame([tier1Deck, tier2Deck, tier3Deck], nobles)
