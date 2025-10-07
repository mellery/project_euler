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

"""Deterministic Markov chain solver for Project Euler 84 with 4-sided dice.

We build a Markov chain on states (position, consecutive_doubles_count)
and compute the stationary distribution by iterating the probability vector.
Community Chest and Chance cards are modeled as random draws (uniform over
the 16 cards) as is standard for this problem.
"""

from math import isclose


NUM_SQUARES = 40
CC = [2, 17, 33]
CH = [7, 22, 36]
R = [5, 15, 25, 35]
U = [12, 28]
G2J = 30
JAIL = 10


def next_r(pos):
    for r in R:
        if r > pos:
            return r
    return R[0]


def next_u(pos):
    for u in U:
        if u > pos:
            return u
    return U[0]


def process_cc(pos):
    # returns dict of resulting positions -> probability
    # CC has 16 cards: 1->GO, 1->JAIL, 14->no move
    return {0: 1/16, JAIL: 1/16, pos: 14/16}


def process_ch(pos):
    # CH has 16 cards with the movement cards as described
    res = {}
    def add(p, prob):
        res[p] = res.get(p, 0) + prob

    # movement cards (10 of 16)
    add(0, 1/16)      # GO
    add(JAIL, 1/16)   # JAIL
    add(11, 1/16)     # C1
    add(24, 1/16)     # E3
    add(39, 1/16)     # H2
    add(5, 1/16)      # R1
    add(next_r(pos), 2/16)  # next R (two cards)
    add(next_u(pos), 1/16)  # next U
    # Go back 3 squares
    back = (pos - 3) % NUM_SQUARES
    # if back lands on CC, process CC
    if back in CC:
        cc_map = process_cc(back)
        for k, v in cc_map.items():
            add(k, v * 1/16)
    else:
        add(back, 1/16)
    # remaining 6 cards: no move
    add(pos, 6/16)
    return res


def build_transition():
    # states indexed by s = pos*3 + dc (dc in 0,1,2)
    N = NUM_SQUARES * 3
    P = [[0.0] * N for _ in range(N)]

    # iterate states
    for pos in range(NUM_SQUARES):
        for dc in range(3):
            s = pos * 3 + dc
            # iterate over dice outcomes (1..4, 1..4)
            for d1 in range(1, 5):
                for d2 in range(1, 5):
                    prob = 1/16
                    if d1 == d2:
                        ndc = dc + 1
                    else:
                        ndc = 0

                    if ndc == 3:
                        # go to jail, reset doubles
                        ns = JAIL * 3 + 0
                        P[s][ns] += prob
                        continue

                    newpos = (pos + d1 + d2) % NUM_SQUARES
                    # process square effects
                    mapping = {newpos: 1.0}
                    if newpos == G2J:
                        mapping = {JAIL: 1.0}
                    elif newpos in CC:
                        mapping = process_cc(newpos)
                    elif newpos in CH:
                        mapping = process_ch(newpos)

                    # for each possible resulting square, add transition
                    for final_pos, p2 in mapping.items():
                        ns = final_pos * 3 + ndc
                        P[s][ns] += prob * p2

    return P


def multiply(vec, P):
    N = len(vec)
    res = [0.0] * N
    for i in range(N):
        vi = vec[i]
        if vi == 0.0:
            continue
        row = P[i]
        for j in range(N):
            res[j] += vi * row[j]
    return res


def solve_markov(eps=1e-14, max_iter=10000):
    P = build_transition()
    N = len(P)
    # start at GO with 0 doubles
    vec = [0.0] * N
    vec[0 * 3 + 0] = 1.0

    for _ in range(max_iter):
        vec2 = multiply(vec, P)
        diff = sum(abs(a - b) for a, b in zip(vec2, vec))
        vec = vec2
        if diff < eps:
            break

    # marginalize over doubles count
    pos_prob = [0.0] * NUM_SQUARES
    for pos in range(NUM_SQUARES):
        for dc in range(3):
            pos_prob[pos] += vec[pos * 3 + dc]

    # get top 3 squares
    top3 = sorted(range(NUM_SQUARES), key=lambda x: -pos_prob[x])[:3]
    return ''.join(f"{x:02d}" for x in top3)


if __name__ == '__main__':
    print(solve_markov())