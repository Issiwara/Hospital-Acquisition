from itertools import permutations
from itertools import combinations


def dist(a,b):
    return abs(a[1]-b[1])**2 + abs(a[0]-b[0])**2

[n,m,k] = list(map(int,str(input()).split(" ")))
vol = []
med = []
for x in range(n):
    vol.append(list(map(int,str(input()).split(" "))))
for y in range(m):
    med.append(list(map(int,str(input()).split(" "))))

out = []
for c in vol:
    info = []
    for d in med:
        info.append(dist(c,d))
    info.sort()
    out.append(info)
out.sort()

output = [[row[z] for row, z in zip(out, permutation)]
          for permutation in permutations(range(len(out)))]

arr = []
for i in output:
    arr.extend([*combinations(i, k)])
 

print(min(list(map(max,arr))))


