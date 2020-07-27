if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
t = tuple(integer_list)
t1 = hash(t)
print(t1)
