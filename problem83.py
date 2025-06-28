"""
Project Euler Problem 83: Path sum: four ways

NOTE: This problem is a significant more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

Find the minimal path sum from the top left to the bottom right by moving left, right, 
up, and down in matrix.txt, a 31K text file containing an 80 by 80 matrix.

Algorithm: This is a shortest path problem. We use Dijkstra's algorithm to find the minimum
path from top-left (0,0) to bottom-right (n-1,n-1) with all four movement directions allowed.
"""

import heapq
from euler_common import load_matrix

def min_path_sum(matrix):
    """
    Find the minimum path sum from top-left to bottom-right.
    All four directions (up, down, left, right) are allowed.
    
    Uses Dijkstra's algorithm for shortest path.
    """
    if not matrix or not matrix[0]:
        return 0
        
    rows, cols = len(matrix), len(matrix[0])
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Distance matrix initialized to infinity
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = matrix[0][0]
    
    # Priority queue: (distance, row, col)
    pq = [(matrix[0][0], 0, 0)]
    visited = set()
    
    while pq:
        current_dist, row, col = heapq.heappop(pq)
        
        # If we've reached the target
        if row == rows - 1 and col == cols - 1:
            return current_dist
            
        # Skip if already visited
        if (row, col) in visited:
            continue
            
        visited.add((row, col))
        
        # Explore all four directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if (new_row, new_col) not in visited:
                    new_dist = current_dist + matrix[new_row][new_col]
                    
                    # Update if we found a better path
                    if new_dist < dist[new_row][new_col]:
                        dist[new_row][new_col] = new_dist
                        heapq.heappush(pq, (new_dist, new_row, new_col))
    
    return dist[rows - 1][cols - 1]

if __name__ == "__main__":
    matrix = load_matrix('input/0082_matrix.txt')  # Same matrix as problem 82
    result = min_path_sum(matrix)
    print(result)