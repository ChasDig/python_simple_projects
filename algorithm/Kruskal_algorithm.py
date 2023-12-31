# Алгоритм Краскала
# Алгоритм для поиска минимального остово взвешенного неорентированного графа
"""
Определение:
    - Остов: подграф исходного графа, который состоит из всех вершин этого графа, соединенного ребрами.
    Ребра не должны образовывать цикл.
Этапы:
    - Сортировка ребер во возрастанию веса ребра.
    - Рассматриваем и соединяем отдельные ребра и их вершины по возрастанию.
    - 1-ая иттерация: Соединять можно только изолированные вершины, или вершины, рпи соединении с которыми, не
    образовывается зацикленность.
    - 2-ая иттерация: Соединяем изолированные группы графов минимальным ребром.
"""

# список ребер графа (длина, вершина 1, вершина 2)
EDGE = [
    (13, 1, 2), (18, 1, 3), (17, 1, 4),
    (14, 1, 5), (22, 1, 6), (26, 2, 3),
    (22, 2, 5), (3, 3, 4), (19, 4, 6),
]


EDGE_SORTED = sorted(EDGE, key=lambda x: x[0])  # Отсортированный список графов по вершинам
CONNECTED_VERT = set()  # Список вершин, которые имеют соединение с другими вершинами
DICT_VERT = dict()  # Словарь с группами вершин. Содержит группы с определенными вершинами.
MIN_OST = list()  # Список ребер минимального остава

# 1-й этап работы алгоритма. Соединяем ребра из разных групп (если хотя бы одна вершина изолированна).
for edge in EDGE_SORTED:
    # Проверяем, чтобы начальная ИЛИ конечная вершина ребра не были соеденены (не находились в множестве CONNECTED_VERT)
    if edge[1] not in CONNECTED_VERT or edge[2] not in CONNECTED_VERT:
        # Проверяем, чтобы ОБЕ вершины были изолированны:
        if edge[1] not in CONNECTED_VERT and edge[2] not in CONNECTED_VERT:
            #  Добавляем в словарь с группами вершин данные изолированные вершин.
            #  Т.е. мы СВЯЗЫВАЕМ две вершины одним и тем же значением. Обозначая тем самым связь.
            DICT_VERT[edge[1]] = [edge[1], edge[2]]
            DICT_VERT[edge[2]] = DICT_VERT[edge[1]]
        else:
            #  Если вершины у нас не изолированны, проверяем какая из вершин у нас изолированна,
            #  и при необходимости добавляем ее в словарь с нашими вершинами.
            if not DICT_VERT.get(edge[1]):
                DICT_VERT[edge[2]].append(edge[1])
                DICT_VERT[edge[1]] = DICT_VERT[edge[2]]
            else:
                DICT_VERT[edge[1]].append(edge[2])
                DICT_VERT[edge[2]] = DICT_VERT[edge[1]]
        # Добавляем ребро в остов:
        MIN_OST.append(edge)
        #  Добавляем вершины в множество соединенных вершин.
        CONNECTED_VERT.add(edge[1])
        CONNECTED_VERT.add(edge[2])


#  2-й этап. Соединяем группы вершин ребром с минимальным весом.
for edge in EDGE_SORTED:
    if edge[1] in DICT_VERT[edge[1]] and edge[2] not in DICT_VERT[edge[1]]:
        MIN_OST.append(edge)
        gr_1 = DICT_VERT[edge[1]]
        DICT_VERT[edge[1]] += DICT_VERT[edge[2]]
        DICT_VERT[edge[2]] += gr_1

print(MIN_OST)
