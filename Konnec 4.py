dollars = '$'
euros = '€'
#class for creating the pieces for the game 
class CurrencyPiece () :
    def __init__(self, team_name) :
        if type(team_name) == str :
            teamCopy = list(team_name.lower())
            realTeam = []
            for i in range(len(teamCopy)) : #I in TEAM lol
                if teamCopy[i] != ' ' :
                    realTeam.append(teamCopy[i]) 
            realTeam = ''.join(realTeam)
            if realTeam == "dollars" :
                self.team_name = "Dollars" 
            elif realTeam == "euros" :
                self.team_name = "Euros" 
            else :
                raise ValueError 
        elif type(team_name) == int :
            if team_name == 0 :
                self.team_name = "Dollars" 
            elif team_name == 1 :
                self.team_name = "Euros" 
            else :
                raise ValueError
        else :
            raise TypeError

    def __str__(self) :
        if self.team_name == "Dollars" :
            return dollars
        if self.team_name == "Euros" :
            return euros

dollar_piece = CurrencyPiece("dollars")
euro_piece = CurrencyPiece(1)

#class creates the board and all other relevant methods for playing the game		
class Board:
    def __init__(self):
        self.board = [] 
        for row in range(6) :
            row = []
            for col in range(7) :
                row.append(None)
            self.board.append(row)
        
        self.current = "Dollars"

    # think about doing this recursively, could be a shorter solution
    def addPiece(self, column):
        if column < 1 or column > 7 :
            raise ValueError

        if self.current == "Dollars" :
            for i in range(len(self.board) - 1, -1, -1) :
                if self.board[i][column - 1] == None :
                    self.board[i][column - 1] = dollar_piece
                    self.current = "Euros"
                    break
        elif self.current == "Euros" :
            for i in range(len(self.board) - 1, -1, -1) :
                if self.board[i][column - 1] == None :
                    self.board[i][column - 1] = euro_piece  
                    self.current = "Dollars"     
                    break
        
    def checkWinner(self):
    # make the checks into functions if needed else where 
    
    #horiz check
        for row in self.board :
            for i in range(len(row) - 3) :
                if row[i:i+4] == [dollar_piece] * 4 :
                    return "Dollars"
                if row[i:i+4] == [euro_piece] * 4 :
                    return "Euros"
        #vert check
        for col in range(len(self.board[0])) :
            for row in range(len(self.board) - 3) :
                if (self.board[row][col] == dollar_piece and self.board[row + 1][col] ==  dollar_piece and self.board[row + 2][col] == dollar_piece 
                and self.board[row + 3][col] ==  dollar_piece) :
                    return "Dollars"
                if (self.board[row][col] == euro_piece and self.board[row + 1][col] ==  euro_piece and self.board[row + 2][col] == euro_piece 
                and self.board[row + 3][col] == euro_piece) :
                    return "Euros"
    
        #diag neg check \
        for row in range(len(self.board) - 3) :
            for col in range(len(self.board[row]) - 3) :
                if (self.board[row][col] == dollar_piece and self.board[row + 1][col + 1] == dollar_piece and 
                self.board[row + 2][col + 2] == dollar_piece and self.board[row + 3][col + 3] == dollar_piece) :
                    return "Dollars"
                if (self.board[row][col] == euro_piece and self.board[row + 1][col + 1] == euro_piece and 
                self.board[row + 2][col + 2] == euro_piece and self.board[row + 3][col + 3] == euro_piece) :
                    return "Euros"
    
        #diag pos check /
        for row in range(len(self.board) - 1, 2, -1) :
            for col in range(len(self.board[row]) - 3) :
                if (self.board[row][col] == dollar_piece and self.board[row - 1][col + 1] == dollar_piece and 
                self.board[row - 2][col + 2] == dollar_piece and self.board[row - 3][col + 3] == dollar_piece) :
                    return "Dollars"
                if (self.board[row][col] == euro_piece and self.board[row - 1][col + 1] == euro_piece and 
                self.board[row - 2][col + 2] == euro_piece and self.board[row - 3][col + 3] == euro_piece) :
                    return "Euros"

        return False 

