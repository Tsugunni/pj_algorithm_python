class Graph:
    class Edge:
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        self.G = [[] for i in range(V)]
        self._E = 0
        self._V = V

    @property
    def E(self):
        return self._E

    @property
    def V(self):
        return self._V

    def add(self, _from, _to, _cost):
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1

    def shortest_path(self, s):
        import heapq

        que = []
        d = [float("inf")] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s))

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            if d[v] < cost:
                continue

            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost
                    heapq.heappush(que, (d[e.to], e.to))
        return d


def sample1():
    V = 10
    g = Graph(V)
    g.add(0, 1, 100)
    g.add(1, 2, 200)
    g.add(2, 8, 1)
    g.add(5, 6, 100)

    d = g.shortest_path(1)


def sample2():
    V = 8
    g = Graph(V)
    g.add(0, 1, 1)
    g.add(1, 0, 1)

    g.add(0, 2, 7)
    g.add(2, 0, 7)

    g.add(0, 3, 2)
    g.add(3, 0, 2)

    g.add(1, 4, 2)
    g.add(4, 1, 2)

    g.add(1, 5, 4)
    g.add(5, 1, 4)

    g.add(2, 5, 2)
    g.add(5, 2, 2)

    g.add(2, 6, 3)
    g.add(6, 2, 3)

    g.add(3, 6, 5)
    g.add(6, 3, 5)

    g.add(4, 5, 1)
    g.add(5, 4, 1)

    g.add(5, 7, 6)
    g.add(7, 5, 6)

    g.add(6, 7, 2)
    g.add(7, 6, 2)

    d = g.shortest_path(0)
