from euler_common import get_digit

def problem17(limit):
    ans = 0
    d = {}
    d[0] = ""
    d[1] = "one"
    d[2] = "two"
    d[3] = "three"
    d[4] = "four"
    d[5] = "five"
    d[6] = "six"
    d[7] = "seven"
    d[8] = "eight"
    d[9] = "nine"
    d[10] = "ten"
    d[11] = "eleven"
    d[12] = "twelve"
    d[13] = "thirteen"
    d[14] = "fourteen"
    d[15] = "fifteen"
    d[16] = "sixteen"
    d[17] = "seventeen"
    d[18] = "eighteen"
    d[19] = "nineteen"
    d[20] = "twenty"
    d[30] = "thirty"
    d[40] = "forty"
    d[50] = "fifty"
    d[60] = "sixty"
    d[70] = "seventy"
    d[80] = "eighty"
    d[90] = "ninety"
    d[100] = "hundred"
    i = 1
    while (i < limit + 1):
    
        if i <= 20:
            word = d[i]
        elif i < 100:
            word = d[i//10*10]+d[i%10]
        elif i == 100:
            word = d[i//100*1]+"hundred"
        elif i < 1000:
            i2 = i%100
            #print(i2)
            if i2 <= 20:
                word2 = d[i2]
            else:
                word2 = d[i2//10*10]+d[i2%10]
            word = d[get_digit(i,2)]+"hundred"
            if i2 != 0:
                word = word +"and"+word2
        elif i == 1000:
            word = "onethousand"

        print(i, word, len(word))
        ans = ans + len(word)

        i = i + 1
    return ans

#print(problem17(100))
#print(problem17(120))
#print(problem17(342))
#print(problem17(115))

print(problem17(1000))