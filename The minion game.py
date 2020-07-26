def minion_game(string):
    vowels = 'AEIOU'

    kev = 0
    stuart = 0

    for i in range(len(string)):
        if s[i] in vowels:
            kev = kev + (len(string)-i)
        else:
            stuart += len(string)-i
    if kev>stuart:
        print("Kevin",kev)
    elif stuart>kev:
        print("Stuart",stuart)
    else:
        print("Draw")                    

if __name__ == '__main__':
    s = input()
    minion_game(s)
