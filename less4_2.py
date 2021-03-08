# 1
n = int(input("Введите N: \n >>"))

a = []
for i in range(n + 1):
    a.append(i)

a[1] = 0

i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1

a = set(a)

print(a)

# 2

a = int(input("Введите число A: \n >>"))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое!")
else:
    print("Число не простое!!!")