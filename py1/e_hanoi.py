def hanoi_solver(n):
    source = list(range(n, 0, -1)) 
    auxiliary = []
    target = []
    moves = []
    
    moves.append(f"{source} {auxiliary} {target}")
    
    def move_disks(num_disks, src, aux, tgt):
        if num_disks == 1:
            tgt.append(src.pop())
            moves.append(f"{source} {auxiliary} {target}")
        else:
            move_disks(num_disks - 1, src, tgt, aux)
            tgt.append(src.pop())
            moves.append(f"{source} {auxiliary} {target}")
            move_disks(num_disks - 1, aux, src, tgt)

    move_disks(n, source, auxiliary, target)
    return '\n'.join(moves)

if __name__ == "__main__":
    num_disks = 2
    solution = hanoi_solver(num_disks)
    print (f"Solution for {num_disks} disks:")
    print(solution)
    