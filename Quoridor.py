# Author: Begaiym Fisher
# Date: 7/31/2021
# Description: The Quoridor game represented by two classes: Player and Quoridor. Two player version of the board game.

class Player:
    """Represents player. Class will store player's num(1 or 2), number of fences available(starts with 10), name, and
    location. It will have getters for all the data members. It has a method for keeping track of fences available for
    player.
    It also will have inheritance relationship with Quoridor class (Quoridor has-a player) since we need to keep track
    of players."""

    def __init__(self, player_id):
        """Initializes private data members"""
        self._player_id = player_id  # 1 or 2
        self._player_name = ''       # P1 or P2
        self._num_of_fences = 10
        self._location = None

    def get_player_id(self):
        """:returns player num"""
        return self._player_id

    def get_player_name(self):
        return self._player_name

    def get_num_of_fences(self):
        """:returns number of fences player has"""
        return self._num_of_fences

    def get_location(self):
        """:returns location of the player."""
        return self._location

    def set_location(self, location):
        """ Sets player's location to given location. CHANGE IT EVERY TIME PLAYER MOVES"""
        self._location = location

    def player_name(self, player_num):
        """ Returns Player's name (P1 or P2)"""
        if player_num == 1:
            return 'P1'
        else:
            return 'P2'

    def subtract_fence(self, num_of_fences_used):
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
        self._current_player = 1  # since P1 takes the first turn
        self._list_of_players = [Player(1), Player(2)]
        self._fence_on_board = {}
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

    def get_fence_on_board(self):
        """:returns dictionary of fences placed on board"""
        return self._fence_on_board

    def print_board(self):
        """Prints board"""
        print('0x', '1x', '2x', '3x', '4x', '5x', '6x', '7x', '8x')
        print("--------------------------")
        for row in self._board:
            for slot in row:
                print(slot, end=" ")
            print()
        print("--------------------------")

    def lookup_player_from_num(self, player_num):
        """ Take player's number and return Player object"""
        for player in self._list_of_players:
            if player_num == player.get_player_id():
                return player
            if player not in self._list_of_players:
                return None

    def opponents_baseline(self, player_num):
        """ returns each player's baseline"""
        if player_num == 1:
            return [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]
        if player_num == 2:
            return [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]

    def is_valid_move_pawn_borders(self, player, coord):
        """ Sets up an initial location of players
        Takes the coordinates that pawns wants to move as a parameter and checks if it's within the bounds.
        checks if destination coord is taken by another player"""
        if coord[0] < 0 or coord[1] < 0:  # border check
            return False
        if coord[0] >= 9 or coord[1] >= 9:
            return False

        if self._board[coord[1]][coord[0]] == player.player_name(self.opponent_player()):  # if block is taken by another player
            return False

        if player.get_location() is None:   # set initial locations
            if player.get_player_id() == 1:
                player.set_location((4, 0))
            elif player.get_player_id() == 2:
                player.set_location((4, 8))
        current_location = player.get_location()
        return True

    def is_valid_move_pawn(self, player, coord):
        """ Takes the coordinates that pawns wants to move as a parameter and checks if it's within the bounds.
        Also checks if there is another pawn. Allows only move
        Returns true if move is legal and False otherwise."""
        current_location = player.get_location()

        # opponent pawn on top
        if 0 <= (current_location[1] - 1) < 9:
            if self._board[current_location[0]][current_location[1] - 1] == player.player_name(self.opponent_player()):
                if (coord != (current_location[0], current_location[1] + 1)) and (
                        coord != (current_location[0], current_location[1] - 2)) and (
                        coord != (current_location[0] + 1, current_location[1])) and (
                        coord != (current_location[0] - 1, current_location[1])):
                    return False
        if 0 <= (current_location[1] + 1) < 9:
            if self._board[current_location[0]][current_location[1] + 1] == player.player_name(self.opponent_player()):
                if (coord != (current_location[0], current_location[1] + 1)) and (
                        coord != (current_location[0], current_location[1] + 2)) and (
                        coord != (current_location[0] + 1, current_location[1])) and (
                        coord != (current_location[0] - 1, current_location[1])):
                    return False
        else:
            if (coord != (current_location[0], current_location[1] + 1)) and (
                    coord != (current_location[0], current_location[1] - 1)) and (
                    coord != (current_location[0] + 1, current_location[1])) and (
                    coord != (current_location[0] - 1, current_location[1])):
                return False
        return True

    def check_pawn_move_fence(self, player, coord):
        """ Checks if there is fence obstructing way and return False if there is another pawn"""

        current_location = player.get_location()

        # check for fences when moving orthogonally
        if coord == (current_location[0], current_location[1] - 1):  # up
            for key, value in self._fence_on_board.items():
                if key == current_location:
                    for i in range(len(value)):
                        if value[i] == 'h':
                            return False
        if coord == (current_location[0], current_location[1] + 1):  # down
            for key, value in self._fence_on_board.items():
                if key == coord:
                    for i in range(len(value)):
                        if value[i] == 'h':
                            return False

        if coord == (current_location[0] - 1, current_location[1]):  # left
            for key, value in self._fence_on_board.items():
                if key == current_location:
                    for i in range(len(value)):
                        if value[i] == 'v':
                            return False

        if coord == (current_location[0] + 1, current_location[1]):  # right
            for key, value in self._fence_on_board.items():
                if key == coord:
                    for i in range(len(value)):
                        if value[i] == 'v':
                            return False
        return True

    def move_pawn(self, player_num, coord):
        """
        if the move is forbidden by the rule or blocked by the fence, return False
        if the move was successful or if the move makes the player win, record it and return True
        if the game has been already won, return False
        """
        print("Current player is: ", self._current_player)

        if self._game_status == 'WON':
            return False
        if player_num != self._current_player:  # make sure it's player's turn
            return False

        player = self.lookup_player_from_num(player_num)

        while self.is_valid_move_pawn_borders(player, coord) and self.is_valid_move_pawn(player, coord) and self.check_pawn_move_fence(player, coord):
            temp = player.get_location()
            player.set_location(coord)
            self._board[coord[1]][coord[0]] = player.player_name(player_num)
            self._board[temp[1]][temp[0]] = '--'
            self.print_board()
            self._current_player = self.opponent_player()
            return True

        if self.is_winner(player_num) is True:  # have to check if game ends if player got to the baseline
            return True
        else:
            return False

    # check validity of fence move
    def is_valid_move_fence(self, player, direction, coord):
        """ Takes the direction and coordinates of where the fence needs to be placed and checks if the move is within
        the bounds. Returns true if move is legal and False otherwise."""

        # border check
        if direction == 'v':
            if coord[0] < 1 or coord[0] >= 9:
                return False
            if coord[1] < 0 or coord[1] >= 9:
                return False
        if direction == 'h':
            if coord[0] < 0 or coord[0] >= 9:
                return False
            if coord[1] < 1 or coord[1] >= 9:
                return False

        # no fence left
        if player.get_num_of_fences() <= 0:
            return False

        # if fence has been placed already
        for key, value in self._fence_on_board.items():
            if key == coord:
                for i in range(len(value)):
                    if value[i] == direction:
                        return False
        return True

    def place_fence(self, player_num, direction, coord):
        """
        if player has no fence left, or if the fence is out of the boundaries of the board, or if there is already a
        fence there and the new fence will overlap or intersect with the existing fence, return False.
        If the fence can be placed, return True.
        If it breaks the fair-play rule (and if you are doing the extra credit part), return exactly the string breaks
        the fair play rule.
        If the game has been already won, return False
        """
        print("Current player is: ", self._current_player)
        # game has been won
        if self._game_status == 'WON':
            return False
        if player_num != self._current_player:  # make sure it's player's turn
            return False

        player = self.lookup_player_from_num(player_num)

        while self.is_valid_move_fence(player, direction, coord):
            for key in self._fence_on_board:
                if key == coord:
                    self._fence_on_board[key].append(direction)
                    self._current_player = self.opponent_player()
                    player.subtract_fence(1)
                    return True

            self._fence_on_board[coord] = [direction]
            self._current_player = self.opponent_player()
            player.subtract_fence(1)
            return True
        else:
            return False

    def is_winner(self, player_num):
        """
        Returns True if that player has won and False if that player has not won.
        Check that by checking if player is on opponents base line.
        """
        player = self.lookup_player_from_num(player_num)

        if player.get_location() in self.opponents_baseline(player_num):
            self.set_game_status('WON')
            return True
        else:
            return False

    def opponent_player(self):
        """ Determine opponent player. If P1 is current player then return P2 as opponent and vice versa"""
        if self._current_player == 1:
            return 2
        else:
            return 1


