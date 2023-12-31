"""
Алгоритм Форда-Фалкерсона (1954г.).

Описание:
        - опредеоение максимальной пропускной способности потока в направленном графе (жидкости, информация и т.д.).
Примечания:
        - чем больше значение веса, тем выше пропускная способность дуги (целое, не отрицательное число).
        - Если в расматриваемом ненасыщенном маршруте встречается противоположная по направлению дуга, то величину ее
        потоко уменьшаем. Для остальных дуг - значение потока увеличиваем.
Применение:
        -
"""
import math


def get_max_matrix(now_graph, MATRIX, graph_array):
    min_meaning = 0  # Минимальное допустимое значение
    graph_meaning = -1  # Следующая вершина графа. Если такой вершины не найдется, то вернется -1.

    for number_graph, value_tuple_graph in enumerate(MATRIX[now_graph]):  # Проходимся по текущему графу.
        if number_graph in graph_array:  # Если мы уже прошлись по данному графу ранее.
            continue
        if value_tuple_graph[2] == 1:  # Если имеется движение вдоль потока (по стрелке).
            if value_tuple_graph[0] > min_meaning:  # Если у текущего графа пропускная способность вдоль потока > min.
                graph_meaning = number_graph  # В качестве следующего графа выбирается данный граф
                min_meaning = value_tuple_graph[0]
            else:  # Если движение вдоль потока >= 0, то выбираем движение против потока (против стрелки).
                if value_tuple_graph[1] > min_meaning:  # Если у текущего графа пропускная способность против потока > min.
                    graph_meaning = number_graph
                    min_meaning = value_tuple_graph[1]
    return graph_meaning


def get_max_flow(TNow):
    list_weight_in_TNow = [weight[0] for weight in TNow]
    return max(*list_weight_in_TNow)


def updateMATRIX(MATRIX, TNow, NOWROUTE):
    for t in TNow:  # Проходим по всем вершинам графа.
        if t[1] == -1:  # Пропускаем исток (не меняем его значения)
            continue
        sgn = MATRIX[t[2]][t[1]][2]  # Определяем направление движения у данного графа

        # меняем веса в таблице для (i,j) и (j,i)
        MATRIX[t[1]][t[2]][0] -= NOWROUTE * sgn
        MATRIX[t[1]][t[2]][1] += NOWROUTE * sgn

        MATRIX[t[2]][t[1]][0] -= NOWROUTE * sgn
        MATRIX[t[2]][t[1]][1] += NOWROUTE * sgn


# Матрица графа. Первая цифра - пропускная способность вдоль потока, Вторая цифра - пропускная способность против потока,
# Третья цифра - направление пропускной способности (вдоль потока или против него).
MATRIX = [[[0,0,1], [20,0,1], [30,0,1], [10,0,1], [0,0,1]],
     [[20,0,-1], [0,0,1], [40,0,1], [0,0,1], [30,0,1]],
     [[30,0,-1], [40,0,-1], [0,0,1], [10,0,1], [20,0,1]],
     [[10,0,-1], [0,0,1], [10,0,-1], [0,0,1], [20,0,1]],
     [[0,0,1], [30,0,-1], [20,0,-1], [20,0,-1], [0,0,1]],
]


COUNT_VERTICES_GRAPH = len(MATRIX)  # Число вершин в графе.
start = 0  # вершина истока
end = 4  # вершина стока
# Метка для вершины истока
# пропускная способность вдоль потока (сам на себя), пропускная способность против потока (сам на себя),
# направление пропускной способности (сам на себя).
TStart = (math.inf, -1, start)
ROUTE = []  # Максимальные потоки для каждого найденного маршрута.

# Индекс текущей вершины:
buf_counter = start

while buf_counter != -1:  # Проверяем наличие следующих вершин относительно истоков. Если -1 - вершин нет, завершаем.
    now_graph = start  # Индекс текущей стартовой вершины.
    TNow = [TStart]  # Инициализируем стартовые метки для текущего маршрута.
    graph_array = {start}  # Множество уже просмотренных вершин и формировании маршрута

    while now_graph != end:  # Пока текущая вершина не дошла до стока (конечной вершины).
        # Выбираем следующую вершину с наибольшей пропускной способностью.
        buf_counter = get_max_matrix(now_graph, MATRIX, graph_array)
        if buf_counter == -1:  # Если мы достигли конечной вершины (или пропускная способность всех графов равна нулю).
            if buf_counter == start:  # И мы находимся на истоке, т.е. узнали максимальные потоки для каждого маршрута.
                break
            else:  # Если мы не на истоке (т.е. дошли до тупика в локальной вершине).
                now_graph = TNow.pop()[2]  # В переписанной метке ниже, берем индекс прошлого графа (откатываемся).
                # Код ниже будет уже исполняться, но уже для прошлой вершины, т.к. у текущей нет положительных потоков.
                continue
        # Определяем вес потока, исходя из его направления (выбираем, первую цифру или вотрую, в зависимости от направления потока)
        # Вес текущего потока в зависимости от его направления:
        current_flow_weight = MATRIX[now_graph][buf_counter][0] if MATRIX[now_graph][buf_counter][2] == 1 else MATRIX[now_graph][buf_counter][1]
        # Добавляем метку маршрута: текущий вес потока, индекс текущей вершины, индекс пройденной вершины
        TNow.append((current_flow_weight, buf_counter, now_graph))
        graph_array.add(buf_counter)  # Добавляем индекс пройденного маршрута

        if buf_counter == end:  # Если индекс текущей вершины равен индексу истока. т.е. мы дошли до истока.
            ROUTE.append(get_max_flow(TNow))  # Находим максимальную пропускную способность среди пройденных вершин графа.
            # Обновляем веса пройденных дуг. Значения берем из максимальных потоков уже найденных маршрутов, которые
            # мы только что добавили.
            updateMATRIX(MATRIX, TNow, ROUTE[-1])
            break  # Нашли весь маршрут, завершаем цикл
    now_graph = buf_counter  # Начинаем искать с истока уже новый маршрут


result = sum(ROUTE)  # Ищем сумму максимальной пропускной способности каждого маршрута
print(f"Вес максимального потока равен: {result}")
