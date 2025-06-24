def get_pairs(vals):
    pairs = []
    for v in vals:
        if vals.count(v) == 2:
            if v not in pairs:
                pairs.append(v)
    return pairs


def score_hand(hand):
    vals = []
    suits = []
    for c in hand:
        if c[0] == 'T':
            v = 10
        elif c[0] == 'J':
            v = 11
        elif c[0] == 'Q':
            v = 12
        elif c[0] == 'K':
            v = 13
        elif c[0] == 'A':
            v = 14
        else:
            v = int(c[0])
            
        vals.append(v)
        suits.append(c[1])

    vals.sort()
    suits.sort()
    #print(vals,suits)

    pairs = get_pairs(vals)

    is_four_of_a_kind = False
    is_flush = False
    is_stright = False
    is_three_of_a_kind = False
    is_pair = False

    x = max(set(vals), key = vals.count)
    #print(vals.count(x))

    valdiff = [vals[n]-vals[n-1] for n in range(1,len(vals))]
    if sum(valdiff) == 4 and max(valdiff) == 1:
        #print(valdiff)
        is_stright = True

    if vals.count(x) == 4:
        is_four_of_a_kind = True
    if vals.count(x) == 3:
        is_three_of_a_kind = True
    if vals.count(x) == 2:
        is_pair = 2

    s = max(set(suits), key = suits.count)

    if suits.count(s) == 5:
        is_flush = True

    #royal flush
    if is_stright and is_flush and max(vals) == 14:
        #return "royal_flush"
        return 1000000000000000000
    
    #straight flush
    if is_stright and is_flush:
        #return "stright_flush"
        return 10000000000000000
    
    #four of a kind
    if is_four_of_a_kind:
        #return "four_of_a_kind"
        return 100000000000000
    
    #full house
    if is_three_of_a_kind and len(pairs) > 0:
        #return "full_house"
        return 1000000000000
    
    #flush
    if is_flush:
        #return "flush"
        return max(vals) * 10000000000
    
    #straight
    if is_stright:
        #return "stright"
        return max(vals) * 100000000

    #three of a kind
    if is_three_of_a_kind:
        #return "three_of_a_kind "+str(x)
        return x * 1000000
    
    #two pairs
    if len(pairs) > 1:
        #return "two_pair"
        return max(pairs) * 10000
    
    #one pair
    if is_pair:
        #return "pair "+str(x)
        return x * 100
    
    #high card
    return max(vals)
    #return "high "+str(max(vals))

def problem54(input):
    ans = 0

    file1 = open(input, 'r')
    lines = file1.readlines()

    for l in lines:
        temp = l.strip()
        cards = temp.split(" ")
        p1 = cards[0:5]
        p2 = cards[5:10]
        
        p1score = score_hand(p1)
        p2score = score_hand(p2)
        if p1score == p2score:
            print("ERROR")
            print(p1,p2)
            print(p1score,p2score)
        if p1score > p2score:
            ans = ans + 1

    return ans

print(problem54('./input/p054_poker.txt'))