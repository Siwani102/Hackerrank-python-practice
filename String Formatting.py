def print_formatted(number):
    width = len(str(bin(n)[2:]))

    for i in range(1,n+1):
        a1 = str(bin(i))
        a2 = str(oct(i))
        a3 = str(hex(i))
        print((str(i)).rjust(width)
          ,a2[2:].rjust(width)
          ,(a3[2:].upper()).rjust(width)
          ,a1[2:].rjust(width));
