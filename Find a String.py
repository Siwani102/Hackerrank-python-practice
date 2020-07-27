def count_substring(string, sub_string):
    count = 0
    index = None
    for i in range(len(string)):
        if len(string)>len(sub_string):
            index = string.find(sub_string)
            if (index>=0):
                count+=1
                string = string[(index+1):]
    return count
