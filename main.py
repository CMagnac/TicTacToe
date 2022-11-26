from random import randint

global STARTGAME

def display_board(board) -> str:
    tabl = "|"+"\t|"*3
    hyphl = ("+"+"-"*7)*3+"+"
    layer1 = [board[0][_] for _ in range(3)]
    layer2 = [board[1][_] for _ in range(3)]
    layer3 = [board[2][_] for _ in range(3)]
    val = lambda x: "|".ljust(4) + f"{x}".ljust(4)
    row1 = [hyphl,tabl,val(layer1[0])+val(layer1[1])+val(layer1[2])+"|",tabl,hyphl]
    row2 = [tabl,val(layer2[0])+val(layer2[1])+val(layer2[2])+"|",tabl,hyphl]
    row3 = [tabl,val(layer3[0])+val(layer3[1])+val(layer3[2])+"|",tabl,hyphl]
    board = [row1,row2,row3]
    for _ in range(3):
        print("\n".join(board[_]))

def make_list_of_free_fields(board) -> list:
    brwrow1,brwrow2,brwrow3 = [],[],[]
    for _ in board[0]:
        if isinstance(_,int):
            brwrow1.append((0,board[0].index(_)))
        else:
            brwrow1.append(None)
    for _ in board[1]:
        if isinstance(_,int):
            brwrow2.append((1,board[1].index(_)))
        else:
            brwrow2.append(None)
    for _ in board[2]:
        if isinstance(_,int):
            brwrow3.append((2,board[2].index(_)))
        else:
            brwrow3.append(None)
    return [brwrow1,brwrow2,brwrow3]

def draw_move(board) -> list:
    freeflds = make_list_of_free_fields(board)
    digits_key = [str(_) for _ in range(1,10)]
    start_bot = True
    while start_bot:
        bot_input = randint(1,9)
        d = dict(zip(digits_key,freeflds[0]+freeflds[1]+freeflds[2]))
        if bool(d[str(bot_input)]):
            crd = d[str(bot_input)]
            board[int(crd[0])][int(crd[1])] = "X"
            del d[str(bot_input)]
            display_board(board)
            start_bot = False
            return board
        else:
            start_bot = True
    
def enter_move(board) -> list:
    user_input = input("Enter a number or enter 'q' to quit : ")
    freeflds = make_list_of_free_fields(board)
    digits_key = [str(_) for _ in range(1,10)]
    if str(user_input) in digits_key:
        d = dict(zip(digits_key,freeflds[0]+freeflds[1]+freeflds[2]))
        if bool(d[str(user_input)]):
            crd = d[str(user_input)]
            board[int(crd[0])][int(crd[1])] = "O"
            del d[str(user_input)]
            display_board(board)
            return board
        else:
            print("Enter a correct number")
            return enter_move(board)
    elif str(user_input).lower() == 'q':
        exit()
    else:
        print("Enter a correct number")
        return enter_move(board)

def victory_for(board, sign=["XXX","OOO"]) -> str:
    row1 = ["".join(str(_)) for _ in board[0]]
    row2 = ["".join(str(_)) for _ in board[1]]
    row3 = ["".join(str(_)) for _ in board[2]]
    row1 = "".join(row1)
    row2 = "".join(row2)
    row3 = "".join(row3)
    result = row1 + row2 + row3
    rows_check = lambda x: [x[0:3],x[3:6],x[6:]]
    cols_check = lambda x: [x[0]+x[3]+x[6],x[1]+x[4]+x[7],x[2]+x[5]+x[8]]
    diags_check = lambda x: [x[0]+x[4]+x[-1],x[2]+x[4]+x[6]]
    result1 = rows_check(result)
    result2 = cols_check(result)
    result3 = diags_check(result)
    bot,user = sign[0],sign[1]
    if user in result1 or user in result2 or user in result3:
        print("User Win")
        exit()
    if bot in result1 or bot in result2 or bot in result3:
        print("Bot Win")
        exit()

def main(board):
    display_board(board)
    STARTGAME = True
    while STARTGAME:
        enter_move(board)
        draw_move(board)
        victory_for(board)

if __name__ == "__main__":
    board = [[1,2,3],[4,"X",6],[7,8,9]]
    main(board)