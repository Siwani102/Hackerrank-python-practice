n,m = map(int, input().split(" "))
for i in range(n//2):
    print(('.|.'*(2*i+1)).center(m,'-'))
print("WELCOME".center(m,'-'))
for i in range(n//2):
    print(('.|.'*((n-2)-2*i)).center(m,'-'))
