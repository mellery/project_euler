"""
Project Euler Problem 81: Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum from the top left to the bottom right by only moving right and down 
in matrix.txt, a 31K text file containing an 80 by 80 matrix.

This is a classic dynamic programming problem. We build up the solution by calculating
the minimum path sum to reach each cell, using only the optimal paths from the cell above
or to the left.
"""

from euler_common import load_matrix

def min_path_sum(matrix):
    """
    Find the minimum path sum from top-left to bottom-right.
    Only right and down movements are allowed.
    
    Uses dynamic programming with O(1) space optimization.
    """
    if not matrix or not matrix[0]:
        return 0
        
    rows, cols = len(matrix), len(matrix[0])
    
    # Use the first row as our DP array, then update in place
    dp = matrix[0][:]
    
    # Initialize first row (can only come from left)
    for j in range(1, cols):
        dp[j] += dp[j-1]
    
    # Process remaining rows
    for i in range(1, rows):
        # First column can only come from above
        dp[0] += matrix[i][0]
        
        # Other columns can come from above or left
        for j in range(1, cols):
            dp[j] = min(dp[j], dp[j-1]) + matrix[i][j]
    
    return dp[cols-1]       


if __name__ == "__main__":
    matrix = load_matrix('input/0081_matrix.txt')
    result = min_path_sum(matrix)
    print(result)