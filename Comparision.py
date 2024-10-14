from queue import PriorityQueue


def AStar(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n is None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('The Shortest Path found using A star is: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


v = 1400
graph = [[] for i in range(v)]


def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True

    while not pq.empty():
        u = pq.get()[1]
        k = u + 65
        l = chr(k)
        print(l, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))
    print()


def add_edge(k, l, cost):
    x = ord(k) % 65
    y = ord(l) % 65
    cost = cost
    add_edg(x, y, cost)


def add_edg(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


def heuristic(n):
    H_dist = {
        'A': 20,
        'B': 22,
        'C': 25,
        'D': 19,
        'E': 24,
        'F': 18,
        'G': 0,
        'H': 17
    }
    return H_dist[n]


add_edge('A', 'B', 22)
add_edge('A', 'F', 18)
add_edge('A', 'C', 25)

add_edge('B', 'A', 20)
add_edge('B', 'E', 24)
add_edge('B', 'C', 25)

add_edge('C', 'A', 20)
add_edge('C', 'B', 22)
add_edge('C', 'E', 24)
add_edge('C', 'D', 19)
add_edge('C', 'G', 0)

add_edge('D', 'E', 24)
add_edge('D', 'C', 23)
add_edge('D', 'F', 18)
add_edge('D', 'G', 0)

add_edge('E', 'B', 22)
add_edge('E', 'C', 23)
add_edge('E', 'D', 19)
add_edge('E', 'F', 18)
add_edge('E', 'H', 17)

add_edge('F', 'H', 17)
add_edge('F', 'A', 20)
add_edge('F', 'E', 24)
add_edge('F', 'D', 19)
add_edge('F', 'G', 0)

add_edge('G', 'C', 23)
add_edge('G', 'D', 19)
add_edge('G', 'F', 18)
add_edge('G', 'H', 17)

add_edge('H', 'E', 24)
add_edge('H', 'F', 18)
add_edge('H', 'G', 0)

source = ord('A') % 65
target = ord('G') % 65
print("The Shortest Path using Best First Search is: ")
best_first_search(source, target, v)

Graph_nodes = {
    'A': [('B', 11), ('C', 10), ('F', 12)],
    'B': [('A', 11), ('E', 19), ('C', 13)],
    'C': [('A', 10), ('B', 13), ('E', 8), ('D', 9), ('G', 6)],
    'D': [('E', 8), ('C', 9), ('F', 4), ('G', 5)],
    'E': [('B', 19), ('C', 8), ('D', 8), ('F', 6), ('H', 14)],
    'F': [('H', 3), ('A', 12), ('E', 6), ('D', 4), ('G', 12)],
    'G': [('C', 6), ('D', 5), ('F', 12), ('H', 7)],
    'H': [('E', 14), ('F', 3), ('G', 7)]
}

AStar('A', 'G')
