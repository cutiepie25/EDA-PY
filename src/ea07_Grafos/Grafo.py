from algs4.graph import Graph
from algs4.depth_first_search import DepthFirstSearch


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