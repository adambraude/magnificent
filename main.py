import random
print ("Hello, and welcome to Splandor!")

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
    nobles = []
    cards = [[],[],[]]
    # white, blue, green, red, black, yellow
    gemsAvailable = [7, 7, 7, 7, 7, 5]
    players = []
    turn = 1

    def setupNewGame(self, decks, ndeck):
        l = len(self.players)+1
        for i in range(l):
            noble = random.choice(ndeck)
            self.nobles.append(noble)
            ndeck.remove(noble)
        for j in range(len(decks)):
            for i in range(4):
                card = random.choice(decks[j])
                self.cards[j].append(card)
                decks[j].remove(card)

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
            for j in range(4):
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
    pass

currentState = GameState()


print ("Tier 1 deck initialized with", len(tier1Deck), "cards")
print ("Tier 2 deck initialized with", len(tier2Deck), "cards")
print ("Tier 3 deck initialized with", len(tier3Deck), "cards")
print ("Noble deck initialized with", len(nobles), "tiles")

numPlayers = 0

while numPlayers < 2 or numPlayers > 5:
    numPlayers = int(input("How many players? (2-5)"))
    if (numPlayers < 2 or numPlayers > 5):
        print("invalid player count:", numPlayers)

class Player:
    gemsOwned = [0,0,0,0,0,0]
    reserve = []
    pass

for i in range(numPlayers):
    currentState.players.append(Player())

currentState.setupNewGame([tier1Deck, tier2Deck, tier3Deck], nobles)
currentState.printState()
