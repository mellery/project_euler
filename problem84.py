'''

In the game, Monopoly, the standard board is set up in the following way:
0084_monopoly_board.png

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL
    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
'''

import random
from collections import Counter

NUM_SQUARES = 40
NUM_TURNS = 10**8  # Increase for better accuracy

# Define board positions for CC, CH, R, U, G2J, JAIL, etc.
CC = [2, 17, 33]
CH = [7, 22, 36]
R = [5, 15, 25, 35]
U = [12, 28]
G2J = 30
JAIL = 10

# Define CC and CH cards as lists of moves (see problem description)
CC_CARDS = [0, JAIL] + [None]*14
CH_CARDS = [0, JAIL, 11, 24, 39, 5, 'R', 'R', 'U', -3] + [None]*6


def roll_dice():
    return random.randint(1, 4), random.randint(1, 4)


def simulate():
    visits = Counter()
    pos = 0
    cc_index = 0
    ch_index = 0
    doubles_count = 0

    cc_deck = CC_CARDS[:]
    ch_deck = CH_CARDS[:]
    random.shuffle(cc_deck)
    random.shuffle(ch_deck)

    for _ in range(NUM_TURNS):
        d1, d2 = roll_dice()
        if d1 == d2:
            doubles_count += 1
        else:
            doubles_count = 0

        if doubles_count == 3:
            pos = JAIL
            doubles_count = 0
            visits[pos] += 1
            continue

        pos = (pos + d1 + d2) % NUM_SQUARES

        # G2J
        if pos == G2J:
            pos = JAIL
        # Community Chest
        elif pos in CC:
            card = cc_deck[cc_index]
            cc_index = (cc_index + 1) % len(cc_deck)
            if card is not None:
                pos = card
        # Chance
        elif pos in CH:
            card = ch_deck[ch_index]
            ch_index = (ch_index + 1) % len(ch_deck)
            if card is not None:
                if card == 'R':
                    # Go to next R
                    pos = next(r for r in R if r > pos) if any(r > pos for r in R) else R[0]
                elif card == 'U':
                    # Go to next U
                    pos = next(u for u in U if u > pos) if any(u > pos for u in U) else U[0]
                elif card == -3:
                    pos = (pos - 3) % NUM_SQUARES
                else:
                    pos = card

        visits[pos] += 1

    # Find top 3 squares
    top3 = [x[0] for x in visits.most_common(3)]
    return ''.join(f"{x:02d}" for x in top3)


if __name__ == "__main__":
    print(simulate())