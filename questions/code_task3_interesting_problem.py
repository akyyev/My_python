# Question:
# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?


def solve(head, leg):
    print(f'We count {head} heads and {leg} legs among the chickens and rabbits in a farm')
    for i in range(head + 1):
        j = head - i
        if 2 * i + 4 * j == leg:
            return i, j


c, r = solve(35, 94)
print('Chicken: %d\nRabbit: %d' % (c, r))
print(f'{c} chicken + {r} rabbit =', c + r, 'heads')
print(f'{c}*2 chicken legs + {r}*4 rabbit legs =', c * 2 + r * 4, 'legs')
