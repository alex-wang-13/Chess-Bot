'''
This is a chess program.
Authors: 
Ghosh, Trisha
Wang, Alex
'''

import chess
import defis
import utils

# START
if 0: #__name__ == '__main__':

    # Explaining the rules.
    # useless: Todo but not urgent: fix this -> utils.clear_terminal()
    utils.explain_UCI()

    # TODO create functionality for AI to play as white
    player = 1 # player = 1 => white's turn; = 0 => black's turn
    board = chess.Board()
    # print the board
    print(board)
    print(defis.BOARD_BREAK)

    while 1:
        # try to play a move
        # TODO check if game is over (i.e. from repetition, 50-move, dead position, etc.)
        try:
            if player:  # if the player is playing
                move: chess.Move = utils.get_move(board)
                if move == 'undo':
                    board.pop()
                else:
                    board.push(move)
                # alternate to the other player's turn
                player = 0
            else:       # if the AI is playing
                # TODO remove this placeholder and add AI move
                move: chess.Move = utils.get_move(board)
                if move == 'undo':
                    board.pop()
                else:
                    board.push(move)
                    # for later: board.push(utils.AI_move(board))
                # alternate to the other player's turn
                player = 1
        except chess.InvalidMoveError:
            print('Invalid Move, Try Again - Should Not Reach Here')
        
        # check if game is over
        utils.check_result(board)

        # print the board after the move
        print(board)
        print(defis.BOARD_BREAK)

else:
    board = chess.Board()
    # print the board
    # board.push(chess.Move.from_uci("g1f3")) # first move
    # board.push(chess.Move.from_uci("g8f6"))
    # board.push(chess.Move.from_uci("f3g1"))
    # board.push(chess.Move.from_uci("f6g8")) # first repetition
    # board.push(chess.Move.from_uci("g1f3"))
    # board.push(chess.Move.from_uci("g8f6"))
    # board.push(chess.Move.from_uci("f3g1"))
    # board.push(chess.Move.from_uci("f6g8")) # second repetition (third time this position occurred)

    for x in range(2):
        board.push(chess.Move.from_uci("g1f3")) # first move
        board.push(chess.Move.from_uci("g8f6"))
        board.push(chess.Move.from_uci("f3g1"))
        board.push(chess.Move.from_uci("f6g8"))
        utils.check_result(board)

    # pawn_mask = board.pieces(chess.PAWN, chess.WHITE).mask
    
    # prints out a 64-bit representation of the positions of the white pawns
    # print(bin(pawn_mask)[2:].zfill(64))