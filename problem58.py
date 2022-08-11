from euler_common import is_prime
def problem58(size):
    edge = 1
    corners = 0
    diagonals = [1]
    i = 3
    edge = 2
    while (i <= size*size):
        #print("corner at ",i,"edge len is ",edge)
        diagonals.append(i)
        corners = corners + 1
        if corners == 4:
            edge = edge + 2
            corners = 0
        i = i + edge
        
    #diagonals.append(size*size)
    #print(i,edge)
    #print(diagonals)
    numprimes = 0
    for d in diagonals:
        if is_prime(d):
            numprimes = numprimes + 1
    return(numprimes/len(diagonals))
 
i = 1
ans = 1
while (ans > 0.1):
    i = i + 2
    ans = problem58(i)
    print(i,ans)
