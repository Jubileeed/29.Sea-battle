import random
#создаем поле
field = []
for x in range(5):
    field.append(["O"] * 5)
#выводим поле
def print_field(field):
    for row in field:
      print("".join(row))
#начало игры - выводим пустую таблицу
print('Добро пожаловать в игру "Морской бой!"')
print_field(field)
#рандомно задаем координаты корабля
def random_row(field):
    return random.randint(0, len(field) - 1)

def random_col(field):
    return random.randint(0, len(field[0]) - 1)

ship_row = random_row(field)
ship_col = random_col(field)
#игровой цикл
for turn in range(4):
    print("Ход", turn + 1)
    guess_row = int(input("Введите номер строки: "))
    guess_col = int(input("Введите номер столбца: "))

    if guess_row == ship_row and guess_col == ship_col:
      print("Победа! Вы подбили корабль!")
      break
    else:
      if guess_row < 0 or guess_row >= len(field) or guess_col < 0 or guess_col >= len(field[0]):
        print("Выход за пределы поля!")
      elif(field[guess_row][guess_col] == "X"):
        print("Вы уже стреляли")
      else:
        print("Вы промахнулись!")
        field[guess_row][guess_col] = "X"
    print_field(field)
if turn == 3:
    print("Ваши попытки исчерпаны. Вы проиграли!")