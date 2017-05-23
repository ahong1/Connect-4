# CPSC 231 Project - Connect 4
# Team number: 111
#-----------------------------------------------------------------------------#
# Known bugs                                                                  #
# 1. Game ends when there is more than 4 connecting tokens                    #
# 2. If player clicks on column before the computer's token is drawn,         #
#    computer will use the next turn to finish drawin in it's token from      #
#    the previous turn (IE. computer loses a turn)                            #
#-----------------------------------------------------------------------------#



import turtle
import random
import time

game_state = []
empty_spaces = 42
cell_width = 40
wn = turtle.Screen()
CPUcolumn = 3
messages = []

# Function to write introduction of the game - Alfred
def messageList():
    global messages
    messages.append("Valid move, placing game piece")
    messages.append("Invalid column, please enter a column from 0 to 6 for your next move")
    messages.append("There is no room in that column, please select a new column")
    messages.append("Game over! End of game")
    messages.append("Saving game...")
    messages.append("Saved game to saveFile.txt")
    messages.append("Loading game... ")
    messages.append("Game Successfully loaded!")
    messages.append("No file exist! Starting new game...")
    
    return

def write_intro():
    intro = turtle.Turtle()
    intro.up()
    intro.hideturtle()
    intro.goto(150,270)

    introductionScript = []
    introductionScript.append('CONNECT FOUR')
    introductionScript.append('The Following is a brief description of how to play the game:')
    introductionScript.append('This is a two player game. Two players alternate putting their')
    introductionScript.append('coloured tokens on the board to try to connect four of their tokens in a line')
    introductionScript.append('either diagonally, horizontally or vertically.')
    introductionScript.append('Begin by choosing a column to place your token in.')
    introductionScript.append("You can save the game by pressing 's'")
    introductionScript.append("or load the game by pressing 'l'")
    introductionScript.append('Lets play! Press space to begin.')

    intro.write(introductionScript[0], move=True, align="center", font=("Ariel",40,"bold"))
    startpoint = 260
    spacing = 10
    for line in range(1,len(introductionScript)):
        intro.write(introductionScript[line], move= False, align="center", font=("Ariel",12,"normal"))
        intro.goto(150,startpoint-(spacing*line))
    return

# function to move turtle to correct coordinates for drawing the game board - Ji
def drawBoard():
    four = turtle.Turtle()
    four.pensize(3)
    #makes turtle start at correct coordinates to draw board
    four.speed(0)
    four.penup()
    four.goto(30,270)
    four.pendown()

    for i in range(7):
        drawColumn(four, 40, 240, 90, 180)

# function to draw game board on turtle window - Ji
def drawColumn(n, row, column, x, y): #drawColumn
    n.penup()
    n.hideturtle()
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



# function that performs the computer's move and takes
# the game state as the argument. computer will place token
# in a random column and check if it is valid and the next
# vacant spot on the game board. cpu_moves is called to
# draw the computer's token. Game state is updated
# and returned at the end of the function. - Julien

def pickCPUColumn(game_state):
    blank_space = 'XXXX'
    validColumnsList = []
    columnList = []

    counter = 0
    columnList = generateColumnLists(counter, columnList)

    # If there is no column with 4 empty spaces, there will be a search
    # for 3 empty spaces instead, and will continue to search until 1 empty spaces
    while blank_space != 'X':
        for column in columnList:
            if blank_space in column:
                validColumnsList.append(counter)
                if validColumnsList == "":
                    blank_space = blank_space[1:]
            counter += 1

        counter = 0
        isValidColumn = False
        while isValidColumn == False:
            pickColumn = random.randrange(0,7)
            for validColumn in validColumnsList:
                if pickColumn == validColumn:
                    isValidColumn = True
                    return pickColumn

def generateColumnLists(counter, columnList):
    global game_state
    rows = 6
    numColumns = 7

    if len(columnList) == numColumns:
        counter = 0
        return columnList
    else:
        column = []
        for element in range(rows):
            column.append(game_state[element][counter])
        column = "".join(column)
        columnList.append(column)
        counter += 1
        return generateColumnLists(counter, columnList)

def computer_play():
    global game_state
    global empty_spaces
    global CPUcolumn
    global cell_width

    counter = 1
    for i in range(0, 6):
        if game_state[i][CPUcolumn] == "R" or game_state[i][CPUcolumn] == "B":
            counter = counter + 1

    if counter == 7:
        CPUcolumn = pickCPUColumn(game_state)
            
        
    row = 6 - counter
    if row == -1:
        row = 5
    else:
        row = row
        #Checks if a token already exist on gameboard
    if game_state[row][CPUcolumn] == "R" or game_state[row][CPUcolumn] == "B" :
        last_row = False
        while last_row == False:
            if game_state[row][CPUcolumn] == "R" or game_state[row][CPUcolumn] == "B":
                row = row - 1
            else:
                last_row = True
        return game_state
    else:
        move_gamepiece(CPUcolumn,cell_width,row, "blue")
        game_state[row][CPUcolumn] = "B"
        row = -1

        taken_spaces = 0
        for i in range(0,6):
            for j in range(0,7):
                if game_state[i][j] == "R" or game_state[i][j] == "B":
                    taken_spaces += 1

                    
        empty_spaces = countEmptySpaces(game_state)
        return game_state



