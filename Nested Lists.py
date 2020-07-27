n=int(input())
list1=[]
list3=[]
for i in range(n):
    name = raw_input()
    score = float(raw_input())
    list1.append([name,score])
list1.sort(key=lambda x:x[1])
mini= list1[0][1]
j=1
for i in range(1,n):
    if(list1[i][1]==mini):
        if(mini>list1[0][1]):
            list3.append(list1[i][0])
    elif(list1[i][1]>mini):
        mini=list1[i][1]
        if (j>1):
            break
        j=j+1
        list3.append(list1[i][0])                    
list3.sort()
l=len(list3)
for i in range(0,l):
    print(list3[i])  
