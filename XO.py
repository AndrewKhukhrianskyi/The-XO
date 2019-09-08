board = list(range(1,10))
X = "X"
O = "O"
# Доска
def draw_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t","----------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t","----------")
    print("\n\t", board[6], "|", board[7], "|", board[8],"\n")

# Алгоритм 
def move(player): 
    while True:
        try:
            player_choose = int(input(f" Куда поставим {player}? Вводи значение от 1 до 9 "))
        except:
            print(' Ошибка - введена буква\слово или не та цифра ' )
            continue
        if 0 < player_choose < 10:
            if (str(board[player_choose-1]) not in "XO"):
                board[player_choose-1] = player
                break
            else:
                print(' Клетка занята ')
               


def check_win(board):
    win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for win_zone in win:
        if board[win_zone[0]] == board[win_zone[1]] == board[win_zone[2]]:
            return board[win_zone[0]]
    return False

def main(board,X,O):
    count = True
    value = 0
    draw_board(board) 
    for i in range(9):
        
        if count == True:
            move("X")
            count = not count
            draw_board(board)

        else:
            move("O")
            count = not count
            draw_board(board)

        if check_win(board):
            print(f"{check_win(board)}, победил!")
            break
    else:
        print("Ничья")


       
    

main(board,X,O)

                
                
            
        
        
        

