"""
Алгоритм Дейкстры

Описание:
        - Определение кратчайшего маршрута от некоторой стартовой вершины графа до остальных его вершин.
Примечания:
        - Рассматриваются только положительные веса дуг графов.

Применение:
        - Мршрутизация информационных пакетов, где вес графа - время передачи информационного пакета.
"""
import math

DATA_GRAPH = (
    (0, 3, 1, 3, math.inf, math.inf),
    (3, 0, 4, math.inf, math.inf, math.inf),
    (1, 4, 0, math.inf, 7, 5),
    (3, math.inf, math.inf, 0, math.inf, 2),
    (math.inf, math.inf, 7, math.inf, 0, 4),
    (math.inf, math.inf, 5, 2, 4, 0),
)

COUNT_GRAPH = len(DATA_GRAPH)  # Количество вершин у графа
DEFAULT_WEIGHT_GRAPH = [math.inf] * COUNT_GRAPH  # Дефолтное значение веаса для каждого графа (бесконечность)
START_GRAPH = 0  # Стартовая вершина
DEFAULT_WEIGHT_GRAPH[START_GRAPH] = 0  # Определяем вес стартового графа
PEAKS_VIEWED = {START_GRAPH}

# Оптимальные свзяи между маршрутами - дефолтные значения
OPTIMAL_CONNECTIONS_GRAPHS = [0] * COUNT_GRAPH


def min_meaning_in_graph(weight_graph, peaks_viewed):
    min_arg = -1
    max_weight = math.inf
    for num_tuple_graph, meaning_in_tuple_graph in enumerate(weight_graph):
        if meaning_in_tuple_graph < max_weight and num_tuple_graph not in peaks_viewed:
            max_weight = meaning_in_tuple_graph
            min_arg = num_tuple_graph
    return min_arg


while START_GRAPH != -1:  # Проходим все вершины в графе
    #  meaning_in_tuple_graph - получаем вес связи данной вершины графа из кортежа,
    #  который всязан с текущей вершиной графа.
    #  num_tuple_graph - номер кортежа с весами текущей вершины
    for num_tuple_graph, meaning_in_tuple_graph in enumerate(DATA_GRAPH[START_GRAPH]):
        #  Если мы не проверяли данную вершину графа
        if meaning_in_tuple_graph not in PEAKS_VIEWED:
            #  Получаем вес данного графа: сумируем вес от начального графа (0) до текущего графа
            graph_weight = DEFAULT_WEIGHT_GRAPH[START_GRAPH] + meaning_in_tuple_graph
            #  Если вес графа (graph_weight) оказался меньше ранее назначенного значения:
            if graph_weight < DEFAULT_WEIGHT_GRAPH[num_tuple_graph]:
                #  Меняем минимальный вес для данного графа
                DEFAULT_WEIGHT_GRAPH[num_tuple_graph] = graph_weight
                #  Устанавливаем оптимальную связь между маршрутами от начального графа до данного графа c мин. весом
                OPTIMAL_CONNECTIONS_GRAPHS[num_tuple_graph] = START_GRAPH
    # Определяем минимальный граф для поиска минимального веса уже в следующем кортеже
    START_GRAPH = min_meaning_in_graph(DEFAULT_WEIGHT_GRAPH, PEAKS_VIEWED)
    #  Находим следующий стартовый узел для следующего графа:
    if START_GRAPH >= 0:
        PEAKS_VIEWED.add(START_GRAPH)

print(DEFAULT_WEIGHT_GRAPH, end="\n"*2)

for item in range(len(DATA_GRAPH)):
    print(f"Лучший вес маршрута от графа '0' до графа '{item}' равен '{DEFAULT_WEIGHT_GRAPH[item]}'")

#  Определение оптимального маршрута от одного графа к другому:
start_graph_id = 0
end_graph_id = end_graph = 4
route = [end_graph]
while end_graph != start_graph_id:
    end_graph = OPTIMAL_CONNECTIONS_GRAPHS[route[-1]]
    route.append(end_graph)

route.reverse()
print(f"\nОптимальный маршрут от графа {start_graph_id} до графа {end_graph_id} равен маршрутам с весами {route}")
