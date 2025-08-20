# For a number written in Roman numerals to be considered valid there are basic rules which must be 
# followed. Even though the rules allow some numbers to be expressed in more than one way there is 
# always a "best" way of writing a particular number.

# For example, it would appear that there are at least six ways of writing the number sixteen:

# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI

# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered 
# to be the most efficient, as it uses the least number of numerals.

# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand 
# numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals 
# for the definitive rules for this problem.

# Find the number of characters saved by writing each of these in their minimal form.

# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive 
# identical units.

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in reversed(s):
        val = roman[c]
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total

def int_to_minimal_roman(n):
    vals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ''
    for v, sym in vals:
        while n >= v:
            res += sym
            n -= v
    return res

total_saved = 0
with open('input/0089_roman.txt', 'r') as f:
    for line in f:
        orig = line.strip()
        n = roman_to_int(orig)
        minimal = int_to_minimal_roman(n)
        total_saved += len(orig) - len(minimal)

print(total_saved)
