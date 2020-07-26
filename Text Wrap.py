import textwrap
def wrap(string, max_width):
    t1 = textwrap.TextWrapper(width = max_width)
    t2 = t1.wrap(text = string)
    print(*t2,sep="\n")
    return " "

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
