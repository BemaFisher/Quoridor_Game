# Author: Begaiym Fisher
# Date: 7/31/2021
# Description:

class Player:
    """Represents player. Class will store player's num(1 or 2), number of fences available(starts with 10), and
    location. It will have getters for all the data members. It has a method for keeping track of fences available for
    player.
    It also will have inheritance relationship with Quoridor class (Quoridor has-a player) since we need to keep track
    of players."""

    def __init__(self, player_num):
        """Initializes private data members"""
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

    def set_location(self, location):
        """ Sets player's location to given location. CHANGE IT EVERY TIME PLAYER MOVES"""
        self._location = location

    def count_fences(self, num_of_fences_used):
        """ Decrease the number of fences everytime player uses one by subtracting number of fences used. """
        self._num_of_fences -= num_of_fences_used


class QuoridorGame:
    """ Class representing the game. In this class,
    - I will be storing and representing the board.
     - print the board with method
     - determine validity of the move whether it is pawn or the fence with is_valid_move method
     - record the move within move_pawn and play_fence methods
     - determine any edge cases and return False when I find one
     - determine the winner with is_winner method
     - keep track of whose turn it is with player turn method"""

    def __init__(self):
        """Initializes private variables"""
        self._game_status = "UNFINISHED"
        self._current_player = 'P1'  # since P1 takes the first turn
        self._board = [['00', '10', '20', '30', 'P1', '50', '60', '70', '80'],
                       ['01', '--', '--', '--', '--', '--', '--', '--', '--'],
                       ['02', '--', '--', '--', '--', '--', '--', '--', '--'],
                       ['03', '--', '--', '--', '--', '--', '--', '--', '--'],
                       ['04', '--', '--', '--', '--', '--', '--', '--', '--'],
                       ['05', '--', '--', '--', '--', '--', '--', '--', '--'],
                       ['06', '--', '--', '--', '--', '--', '--', '--', '--'],
                       ['07', '--', '--', '--', '--', '--', '--', '--', '--'],
                       ['08', '--', '--', '--', 'P2', '--', '--', '--', '--'],
                       ]

    def get_current_player(self):
        """:returns current player"""
        return self._current_player

    def set_current_player(self, opponent_player):
        """ Sets current payer player. Set it to the opponent player everytime current player
        has made a successful move. """
        self._current_player = opponent_player

    def get_game_status(self):
        """:returns status of the game"""
        return self._game_status

    def set_game_status(self, status):
        """ Sets status of the game. CHANGE TO 'WIN' IF MOVE CAUSED WIN"""
        self._game_status = status

    def print_board(self):
        """Prints board"""
        print('0x', '1x', '2x', '3x', '4x', '5x', '6x', '7x', '8x')
        print("--------------------------")
        for row in self._board:
            for slot in row:
                print(slot, end=" ")
            print()
        print("--------------------------")

    def is_valid_move_pawn(self, coord):
        """ Takes the coordinates that pawns wants to move as a parameter and checks if it's within the bounds.
        Returns true if move is legal and False otherwise."""
        pass

    def is_valid_move_fence(self, direction, coord):
        """ Takes the direction and coordinates of where the fence needs to be placed and checks if the move is within
        the bounds. Returns true if move is legal and False otherwise."""
        pass

    def lookup_player_from_num(self, player_num):
        """ Take player's number and return Player object"""
        pass

    def players_baseline(self, player_num):
        """ returns each player's baseline"""
        pass

    def fence_placement(self, direction, coord):
        """ Records every fence's placement on the board which will help to determine if fence placement is valid
        (because we can't place fences on top of each other) and
        if fence is obstructing pawn's move."""
        pass

    def move_pawn(self, player, coord):
        """
        if the move is forbidden by the rule or blocked by the fence, return False
        if the move was successful or if the move makes the player win, record it and return True
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
        pass

    def opponent_player(self, current_player):
        """ Determine opponent player. If P1 is current player then return P2 as opponent and vice versa"""
        pass


# game_1 = QuoridorGame()
# game_1.print_board()

# #### "DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"

# -----Determining how to store the board.-----
# I will be storing my board in list of lists which I initialized in the init method of the QuoridorGame class.
# In that board, I will keep track pawns and where they are moving and validating pawn's moves. In separate method,
# I will be tracking where all the fences are placed, inside that method I will also see if the move is valid.

# -----Initializing the board.-----
# I initialized my board in the init method of QuoridorGame class and print it in print_board method in QuoridorGame
# class.

# -----Determining how to track which player's turn it is to play right now.-----
# I have current_player data member in the QuoridorGame class and also have set_current_player method.
# At first, player is initialized to P1 but then everytime a player makes a successful move I will update current player
# through set_current_player method.

# -----Determining how to validate a moving of the pawn.-----
# After checking for things like player's turn, game status I will check if the pawn is within bounds with is
# valid_move_pawn method. I will also check if the destination coord is empty within move_pawn methods. If all is clear,
# record the move in move_pawn.

# -----Determining how to validate placing of the fences.-----
# Similarly to validating pawn's move, I will check for same edge cases but I have separate method called
# is_valid_move_fence for checking move validity since fence coordinates are bit different.

# -----Determining how to keep track of fences on the board and off the board.-----
# Each player will have count of their fences within Player class and count_fence methods that will be updated everytime
# player uses a fence. All fences placed on the board will be stored in a list in a fence_placement method
# inside QuoridorGame  class.
#

# -----Determining how to keep track of the pawn's position on the board.-----
# As I said above, pawn's position on the board will be tracked in the board initialized in QuoridorGame class
# and moves will be record in move_pawn method. I also have location data member in Player class where we can check
# player's current location.
