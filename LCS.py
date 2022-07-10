import sys
def format_print_matrix(M, X_Axis, Y_Axis):
    #borrowed code from here: https://stackoverflow.com/questions/37093510/how-to-print-array-as-a-table-in-python
    #Used provided code for formatting, but changed the code to replace column and row number with corresponding character instead
    
    listX = ['0'] + list(X_Axis)
    listY = ['0'] + list(Y_Axis)
    
        # Do heading
    print("     ", end="")

    for j in range(len(M[0])):
        print("%5s " % listY[j], end="")
    print()
    print("     ", end="")
    for j in range(len(M[0])):
        print("------", end="")
    print()
    # Matrix contents
    for i in range(len(M)):
        print("%3s |" % listX[i], end="") # Row nums
        for j in range(len(M[0])):
            print("%5s " % (M[i][j]), end="")
        print()  
        
## Collects to strings and returns their edit distance
# Storing in a matrix will be a different ballgame 

def edit_dist(X_axis, Y_axis):
    #first find lengths
    len_X_Ax = len(X_axis)
    len_Y_Ax = len(Y_axis)
    
    MATRIX = [[None]*(len_Y_Ax+1) for i in range(len_X_Ax+ 1)]
    '''
    Description of how this matrix functions:
    if N is "HELLO"
    and M is "ELLO"
    The corresponding matrix would look like this:
    [ 
          0     H      E    L      L    O
    0:  [None, None, None, None, None, None], 
    E:  [None, None, None, None, None, None], 
    L : [None, None, None, None, None, None], 
    L : [None, None, None, None, None, None], 
    O : [None, None, None, None, None, None]    
    ]
    **Note, I added in the letters for reference only, in the actual code these are not present.
    
    This gives us a tuple for each possible combination of Letters
    That we can then populate by iterating over each row and column
    of the words to populate the matrix instead of running the problem
    recursively. 
'''
    #now that the matrix is defined, we will iterate through every cell:
    for X in range(1+ len_X_Ax):
        for Y in range(1+len_Y_Ax):
            if X == 0 or Y == 0:
                MATRIX[X][Y] = 0
            elif X_axis[X-1] == Y_axis[Y-1]:
                MATRIX[X][Y] = MATRIX[X-1][Y-1]+1
            else:
                MATRIX[X][Y] = max(MATRIX[X-1][Y], MATRIX[X][Y-1])
    
    print("+--- Comparing", X_axis, "and", Y_axis, "---+")
    print('Matrix: ')
    format_print_matrix(MATRIX, X_axis, Y_axis)
    print("\nLength:")
    
    print("The length of the LCS is:", MATRIX[X][Y])
    
    #check if either is zero
    #if len_n == 0 or len_m == 0:
     #   return 0
    
    #if string_m[len_n]
    
    

edit_dist(str(sys.argv[1]),str(sys.argv[2]))
