a = int(input('Ведите число от 3 до 20: '))
result =[]
for i in range(1, a):
    if i == a:
        continue
    for j in range(i+1,a+1):
        if a % (i+j) == 0:
         result.append((i,j))
print(*result)

