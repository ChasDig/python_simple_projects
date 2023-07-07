"""
Алгоритм Флойда

Описание:
        - поиск кратчайшего пути во взвешенном графе.
        - общее с алгоритмом Дейкстры - поиск кратчайшего маршрута.
        - в ОТЛИЧИИ от алгоритма Дейкстры:
            -- умеет работать с ОТРИЦАТЕЛЬНЫМИ ВЕСАМИ ДУГ;
            -- находит кратчайшиме маршруты между всеми вершинами графа;
        - построен на принципах динамического програмирования.
"""
import math


def get_path(number_vector, start, end):
    path = [start]
    while start != end:  # Проходим по всем вершинам графа с минимальным весом от старта до конца:
        start = number_vector[start][end]
        path.append(start)
    return path


VECTOR = [
    [0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
    [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
    [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
    [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
    [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
    [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
]

NUMBER_VERTICES = len(VECTOR)  # число вершин в графе
#  Список с начальными значениями графа:
START_NUMBER_VECTOR = [[vector_2 for vector_2 in range(NUMBER_VERTICES)] for vector_1 in range(NUMBER_VERTICES)]

# VECTOR ^ 3
for k in range(NUMBER_VERTICES):
    for i in range(NUMBER_VERTICES):
        for j in range(NUMBER_VERTICES):
            buffer = VECTOR[i][k] + VECTOR[k][j]  # Получаем вес дуги графа с учетом промежуточной вершины
            if VECTOR[i][j] > buffer:  # Проверяем вес данного маршрута с учетом промежуточного графа (ищем мин.)
                VECTOR[i][j] = buffer
                START_NUMBER_VECTOR[i][j] = k  # Номер промежуточной вершины с минимальным сумарным весом

t_start = 3
t_end = 6
print(get_path(START_NUMBER_VECTOR, t_start, t_end))
