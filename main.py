n1 = float(input("Введите первое число: ")) # ввод первого числа
n2= float(input("Введите второе число: ")) # ввод второго числа

result = "Числа равны" if n1 == n2 else (f"Наименьшее число: {n1}" if n1 < n2 else f"Наименьшее число: {n2}") # определение наименьшего числа

print(result) # вывод результата
