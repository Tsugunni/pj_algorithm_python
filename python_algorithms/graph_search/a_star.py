import heapq
import itertools


def _find_ch(ch: str) -> tuple:
    for i, l in enumerate(dungeon):
        for j, c in enumerate(l):
            if c == ch:
                return (i, j)


def _nexts(pos: tuple):
    wall = "O"
    for a, b in itertools.product([" + 1", " - 1", ""], repeat=2):
        if a or b:
            if dungeon[eval("pos[0]" + a)][eval("pos[1]" + b)] != wall:
                yield (eval("pos[0]" + a), eval("pos[1]" + b))


def _heuristic(pos: tuple) -> float:
    return ((pos[0] - goal[0]) ** 2 + (pos[1] - goal[1]) ** 2) ** 0.5


def _distance(path: list) -> int:
    return len(path)


def _render_path(path: list) -> list:
    buf = [[ch for ch in l] for l in dungeon]
    for pos in path[1:-1]:
        buf[pos[0]][pos[1]] = "*"
    buf[path[0][0]][path[0][1]] = "s"
    buf[path[-1][0]][path[-1][1]] = "g"
    return ["".join(l) for l in buf]


def astar(init_pos: tuple, goal: tuple) -> list:
    passed_list = [init_pos]
    init_score = _distance(passed_list) + _heuristic(init_pos)
    checked = {init_pos: init_score}
    searching_heap = []
    heapq.heappush(searching_heap, (init_score, passed_list))
    while len(searching_heap) > 0:
        score, passed_list = heapq.heappop(searching_heap)
        last_passed_pos = passed_list[-1]
        if last_passed_pos == goal:
            return passed_list
        for pos in _nexts(last_passed_pos):
            new_passed_list = passed_list + [pos]
            pos_score = _distance(new_passed_list) + _heuristic(pos)

            if pos in checked and checked[pos] <= pos_score:
                continue

            checked[pos] = pos_score
            heapq.heappush(searching_heap, (pos_score, new_passed_list))
    return []


# Run example
if __name__ == "__main__":
    dungeon = [
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
        "OS  O     O     O         O          O",
        "O   O  O  O  O            O    OOOO GO",
        "O      O     O  O   OOOO  O    O  OOOO",
        "OOOOOOOOOOOOOOOOOO  O     O    O     O",
        "O                O  O     O          O",
        "O        OOO     O  O     OOOOOOOOO  O",
        "O  OO    O    OOOO  O     O      OO  O",
        "O   O    O          O     O  O   O   O",
        "O   OOO  O          O        O   O   O",
        "O        O          O        O       O",
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    ]
    init = _find_ch("S")
    goal = _find_ch("G")
    path = astar(init, goal)
    start_goal_map = "\n".join(_render_path(path))
    print(start_goal_map)


# Run result
"""
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
Os  O  *  O  *  O         O    ****  O
O **O**O**O**O**********  O   *OOOO*gO
O   *  O  *  O  O   OOOO* O   *O  OOOO
OOOOOOOOOOOOOOOOOO  O    *O   *O**   O
O                O  O    *O    *  *  O
O        OOO     O  O    *OOOOOOOOO* O
O  OO    O    OOOO  O    *O ***  OO *O
O   O    O          O    *O* O * O * O
O   OOO  O          O     *  O  *O*  O
O        O          O        O   *   O
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
"""
