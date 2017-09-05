if __name__ == '__main__':
    students = []
    grades = []
    inst = []
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append(score)
        inst = [name, score]
        students.append(inst)
    sort = sorted(set(grades))
    secondlowest = sort[1]
    for i in students:
        if secondlowest in i:
            result.append(i[0])
    result = sorted(result)
    for i in result:
        print(i)
