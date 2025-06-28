"""
Project Euler Problem 82: Path sum: three ways

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column 
and finishing in any cell in the right column, and only moving up, down, and right, 
is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum from the left column to the right column in matrix.txt, 
a 31K text file containing an 80 by 80 matrix.

Algorithm: For each column, we need to find the minimum path sum to reach each cell.
We can move right from the previous column, or up/down within the current column.
We process each column by iteratively updating distances until convergence.
"""

from euler_common import load_matrix

def min_path_sum(matrix):
    """
    Find the minimum path sum from any cell in the left column to any cell in the right column.
    Movements allowed: up, down, right.
    
    Uses dynamic programming, processing column by column.
    """
    if not matrix or not matrix[0]:
        return 0
        
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize distances to first column
    dist = [matrix[i][0] for i in range(rows)]
    
    # Process each subsequent column
    for col in range(1, cols):
        new_dist = [float('inf')] * rows
        
        # Initialize with distances coming from the left
        for row in range(rows):
            new_dist[row] = dist[row] + matrix[row][col]
        
        # Iteratively improve by considering up/down movements within this column
        # Continue until no improvements are made
        changed = True
        while changed:
            changed = False
            # Update distances by moving down
            for row in range(rows - 1):
                new_cost = new_dist[row] + matrix[row + 1][col]
                if new_cost < new_dist[row + 1]:
                    new_dist[row + 1] = new_cost
                    changed = True
            
            # Update distances by moving up
            for row in range(rows - 1, 0, -1):
                new_cost = new_dist[row] + matrix[row - 1][col]
                if new_cost < new_dist[row - 1]:
                    new_dist[row - 1] = new_cost
                    changed = True
        
        dist = new_dist
    
    return min(dist)        

if __name__ == "__main__":
    matrix = load_matrix('input/0082_matrix.txt')
    result = min_path_sum(matrix)
    print(result)
