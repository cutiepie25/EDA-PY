from algs4.digraph import Digraph


if __name__=="__main__":
    g = Digraph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 4)
    g.add_edge(3, 2)
    g.add_edge(4, 1)
    g.add_edge(4, 2)
    g.add_edge(4, 3)

    print('Grafo como string:\n', str(g), sep='')

    # print('Grado entrante a 4:', g.indegree(4))   # No implementado en la biblioteca
    print('Grado entrante a 4:', g.adj[4].size())   # No implementado, pero se puede obtener del Bag

    print('Vecinos de 4:', end='  ')
    for v in g.adj[4]:
        print(v, end=', ')
    print()

    ginv = g.reverse()
    print('Grafo inverso:\n', ginv, sep='')