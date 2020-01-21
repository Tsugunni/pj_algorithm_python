class Graph:
    class Edge:
        def __init__(self, _from, _to, _cost):
            self.from_ = _from
            self.to = _to
            self.cost = _cost

    def __init__(self):
        self.edges = []
        self.v_set = set()

    @property
    def E(self):
        return len(self.edges)

    @property
    def V(self):
        return len(self.v_set)

    def add(self, _from, _to, _cost):
        self.edges.append(self.Edge(_from, _to, _cost))
        self.v_set.add(_from)
        self.v_set.add(_to)

    def shortest_path(self, s):
        d = [float("inf")] * self.V
        d[s] = 0

        while True:
            do_update = False
            for i in range(self.E):
                e = self.edges[i]
                if d[e.from_] != float("inf") and d[e.to] > d[e.from_] + e.cost:
                    d[e.to] = d[e.from_] + e.cost
                    do_update = True

            if not do_update:
                break

        return d


g = Graph()
g.add(0, 1, 5)
g.add(0, 2, 4)
g.add(1, 2, -2)
g.add(1, 3, 1)
g.add(2, 3, 2)
g.add(2, 4, 1)
g.add(2, 5, 4)
g.add(3, 5, 3)
g.add(4, 5, 4)

path = g.shortest_path(0)
