from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start: int, goal: int) -> bool:
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

        # 探索スタート地点を「探索候補スタック」に積む
        # while スタックが空っぽになるまで
        #     スタックから次の探索地点を1つ取り出す（pop）
        #     「探索済みリスト」に取り出した地点を格納（ここが現在地点）
        #     　　現在地点から、次に行こうと思えば行けるポイントを全部探し出す
        #     for 地点 in 次に行こうと思えば行けるポイント
        #         if その地点は既に「探索済みリスト」にある？
        #         探索済みなので「探索候補スタック」には入れない（continue）
        #         if その地点は既に「探索候補スタック」にある？（閉路があるなら可能性あり、木なら可能性なし）
        #         探索予定なので「探索候補スタック」には入れない（continue）
        #         未探索かつ候補にも入っていない地点なので「探索候補スタック」に追加する（append）
        #         print
        #         探索済み地点


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.BFS(2, 5))
