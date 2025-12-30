def hanoi_solver(disks):
    rod_a = list(range(disks, 0, -1))
    rod_b = []
    rod_c = []

    result = []

    def get_state():
        return f'{rod_a} {rod_b} {rod_c}'

    result.append(get_state())

    
    def hanoi(n, source, destination, auxiliary):
        if n == 1:
            destination.append(source.pop())
            result.append(get_state())
            return

        else:
            hanoi(n -1, source, auxiliary, destination)
            destination.append(source.pop())
            result.append(get_state())
            hanoi(n -1, auxiliary, destination, source)

    hanoi(disks, rod_a, rod_c, rod_b)

    return '\n'.join(result)

print(hanoi_solver(5))
print()
print(hanoi_solver(4))
print()
print(hanoi_solver(3))