#In the by matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to

#.
#Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an by matrix.

import numpy as np
def load_matrix(filename):
    with open(filename, 'r') as f:
        matrix = [list(map(int, line.strip().split(','))) for line in f]
    return np.array(matrix)

def min_path_sum(matrix):
    rows, cols = matrix.shape
    dp = np.zeros((rows, cols), dtype=int)
    
    dp[0, 0] = matrix[0, 0]
    
    for i in range(1, rows):
        dp[i, 0] = dp[i-1, 0] + matrix[i, 0]
    
    for j in range(1, cols):
        dp[0, j] = dp[0, j-1] + matrix[0, j]
    
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i, j] = min(dp[i-1, j], dp[i, j-1]) + matrix[i, j]
    
    return dp[-1, -1]       


if __name__ == "__main__":
    matrix = load_matrix('input/0081_matrix.txt')
    result = min_path_sum(matrix)
    print(result)