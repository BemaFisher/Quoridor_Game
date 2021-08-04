# Author: Begaiym Fisher
# Date: 7/31/2021
# Description:

class Player:
    """Represents player. Class will store player's num, number of fences available, and location."""

    def __init__(self, player_num):
        """Initializes private data member's"""
        self._player_num = player_num
        self._num_of_fences = 10
        self._location = None  # not sure about this

    def get_player_num(self):
        """:returns player num"""
        return self._player_num

    def get_num_of_fences(self):
        """:returns number of fences player has"""
        return self._num_of_fences

    def get_location(self):
        """:returns location of the player."""
        return self._location

    def set_location(self):
        """ Sets player's location. CHANGE IT EVERY TIME PLAYER MOVES"""

    def count_fences(self, num_of_fences_used):
        """ Decrease the number of fences everytime player uses one"""
        self._num_of_fences -= num_of_fences_used


class QuoridorGame:
    """ class representing a game"""

    def __init__(self):
        """Initializes private variables"""
        self._game_status = "UNFINISHED"
        self._current_player = 'P1'  # since P1 takes the first turn
        self._board = [['|', ' 0', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P1', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 1', ' ', '  ', ' ', '  ', ' ', '  ', ' ', '  ', ' ', '  ', ' ', '  ', ' ', '  ', ' ',
                        '  ', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 2', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P1', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 3', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P1', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 4', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P1', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 5', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P1', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 6', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P1', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 7', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P1', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|'],
                       ['+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+', '  ', '+',
                        '  ', '+'],
                       ['|', ' 8', ' ', ' 1', ' ', ' 2', ' ', ' 3', ' ', 'P2', ' ', ' 5', ' ', ' 6', ' ', ' 7', ' ',
                        ' 8', '|']]

    #  ['+', '==', '+', '==', '+', '==', '+', '==', '+', '==', '+', '==', '+', '==', '+', '==', '+',
    #                         '==', '+']
    def print_board(self):
        """Prints board"""
        print('+ == + == + == + == + == + == + == + == + == +')
        for row in self._board:
            for slot in row:
                print(slot, end=" ")
            print()
        print('+ == + == + == + == + == + == + == + == + == +')

    def move_pawn(self, player, coord):
        """
        if the move is forbidden by the rule or blocked by the fence, return False
        if the move was successful or if the move makes the player win, return True
        if the game has been already won, return False
        """
        pass

    def play_fence(self, player, direction, coord):
        """
        if player has no fence left, or if the fence is out of the boundaries of the board, or if there is already a
        fence there and the new fence will overlap or intersect with the existing fence, return False.
        If the fence can be placed, return True.
        If it breaks the fair-play rule (and if you are doing the extra credit part), return exactly the string breaks
        the fair play rule.
        If the game has been already won, return False
        """
        pass

    def is_winner(self, player):
        """
        Returns True if that player has won and False if that player has not won.
        Check that by checking if player is on opponents base line
        """

    def player_turn(self, current_player):
        """ Switch turns. If current player is P1 then switch turn to P2 and vice versa"""


game_1 = QuoridorGame()
game_1.print_board()

# board = [
#     ['|', (0, 0), 'X ', 'X ', 'X ', 'P1 ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', (0, 1), 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', "(0, 2)", 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', 'X ', '|'],
#     ['|', 'X ', 'X ', 'X ', 'X ', 'P2 ', 'X ', 'X ', 'X ', 'X ', '|'],
#     [' ', '--', '--', '--', '--', '--', '--', '--', '--', '--']]
#
# val = "(0, 2)"
#
# for row in board:
#     for item in row:
#         if item == val:
#             print("it works")






##### "DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"
# Determining how to store the board.
# Initializing the board
# Determining how to track which player's turn it is to play right now.
# Determining how to validate a moving of the pawn.
# Determining how to validate placing of the fences.
# Determining how to keep track of fences on the board and off the board.
# Determining how to keep track of the pawn's position on the board.