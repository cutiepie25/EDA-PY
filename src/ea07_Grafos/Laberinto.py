from algs4.graph import Graph
from algs4.depth_first_search import DepthFirstSearch

if __name__=="__main__":
    lab = Graph(4*5)
    lab.add_edge(0,1)
    lab.add_edge(1,6)
    lab.add_edge(2,7)
    lab.add_edge(2,3)
    lab.add_edge(3,4)
    lab.add_edge(4,9)
    lab.add_edge(5,10)
    lab.add_edge(6,7)
    lab.add_edge(6,11)
    lab.add_edge(8,9)
    lab.add_edge(9,14)
    lab.add_edge(10,15)
    lab.add_edge(11,12)
    lab.add_edge(12,17)
    lab.add_edge(13,18)
    lab.add_edge(13,14)
    lab.add_edge(15,16)
    lab.add_edge(16,17)
    lab.add_edge(18,19)

    # TODO: Esta implementación recorre todo el grafo y marca visitados los nodos, 
    #       queremos adicionalmente que nos reporte la ruta para ir del vértice origen
    #       al vértice destino.
    dfs = DepthFirstSearch(lab,0)
    print('Cantidad nodos recorridos:', dfs.count)
    print('Nodos visitados:', dfs.marked)
