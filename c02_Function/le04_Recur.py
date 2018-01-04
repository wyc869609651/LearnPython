# Homework: 汉诺塔


def hanno(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanno(n-1, a, c, b)
        print(a, '-->', c)
        hanno(n-1, b, a, c)


hanno(5, 'A', 'B', 'C')

