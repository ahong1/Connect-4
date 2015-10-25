#Team 111 Connect 4 - Task 2

#board_string = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#  Connect 4
#    Board
#   023456
#
# 0 XXXXXXX         [ 0][ 1][ 2][ 3][ 4][ 5][ 6]
# 1 XXXXXXX         [ 7][ 8][ 9][10][11][12][13]
# 2 XXXXXXX         [14][15][16][17][18][19][20]
# 3 XXXXXXX         [21][22][23][24][25][26][27]
# 4 XXXXXXX         [28][29][30][31][32][33][34]
# 5 XXXXXXX         [35][36][37][38][39][40][41]

# X = Blank Space
# R = Player (RED)
# B = Computer (BLUE)


import turtle

#function to run introduction of game
def write_intro():
    intro = turtle.Turtle()
    intro.up()
    intro.hideturtle()
    intro.goto(150,270)
    intro.write("CONNECT FOUR", move=True, align="center", font=("Ariel",40,"bold"))
    intro.goto(150,260)
    intro.write("The Following is a brief description of how to play the game:", move= False, align="center", font=("Ariel",12,"normal"))
    intro.goto(150,250)
    intro.write("This is a two player game. Two players alternate putting their", move= False, align="center", font=("Ariel",12,"normal"))
    intro.goto(150,240)
    intro.write("coloured tokens to try to connect four of their tokens in a line", move= False, align="center", font=("Ariel",12,"normal"))
    intro.goto(150,230)
    intro.write("either diagonally, horizontally or vertically. Begin by choosing", move= False, align="center", font=("Ariel",12,"normal"))
    intro.goto(150,220)
    intro.write("a column A to G to place your token in. The line", move= False, align="center", font=("Ariel",12,"normal"))
    intro.goto(150,210)
    intro.write("MUST be exactly four tokens long. You can return to the intro", move= False, align="center", font=("Ariel",12,"normal"))
    intro.goto(150,200)
    intro.write("by typing in 'intro' at the prompt.", move= False, align="center", font=("Ariel",12,"normal"))
    intro.goto(150,190)
    intro.write("Lets play! Type next to begin.", move= False, align="center", font=("Ariel",12,"normal"))
    return

#function to move turtle to correct coordinates for drawing the game board
def initial_n():
    alpha = ["0","1","2","3","4","5","6"]
    four = turtle.Turtle()
    four.pensize(3)
    #makes turtle start at correct coordinates to draw board
    four.speed(10)
    four.penup()
    four.goto(30,270)
    four.pendown()

    for i in alpha:
        drawboard(four, 40, 240, 90, 180, i)

#function to draw game board
def drawboard(n, row, column, x, y, w):
    n.write(w,move=False, align="center", font=("Ariel", 14, "bold" ))
    n.penup()
    n.left(y)
    n.forward(row / 2)
    n.pendown()
    n.left(x)
    n.forward(column)
    n.left(x)
    n.forward(row)
    n.left(x)
    n.forward(column)
    n.penup()
    n.right(x)
    n.forward(row / 2)
    return

def move_gamepiece(column,cell_width,row):
    jt = turtle.Turtle()
    #Row locations
    print("The first column is 0, second is 1, and so on")
    #Asks the sure for which column to place the game piece in
    #a = int(input("Which column would you like? "))
    jt.penup()
    jt.speed(10)
    #move turtle to appropirate column and the top of the board
    jt.goto(10+(cell_width*column), 300)
    #Hides the body of the turtle. Looks better and draws faster
    jt.hideturtle()
    jt.right(90)
    #Put the game piece at the bottom of the board ----- adjusted to account for
    #column height
    jt.forward(250 - ((5-row) * 40))
    jt.pendown()
    jt.color("red")
    jt.fillcolor("red")
    jt.begin_fill()
    #fills the shape it is drawing at the end with the colour red
    jt.circle(20)
    #draws a circle of diaeter 20
    jt.end_fill()
    return


#Function that takes the game state as a parameter and returns an
#updated game_state based on player/computer move
def update_game(game_state):
    column =  int(input("Please enter the column of your next move "))
    valid_move = False
    cell_width = 40
    while valid_move == False:
        #If column is invalid
        if column < 0 or column > 6:
            column = int(input("Invalid column, please enter a column from 0 to 6 for your next move "))

        else:
            valid_move = True
            print("Valid Move! Updating game state... ")
            row  = 5
            while row >=0:
                counter = 1
                #If column is completely filled with token
                for i in range(0,6):
                    if game_state[column + (7*i)] == "R":
                        counter = counter + 1
                        
                if counter == 7:
                    print("No room to place token in column " + str(column) + "!")
                    column = int(input("Please enter the column of your next move"))

                #Checks if a token already exist on gameboard
                elif  game_state[column + (7*row)] == "R" or game_state[column + (7*row)] == "B":
                    row = row - 1
                    Position =  column + (7*row)
                
                else:
                    print("Putting game piece to column " + str(column) + " and row " + str(row))
                    move_gamepiece(column,cell_width,row)
                    game_state = game_state[:column+(7*row)] + "R" + game_state[column+(7*row)+1:]
                    row = -1
    return game_state


