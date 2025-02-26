import numpy as np

table = np.array([['a', 'b', 'c'],
                  ['d', 'e', 'f'],
                  ['g', 'h', 'i']])

player1 = input("Jogador 1(x), Digite o seu nome: ")
player2 = input("Jogador 2(o), Digite o seu nome: ")

def ganhou(args):
    if table[0,0] == args and table[0,1] == args and table[0,2] == args:
        return True
    elif table[1,0] == args and table[1,1] == args and table[1,2] == args:
        return True
    elif table[2,0] == args and table[2,1] == args and table[2,2] == args:
        return True
    elif table[0,0] == args and table[1,0] == args and table[2,0] == args:
        return True
    elif table[0,1] == args and table[1,1] == args and table[2,1] == args:
        return True
    elif table[0,2] == args and table[1,2] == args and table[2,2] == args:
        return True
    elif table[0,0] == args and table[1,1] == args and table[2,2] == args:
        return True
    elif table[0,2] == args and table[1,1] == args and table[2,0] == args:
        return True
    else:
        return False

for x in range(9):
    print(f'\n{table}')
    if x % 2 == 0 and x != 8:
        esc = input(f"\n{player1}, escolha sua posição: ")
        ind = np.where(table == esc.lower())
        table[ind] = "X"
        if ganhou("X"):
            print(f"\n{table}")
            print(f"\nParabéns {player1}, você venceu!")
            break
    elif x % 2 != 0 and x != 9:
        esc = input(f"\n{player2}, escolha sua posição: ")
        ind = np.where(table == esc.lower())
        table[ind] = "O"
        if ganhou("O"):
            print(f"\n{table}")
            print(f"\nParabéns {player2}, você venceu!")
            break
    elif x == 8:
        esc = input(f"\n{player1}, escolha sua posição: ")
        ind = np.where(table == esc.lower())
        table[ind] = "X"
        print(f"\n{table}")
        print(f"\n{player1} e {player2} empataram!")