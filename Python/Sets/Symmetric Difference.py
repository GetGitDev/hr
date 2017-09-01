#!/usr/bin/python
def sym_dif(num1, num2):
    set3 = num1.difference(num2)
    set3.update(num2.difference(num1))
    return sorted(set3)


if __name__ == '__main__':
    len1 = input()
    string1 = set(map(int, input().split(" ")))
    len2 = input()
    string2 = set(map(int, input().split(" ")))
    output = sym_dif(string1, string2)
    for i in range(0, len(output)):
        print(output[i])
