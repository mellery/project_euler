from multiprocessing.connection import answer_challenge


def problem1(input):
    ans = 0
    for i in range(1,input):
        #print(i)
        if (i%3 == 0) or (i%5 == 0):
            #print(i)
            ans = ans + i
    return ans

#print(problem1(10)) #23
print(problem1(1000))