# --- NOT CODED BY ME ---
    def __str__(self) -> str:
        """
        I have given you this because I wanted it to look fancy.
        Just know, in 2nd year, you would be expected to make something like this.
        Maybe remember this code when you get to 2ME3... 
        Good chance it might be helpful.
        """
        s = "╔" + ("══╦" * 6) + "═" * 3 + "╗\n"
        for row_index, row in enumerate(self.board):
            s += "║"
            for col_index, column in enumerate(row):
                s += f" {str(column if column != None else ' ')} ║"
            if row_index < 5:
                s += "\n╠" + ("═══╬" * 6) + "═══╣\n"
            else:
                s += '\n'
        return s + "╚" + "═══╩" * 6 + "═" * 3 + "╝\n"

    def parseMove(self, column, row = 1) :
        return 
# --- My code starts from here 

    def clear(self) :
        Board.__init__(self
        
# --- NOT CODED BY ME ---
# code below lets you play the game 
from IPython.display import clear_output
board = Board()
moves = []
while board.checkWinner() == False and board.checkWinner() != "Dollars" and board.checkWinner() != "Euros" :
    clear_output()
    print("Board:")
    print(str(board))
    print("Current Player:", board.current)
    print(f'Past Moves: {moves}')
    column = input("Pick a column to place your coin! >> ")
    try:
        if column.lower() in ('q', "quit", 'e', "exit"):
            break
        column = int(column)
        moves.append(column)
        try:
            if board.parseMove((1, column)):
                board.addPiece(column)
            else:
                print("That is an invalid move!")
        except Exception as e:
            print("An error occured:", e)
    except Exception as e:
        print("Uh oh... An error occured:", e)
if board.checkWinner():
    clear_output()
    print("Board:")
    print(str(board))
    print(board.board)
    print("And the winner is:", board.checkWinner())
    print(f'Moves: {moves}')
    
# --- My code begins ---

#code below lets the game be played from a yaml or txt file with valid inputs/moves
import yaml

class NoKonnec4(Exception) :
    pass

class BadMoveSon(Exception) :
    pass

def playKonnecFile(move_list) :
    if type(move_list) != str :
        raise TypeError
    if move_list[-5:] != ".yaml" and move_list[-4:] != ".txt" :
        raise ValueError 
    
    if move_list[-5:] == ".yaml" :
        with open(move_list, 'r') as fh :
            contentCopy = yaml.load(fh.read(), Loader = yaml.loader.SafeLoader) 
            moves = []
            for i in range(len(contentCopy["data"])) :
                if contentCopy["data"][i]["game"] == "Konnec 4" :
                    moves = contentCopy["data"][i]["moves"]
                    break
    if move_list[-4:] == ".txt" :
        with open(move_list, 'r') as fh :
            content = fh.read() 
            moves = content.split("\n")

    #print(moves)
    if moves == [''] or moves == [] :
        raise NoKonnec4
    
    # nums = [0,1,2,3,4,5,6,7,8,9]
    # for num in nums :
    #     if "A" + str(num) not in moves and "P" not in moves and "R" not in moves :
    #         raise NoKonnec4

    board = Board() 
    p_counter = 0
    dollarWinCounter = 0
    euroWinCounter = 0
    for move in moves :
        if move[0] == "A" :
            board.addPiece(int(move[1]))
        elif move == "P" :
            print(str(board))
            p_counter += 1
        elif move == "R" :
            board.clear()
        else :
            raise BadMoveSon
        if board.checkWinner() == "Dollars" :
            dollarWinCounter += 1
        if board.checkWinner() == "Euros" :
            euroWinCounter += 1

    return (board, p_counter, (dollarWinCounter, euroWinCounter))