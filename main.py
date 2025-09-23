def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Добавьте вызов функции в конец файла
print(f"Факториал числа {rows}: {factorial(rows)}")