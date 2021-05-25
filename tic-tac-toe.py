#! python3
# This is a simple, but functional, tic-tac-toe game
# Use: python tic-tac-toe.py
import random
from time import sleep

mainSymbols = ['o', 'x']
availableSymbols = ['a', 'b', 'c', 'd']

def create_board(x, y):
    assert x == y
    assert (not x > 6) and (not x < 3)
    board = []
    for x_ in range(x):
        table = []
        board.append(table)
        for y_ in range(y):
            board[x_].append(' ')
    return board

def print_board(board, alphaChars=['a', 'b', 'c', 'd', 'e', 'f']):
    tables = [' | '.join(table) for table in board]
    print('==' * len(tables[0]))
    print('   ' + '   '.join(alphaChars[:len(board[0])]))
    tableNum = 1
    for table in tables:
        table = str(tableNum) + '  ' + table
        print(table)
        if tableNum != len(tables):
            sepString = ('--+-' * (len(board[0]) - 1) + '-')
            print('   ' + sepString)
        tableNum += 1

def get_coordinates(coordinateStr, maxX=3, maxY='c', alphaChars=['a', 'b', 'c', 'd', 'e', 'f']):
    # a = Numerical coordinate
    # b = Alphabetical coordinate
    if len(coordinateStr) != 2: return None
    if coordinateStr[1] not in alphaChars: return None
    if int(coordinateStr[0]) > maxX and coordinateStr[1].lower() > maxY: return None
    return int(coordinateStr[0]) - 1, alphaChars.index(coordinateStr[1])

def check_winner(board):
    assert all([len(x) == len(max(board)) for x in board]) # Checks if all inner lists are the same size
    assert len(board) >= 3 # Self-explanatory
    assert len(board) == len(board[1]) # x and y needs to be the same size too

    # Horizontal check
    def Horizontal():
        for i in range(len(board)):
            items = board[i].copy()
            if items[0] in ['', ' ']: continue
            if all([x == items[0] for x in items]):
                return items[0]

    # Vertical check
    def Vertical():
        for x in range(len(board)):
            items = []
            for y in range(len(max(board))):
                items.append(board[y][x])
                if board[y][x] in ['', ' ']: break
            if items[0].isspace(): continue
            if all([x == items[0] for x in items]):
                return items[0]

    # Diagonal check
    def Diagonal():
        maxBoard = len(max(board))
        def diagonal1():
            items = []
            for i in range(maxBoard):
                if board[i][i] in ['', ' ']: return
                items.append(board[i][i])
            if all([x == items[0] for x in items]): return items[0]

        def diagonal2(): # Not really right to left, but you get my point here
            items = []
            x, y = 0, len(board) - 1
            while x != maxBoard:
                if board[y][x] in ['', ' ']: return
                items.append(board[y][x])
                y -= 1
                x += 1
            if all([x == items[0] for x in items]): return items[0]

        return diagonal1() or diagonal2()
                
    return Horizontal() or Vertical() or Diagonal()

class Player():
    def __init__(self, player, score=0, is_bot=False):
        self.player = player.lower()
        self.is_bot = is_bot
        self.score = score

board = create_board(3, 3)
alphaCoordinates = ['a', 'b', 'c']
players = [Player('x'), Player('o', is_bot=True)]

print_board(board)
winner = None
while winner == None:
    for playerIndex in range(len(players)):
        player = players[playerIndex]
        
        # Each player has 3 chances of give a valid coordinate before loosing it's turn
        if not player.is_bot:
            for i in range(3):
                print('Player\'s %s turn.' %player.player)
            
                coordinateStr = input('Coordinate: ')
                if not get_coordinates(coordinateStr, 3, 'c'):
                    print('Invalid coordinates. Try something like 1A or 2B.')
                    print('===' * 5)
                    continue
                else:
                    x, y = get_coordinates(coordinateStr)
                    if board[x][y].isspace():
                        break
                    else:
                        print('Coordinates already in board. Try again.')
                        print('===' * 5)
            else:
                print('Player lost turn. Moving on to player %s.' %(players[playerIndex - 1].player))
                continue
        else:
            choices = [(x, y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y].isspace()]
            x, y = random.choice(choices)
            print('===' * 5)
            print('Player ' + player.player + ' turn.')
            sleep(1)

        board[x][y] = player.player
        print_board(board)
        winner = check_winner(board)
        if winner:
            break
        
if not winner:
    print('No winners this game :(')
else:
    print('Player ' + winner + ' won this game!')