n = int(raw_input())
arr = list(map(int, raw_input().split()))
list2=[]
for i in arr:
    if i not in list2:
        list2.append(i)
list2.sort(reverse=True)
print(list2[1])         
