def get_tri(limit):
    results = []
    i = 1
    while(1):
        n = i*(i+1)//2
        i = i + 1
        if n <= limit:
            results.append(n)
        else:
            return results
        
def get_square(limit):
    results = []
    i = 1
    while(1):
        n = i*i
        i = i + 1
        if n <= limit:
            results.append(n)
        else:
            return results

def get_pent(limit):
    results = []
    i = 1
    while(1):
        n = i*(3*i-1)//2
        i = i + 1
        if n <= limit:
            results.append(n)
        else:
            return results

def get_hex(limit):
    results = []
    i = 1
    while(1):
        n = i*(2*i-1)
        i = i + 1
        if n <= limit:
            results.append(n)
        else:
            return results

def get_hept(limit):
    results = []
    i = 1
    while(1):
        n = i*(5*i-3)//2
        i = i + 1
        if n <= limit:
            results.append(n)
        else:
            return results

def get_oct(limit):
    results = []
    i = 1
    while(1):
        n = i*(3*i-2)
        i = i + 1
        if n <= limit:
            results.append(n)
        else:
            return results

limit = 10000

print(len(get_tri(limit)))
print(len(get_square(limit)))
print(len(get_pent(limit)))
print(len(get_hex(limit)))
print(len(get_hept(limit)))
print(len(get_oct(limit)))