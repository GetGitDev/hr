n,m = (map(int,input().split()))
array = list(map(int,input().split()))
seta = set(map(int,input().split()))
setb = set(map(int,input().split()))
happy = 0
for i in array:
    if (i in seta):
        happy += 1
    elif (i in setb):
        happy -= 1
print (happy)
