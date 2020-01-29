import heapq
import itertools


class AstarObject(object):
    def astar(self, init_pos: tuple, goal: tuple) -> list:
        """
        >>> dungeon = [ \
            "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",\
            "OS  O     O     O         O          O",\
            "O   O  O  O  O            O    OOOO GO",\
            "O      O     O  O   OOOO  O    O  OOOO",\
            "OOOOOOOOOOOOOOOOOO  O     O    O     O",\
            "O                O  O     O          O",\
            "O        OOO     O  O     OOOOOOOOO  O",\
            "O  OO    O    OOOO  O     O      OO  O",\
            "O   O    O          O     O  O   O   O",\
            "O   OOO  O          O        O   O   O",\
            "O        O          O        O       O",\
            "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",\
            ]
        >>> ast = AstarObject()
        >>> init = ast.find_ch("S")
        >>> goal = ast.find_ch("G")
        >>> path = ast.astar(init, goal)
        """
        passed_list = [init_pos]
        init_score = self.distance(passed_list) + self.heuristic(init_pos)
        checked = {init_pos: init_score}
        searching_heap = []
        heapq.heappush(searching_heap, (init_score, passed_list))

        while len(searching_heap) > 0:
            score, passed_list = heapq.heappop(searching_heap)
            last_passed_pos = passed_list[-1]

            if last_passed_pos == goal:
                return passed_list

            for pos in self.nexts(last_passed_pos):
                new_passed_list = passed_list + [pos]
                pos_score = self.distance(new_passed_list) + self.heuristic(pos)

                if pos in checked and checked[pos] <= pos_score:
                    continue

                checked[pos] = pos_score
                heapq.heappush(searching_heap, (pos_score, new_passed_list))

        return []

    def find_ch(ch: str) -> tuple:
        for i, l in enumerate(dungeon):
            for j, c in enumerate(l):
                if c == ch:
                    return (i, j)

    def nexts(pos: tuple):
        wall = "O"

        for a, b in itertools.product([" + 1", " - 1", ""], repeat=2):
            if a or b:
                if dungeon[eval("pos[0]" + a)][eval("pos[1]" + b)] != wall:
                    yield (eval("pos[0]" + a), eval("pos[1]" + b))


def heuristic(pos: tuple) -> float:
    return ((pos[0] - goal[0]) ** 2 + (pos[1] - goal[1]) ** 2) ** 0.5


def distance(path: list) -> int:
    return len(path)


def render_path(path: list) -> list:
    buf = [[ch for ch in l] for l in dungeon]

    for pos in path[1:-1]:
        buf[pos[0]][pos[1]] = "*"

    buf[path[0][0]][path[0][1]] = "s"
    buf[path[-1][0]][path[-1][1]] = "g"
    return ["".join(l) for l in buf]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
# # Run example
# path = astar(init, goal)

# if len(path) > 0:
#     print("\n".join(render_path(path)))
# else:
#     print("failed")


# Run result

#   OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#   Os  O  *  O  *  O         O    ****  O
#   O **O**O**O**O**********  O   *OOOO*gO
#   O   *  O  *  O  O   OOOO* O   *O  OOOO
#   OOOOOOOOOOOOOOOOOO  O    *O   *O**   O
#   O                O  O    *O    *  *  O
#   O        OOO     O  O    *OOOOOOOOO* O
#   O  OO    O    OOOO  O    *O ***  OO *O
#   O   O    O          O    *O* O * O * O
#   O   OOO  O          O     *  O  *O*  O
#   O        O          O        O   *   O
#   OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
