# Umar Chaudhry 8/3/2022
# Tic Tac Toe Game
import random

class Board:    
    def __init__(self):
        # 'self.board' will be used to display and manipulate the game board
        self.board = [["?","?","?"],
                      ["?","?","?"],
                      ["?","?","?"]]
        # 'self.over' will be used to tell if the game is over and that the program should end
        self.over = False
        # 'self.winner' will be used to store data on which player has won the game
        self.winner = None
    def __str__(self):
        # this method is used so the print() for the class object will construct
        # a 3 by 3 matrix that is desired when viewing the game board

        # 'game_display' will be a string that contains the game board and it is
        # formed by iterating over 'self.board' and adding appropriate spacing and lines
        game_display = ""
        for row in self.board:
            for mark in row:
                game_display += mark + "|"
            game_display += "\n"+ "-"*6 + "\n"
        return game_display

    def checkHorizontal(self):
        # 'win' will be a variable that is returned to check if a player has won through
        # a three horizontal marking
        # 'winnerChar' will be used to store data on whether the winner is the player using
        # the X or O string

        # by iterating over 'self.board' we can see if the elements in each row of the
        # board are equal to each other not a blank space (?) and tell if the player has won
        win = False
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != "?":
                win = True
                winnerChar = row[1]
        if win:
            return (winnerChar, win)
        else:
            return (None, win)
    
    def checkVertical(self):
        # 'win' will be a variable that is returned to check if a player has won through
        # a three vertical marking and since 'win' is a variable being used in a function scope
        # we can reuse the variable name again
        # 'winnerChar' will be used to store data on whether the winner is the player using
        # the X or O string and we can also reuse this variable name for clarity

        # by iterating over a range of 3 we can check if the same index number elements in corresponding 
        # rows are equal and not a blank space (?) and tell if the player has won
        # since we are referencing self.board many times, it becomes more readable and less redundant 
        # by referring to a shorter variable 'board' which holds the same data needed
        win = False
        board = self.board
        for index in range(3):
            if board[0][index] == board[1][index] and board[1][index] == board[2][index] and board[0][index] != "?":
                win = True
                winnerChar = board[1][index]
        if win:
            return (winnerChar, win)
        else:
            return (None, win)

    def checkDiagonal(self):
        # 'win' and 'winnerChar' are being used for the same purpose as before with now checking
        # a diagonal victory

        # in this case since theres only two possible cases for a victory diagonally
        # iterating may not be neccessary in order to check for a victory
        # since we are referencing self.board many times, it becomes more readable and less redundant 
        # by referring to a shorter variable 'board' which holds the same data needed

        win = False
        board = self.board
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "?":
            win = True
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "?":
            win = True
        if win:
            winnerChar = board[1][1]
            return (winnerChar, win)
        else:
            return (None, win)
    
    def isGameTie(self):
        # 'noEmptySpaces' is a variable used to keep track if all the spots
        # in the board are filled
        # by iterating over the board, we can find if the board has any empty
        # spaces and a return a boolean as appropriate

         noEmptySpaces = True  
         for row in self.board:
            for mark in row:
                if mark == "?":
                    noEmptySpaces = False
         if noEmptySpaces:
            return True
         else:
            return False

    def checkGameStatus(self):
        # using the four previous methods and their returning data
        # we can check for the four cases of victory through horizontal
        # vertical or diagonal means and check the case of a tie
        # then declare a possible winner and adjust 'self.over' to end the game
        # as well as adjust 'self.winner' to show the winner of game
        # this aspect of ending the games comes more to play in the methods
        # nextPossibleMoves() and testGame() and oneThousandTrials()
        # by returning in each of the cases, the isGameTie() will work properly
        # by being the last condition checked

        if self.checkHorizontal()[1]:
            winnerChar = self.checkHorizontal()[0]
            print("The {} player has won!".format(winnerChar))
            self.over = True
            self.winner = winnerChar
            return
        elif self.checkVertical()[1]:
            winnerChar = self.checkVertical()[0]
            print("The {} player has won!".format(winnerChar))
            self.over = True

            self.winner = winnerChar
            return
        elif self.checkDiagonal()[1]:
            winnerChar = self.checkDiagonal()[0]
            print("The {} player has won!".format(winnerChar))
            self.over = True
            self.winner = winnerChar
            return
        elif self.isGameTie():
            print("The game is a tie!")
            self.over = True
            winnerChar = None
            


    def nextPossibleMoves(self):
        # 'moves' will store the indices of the positions in 'self.board' that have
        # not been marked by a player
        # by taking the length of 'moves' we can declare how many options the two players 
        # have assuming player X goes first
        
        moves = []
        for firstIndex in range(3):
            for secondIndex in range(3):
                if self.board[firstIndex][secondIndex] not in ["X","O"]:
                    moves.append((firstIndex,secondIndex))
        print("Player X has {} available moves and Player O has {} available moves".format(len(moves),len(moves)-1))
        
        chosenIndex = random.choice(moves)
        moves.remove(chosenIndex)
        self.board[chosenIndex[0]][chosenIndex[1]] = "X"
        self.checkGameStatus()
        if self.over != True:
            chosenIndex = random.choice(moves)
            moves.remove(chosenIndex)
            self.board[chosenIndex[0]][chosenIndex[1]] = "O"
            self.checkGameStatus()

    def displayBoard(self):
        # this method is the same as __str__ and its useful merely to call
        # the board to be displayed in the method testGame() as one cant
        # call print(class_object) inside a method one can only call
        # print(self.board) which does not trigger the __str__ method
        game_display = ""
        for row in self.board:
            for mark in row:
                game_display += mark + "|"
            game_display += "\n"+ "-"*6 + "\n"
        return game_display

    def testGame(self, turns):
        # based on the parameter, 'turns', assumed to be an integer, the program will have the computers play
        # each other in a tic tac toe game for that number of turns iterating over range(turns) by calling
        # the previous methods and checking if the game is over to end the program when appropriate
        # 'ready' is used to take in input to give some breathing room and time to examine between turns
        
        for i in range(turns):
            self.nextPossibleMoves()
            print(self.displayBoard())
            if self.over:
                self.board = [["?","?","?"],
                      ["?","?","?"],
                      ["?","?","?"]]
                self.over = False
                break
            
    def oneThousandTrials(self):
            Xwins = []
            Owins = []
            ties = []
            for i in range(1000):
                self.testGame(5)
                if self.winner == "X":
                    Xwins.append(True)
                elif self.winner == "O":
                    Owins.append(True)
                elif self.winner == None:
                    ties.append(True)
                self.winner = None 
            return (len(Xwins),len(Owins),len(ties))

# the code below is sample output

board =  Board()
p1wins, p2wins, ties = board.oneThousandTrials()

print("Player one (X) won {} games".format(p1wins))
print("Player two (O) won {} games".format(p2wins))
print("There were {} ties".format(ties))