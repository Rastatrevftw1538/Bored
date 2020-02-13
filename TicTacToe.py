

def Score(winner, score1, score2):
    p1 = score1
    p2 = score2
    print("Winner is ", winner, "\n")
    if winner == "p1":
        p1 += 1
    if winner == "p2":
        p2 += 1
    play_again = str(input("Play again?: y/n "))
    if play_again == "y":
        Game_Thing(p1, p2, True)
    if play_again == "n":
        Game_Thing(p1, p2, True)


def Game_Thing(score1, score2, game):
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]
    p1 = "X"
    p2 = "O"
    p1_score = score1
    p2_score = score2
    p1Turn = True
    p2Turn = False
    print("P1: ", p1_score, "\nP2: ", p2_score)
    if game == False:
        print("Thank you for playing!")
        quit()
    else:
        print("Welcome to TicTacToe!\n")
        print(board[0])
        print(board[1])
        print(board[2])
        while game == True:
            while p1Turn == True:
                try:
                    p1Select = int(input("P1, Enter a number from 1-9: "))
                except:
                    print("please put 1-9!")
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    break
                if type(p1Select) == int:
                    if p1Select <= 9 and p1Select >= 1:
                        if p1Select <= 3 and p1Select >= 1:
                            if board[0][p1Select-1] == p1 or board[0][p1Select-1] == p2:
                                print("Select another spot")
                                break
                            else:
                                board[0][p1Select - 1] = p1
                                p1Turn = False
                                p2Turn = True
                                continue
                        if p1Select <= 6 and p1Select >= 4:
                            if board[1][p1Select - 4] == p1 or board[1][p1Select - 4] == p2:
                                print("Select another spot")
                                break
                            else:
                                board[1][p1Select - 4] = p1
                                p1Turn = False
                                p2Turn = True
                                continue
                        if p1Select <= 9 and p1Select >= 7:
                            if board[2][p1Select-7] == p1 or board[2][p1Select-7] == p2:
                                print("Select another spot")
                                break
                            else:
                                board[2][p1Select - 7] = p1
                                p1Turn = False
                                p2Turn = True
                                continue
                    else:
                        print("please put 1-9!")
                        break
            while p2Turn == True:
                try:
                    p2Select = int(input("P2, Enter a number from 1-9: "))
                except:
                    print("please put 1-9!")
                    print(board[0])
                    print(board[1])
                    print(board[2])
                    break
                if type(p2Select) == int:
                    if p2Select <= 9 and p2Select >= 1:
                        if p2Select <= 3 and p2Select >= 1:
                            if board[0][p2Select-1] == p2 or board[0][p2Select-1] == p1:
                                print("Select another spot")
                                break
                            else:
                                board[0][p2Select - 1] = p2
                                p2Turn = False
                                p1Turn = True
                                continue
                        if p2Select <= 6 and p2Select >= 4:
                            if board[1][p2Select - 4] == p2 or board[1][p2Select - 4] == p1:
                                print("Select another spot")
                                break
                            else:
                                board[1][p2Select - 4] = p2
                                p2Turn = False
                                p1Turn = True
                                continue
                        if p2Select <= 9 and p2Select >= 7:
                            if board[2][p2Select-7] == p2 or board[2][p2Select-7] == p1:
                                print("Select another spot")
                                break
                            else:
                                board[2][p2Select - 7] = p2
                                p2Turn = False
                                p1Turn = True
                                continue
                    else:
                        print("please put 1-9!")
                        break
            for i in range(3):
                if board[i].count(p1) == 3:
                    Score("p1", p1_score, p2_score)
                    break
                if board[0][i] == p1:
                    if board[1][i] == p1 or board[1][1] == p1:
                        if board[2][i] == p1 or board[2][2] == p1:
                            Score("p1", p1_score, p2_score)
                            break
                elif board[i].count(p2) == 3:
                    Score("p2", p1_score, p2_score)
                    break
                elif board[0][i] == p2:
                    if board[1][i] == p2 or board[1][1] == p2:
                        if board[2][i] == p2 or board[2][2] == p2:
                            Score("p2", p1_score, p2_score)
                            break
            print(board[0])
            print(board[1])
            print(board[2])


Game_Thing(0, 0, True)
