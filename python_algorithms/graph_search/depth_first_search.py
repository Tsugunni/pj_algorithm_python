from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u: int, v: int):
        self.graph[u].append(v)

    def DepthFirstSearch(self, start: int, goal: int) -> bool:
        suggestions = [start]
        seen = []
        while suggestions:
            stack = suggestions.pop()
            if stack == goal:
                return True
            seen.append(stack)
            next = self.graph[stack]
            for point in next:
                if point in seen:
                    break
                elif point in suggestions:
                    break
                else:
                    suggestions.append(point)

        return False


# Run example
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.DepthFirstSearch(0, 3))


# Run result
# False
