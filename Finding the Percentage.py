if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    K1=student_marks.keys()
    K2=student_marks.values()
    n2=student_marks[query_name]
    a=(n2[0]+n2[1]+n2[2])/3
    print(format(a,'.2f'))
