# -*- coding: utf-8 -*-
"""
@Time    : 26/12/2020 02:01
@Author  : Colm Keyes
@Email   : keyesco@tcd.ie
@File    : Chess_pgn_player_class_test
"""

import numpy as np
import chess.pgn
from chessboard import display
import pandas as pd
import time
import PySimpleGUI as sg


class Chess_pgn_player_class:


    def __init__(self): #, game_a, board, coordinates, mainline_moves ):
        self.game_a = chess.pgn.read_game(open("C:/Users/Lord Colm/Desktop/Chess_CNN/December4.pgn"))
        self.board = self.game_a.board()
        self.board_behind = self.game_a.board()
        self.coordinates = [(x + 1, y + 1) for x in range(8) for y in range(8)]
        self.mainline_moves = list(self.game_a.mainline_moves())
        self.d=2
        self.move_number = 0


    def move(self, mainline_move):
        self.board.push(mainline_move)


    def attack_squares_coords(self):
        total_square_attackers_dict = []
        total_square_attackers_dict_basic = []
        attackers_white = []
        attackers_black = []
        for square in chess.SQUARES:

            attackers_white_bool = chess.SquareSet.tolist(self.board.attackers(chess.WHITE, square))
            attackers_black_bool = chess.SquareSet.tolist(self.board.attackers(chess.BLACK, square))
            total_square_attackers = np.sum(np.count_nonzero(attackers_white_bool) + np.count_nonzero(attackers_black_bool) * -1)
            total_square_attackers_normalized = np.round((total_square_attackers + 6) / (7 + 6),
                                                         2)
            attackers_black.append(attackers_black_bool)
            attackers_white.append(attackers_white_bool)

            total_square_attackers_dict_basic.append([total_square_attackers])
            total_square_attackers_dict.append([total_square_attackers_normalized])

        attack_squares_coords = pd.DataFrame(data=(total_square_attackers_dict, self.coordinates))

        return attack_squares_coords


    def main(self):
        print("main start")
        display.start(self.board.fen())
        while not display.checkForQuit():
            for mainline_move in self.mainline_moves:

                print("board move", mainline_move)
                print("move number", self.move_number)

                if self.move_number >= 1:
                    self.board = board_saved
                attack_squares_coords = self.attack_squares_coords()

                board_saved = self.board
                self.board = self.board_behind
                attack_squares_coords_behind = self.attack_squares_coords()
                self.board = board_saved

                attack_squares_coords1 = attack_squares_coords.transpose()
                attack_squares_coords1_behind = attack_squares_coords_behind.transpose()
                display.update(self.board.fen(), attack_squares_coords1, attack_squares_coords1_behind)

                self.move(mainline_move)
                if self.move_number >= 1:
                    self.board_behind.push(self.mainline_moves[self.move_number - 1])
                    #print("board behind move",self.mainline_moves[self.move_number - 1])

                self.move_number += 1




            display.terminate()


if __name__ == "__main__":
    # execute only if main as a script
    player = Chess_pgn_player_class_test()
    player.main()

Chess_pgn_player_class_test