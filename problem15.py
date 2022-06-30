#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20×20 grid?

def problem15(n):
    
    grid = {}
    for x in range(0,n+1):
        for y in range(0,n+1):
            grid[(x,y)] = 0

    for i in range(0,n+1):
        grid[(0,i)] = 1
        grid[(i,0)] = 1

    for x in range(1,n+1):
        for y in range(1,n+1):
            if grid[(x-1,y)] != 0 and grid[x,y-1] != 0:
                grid[(x,y)] = grid[(x-1,y)] + grid[(x,y-1)]
    
    return grid[(n,n)]

#print(problem15(3))
print(problem15(20))