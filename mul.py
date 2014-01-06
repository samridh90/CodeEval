from itertools import product, groupby
 
for k, g in groupby(product(range(1, 13), repeat=2), lambda x: x[0]):
    print ''.join([str(i * j).rjust(4) for i, j in g]).strip()