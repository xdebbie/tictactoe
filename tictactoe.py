from flask import Flask, request, abort
app = Flask(__name__)

# Accepted characters
char_list = ["o", "x", " "]
# Initialise boardArray
boardArray = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


@app.route('/', methods=['GET'])
def TicTacToe():
    # Retrieve the 'board' parameter
    board = request.args.get("board", None)
    print(f"Received {board}")
    # Check whether a board was received
    if not board:
        print("No board was found, please send something.")
        abort(400)
    else:
        # If there's a board, check whether the board sent is valid
        if isValid(boardArray) == True:
            # Check whether there's a victory
            if victory(boardArray, board) == True:
                return "".join(board)
            else:
                # If the game is not over yet and it's the bot's turn, make a move and show the result. Else, show the current board since it's the player's turn.
                if botsTurn(board) == True:
                    return botMove(boardArray)
                else:
                    return "".join(board)


def isValid(boardArray):
    board = request.args.get("board", None)
    boardArray = list(board)
    error = False
    # Check whether the board is valid (contains the accepted chars and it has 9 chars)
    matched_list = [characters in char_list for characters in board]
    string_contains_chars = all(matched_list)
    if string_contains_chars == True and len(board) == 9:
        # Check whether there are 2 winners
        if board.count('x') >= 3 and board.count('o') >= 3:
            if set(boardArray[0:3]) == set(['o']) and set(boardArray[3:6]) == set(['x']):
                error = True
            elif set(boardArray[0:3]) == set(['o']) and set(boardArray[6:9]) == set(['x']):
                error = True
            elif set(boardArray[3:6]) == set(['o']) and set(boardArray[0:3]) == set(['x']):
                error = True
            elif set(boardArray[3:6]) == set(['o']) and set(boardArray[6:9]) == set(['x']):
                error = True
            elif set(boardArray[6:9]) == set(['o']) and set(boardArray[0:3]) == set(['x']):
                error = True
            elif set(boardArray[6:9]) == set(['o']) and set(boardArray[3:6]) == set(['x']):
                error = True
            elif all(item == 'o' for item in boardArray[0:7:3]) and all(item == 'x' for item in boardArray[1:8:3]):
                error = True
            elif all(item == 'o' for item in boardArray[0:7:3]) and all(item == 'x' for item in boardArray[2:9:3]):
                error = True
            elif all(item == 'o' for item in boardArray[1:8:3]) and all(item == 'x' for item in boardArray[0:7:3]):
                error = True
            elif all(item == 'o' for item in boardArray[1:8:3]) and all(item == 'x' for item in boardArray[2:9:3]):
                error = True
            elif all(item == 'o' for item in boardArray[2:9:3]) and all(item == 'x' for item in boardArray[0:7:3]):
                error = True
            elif all(item == 'o' for item in boardArray[2:9:3]) and all(item == 'x' for item in boardArray[1:8:3]):
                error = True
        if error == True:
            print(f"The board is not valid. There are 2 winners.")
            abort(400)
        else:
            botsTurn(board)
            print(f"This is the new board in array format: {boardArray}")
            return True
    else:
        print(
            f"The board is NOT valid! The board can only have 'x', 'o' or ' '. The board size is 9 characters. The value submitted is: {board} and there are {len(board)} characters.")
        abort(400)


