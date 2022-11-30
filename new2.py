import random
import time

#to display new table / also reset table
def table():
    global spots, order, limit, turn, empty_spots, comp
    turn = 0
    order = int(input('\n ENTER THE ORDER OF MATRIX: '))
    a = input('DO YOU WANT PLAY AGAINST COMPUTER? (Y/N): ')
    if a.upper() == 'Y':
        comp = True
    else:
        comp = False
    limit = order * order
    spots = list(range(limit))
    empty_spots = list(range(limit))

#to display current table
def table_display():
    spot = 1
    for i in range(order):
        for j in range(order):
            if spots[spot - 1] == 'x' or spots[spot -1] == 'o':
                print(' | ' + spots[spot -1] + ' | ', end=' ')
            else:
                print(' | ' + str(spot) + ' | ', end=' ')
            spot += 1
        print()

#For checking winner
def winner():

    #for checking row
    for i in range(order):
        row_check = ''
        for j in range(order):
            spot = (order * i) + j
            row_check = row_check + str(spots[spot])
        if row_check == 'x' * order or row_check == 'o'*order:
            return True
            break
    #for checking column
    for i in range(order):
        column_check = ''
        for j in range(order):
            spot = i + (order * j)
            column_check = column_check + str(spots[spot])
        if column_check == 'x' * order or column_check == 'o' * order:
            return True
            break
    #for main diagonal
    mdiagonal_check = ''
    for i in range(order):
        spot = (order * i) + i
        mdiagonal_check = mdiagonal_check + str(spots[spot])

    if mdiagonal_check == 'x' * order or mdiagonal_check == 'o' * order:
        return True

    #for second diagonal
    sdiagonal_check = ''
    j = order - 1
    for i in range(order):
        spot = (order * i) + j
        j -= 1
        sdiagonal_check = sdiagonal_check + str(spots[spot])
    if sdiagonal_check == 'x' * order or sdiagonal_check == 'o' * order:
        return True


while True:
    table()
    table_display()

    while turn < limit:
        if turn % 2 == 0:
            spot = int(input(f'Enter Place for x-player (1-{limit}): '))

            if spot - 1 in empty_spots:
                spots[spot - 1] = 'x'
                empty_spots.remove(spot - 1)
                turn += 1
                table_display()
            else:
               print('PLACE ALREADY TAKEN !! TRY AGAIN!!')
            if winner():
                print("\n x-player wins!!")
                break

        elif turn % 2 != 0 and comp:
            time.sleep(1)
            print()
            spot = random.choice(empty_spots)
            spots[spot] = 'o'
            empty_spots.remove(spot)
            turn += 1
            table_display()
            print()
            if winner():
                print("\n o-player wins!!")
                break

        else:
            spot = int(input(f'Enter Place for o-player (1-{limit}): '))

            if spot - 1 in empty_spots:
                spots[spot - 1] = 'o'
                empty_spots.remove(spot - 1)
                turn += 1
                table_display()
            else:
                print("PLACE ALREADY TAKEN !! TRY AGAIN!!")

            if winner():
                print("\n o-player wins!!")
                break

    if len(empty_spots) == 0:
        print("\n DRAW!!")
    replay = input('\n DO YOU WANNA PLAY AGAIN? (Y/N): ')
    if replay.upper() == 'N':
        break