from itertools import product
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
a = list(product(A,B))
for i in a:
    print(i,end=" ")
