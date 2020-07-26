def merge_the_tools(string, k):
    list1 = []
    list2 = []
    list3 = []
    a = set()
    n = len(string)
    s = n/k
    for i in range(0,n,k):
        list1.append(string[i:i+k])  
    for i in range(len(list1)):
        for j in list1[i]:
            if j not in a:
                a.add(j)
                list2.append(j)  
        b = "".join(list2)    
        list3.append(b)
        list2.clear()
        a.clear()
    for i in range(len(list3)):        
        print(list3[i])        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
