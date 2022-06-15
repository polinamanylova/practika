# Шаблон уровня

class Level:
    # Объявление некоторых переменных, отвечающих за прохождение и наполнение каждого из урвоней
    def __init__(self, vertices_positions, edges_list):
        self.vertices_positions = vertices_positions
        self.edges_list = edges_list
        self.edges_positions_list = calculate_edges_positions_list(self.vertices_positions, self.edges_list)
        self.bypassed_edges = []
        self.current_painted_vertex = -1
        self.previous_painted_vertex = -1

    # Проверка того, что заданное ребро имеется в списке ребер
    def edge_exists(self, edge):
        return edge in self.edges_list

    # Проверка существования вершины графа (разница между заданной координатой и пройденной пользователем может быть
    # чуть больше нуля, поскольку вершины графа изображаются кругом с некоторым радиусом (a/2)
    # В случае нахождения такой вершины возвращает ее номер в списке вершин, иначе -1
    def vertex_exists(self, vertex_x, vertex_y):
        for i in range(len(self.vertices_positions)):
            vertex = self.vertices_positions[i]
            if abs(vertex[0] - vertex_x) <= 15 and abs(vertex[1] - vertex_y) <= 15:
                return i
        return -1


# Мне было немного лень вручную писать координаты для всех ребер, поэтому эта функция делает это
# (координаты начальной и конечной точки, если быть точным)
def calculate_edges_positions_list(vertices_positions, edges_list):
    edges_positions_list = []
    for edge in edges_list:
        edges_positions_list.append(vertices_positions[edge[0]] + vertices_positions[edge[1]])
    return edges_positions_list
