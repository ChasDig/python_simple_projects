# Алгоритм Прима
# Алгоритм для поиска минимального остово взвешенного неорентированного графа
"""
Определение:
    - Остов: подграф исходного графа, который состоит из всех вершин этого графа, соединенного ребрами.
    Ребра не должны образовывать цикл.
Этапы:
    -
"""

import math


def get_min_edge(count_graph_vertices, graph):
    buffer_min = (math.inf, -1, -1)
    for graph_vertices in count_graph_vertices:
        min_graph = min(
            graph,
            key=lambda x: x[0] if(x[1] == graph_vertices or x[2] == graph_vertices) and (x[1] not in count_graph_vertices or x[2] not in count_graph_vertices) else math.inf,
        )
        if buffer_min > min_graph:
            buffer_min = min_graph
    return buffer_min


# Список ребер графа (длина, вершина 1, вершина 2):
Graph = [
    (math.inf, -1, -1), (13, 1, 2), (18, 1, 3),
    (17, 1, 4), (14, 1, 5), (22, 1, 6), (26, 2, 3),
    (19, 2, 5), (30, 3, 4), (22, 4, 6),
]
number_graph = 6  # Количество вершин графа
count_graph_vertices = {1}  # Множество соединенных вершин графа
count_edge_ostov = []  # Список ребер остовов

while len(count_graph_vertices) < number_graph:
    min_edge = get_min_edge(count_graph_vertices, Graph)
    if min_edge == math.inf:
        break
    count_graph_vertices.add(min_edge[1])
    count_graph_vertices.add(min_edge[2])
    count_edge_ostov.append(min_edge)


print(count_edge_ostov)
