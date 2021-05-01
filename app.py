import random

numbers = range(2, 13)

while True:
    a = random.choice(numbers)
    b = random.choice(numbers)

    answer = input(f"{a} x {b} = ")

    if (a * b == int(answer)):
        print(f"\033[F{a} x {b} = {answer} 🟢")
    else:
        print(f"\033[F{a} x {b} = {answer} 🔴 ({a*b})")