def printMessage(mstring):
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.speed(0)
    message.goto(150,10)
    message.write(mstring, align="center", font=("Ariel",15,"normal"))
    time.sleep(1.5)
    message.clear()
    return

def whichColumn(mousex):
    global cell_width
    numColumns = 7
    columnLocations = []

    for i in range(numColumns+1):
        columnLocations.append(10+(i*cell_width))
    

    if mousex < columnLocations[0] or mousex > columnLocations[-1]:
        return -1

    for column in range(len(columnLocations)):
        if mousex >= columnLocations[column] and mousex <= columnLocations[column+1]:
            return column
    
    

# Function that takes the current game state and
# x/y coordinates of mouseclick to determine player's
# move. The function checks if the mouse click in valid
# and will continue to ask for user input until a valid column
# is chosen. move_gamepiece function is called to draw the player's
# token in the coorect place. Game state and number of moves left is updated
# and game state is returned - Alfred

def person_play(game_state,mousex,mousey):
    global empty_spaces
    global cell_width

    counter = 1

    column = whichColumn(mousex)        
    if column < 0 or column > 6:
        printMessage(messages[1])
        return game_state

    else:
        valid_move = True
        row  = 5
        for i in range(6):
            if game_state[5-i][column] == 'R' or game_state[5-i][column] == 'B' :
                counter = counter + 1
                        
        row = 6 - counter
        if counter == 7:
            printMessage(messages[2])
            return game_state
                
        else:
            printMessage(messages[0])
            move_gamepiece(column,cell_width,row, "red")
            game_state[row][column] = "R"
            row = -1               
            taken_spaces = 0
            for i in range(0,6):
                for j in range(0,7):
                    if game_state[i][j] == "R" or game_state[i][j] == "B":
                        taken_spaces += 1

                    
            empty_spaces = countEmptySpaces(game_state)
                
            return game_state
    return game_state
   
def countEmptySpaces(game_state):
    empty_spaces = 0
    for row in game_state:
        for column in range(len(row)):
            if row[column] == 'X':
                empty_spaces += 1
    return empty_spaces
            

# function that takes which column to move to and the cell width as aruments
# and move the player or CPU's token to the row and column - Julien
def move_gamepiece(column,cell_width,row,color): 
    jt = turtle.Turtle()
    jt.penup()
    jt.speed(0)
    jt.goto(10+(cell_width*column), 300) 
    jt.hideturtle()
    jt.right(90)
    jt.forward(250 - ((5-row) * 40))
    jt.pendown()
    jt.color(color)
    jt.fillcolor(color)
    jt.begin_fill()
    jt.circle(20)
    jt.end_fill()
    return


# Function to check the win condition from the
# game state - Ji

def check_win(game_state):
    PLAYER = 'R'
    CPU = 'B'

    # Vertical - Tested and Works
    for row in range(3):
        for col in range(7):
            if game_state[row][col] == PLAYER and game_state[row+1][col] == PLAYER and game_state[row+2][col] == PLAYER and game_state[row+3][col] == PLAYER:
                return True
            elif game_state[row][col] == CPU and game_state[row+1][col] == CPU and game_state[row+2][col] == CPU and game_state[row+3][col] == CPU:
                return True
    # Horizontal - Tested and Works
    for col in range(4):
        for row in range(6):
            if game_state[row][col] == PLAYER and game_state[row][col+1] == PLAYER and game_state[row][col+2] == PLAYER and game_state[row][col+3] == PLAYER:
                return True
            elif game_state[row][col] == CPU and game_state[row][col+1] == CPU and game_state[row][col+2] == CPU and game_state[row][col+3] == CPU:
                return True

    # diagonal- tested and works
    for col in range(4):
        for row in range(3):
            if game_state[row][col] == PLAYER and game_state[row+1][col+1] == PLAYER and game_state[row+2][col+2] == PLAYER and game_state[row+3][col+3] == PLAYER:
               return True
            elif game_state[row][col] == CPU and game_state[row+1][col+1] == CPU and game_state[row+2][col+2] == CPU and game_state[row+3][col+3] == CPU:
                return True
    # diagonal - Tested and works
    for col in range(6,2,-1):
        for row in range(3):
            if game_state[row][col] == PLAYER and game_state[row+1][col-1] == PLAYER and game_state[row+2][col-2] == PLAYER and game_state[row+3][col-3] == PLAYER:
                return True
            elif game_state[row][col] == CPU and game_state[row+1][col-1] == CPU and game_state[row+2][col-2] == CPU and game_state[row+3][col-3] == CPU:
                return True




