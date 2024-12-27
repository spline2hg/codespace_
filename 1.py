n = int(input())
k = int(input())
result = [0]

for _ in range(n-1):
    temp = []
    for char in result:
        if char == 0:
            temp.extend([0, 1])
        elif char == 1:
            temp.extend([1, 0])
    result = temp
    print(result)

print(result[k-1])