def victory(boardArray, board):
    boardArray = list(board)
    # Check whether there was a victory if one of the 8 winning combinations are 'ooo' or 'xxx', excluding the case where there are 3 empty slots '+++'
    numberOfPieces = board.count('x') + board.count('o')
    if numberOfPieces >= 5:
        if boardArray[0] == boardArray[1] == boardArray[2] and boardArray[0] != ' ':
            if boardArray[0] == 'o':
                print("You lost!")
                return True
            elif boardArray[0] == 'x':
                print("You won!")
                return True
        elif boardArray[3] == boardArray[4] == boardArray[5] and boardArray[3] != ' ':
            if boardArray[3] == 'o':
                print("You lost!")
                return True
            elif boardArray[3] == 'x':
                print("You won!")
                return True
        elif boardArray[6] == boardArray[7] == boardArray[8] and boardArray[6] != ' ':
            if boardArray[6] == 'o':
                print("You lost!")
                return True
            elif boardArray[6] == 'x':
                print("You won!")
                return True
        elif boardArray[0] == boardArray[3] == boardArray[6] and boardArray[0] != ' ':
            if boardArray[0] == 'o':
                print("You lost!")
                return True
            elif boardArray[0] == 'x':
                print("You won!")
                return True
        elif boardArray[1] == boardArray[4] == boardArray[7] and boardArray[1] != ' ':
            if boardArray[1] == 'o':
                print("You lost!")
                return True
            elif boardArray[1] == 'x':
                print("You won!")
                return True
        elif boardArray[2] == boardArray[5] == boardArray[8] and boardArray[2] != ' ':
            if boardArray[2] == 'o':
                print("You lost!")
                return True
            elif boardArray[2] == 'x':
                print("You won!")
                return True
        elif boardArray[0] == boardArray[4] == boardArray[8] and boardArray[0] != ' ':
            if boardArray[0] == 'o':
                print("You lost!")
                return True
            elif boardArray[0] == 'x':
                print("You won!")
                return True
        elif boardArray[2] == boardArray[4] == boardArray[6] and boardArray[2] != ' ':
            if boardArray[2] == 'o':
                print("You lost!")
                return True
            elif boardArray[2] == 'x':
                print("You won!")
                return True
        else:
            return False
    else:
        print("There aren't enough moves for a winner yet...")
        return False


def botsTurn(board):
    board = request.args.get("board", None)
    # Check whether it's the bot's turn
    if board.count('x') == board.count('o') or board.count('x') - board.count('o') == 1:
        print(
            f"There are {board.count('x')} Xs and {board.count('o')} Os in the board. It's the bot's turn.")
        return True
    # Check whether it's the player's turn
    elif board.count('o') - board.count('x') == 1:
        print(
            f"There are {board.count('x')} Xs and {board.count('o')} Os in the board. It's the player's turn.")
        return False
    # If there's any other situation, then the board is invalid
    else:
        print(
            f"The board is not valid. There are {board.count('x')} Xs and {board.count('o')} Os in the board.")
        abort(400)


