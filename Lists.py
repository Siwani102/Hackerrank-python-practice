list1=[]
N = int(input())
for i in range(N):
    arr = list(map(str, input().split(" ")))
    e=0
    if arr[0]=="insert":
        e = int(arr[2])
        i = int(arr[1])
        list1.insert(i,e)
    elif arr[0]=="print":
        print(list1)
    elif arr[0]=="remove":
        e = int(arr[1])
        list1.remove(e)
    elif arr[0]=="sort":
        list1.sort()
