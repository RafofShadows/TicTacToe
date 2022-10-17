field = [["-", "-", "-"] for i in range(3)]
current_player = 0
cr = ["x", "0"]


def print_field():
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {' '.join(field[i])}")


def rules():
    print("""Игроки ходят по очереди. Первый игрок ставит Х, второй игрок ставит О.
    Выигрывает игрок, собравший три символа в одной вертикали, горизонтали или вертикали.
    Ход осуществляется посредством ввода координат через пробел, например '1 1'
    Вля выхода введите exit.\n""")


def incorrect_input():
    print("Неверный формат ввода. Попробуйте еще раз.")


def occupied():
    print("Позиция занята. Выберите другое место.")


def win():
    print(f"Победил игрок {current_player+1 }")


def game_finished():
    # horizontal:
    for item in field:
        if all([i == item[0] for i in item]) and item[0] != "-":
            win()
            return True
    # vertical:
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] != "-":
            win()
            return True
    # diagonal:
    if (field[0][0] == field[1][1] == field[2][2] and field[0][0] != "-") or (field[0][2] == field[1][1] == field[2][2] and field[2][0] != "-"):
        win()
        return True
    if all(c != "-" for c in [i for item in field for i in item]):
        print("Ничья!")
        return True
    return False


rules()
while True:
    print_field()
    in_str = input(f"Player{current_player + 1}:").strip()
    if "exit" in in_str:
        break
    in_list = in_str.split(" ")
    is_correct = len(in_list) == 2 and all([list(map(lambda s: (s.isdigit and 0 <= int(s) < 3), in_list))])
    if not is_correct:
        incorrect_input()
        continue
    else:
        x = int(in_list[0])
        y = int(in_list[1])
        if field[y][x] != "-":
            occupied()
            continue
        else:
            field[y][x] = cr[current_player]
            current_player = (current_player + 1) % 2
    win_draw = game_finished()
    if win_draw:
        print_field()
        break
