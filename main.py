

def table():
    print(spot[1] + ' | ' + spot[2] + ' | ' + spot[3])
    print(spot[4] + ' | ' + spot[5] + ' | ' + spot[6])
    print(spot[7] + ' | ' + spot[8] + ' | ' + spot[9])

def check(spot):
    o1 = spot[1]+spot[2]+spot[3]
    o2 = spot[4]+spot[5]+spot[6]
    o3 = spot[7]+spot[8]+spot[9]
    o4 = spot[1] + spot[4] + spot[7]
    o5 = spot[2] + spot[8] + spot[5]
    o6 = spot[3] + spot[6] + spot[9]
    o7 = spot[1] + spot[5] + spot[9]
    o8 = spot[7] + spot[5] + spot[3]
    if (o1 == 'XXX' or o2 == 'XXX' or o3 == 'XXX' or o4 == 'XXX' or
        o5 == 'XXX' or o6 == 'XXX' or o7 == 'XXX' or o8 == 'XXX')  or (o1 == 'OOO' or o2 == 'OOO'
        or o3 == 'OOO' or o4 == 'OOO' or o5 == 'OOO' or o6 == 'OOO' or o7 == 'OOO' or o8 == 'OOO'):
        return True
    else:
        return False



while True:
    spot = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    turn = 1

    table()
    while turn <= 9:
        if turn % 2 == 0:  # X turn
            a = int(input("CHOOSE A SPOT FOR X!! (1-9): "))
            if spot[a] != 'X' or spot[a] != 'O':
                spot[a] = 'X'
                turn += 1
                table()
                if check(spot):
                    print("\n X WINS!!! \n")
                    break
            else:
                print("SPACE ALREADY TAKEN!! TRY AGAIN!!")
        else:
            a = int(input("CHOOSE A SPOT FOR O!! (1-9): "))
            if spot[a] != 'X' or spot[a] != 'O':
                spot[a] = 'O'
                turn += 1
                table()
                if check(spot):
                    print("\n O WINS!! \n")
                    break
            else:
                print("SPACE ALREADY TAKEN!! TRY AGAIN!!")

    if turn >= 9:
        print("\n ITS A DRAW!!! \n")

    a = input("PLAY AGAIN?? (Y/N) : ")
    if a.upper() == 'N':
        break

print('TEST CHANGE')
print('BRANCH CHECK')


