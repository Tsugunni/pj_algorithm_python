from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u: int, v: int):
        self.graph[u].append(v)

    def breadthFirstSearch(self, start: int, goal: int) -> bool:
        suggestions = deque()
        suggestions.append(start)
        seen = []
        while suggestions:
            cur = suggestions.popleft()
            if cur == goal:
                return True
            seen.append(cur)
            next = self.graph[cur]
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

print(g.breadthFirstSearch(2, 0))


# Run result

#
# True
#
