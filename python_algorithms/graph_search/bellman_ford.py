class BellmanFord:
    class Edge:
        def __init__(self, _from, _to, _cost):
            self.from_ = _from
            self.to = _to
            self.cost = _cost

    def __init__(self):
        self.edges = []  # 辺
        self.v_set = set()  # 頂点の集合

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

    def exist_negative_loop(self):
        d = [0] * self.V
        for i in range(self.V):
            for j in range(self.E):
                e = self.edges[j]
                if d[e.to] > d[e.from_] + e.cost:
                    d[e.to] = d[e.from_] + e.cost
                    if i == self.V - 1:
                        return True
        return False


def sample1():
    print("---sample1---")

    bf = BellmanFord()
    bf.add(0, 1, 5)
    bf.add(0, 2, 4)
    bf.add(1, 2, -2)
    bf.add(1, 3, 1)
    bf.add(2, 3, 2)
    bf.add(2, 4, 1)
    bf.add(2, 5, 4)
    bf.add(3, 5, 3)
    bf.add(4, 5, 4)

    print(f"bf.exist_negatve_loop(): {bf.exist_negative_loop()}")

    path = bf.shortest_path(0)
    print(f"path: {path}")


if __name__ == "__main__":
    sample1()
