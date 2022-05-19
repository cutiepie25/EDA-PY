from algs4.graph import Graph
from algs4.depth_first_search import DepthFirstSearch
from algs4.breadth_first_paths import BreadthFirstPaths


if __name__=="__main__":
    vuelos = Graph(6)
    vuelos.add_edge(1, 2)
    vuelos.add_edge(2, 3)
    vuelos.add_edge(2, 4)
    vuelos.add_edge(3, 5)
    vuelos.add_edge(3, 0)

    print(vuelos.adj[3].size())
    for vecino in vuelos.adj[3]:
        print(vecino, ',', end='')
    print()

    print('Graph:\n', str(vuelos))

    dfs = DepthFirstSearch(vuelos,1)
    print('Cantidad nodos recorridos:', dfs.count)
    print('Nodos visitados:', dfs.marked)


    bfs = BreadthFirstPaths(vuelos, 1)
    print('Tiene camino hasta 5:', bfs.has_path_to(5))
    print('Camino hasta 5', [ x for x in bfs.path_to(5)])

