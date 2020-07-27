from collections import Counter
X = int(input())
arr = list(map(int, input().split(" ")))
Values = Counter(arr).values()
Key = Counter(arr).keys()
Value_list = []
Key_list = []
amount = 0
for k in Values:
    Value_list.append(k)
for j in Key:
    Key_list.append(j)
N = int(input())
for i in range(N):
    arr2 = list(map(int, input().split(" ")))
    size = arr2[0]
    price = arr2[1]
    if size in Key_list:
        Key_index = Key_list.index(size)
        ValueAtIndex = Value_list[Key_index]

        if (ValueAtIndex>0):
            amount = amount+int(price)
            Value_list.pop(Key_index)
            ValueAtIndex = ValueAtIndex - 1
            Value_list.insert(Key_index,ValueAtIndex)
            
    
        else:
            amount = amount+0
    else:
        amount = amount + 0
print(amount)        
