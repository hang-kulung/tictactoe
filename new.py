def table():
    global spots, order, limit, turn
    turn = 1
    spots = []
    order = int(input('ENTER THE ORDER OF MATRIX: '))
    limit = order * order
    rows = list(range(order))

    for i in range(order):
        spots.append(rows)


def table_display():
    colunm = 0
    for i in spots:
        for j in range(order):
            if i[j] == 'x' or i[j] == 'o':
                print(' | ' + i[j] + ' | ', end=' ')
            else:
                print(' | ' + str(colunm + j + 1) + ' | ', end=' ')
        colunm += order
        print()

table()
table_display()



while turn <= limit:
    if turn%2 == 0:
        a = int(input(f'Enter Place for x-player (1-{limit}): '))
        c = (a-1) % order
        r = int((a-1)/order)


        if spots[r][c] != 'x' or spots[r][c] != 'o':
            spots[r][c] = 'x'
            turn += 1
            table_display()
        else:
            print('PLACE ALREADY TAKEN !! TRY AGAIN!!')

    else:
        a = int(input(f'Enter Place for o-player (1-{limit}): '))
        if spots[a-1] != 'x' or spots[a - 1] != 'o':
            spots[a-1] = '0'
            turn += 1
            table_display()
        else:
            print('PLACE ALREADY TAKEN !! TRY AGAIN!!')



