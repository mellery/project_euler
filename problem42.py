from numpy import tri


def triangle(n):
    return (0.5*n*(n+1))

def problem42(input):
    ans = 0

    file1 = open(input, 'r')
    lines = file1.readlines()

    triangles = []
    for i in range(0,200):
        triangles.append(triangle(i))

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
            score = temp
            if score in triangles:
                print(name,score)
                ans = ans + 1
            n = n + 1
    
    return ans

    
    
print(problem42('input\p042_words.txt'))