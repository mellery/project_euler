def problem22(input):
    ans = 0

    file1 = open(input, 'r')
    lines = file1.readlines()

    n = 1
    for l in lines:
        names = l.strip().split(",")
        names.sort()
        for name in names:
            letters = list(name)
            temp = 0
            for l in letters:
                if l != '"':
                    temp = temp + ord(l) - ord('A') + 1
            score = temp*n

            ans = ans + score
            n = n + 1
    
    return ans

    
    
print(problem22('input\p022_names.txt'))