def botMove(boardArray):
    board = request.args.get("board", None)
    boardArray = list(board)
    print("The bot will play...")
    print("Board before:")
    print(f"{boardArray[0:3]}")
    print(f"{boardArray[3:6]}")
    print(f"{boardArray[6:9]}")
    # WIN strategy: check whether there are 2 'o's in a potential winning position and go for the win.
    if set((boardArray[0], boardArray[1])) == set(['o']) and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif set((boardArray[0], boardArray[2])) == set(['o']) and boardArray[1] == ' ':
        boardArray[1] = 'o'
    elif set((boardArray[0], boardArray[3])) == set(['o']) and boardArray[6] == ' ':
        boardArray[6] = 'o'
    elif set((boardArray[0], boardArray[4])) == set(['o']) and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif set((boardArray[0], boardArray[6])) == set(['o']) and boardArray[3] == ' ':
        boardArray[3] = 'o'
    elif set((boardArray[0], boardArray[8])) == set(['o']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[1], boardArray[2])) == set(['o']) and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif set((boardArray[1], boardArray[4])) == set(['o']) and boardArray[7] == ' ':
        boardArray[7] = 'o'
    elif set((boardArray[1], boardArray[7])) == set(['o']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[2], boardArray[4])) == set(['o']) and boardArray[6] == ' ':
        boardArray[6] = 'o'
    elif set((boardArray[2], boardArray[5])) == set(['o']) and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif set((boardArray[2], boardArray[6])) == set(['o']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[2], boardArray[8])) == set(['o']) and boardArray[5] == ' ':
        boardArray[5] = 'o'
    elif set((boardArray[3], boardArray[4])) == set(['o']) and boardArray[5] == ' ':
        boardArray[5] = 'o'
    elif set((boardArray[3], boardArray[5])) == set(['o']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[3], boardArray[6])) == set(['o']) and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif set((boardArray[4], boardArray[5])) == set(['o']) and boardArray[3] == ' ':
        boardArray[3] = 'o'
    elif set((boardArray[4], boardArray[6])) == set(['o']) and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif set((boardArray[4], boardArray[7])) == set(['o']) and boardArray[1] == ' ':
        boardArray[1] = 'o'
    elif set((boardArray[4], boardArray[8])) == set(['o']) and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif set((boardArray[5], boardArray[8])) == set(['o']) and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif set((boardArray[6], boardArray[7])) == set(['o']) and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif set((boardArray[6], boardArray[8])) == set(['o']) and boardArray[7] == ' ':
        boardArray[7] = 'o'
    elif set((boardArray[7], boardArray[8])) == set(['o']) and boardArray[6] == ' ':
        boardArray[6] = 'o'
    # BLOCK strategy: check whether there are 2 'x's in a potential winning position and block the move.
    elif set((boardArray[0], boardArray[1])) == set(['x']) and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif set((boardArray[0], boardArray[2])) == set(['x']) and boardArray[1] == ' ':
        boardArray[1] = 'o'
    elif set((boardArray[0], boardArray[3])) == set(['x']) and boardArray[6] == ' ':
        boardArray[6] = 'o'
    elif set((boardArray[0], boardArray[4])) == set(['x']) and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif set((boardArray[0], boardArray[6])) == set(['x']) and boardArray[3] == ' ':
        boardArray[3] = 'o'
    elif set((boardArray[0], boardArray[8])) == set(['x']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[1], boardArray[2])) == set(['x']) and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif set((boardArray[1], boardArray[4])) == set(['x']) and boardArray[7] == ' ':
        boardArray[7] = 'o'
    elif set((boardArray[1], boardArray[7])) == set(['x']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[2], boardArray[4])) == set(['x']) and boardArray[6] == ' ':
        boardArray[6] = 'o'
    elif set((boardArray[2], boardArray[5])) == set(['x']) and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif set((boardArray[2], boardArray[6])) == set(['x']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[2], boardArray[8])) == set(['x']) and boardArray[5] == ' ':
        boardArray[5] = 'o'
    elif set((boardArray[3], boardArray[4])) == set(['x']) and boardArray[5] == ' ':
        boardArray[5] = 'o'
    elif set((boardArray[3], boardArray[5])) == set(['x']) and boardArray[4] == ' ':
        boardArray[4] = 'o'
    elif set((boardArray[3], boardArray[6])) == set(['x']) and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif set((boardArray[4], boardArray[5])) == set(['x']) and boardArray[3] == ' ':
        boardArray[3] = 'o'
    elif set((boardArray[4], boardArray[6])) == set(['x']) and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif set((boardArray[4], boardArray[7])) == set(['x']) and boardArray[1] == ' ':
        boardArray[1] = 'o'
    elif set((boardArray[4], boardArray[8])) == set(['x']) and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif set((boardArray[5], boardArray[8])) == set(['x']) and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif set((boardArray[6], boardArray[7])) == set(['x']) and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif set((boardArray[6], boardArray[8])) == set(['x']) and boardArray[7] == ' ':
        boardArray[8] = 'o'
    elif set((boardArray[7], boardArray[8])) == set(['x']) and boardArray[6] == ' ':
        boardArray[6] = 'o'
    # FORK strategy: create a fork if possible by placing a piece in a position in which 2 ways to win are created
    # elif set((boardArray[0], boardArray[8])) == set(['o']) and set((boardArray[4], boardArray[6])) == set(['x']) and boardArray[2] == ' ':
    #     boardArray[2] = 'o'
    elif boardArray[0] == 'o' and boardArray[2] == ' ' and boardArray[4] == 'x' and boardArray[6] == 'x' and boardArray[8] == 'o':
        boardArray[2] = 'o'
    elif boardArray[0] == 'o' and boardArray[4] == 'o' and boardArray[6] == ' ' and boardArray[7] == 'x' and boardArray[8] == 'x':
        boardArray[6] = 'o'
    elif boardArray[0] == 'o' and boardArray[2] == 'x' and boardArray[4] == 'x' and boardArray[6] == ' ' and boardArray[8] == 'o':
        boardArray[6] = 'o'
    elif boardArray[0] == 'o' and boardArray[2] == ' ' and boardArray[4] == 'x' and boardArray[7] == 'x' and boardArray[8] == 'o':
        boardArray[2] = 'o'
    elif boardArray[0] == 'o' and boardArray[1] == 'x' and boardArray[4] == 'x' and boardArray[6] == ' ' and boardArray[8] == 'o':
        boardArray[6] = 'o'
    elif boardArray[0] == 'o' and boardArray[4] == 'x' and boardArray[5] == 'x' and boardArray[6] == ' ' and boardArray[8] == 'x':
        boardArray[6] = 'o'
    elif boardArray[0] == 'o' and boardArray[2] == ' ' and boardArray[3] == 'x' and boardArray[4] == 'x' and boardArray[8] == 'o':
        boardArray[2] = 'o'
    elif boardArray[1] == 'o' and boardArray[0] == ' ' and boardArray[3] == 'o' and boardArray[4] == 'x' and boardArray[8] == 'x':
        boardArray[0] = 'o'
    elif boardArray[1] == 'o' and boardArray[2] == ' ' and boardArray[4] == 'x' and boardArray[5] == 'o' and boardArray[6] == 'x':
        boardArray[2] = 'o'
    elif boardArray[2] == 'o' and boardArray[1] == 'x' and boardArray[4] == 'x' and boardArray[6] == 'o' and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif boardArray[2] == 'o' and boardArray[4] == 'o' and boardArray[6] == 'x' and boardArray[7] == 'x' and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif boardArray[2] == 'o' and boardArray[0] == ' ' and boardArray[4] == 'x' and boardArray[6] == 'o' and boardArray[8] == 'x':
        boardArray[0] = 'o'
    elif boardArray[2] == 'o' and boardArray[0] == 'x' and boardArray[4] == 'x' and boardArray[6] == 'o' and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif boardArray[2] == 'o' and boardArray[0] == ' ' and boardArray[4] == 'x' and boardArray[6] == 'o' and boardArray[7] == 'x':
        boardArray[0] = 'o'
    elif boardArray[2] == 'o' and boardArray[0] == ' ' and boardArray[4] == 'x' and boardArray[5] == 'x' and boardArray[6] == 'o':
        boardArray[0] = 'o'
    elif boardArray[2] == 'o' and boardArray[3] == 'x' and boardArray[4] == 'x' and boardArray[6] == 'o' and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif boardArray[3] == 'o' and boardArray[2] == 'x' and boardArray[4] == 'x' and boardArray[6] == ' ' and boardArray[7] == 'o':
        boardArray[6] = 'o'
    elif boardArray[4] == 'o' and boardArray[0] == 'x' and boardArray[1] == 'x' and boardArray[2] == ' ' and boardArray[8] == 'o':
        boardArray[2] = 'o'
    elif boardArray[4] == 'o' and boardArray[0] == ' ' and boardArray[1] == 'x' and boardArray[2] == 'x' and boardArray[6] == 'o':
        boardArray[0] = 'o'
    elif boardArray[5] == 'o' and boardArray[0] == 'x' and boardArray[4] == 'x' and boardArray[7] == 'o' and boardArray[8] == ' ':
        boardArray[8] = 'o'
    # BLOCK A FORK strategy: if there's a possible incoming fork for the opponent, block it
    elif boardArray[4] == 'o' and boardArray[0] == 'x' and boardArray[8] == 'x' and boardArray[1] == ' ':
        boardArray[1] = 'o'
    elif boardArray[4] == 'o' and boardArray[0] == 'x' and boardArray[8] == 'x' and boardArray[3] == ' ':
        boardArray[3] = 'o'
    elif boardArray[4] == 'o' and boardArray[0] == 'x' and boardArray[8] == 'x' and boardArray[5] == ' ':
        boardArray[5] = 'o'
    elif boardArray[4] == 'o' and boardArray[0] == 'x' and boardArray[8] == 'x' and boardArray[7] == ' ':
        boardArray[7] = 'o'
    elif boardArray[4] == 'o' and boardArray[2] == 'x' and boardArray[6] == 'x' and boardArray[1] == ' ':
        boardArray[1] = 'o'
    elif boardArray[4] == 'o' and boardArray[2] == 'x' and boardArray[6] == 'x' and boardArray[3] == ' ':
        boardArray[3] = 'o'
    elif boardArray[4] == 'o' and boardArray[2] == 'x' and boardArray[6] == 'x' and boardArray[5] == ' ':
        boardArray[5] = 'o'
    elif boardArray[4] == 'o' and boardArray[2] == 'x' and boardArray[6] == 'x' and boardArray[7] == ' ':
        boardArray[7] = 'o'
    elif boardArray[4] == 'x' and boardArray[0] == 'o' and boardArray[8] == 'x' and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif boardArray[4] == 'x' and boardArray[0] == 'o' and boardArray[8] == 'x' and boardArray[6] == ' ':
        boardArray[6] = 'o'
    elif boardArray[4] == 'x' and boardArray[0] == 'x' and boardArray[8] == 'o' and boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif boardArray[4] == 'x' and boardArray[0] == 'x' and boardArray[8] == 'o' and boardArray[6] == ' ':
        boardArray[6] = 'o'
    elif boardArray[4] == 'x' and boardArray[2] == 'o' and boardArray[6] == 'x' and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif boardArray[4] == 'x' and boardArray[2] == 'o' and boardArray[6] == 'x' and boardArray[8] == ' ':
        boardArray[8] = 'o'
    elif boardArray[4] == 'x' and boardArray[2] == 'x' and boardArray[6] == 'o' and boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif boardArray[4] == 'x' and boardArray[2] == 'x' and boardArray[6] == 'o' and boardArray[8] == ' ':
        boardArray[8] = 'o'
    # CENTER strategy: as it's a bot vs a potential imperfect player (human), playing a corner as a first move is better than playing center. So it will play a corner
    elif board.count('o') == 0 and board.count('x') == 0:
        boardArray[0] = 'o'
    # OPPOSITE CORNER strategy: if the opponent is in the corner, the bot plays the opposite corner
    elif board.count('x') == 1 and board.count('o') == 0:
        if boardArray[0] == 'x':
            boardArray[8] = 'o'
        elif boardArray[2] == 'x':
            boardArray[6] = 'o'
        elif boardArray[6] == 'x':
            boardArray[2] = 'o'
        elif boardArray[8] == 'x':
            boardArray[0] = 'o'
    # EMPTY CORNER strategy: the bot plays in a corner square
    elif boardArray[0] == ' ':
        boardArray[0] = 'o'
    elif boardArray[2] == ' ':
        boardArray[2] = 'o'
    elif boardArray[6] == ' ':
        boardArray[6] = 'o'
    elif boardArray[8] == ' ':
        boardArray[8] = 'o'
    # EMPTY SIDE strategy: the bot plays in a middle square
    elif boardArray[1] == ' ':
        boardArray[1] = 'o'
    elif boardArray[3] == ' ':
        boardArray[3] = 'o'
    elif boardArray[5] == ' ':
        boardArray[5] = 'o'
    elif boardArray[7] == ' ':
        boardArray[7] = 'o'

    print("Board after:")
    print(f"{boardArray[0:3]}")
    print(f"{boardArray[3:6]}")
    print(f"{boardArray[6:9]}")
    return "".join(boardArray)


if __name__ == '__main__':
    # Allow for parallel requests
    app.run(threaded=True, port=5000)
