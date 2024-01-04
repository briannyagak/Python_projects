x = [
    [1,23,43],
    [33,4,6],
    [454,5,7]
]
result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[j][i]

for r in result:
    print(r)