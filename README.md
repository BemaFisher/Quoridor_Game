# portfolio-project

A board game called Quoridor. 

Details about the game, validation rules, implementation, game play are below.

## Game

You can see the rules of the game in this [video](https://www.youtube.com/watch?v=6ISruhN0Hc0) and [Page 9 of this educative-sheet_quoridor-english.pdf](https://en.gigamic.com/files/media/fiche_pedagogique/educative-sheet_quoridor-english.pdf) 

This a program for a two-player version of the game.  Each player will have 10 fences.

The board is formed by 9x9 cells, and the pawn will move on the cells.  The fence will be placed on the edges of the cells.  The four sides of the board are treated as fences and no more fence should be placed on top of it.

The board should be treated as the following picture shows:

![image](https://user-images.githubusercontent.com/21003726/127106790-aaf4e265-a122-4fc3-bc70-77a261c78ea2.png)
 
The pawn position `(x,y)` is defined by the coordinate of the top left corner of the cell that the pawn is on. `x` is the number from the vertical line and `y` is the number from the horizontal line, making the top left corner of the cell. The board positions start with `(0,0)` and end at `(8,8)`. At the beginning of the game, player 1 places pawn 1 (P1) on the top center of the board and player 2 places pawn 2 (P2) on the bottom center of the board.  The position of P1 and P2 is `(4,0)` and `(4,8)` when the game begins.   

The four edges are labeled as fences. The row of the cells where the pawns are positioned at the start of the game are called base lines.

When each player tries to place a fence on the board, the position of the fence is defined by a letter and coordinates.  For vertical fences, we use `v` and for horizontal fences, we use `h`.  As an example, for the blue fence (vertical) in the picture, we use the coordinate of the top corner to define it and for the red fence (horizontal), we use coordinate of the left corner to define it. 

## Validation rules

For example, jumping over the pawn is allowed only when the two pawns face each other. Diagonal movement is allowed when blocked by pawn + fence. A fence only blocks 1 square. Fences cannot be moved once placed thus they cannot be reused. The baseline cannot be blocked off with the fences. All the rules from the video and the PDF apply unless the README or an Instructor explicitly says otherwise.

## Playing the game

Player 1 will start the game. Each player takes turn playing. On a player’s turn they will make one move. They can either move the pawn (`move_pawn`) or place a fence (`place_fence`). Your program should be able to determine whether the movement is valid. A turn lasts until the player has made a valid move.
 
The first player whose pawn reaches any of the cells of the opposite player's base line wins the game. No turn can be played after a player has won.

## Implementation
Your `QuoridorGame` class must include the following methods:

* `init` method that initializes the board with the fences (four edges) and pawns (P1 and P2) placed in the correct positions. 

* `move_pawn` method takes following two parameters in order: an integer that represents which player (1 or 2) is making the move and a tuple with the coordinates of where the pawn is going to be moved to.
    - if the move is forbidden by the rule or blocked by the fence, return `False`
    - if the move was successful or if the move makes the player win, return `True`
    - if the game has been already won, return `False`

* `place_fence` method takes following parameters in order: an integer that represents which player (1 or 2) is making the move, a letter indicating whether it is vertical (v) or horizontal (h) fence, a tuple of integers that represents the position on which the fence is to be placed.   
    - if player has no fence left, or if the fence is out of the boundaries of the board, or if there is already a fence there and the new fence will overlap or intersect with the existing fence, return `False`. 
    - If the fence can be placed, return `True`.
    - If it breaks the fair-play rule (and if you are doing the extra credit part), return exactly the string `breaks the fair play rule`.
    - If the game has been already won, return `False`

* `is_winner` method that takes a single integer representing the player number as a parameter and returns `True` if that player has won and `False` if that player has not won.


## How your game will be played?

Here's a very simple example of how QuoridorGame class will be used and is expected to behave:

```
q = QuoridorGame()
q.move_pawn(2, (4,7)) #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
q.move_pawn(1, (4,1)) #moves the Player1 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- out of turn move, returns False 
q.move_pawn(2, (4,7)) #moves the Player2 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- returns True
q.place_fence(2, 'v',(3,3)) #places Player2's fence -- returns True
q.is_winner(1) #returns False because Player 1 has not won
q.is_winner(2) #returns False because Player 2 has not won

```