def horizontalWin(game_state):
    
    Row1 = game_state[0:7]
    Row2 = game_state[7:14]
    Row3 = game_state[14:21]
    Row4 = game_state[21:28]
    Row5 = game_state[28:35]
    Row6 = game_state[35:42] 

    p_win = 'RRRR'
    c_win = 'BBBB'

    if p_win in Row1:
        return True
    elif p_win in Row2:
        return True
    elif p_win in Row3:
        return True
    elif p_win in Row4:
        return True
    elif p_win in Row5:
        return True
    elif p_win in Row6:
        return True
    elif c_win in Row1:
        return True
    elif c_win in Row2:
        return True
    elif c_win in Row3:
        return True
    elif c_win in Row4:
        return True
    elif c_win in Row5:
        return True
    elif c_win in Row6:
        return True
    else:
        return False

def vertical_check(game_state):
    #row_1 = board_game[0:7]
    #row_2 = board_game[7:14]
    #row_3 = board_game[14:21]
    #row_4 = board_game[21:28]
    #row_5 = board_game[28:35]
    #row_6 = board_game[35:42]

    #column1 = [0,7,14,21,28,35]
    #column2 = [1,8,15,22,29,36]
    #column3 = [2,9,16,23,30,37]
    #column4 = [3,10,17,24,31,38]
    #column5 = [4,11,18,25,32,39]
    #column6 = [5,12,19,26,33,40]
    #column7 = [6,13,20,27,34,41]

    column_1 = game_state[0:36:7]
    column_2 = game_state[1:37:7]
    column_3 = game_state[2:38:7]
    column_4 = game_state[3:39:7]
    column_5 = game_state[4:40:7]
    column_6 = game_state[5:41:7]
    column_7 = game_state[6:42:7]


    p_win = 'RRRR' # Player win

    if p_win in column_7:
        return True
    elif p_win in column_6:
        return True
    elif p_win in column_5:
        return True
    elif p_win in column_4:
        return True
    elif p_win in column_3:
        return True
    elif p_win in column_2:
        return True
    elif p_win in column_1:
        return True
    else:
        return False

def diagonal_check(game_state):
    
    diagonal_1 = game_state[0:41:8]
    diagonal_2 = game_state[1:42:8]
    diagonal_3 = game_state[2:35:8]
    diagonal_4 = game_state[3:28:8]
    diagonal_5 = game_state[7:40:8]
    diagonal_6 = game_state[14:39:8]
    diagonal_7 = game_state[6:37:6]
    diagonal_8 = game_state[13:38:6]
    diagonal_9 = game_state[20:39:6]
    diagonal_10 = game_state[5:36:6]
    diagonal_11 = game_state[4:29:6]
    diagonal_12 = game_state[3:22:6]

    p_win = 'RRRR'

    if p_win in diagonal_1:
        return True
    elif p_win in diagonal_2:
        return True
    elif p_win in diagonal_3:
        return True
    elif p_win in diagonal_4:
        return True
    elif p_win in diagonal_5:
        return True
    elif p_win in diagonal_6:
        return True
    elif p_win in diagonal_7:
        return True
    elif p_win in diagonal_8:
        return True
    elif p_win in diagonal_9:
        return True
    elif p_win in diagonal_10:
        return True
    elif p_win in diagonal_11:
        return True
    elif p_win in diagonal_12:
        return True
    else:
        return False

def check_win(game_state):
    hwin = horizontalWin(game_state)
    vwin = vertical_check(game_state)
    dwin = diagonal_check(game_state)

    if hwin == True or vwin == True or dwin == True:
        return True
    else:
        return False

def main():
    #import relevent modules
    wn = turtle.Screen()
    wn.screensize(300, 300)
    wn.setworldcoordinates(0,0,300,300)

    #Setting constants for number of cell and size of cell
    cell_width = 40
    cell_height = 40
    num_of_cell = 42
    game_state = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    write_intro()
    next = input("Please type next to continue ")
    next = next.upper()
    while next != "NEXT":
        next = input("Please type next to continue ")
        next = next.upper()
        
    wn.clearscreen()
    initial_n()
    while check_win(game_state) == False:
        game_state = update_game(game_state)
        num_of_cell = game_state.count("X")
        if num_of_cell == 0:
            print("end of Game")
            wn.exitonclick()
        print(str(num_of_cell))

    print("end of Game")
    wn.exitonclick()

main()

