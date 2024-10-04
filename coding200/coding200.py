import string

# Definición inicial del mapa
data = """..B.
a..&
&.&&
aA.&
"""

# Lectura del mapa desde un archivo de texto
with open("map.txt", "r") as f:
    data = f.read()

# Se transforma el mapa en una lista de listas de caracteres
initial_map = list(map(lambda x: list(x), data.split("\n")))[:-1]

# Coordenadas que representan las posiciones adyacentes
surrounding = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Movimientos posibles con sus respectivas coordenadas
movements = {
    "N": (-1, 0),
    "W": (0, -1),
    "E": (0, 1),
    "S": (1, 0)
}

# Función para obtener el valor de una posición del mapa de forma segura
def safe_get(map_data, x, y, dx, dy):
    if x + dx < 0 or x + dx >= len(map_data):
        return None
    if y + dy < 0 or y + dy >= len(map_data[0]):
        return None
    return map_data[x + dx][y + dy]

# Función que obtiene el valor de una posición del mapa si no ha sido visitada
def safe_v_get(map_data, visited, x, y, dx, dy):
    if (x + dx, y + dy) in visited:
        return None
    return safe_get(map_data, x, y, dx, dy)

# Función para realizar una copia profunda del mapa
def deepcopy(map_data):
    new_map = []
    for row in map_data:
        new_map.append(row[:])
    return new_map

# Destruir los portales en el mapa, reemplazándolos con otro símbolo
def destroy_portals(map_data, portal, new_state):
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == portal:
                map_data[i][j] = new_state

# Clase que representa el estado actual en la búsqueda
class State:
    def __init__(self, map_state, player_x, player_y, depth, portal_count, path, visited):
        self.map_state = map_state  # Estado actual del mapa
        self.player_x = player_x  # Posición del jugador en X
        self.player_y = player_y  # Posición del jugador en Y
        self.depth = depth  # Profundidad en la búsqueda (número de movimientos)
        self.portal_count = portal_count  # Número de portales usados
        self.path = path  # Ruta recorrida
        self.visited = visited  # Lista de posiciones visitadas

    def dump(self):
        print(f"{self.depth} {self.portal_count} [{self.player_x},{self.player_y}] {self.path}")

# Clase que representa el estado del mapa con sus portales
class MapState:
    def __init__(self, map_data, portals):
        self.map_data = map_data  # Matriz del mapa
        self.portals = portals  # Diccionario de portales

    def dumpmap(self):
        print("\n".join(map(lambda row: "".join(row), self.map_data)))

    # Actualiza el mapa al siguiente estado según las reglas de los agujeros negros
    def get_next_map(self):
        new_map = deepcopy(self.map_data)
        new_portals = self.portals.copy()

        for i in range(len(self.map_data)):
            for j in range(len(self.map_data[0])):
                around_blackholes = 0
                for (dx, dy) in surrounding:
                    if safe_get(self.map_data, i, j, dx, dy) == "&":
                        around_blackholes += 1

                if self.map_data[i][j] == "&":  # Si es un agujero negro
                    if around_blackholes != 2 and around_blackholes != 3:
                        new_map[i][j] = "."  # Se convierte en vacío
                else:  # Si no es un agujero negro
                    if around_blackholes >= 3:
                        new_map[i][j] = "&"  # Se convierte en agujero negro
                        # Revisa si destruyó un portal
                        if self.map_data[i][j] in string.ascii_lowercase:
                            if self.map_data[i][j] in new_portals:
                                del new_portals[self.map_data[i][j]]
                            destroy_portals(new_map, self.map_data[i][j], "&")

        return MapState(new_map, new_portals)

    # Destruye un portal específico y lo reemplaza con vacío
    def destroyed_portal(self, portal):
        new_map = deepcopy(self.map_data)
        new_portals = self.portals.copy()

        del new_portals[portal]  # Elimina el portal del diccionario
        destroy_portals(new_map, portal, ".")  # Destruye el portal en el mapa
        return MapState(new_map, new_portals)

# Inicializa la posición del jugador (A) y la meta (B)
for i in range(len(initial_map)):
    if "A" in initial_map[i]:
        start_x = i
        start_y = initial_map[i].index("A")
        initial_map[start_x][start_y] = "."  # Reemplaza A por un espacio vacío
    if "B" in initial_map[i]:
        goal_x = i
        goal_y = initial_map[i].index("B")
        initial_map[goal_x][goal_y] = "."  # Reemplaza B por un espacio vacío

# Encuentra y almacena las posiciones de los portales
portals = {}
for portal in string.ascii_lowercase:
    first_location = None
    second_location = None
    for i in range(len(initial_map)):
        for j in range(len(initial_map[0])):
            if initial_map[i][j] == portal:
                if first_location:
                    second_location = (i, j)
                    portals[portal] = (first_location, second_location)
                    break
                else:
                    first_location = (i, j)

# Inicializa el primer estado del mapa
first_state = MapState(initial_map, portals)

min_depth = -1
queue = []
queue.append(State(first_state, start_x, start_y, 0, 0, "", []))

solutions = []
cache = []

# Búsqueda en amplitud (BFS)
while True:
    current_state = queue.pop(0)
    key = (current_state.depth, current_state.player_x, current_state.player_y, "".join(current_state.map_state.portals.keys()))
    
    # Si la profundidad mínima ha sido alcanzada, se termina la búsqueda
    if min_depth != -1 and current_state.depth > min_depth:
        break

    # Si se llega al objetivo (B), se guarda la solución
    if current_state.player_x == goal_x and current_state.player_y == goal_y:
        min_depth = current_state.depth
        solutions.append(current_state)
        continue

    next_map_state = current_state.map_state.get_next_map()

    # Explora los posibles movimientos
    for move in movements:
        (dx, dy) = movements[move]
        original_target = safe_v_get(current_state.map_state.map_data, current_state.visited, current_state.player_x, current_state.player_y, dx, dy)
        if original_target is None:
            continue  # Fuera de los límites
        next_target = safe_get(next_map_state.map_data, current_state.player_x, current_state.player_y, dx, dy)
        if original_target == "&" or next_target == "&":
            continue  # Es un agujero negro
        if original_target in next_map_state.portals:
            # Si el jugador entra en un portal
            if (current_state.player_x + dx, current_state.player_y + dy) == current_state.map_state.portals[original_target][0]:
                (new_player_x, new_player_y) = current_state.map_state.portals[original_target][1]
            else:
                (new_player_x, new_player_y) = current_state.map_state.portals[original_target][0]
            queue.append(State(next_map_state.destroyed_portal(original_target), new_player_x, new_player_y, current_state.depth + 1, current_state.portal_count + 1, current_state.path + move, current_state.visited + [(new_player_x, new_player_y), (current_state.player_x + dx, current_state.player_y + dy)]))
        else:
            (new_player_x, new_player_y) = (current_state.player_x + dx, current_state.player_y + dy)
            queue.append(State(next_map_state, new_player_x, new_player_y, current_state.depth + 1, current_state.portal_count, current_state.path + move, current_state.visited + [(new_player_x, new_player_y)]))

# Filtra las soluciones que utilizan la máxima cantidad de portales
max_portals = max(map(lambda x: x.portal_count, solutions))
max_solutions = filter(lambda x: x.portal_count == max_portals, solutions)
paths = sorted(list(map(lambda x: x.path, max_solutions)))

# Imprime el resultado
print(f"{len(paths)}-{''.join(paths)}-{max_portals}")