# game_1 = QuoridorGame()
# game_1.print_board()
# print(game_1.move_pawn(1, (4, 1)))
# print(game_1.move_pawn(2, (4, 7)))
# print(game_1.move_pawn(1, (4, 2)))
# print(game_1.move_pawn(2, (4, 6)))
# print(game_1.move_pawn(1, (4, 3)))
# print(game_1.move_pawn(2, (4, 5)))
# print(game_1.move_pawn(1, (4, 4)))
# print(game_1.move_pawn(2, (4, 3)))
# print(game_1.place_fence(1, 'h', (0, 1)))
# print(game_1.move_pawn(1, (4, 2)))
# print(game_1.move_pawn(1, (5, 1)))
# print(game_1.move_pawn(2, (4, 5)))

# print(game_1.move_pawn(2, (4, 7)))
# print(game_1.get_game_status())

# print(game_1.place_fence(1, 'h', (6, 5)))
# print(game_1.place_fence(2, 'v', (6, 5)))
# print(game_1.place_fence(1, 'v', (5, 5)))
# print(game_1.place_fence(2, 'h', (6, 5)))
# print(game_1.place_fence(1, 'v', (0, 5)))
# print(game_1.place_fence(2, 'v', (6, 0)))
# print(game_1.get_fence_on_board())


