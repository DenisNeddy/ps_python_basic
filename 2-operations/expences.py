# Ввести три траты: еда, транспорт, развлечения. Вывести общую сумму и среднее - файл expences.py



food = input("Введите сумму потраченную на еду: ")
transport = input("Введите сумму потраченную на транспорт: ")
entertainment = input("Введите сумму потраченную на развлечение: ")
total = int(food) + int(transport) + int(entertainment)
average = total // 3
print(f"Общие траты составят: {total}")
print(f"Средняя сумма составит: {average}")