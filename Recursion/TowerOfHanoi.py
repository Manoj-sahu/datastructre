def toh(n, fromRod, toRod, auxRod):
    if n== 1:
        print('Move disk 1 from rod', fromRod, 'to Rod', toRod)
        return
    toh(n-1, fromRod, auxRod, toRod)
    print('move disk', n, 'from rod ', fromRod, 'to rod', toRod)
    toh(n-1, auxRod, toRod, fromRod)

toh(4, 'A', 'C', 'B')