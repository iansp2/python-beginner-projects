def print_(func):
    print(func.__name__)
    print("-" * 13)
    print(f"| 0 | 0 | {func(0, 0)} |")
    print(f"| 0 | 1 | {func(0, 1)} |")
    print(f"| 1 | 0 | {func(1, 0)} |")
    print(f"| 1 | 1 | {func(1, 1)} |")
    print("-" * 13)
    print("\n")

def and_(x: int, y: int) -> int:
    if x==1 and y==1:
        return 1
    
    return 0

def or_(x: int, y: int) -> int:
    if x==1 or y==1:
        return 1
    
    return 0

def not_(x: int, y: int) -> int:
    if x == 0:
        return 1
    
    return 0

def xor_(x: int, y: int) -> int:
    if x != y:
        return 1
    
    return 0

def equiv(x: int, y: int) -> int:
    if x == y:
        return 1
    
    return 0

def imp(x: int, y: int) -> int:
    if x == 1:
        return y
    
    return 1

def nand(x: int, y: int) -> int:
    return not_(and_(x, y), y)

def nor(x: int, y: int) -> int:
    return not_(or_(x, y), y)

# print_(and_)
# print_(or_)
# print_(not_)
# print_(xor_)
# print_(equiv)
# print_(imp)
# print_(nand)
# print_(nor)

def half_adder(x: int, y: int) -> list:
    right_digit = xor_(x, y)
    left_digit = and_(x, y)
    return [left_digit, right_digit]

def full_adder(x: int, y: int, carry: int) -> list:
    x_y_HA = half_adder(x, y)
    c_HA = half_adder(carry, x_y_HA[1])
    right_digit = c_HA[1]
    carry = or_(c_HA[0], x_y_HA[0])
    return [carry, right_digit]

def calculator(num1: str, num2: str) -> list:
    carry = 0
    result = []
    #to improve in future: add padding in case numbers aren't same size
    for i in range(len(num1), 0, -1):
        x = int(num1[i - 1])
        y = int(num2[i - 1])
        sum = full_adder(x, y, carry)
        carry = sum[0]
        result = [sum[1]] + result
        if i == 1 and carry == 1:
            result = [1] + result
    return result

num1 = "101010"
num2 = "101010"

print(calculator(num1, num2))