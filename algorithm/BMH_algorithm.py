# https://www.youtube.com/watch?v=kvWFAZwZ_8U&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=2
# Алгоритмы Бойерв-Мура-Хорспула
# Оптимизирует алгоритмы поиска образа в строке
"""
- Худший вариант: О(n-символов строки * m-символов-образа)
- Лучший вариант: О(n-символов строки / m-символов-образа)
- Среднее: О(m-символов-образа / |алфавит, над которым производится сравнение(уникальные символы в строке и образе)|
Этапы:
    - формирование таблицы смещения образа.
    - поиск образа в строке.
"""

# образ
t = "данные"

# 1 Этап - формирование таблицы смещений:

S = set()  # Множество уникальных значений
M = len(t)  # Длина образа
d = dict()  # Словарт: уникальный символ образа и его 'вес'

for item in range(M-2, -1, -1):  # Начинаем иттерацию с предпоследнего символа
    if t[item] not in S:  # Если символа еще нет в таблице:
        d[t[item]] = M - item - 1
        S.add(t[item])

if t[M-1] not in S:  # Формируем вес последнего символа:
    d[t[M-1]] = M
d["*"] = M  # Формируем смещение для прочих символов:

print(d)

# 2 этап - поиск образа в строке

a = "большие метeоданные"  # строка поиска
N = len(a)

if N >= M:  # Если длина искомой строки больше либо равна длине образа
    i = M - 1  # То счетчик проверяемого символа в строке поиска устанавливаем на предпоследний элемент (-1 т.к. индекс)

    while i < N:  # пока счетчик проверяемого символа не стал равен индексу последнего символа в поисковой строке
        k = 0  # индекс символа в поисковой строке, с которым производим сравнение символов из образа
        for j in range(M - 1, -1, -1):  # Иттерируемся по образу начиная с конца (с индекса последнего символа):
            if a[i - k] != t[j]:  # Если текущий элемент в поисковой строке не равен символу из образа
                # Если у нас не совпал последний символ поисковой строки
                # (первый символ при иттерации, т.к. начинаем с конца)
                if j == M - 1:
                    # off - определяет шаг смещения поискового курсора
                    # если в нашем словаре 'd' имеется данный список, то смешаем курсор на этот символ, тем самым
                    # делая его текущим. Если такого символа в словаре нет - смещаемся на длину, равной образу '["*"]'
                    off = d[a[i]] if d.get(a[i], False) else d["*"]
                else:
                    # Если не равен любой другой элемент (а не последний), то из словаря 'd' берем вес смещения символа
                    # из шаблона, с который не равен символу из поисковой строки, и производим смещение на этот шаг(вес)
                    off = d[t[j]]
                i += off  # Производим смещение курсора на определенной шаг, т.к. шаблон не равен участку строки
                break  # Прекращаем дальнейшее сравнивание строки с шаблоном

            # Если символ из поисковой строки равен символу из шаблона, то проверяем следующий символ:
            k += 1

        # Если курсор равен нулю, т.е. мы дошли до послежнего символа в образе, т.е. образ совпал с
        # проверяемым участком поисковой строки:
        if j == 0:
            print(f"Образ найден по индексу {i - k + 1}")
            break
else:
    print("Образ не найден")
