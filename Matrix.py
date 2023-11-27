L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]

count = 0

for r in range(3):
    for c in range(3):
        if (L[r][c]%2==0): #Перевірка на парність числа
            count+=1       #Якщо парне, додаємо до 'count'

print(count)

for r in range(3):
    for c in range(3):
        print(L[r][c], end=" ")
    print()


for r in range(3):
    for c in range(3):
        count+=1
print(count)