# Function that takes the x/y coordinates of the user mouse click
# as arguments. Checks if the game state has been updated. If
# game state did not change after player's move, then user is prompted
# to choose a valid column. Function also checks if the player or compuuter
# has won or if there is no more moves left, which will prompt the user and
# end the program. If the game state did change afterthe player's turn, then
# the computer proceeds to make a move. - Alfred

def turn_cycle(mousex,mousey):
    global game_state
    global wn
    global empty_spaces

    
    oldEmptySpaces = empty_spaces
    
    game_state = person_play(game_state,mousex,mousey) #boolean to check

    if oldEmptySpaces == empty_spaces:
        return
    if check_win(game_state) == True or empty_spaces == 0:
        endgame()
        return
    #Makes sure computer's turn is not skipped if computer chooses a full column
    computerMove = False
    oldEmptySpaces = empty_spaces
    while computerMove == False:
        if oldEmptySpaces == empty_spaces:
            game_state = computer_play()
        else:
            computerMove = True
    if check_win(game_state) == True or empty_spaces == 0:
        endgame()
    return
    
# function to clone the game state for comparison
# game state to determine how the game should proceed
# from turn_cycle - Alfred

# function to force the game to end when win condition
# is met or there are no more number of moves. Used to bypass
# the mainloop method - Alfred

def endgame():
    global wn
    wn.onscreenclick(None)
    printMessage(messages[3])
    turtle.exitonclick()
    


# Function to initialize the game state for a new game.
# returns a 2d list containing the rows and columns of the
# game state - JI
# Recursive function

def createGameState(row,column):
    global game_state

    if len(game_state) == row:
        return game_state
    else:
        empty_row = ['X'] * 7
        game_state.append(empty_row)
        return createGameState(row,column)


# Function that takes the game state as the argument and
# write the game state to a text file
# for later use - Alfred and Kris

def saveGame():
    global game_state
    printMessage(messages[4])
    save_file = open("saveFile.txt" , 'w')
    for row in game_state:
        row = " ".join(row)
        save_file.write(row + '\n')
    save_file.close()
    printMessage(messages[5])
    return

# Function that reads a text file containing and older game state.
# Function will clear the screen and redraw the game board based off
# the game state read in the text file. Function will also call startgame()
# to resume the game after the function draws the board - Ji and Julien

def loadGame():
    global game_state
    global empty_spaces
    try:
        game_state = []
        printMessage(messages[6])
        load_file = open('saveFile.txt', 'r')
        for row in load_file:
            tokens = row.split()
            game_state.append(tokens)
        drawNewBoard(game_state)
        load_file.close()
        printMessage(messages[7])
        empty_spaces = countEmptySpaces(game_state)
        if check_win(game_state) == True or empty_spaces == 0:
            endgame()
        else:    
            startgame()
    except IOError:
        printMessage(messages[8])
        startgame()
    return

# Function that takes the game state that was read from the text file
# and draws the game board according to the state of each cell on the game
# board - Ji and Julien

def drawNewBoard(game_state):
    global wn
    wn.clearscreen()
    drawBoard()

    for rowIndex in range(len(game_state)):
        for colIndex in range(len(game_state[rowIndex])):

            if game_state[rowIndex][colIndex] == 'R':
                move_gamepiece(colIndex, cell_width, rowIndex)

            elif game_state[rowIndex][colIndex] == 'B':
                cpu_moves(colIndex, cell_width, rowIndex)

    return

# Function to start running the game after loading a previous
# game state. - Ji and Julien
def startgame():
    global game_state
    global wn
    global cell_width
    global cell_height
    
    turn = random.randrange(0,2)
    if turn == 0:
        game_state = computer_play()
    

    wn.onkey(saveGame, 's')
    wn.onkey(loadGame, 'l')
    wn.onscreenclick(turn_cycle)
    wn.listen()
    turtle.mainloop()


def clearScreenStartGame():
    wn.clearscreen()
    drawBoard()
    startgame()
    return


# Function that contains to main parts of the program
def main():
    global game_state
    global wn
    global cell_width

    windowLength = 300
    row = 6
    column = 7

    game_state = createGameState(row,column)
    messages = messageList()
    wn.screensize(windowLength, windowLength)
    wn.setworldcoordinates(0,0,windowLength,windowLength)
    write_intro()
    wn.onkey(clearScreenStartGame, "space")
    wn.listen()
    turtle.mainloop()
        

main()

