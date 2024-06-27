      
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
       
        print(
        """
        +-------+-------+-------+
        |       |       |       |
        |  """, board[0][0], """  |  """, board[0][1], """  |  """, board[0][2], """  |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |  """, board[1][0], """  |  """, board[1][1], """  |  """, board[1][2], """  |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |  """, board[2][0], """  |  """, board[2][1], """  |  """, board[2][2], """  |
        |       |       |       |
        +-------+-------+-------+
        """
        )
        


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
        a = 0
        print("Players Turn")
        while a == 0:
                try:
                        move = int(input("Enter move "))
                        if move == 1:
                            choice = (0,0)
                            a = 1
                        elif move == 2:
                            choice = (0,1)
                            a = 1
                        elif move == 3:
                            choice = (0,2)
                            a = 1
                        elif move == 4:
                            choice = (1,0)
                            a = 1
                        elif move == 6:
                            choice = (1,2)
                            a = 1
                        elif move == 7:
                            choice = (2,0)
                            a = 1
                        elif move == 8:
                            choice = (2,1)
                            a = 1
                        elif move == 9:
                            choice = (2,2)
                            a = 1
                except ValueError:
                        print("Invalid move, try again")
                        continue
     
        while choice not in free_cell:
          print("Move not available, try again")
          return enter_move(board)
    
        if move == 1:
            board[0][0] = "O"
        elif move == 2:
            board[0][1] = "O"
        elif move == 3:
            board[0][2] = "O"
        elif move == 4:
            board[1][0] = "O"
        elif move == 6:
            board[1][2] = "O"
        elif move == 7:
            board[2][0] = "O"
        elif move == 8:
            board[2][1] = "O"
        elif move == 9:
            board[2][2] = "O"
            
      

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
       global free_cell

       free_cell = []
       
       for i in range(3):   
           if board[0][i] != "X" and board[0][i] != "O":
               free_cell.insert(0,(0,i))
           
           if board[1][i] != "X" and board[1][i] != "O":
               free_cell.insert(0,(1,i))
           
           if board[2][i] != "X" and board[2][i] != "O":
               free_cell.insert(0,(2,i))
       

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    Empty = []
            
    for i in range(3):
        if (board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X") or (board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X") or (board[0][0] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[2][0] == "X"):
            print("Game over: Computer wins")
            return True
            break
                
        elif board[i][0:3] == ["O", "O", "O"] or (board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O"):
            print("Game over: Player wins")
            return True
            break
                    
        elif n == 8:
            print("Game over: Tie")
            return True
            break
                
        else:
            return False
                

def draw_move(board):
        # The function draws the computer's move and updates the board.
        
        if turn == "computer":
            from random import randrange
            for i in range(1):
                move = randrange(10)
        
        if move == 1:
            choice = (0,0)
        elif move == 2:
            choice = (0,1)
        elif move == 3:
            choice = (0,2)
        elif move == 4:
            choice = (1,0)
        elif move == 6:
            choice = (1,2)
        elif move == 7:
            choice = (2,0)
        elif move == 8:
            choice = (2,1)
        elif move == 9:
            choice = (2,2)
        else:
            return draw_move(board)
      
        while choice not in free_cell:
           return draw_move(board)
     
        if move == 1:
             board[0][0] = "X"
        elif move == 2:
             board[0][1] = "X"
        elif move == 3:
             board[0][2] = "X"
        elif move == 4:
             board[1][0] = "X"
        elif move == 6:
             board[1][2] = "X"
        elif move == 7:
             board[2][0] = "X"
        elif move == 8:
             board[2][1] = "X"
        elif move == 9:
             board[2][2] = "X"
             

game = False
turn = 0
sign = 0
n = 0

board = []
        
for i in range(3):
        row = [0 for i in range(3)]
        board.append(row)
        
board[0][0] = 1
board[0][1] = 2
board[0][2] = 3
board[1][0] = 4
board[1][1] = "X"
board[1][2] = 6
board[2][0] = 7
board[2][1] = 8
board[2][2] = 9
        

if game == False:
    game =input("Start game? y/n ")

if game == "y":
        display_board(board)
        make_list_of_free_fields(board)
        turn = "user"
        
else:
        print("Goodbye")


while victory_for(board, sign) == False:
        if turn == "user":
                make_list_of_free_fields(board)
                enter_move(board)
                n += 1
                turn = "computer"
                
                
        if turn == "computer":
                make_list_of_free_fields(board)
                draw_move(board)
                display_board(board)
                n += 1
                turn = "user"
        continue  
        
