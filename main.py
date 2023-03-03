'''
This is a chess program.
Authors: 
Ghosh, Trisha
Wang, Alex
'''

import chess
import defis
import utils

if __name__ == '__main__':

    player = True; # TODO player = 1 => white's turn; = 0 => black's turn
    board = chess.Board()

    utils.clear_terminal()
    utils.explain_UCI()

    while 1:
        # try to play a move
        # TODO check for valid move
        # TODO check that the correct player is making a move (black cannot move a white piece)
        # TODO check for valid en passant + castling
        # TODO check if game is over (i.e. from repetition, 50-move, dead position, etc.)
        try:
            if player:  # if the player is playing
                test_move = chess.Move.from_uci(input())
                board.push(test_move)
                player = 0
            else:       # if the AI is playing
                board.push(utils.AI_move(board))
                player = 1
        except chess.InvalidMoveError:
            print('Invalid Move, Try Again')