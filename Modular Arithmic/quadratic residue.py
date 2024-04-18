p = 29
ints = [14, 6, 11]
squareRoot = 100000 # max
quadRes = 0
for n in ints:
    for a in range(1,p):
       #or pow(a,2,p)
        if pow(a, 2)%p == n:
            squareRoot = min(squareRoot,a)
            quadRes = n
            
print(f'Quadratic Residue is {quadRes} and minimum square root of it is {squareRoot} ' )
