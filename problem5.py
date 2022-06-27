#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def problem5(limit):
    
    value = limit
    while(1):
        valid = True
        for i in range(1,limit+1):
            if value%i != 0:
                valid = False
        if valid:
            return value
        else:
            value = value + limit

#print(problem5(10))
print(problem5(20))