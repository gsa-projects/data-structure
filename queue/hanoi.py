def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print(f'disk 1: {fr} -> {to}')
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        print(f'disk {n}: {fr} -> {to}')
        hanoi_tower(n - 1, tmp, fr, to)

hanoi_tower(4, 'A', 'B', 'C')
