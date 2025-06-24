from fractions import Fraction

curious_fractions = []
for a in range(10, 100):
    for b in range(a + 1, 100):  # Ensure a < b so fraction is < 1
        astr = str(a)
        bstr = str(b)
        
        # Check if we can "cancel" a common digit
        if astr[0] == bstr[1] and int(bstr[0]) != 0:
            # Cancel first digit of a with second digit of b
            if int(astr[1]) * b == int(bstr[0]) * a:
                curious_fractions.append(Fraction(a, b))
        
        if astr[1] == bstr[0] and int(bstr[1]) != 0:
            # Cancel second digit of a with first digit of b
            if int(astr[0]) * b == int(bstr[1]) * a:
                curious_fractions.append(Fraction(a, b))

# Calculate the product of all curious fractions
product = Fraction(1, 1)
for frac in curious_fractions:
    product *= frac

# The answer is the denominator of the reduced product
print(product.denominator)