def half_adder(x: int, y: int) -> list:
    return [x & y, x ^ y]

def full_adder(x: int, y: int, carry: int = 0) -> list:
    if carry == 0:
        return half_adder(x, y)
    else:
        # Ternary is not bitwise, but there is no bitwise equivalence operation
        return [x | y, 1 if x == y else 0]

def calculator(x: int, y: int) -> int:
    carry = 0
    while True:
        carry = x & y
        x = x ^ y
        y = carry << 1

        if carry == 0:
            break
    return x

def one_line(x: int, y: int) -> int:
    return x if y == 0 else one_line(x ^ y, (x & y) << 1)

print(one_line(20, 22))