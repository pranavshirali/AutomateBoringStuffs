def Zero_division(dividedby):
    try:
        return 40 / dividedby
    except ZeroDivisionError:
        print('Error: Invalid Argument (0).')

print(Zero_division(12))
print(Zero_division(10))
print(Zero_division(0))
print(Zero_division(3))