def fac(i,comp):
    for k in range(1,i+1):
        comp *= k
    return 1/comp
exp = 1
comp = 1
n = 18
n_l = range(1,n+1)
for i in n_l:
    comp = 1
    exp += fac(i,comp)
print( "exp =" , exp )
