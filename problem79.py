"""
Project Euler Problem 79: Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file to determine the shortest possible secret passcode of unknown length.
"""

def solve_problem79():
    """
    Analyze the keylog to determine the shortest possible secret passcode.
    
    The keylog contains three-digit login attempts where each attempt represents
    three characters from the secret passcode in their correct relative order.
    
    Returns:
        str: The shortest possible secret passcode
    """
    
    # Read the keylog data
    keylog_data = read_keylog("input/0079_keylog.txt")
    
    # Build a directed graph of character dependencies
    # If we have "ABC" in keylog, then A->B->C (A comes before B, B comes before C)
    dependencies = {}
    all_chars = set()
    
    for entry in keylog_data:
        if len(entry) == 3:
            a, b, c = entry[0], entry[1], entry[2]
            all_chars.update([a, b, c])
            
            # Add dependencies: a before b, b before c
            if a not in dependencies:
                dependencies[a] = set()
            if b not in dependencies:
                dependencies[b] = set()
            if c not in dependencies:
                dependencies[c] = set()
                
            dependencies[a].add(b)
            dependencies[b].add(c)
    
    # Perform topological sort to find the correct order
    def topological_sort():
        # Calculate in-degrees
        in_degree = {char: 0 for char in all_chars}
        for char in dependencies:
            for dependent in dependencies[char]:
                in_degree[dependent] += 1
        
        # Start with characters that have no dependencies
        queue = [char for char in all_chars if in_degree[char] == 0]
        result = []
        
        while queue:
            # Sort to ensure consistent ordering when multiple choices exist
            queue.sort()
            char = queue.pop(0)
            result.append(char)
            
            # Remove this character and update in-degrees
            for dependent in dependencies.get(char, []):
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        return ''.join(result)
    
    return topological_sort()

def read_keylog(filename="input/0079_keylog.txt"):
    """
    Read the keylog data from file.
    
    Args:
        filename (str): Path to the keylog file
        
    Returns:
        list: List of three-digit login attempts
    """
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Main execution
if __name__ == "__main__":
    result = solve_problem79()
    print(result)