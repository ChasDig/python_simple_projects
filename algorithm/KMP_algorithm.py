# https://www.youtube.com/watch?v=S2I0covkyMc&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=1&t=6s
# Алгоритм Кнута-Морриса-Пратта
# Алгоритм для поиска максимального суффикса
"""
Этапы:
    - формирование массива 'p': для сдвига по префиксам,
    - поиск образца в строке.
"""

t = "лилила"

p = [0]*len(t)
j = 0
i = 1


while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        j += 1
        i += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

a = "лилилось лилилась"
m = len(t)
n = len(a)

i = 0
j = 0

while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Образ найден")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1
if i == n and j != m:
    print("Образ не найден")

