border = input("Введите граничное значение: ")
border = int(border)

new_list = []

for i in range(0, border + 1):
    new_list.append(i)
    i += 1

for i in new_list:
    if i % 2 == 0:
        print(i)
    i += 1
