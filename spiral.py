
def adds(n):
    sums = 0
    for i in range(4):
        sums += (n**2 - (i*(n-1)))

    return sums


ans = 1

for i in range(3,1002,2):
    ans += adds(i)

print ans

'''
Each row in a nxn spiral requires n**2 numbers, and the corners are n**2 - (n-1)
so i just find those four number for each row and add them up, remembering to
start with one
'''
        
