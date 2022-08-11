def problem28(size):
    edge = 1
    corners = 0
    diagonals = [1]
    i = 3
    edge = 2
    while (i <= size*size):
        print("corner at ",i,"edge len is ",edge)
        diagonals.append(i)
        corners = corners + 1
        if corners == 4:
            edge = edge + 2
            corners = 0
        i = i + edge
        
    #diagonals.append(size*size)
    print(i,edge)
    print(diagonals)
    return(sum(diagonals))
 
#print(problem28(5))
print(problem28(1001))