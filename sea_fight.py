def generate_table(pos):
    return f'''
        -------------
        | {pos[1]} | {pos[2]} | {pos[3]} |
        -------------
        | {pos[4]} | {pos[5]} | {pos[6]} |
        -------------
        | {pos[7]} | {pos[8]} | {pos[9]} |
        -------------
        '''


def input_step(pos, sign):
    while True:
        answer = input('Введите номер ячейки: ')
        try:
            if int(answer) in range(1, 10):
                if pos[int(answer)] == answer:
                    pos[int(answer)] = sign
                    return generate_table(pos)
                else:
                    print('Ячейка занята')
                    continue
            else:
                print('Введено некоректное значение (нужно число от 1 до 9)')
                continue
        except ValueError:
            print('Введено некоректное значение (нужно число от 1 до 9)')
            continue


def check_win(pos):
    win_pos = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for i in win_pos:
        if pos[i[0]] == pos[i[1]] == pos[i[2]]:
            return pos[i[0]]
    return False


def main(pos):
    count = 0
    win = False
    print(generate_table(pos))
    while not win:
        if count % 2 == 0:
            print(input_step(pos, 'X'))
        else:
            print(input_step(pos, 'O'))
        count += 1
        if count > 4:
            player = check_win(pos)
            if player:
                print('Игрок:', player, 'выиграл!')
                win = True
        if count == 9:
            print("Ничья!")
            break


if __name__ == '__main__':
    pos = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    main(pos)