def find_cubic_permutations():
    """Find the smallest cube for which exactly 5 permutations of its digits are also cubes"""
    
    # Group cubes by their digit signature (sorted digits)
    digit_groups = {}
    
    n = 1
    while True:
        cube = n ** 3
        
        # Create digit signature by sorting the digits
        signature = ''.join(sorted(str(cube)))
        
        # Add to the appropriate group
        if signature not in digit_groups:
            digit_groups[signature] = []
        digit_groups[signature].append((n, cube))
        
        # Check if we found a group with exactly 5 cubes
        if len(digit_groups[signature]) == 5:
            # Return the smallest cube in this group
            return min(digit_groups[signature], key=lambda x: x[1])[1]
        
        n += 1
        
        # Safety limit to prevent infinite loop
        if n > 100000:
            break
    
    return None

result = find_cubic_permutations()
print(result)