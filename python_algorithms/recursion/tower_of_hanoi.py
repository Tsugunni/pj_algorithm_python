def TowerOfHanoi(n: int, from_rod: str, to_rod: str, aux_rod: str):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# Run example
n = 4
TowerOfHanoi(n, "A", "C", "B")


# Run result
# Move disk 1 from rod A to rod B
# Move disk 2 from rod A to rod C
# Move disk 1 from rod B to rod C
# Move disk 3 from rod A to rod B
# Move disk 1 from rod C to rod A
# Move disk 2 from rod C to rod B
# Move disk 1 from rod A to rod B
# Move disk 4 from rod A to rod C
# Move disk 1 from rod B to rod C
# Move disk 2 from rod B to rod A
# Move disk 1 from rod C to rod A
# Move disk 3 from rod B to rod C
# Move disk 1 from rod A to rod B
# Move disk 2 from rod A to rod C
# Move disk 1 from rod B to rod C
