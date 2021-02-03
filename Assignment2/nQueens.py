'''
Homework 2
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.02
'''

'''
Place n Queens on the board without conflict
'''
def check(board, row, col):
    #check row, left
    for i in range(n):
        if board[row][i] == 1:
            return False

    #check diagonal, upper left
    #zip() > joins two tuples together
    for i, j in zip(range(row, -1, -1),range(col, -1, -1)):
            if board[i][j] == 1:
                return False

    #check diagonal, lower left
    for i, j in zip(range(row, n, -1),range(col, -1, -1)):
            if board[i][j] == 1:
                return False

    return True

def queens(n):
    #create an nxn board
    board = [[0] * n for p in range(n)]
    
    #find a solution
    def recursion(j):
        #base case
        if j >= n:
            return True

        #recursion
        for i in range(n):
            if check(board, i, j):

                #place queen on board
                board[i][j] = 1

                #place rest of queens  on board
                if recursion(j + 1) == True:
                    return True

                #if placing a queen didnt lead to a solution
                #YEET IT
                board[i][j] = 0

        #if no queen can be placed in present column
        return False       

    if recursion(0) == False:
        print("No solution exists")
        return []

    return board
            

'''
Print the board
'''
def printBoard(board, n):
    for i in range(0,n):
        print(board[i])


if __name__ == '__main__':

    #board size
    n = 10
    
    #place queens in safety
    board = queens(n)

    #print the board
    #where True is a safe spot to place a Queen with no
    #conflicts
    if len(board) != 0:
        printBoard(board, n)
    
    
    
