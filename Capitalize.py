def solve(s):
    s1 = s.split(' ')
    for i in range(len(s1)):
        s1[i] = s1[i].capitalize()
    result = ' '.join(s1) 
    return result  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
