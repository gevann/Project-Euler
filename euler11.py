#!/usr/bin/python

#INPUT: Matrix of ints, M
#OUTPUT: the largest sum of 4 consective numbers in M
#        along the left-right diagonal
def max_LR(M):
    l=g(biggest_four_row(LR_diag_as_row(M,0, 0 )))
    for x in range(1,19):
        m =g(biggest_four_row(LR_diag_as_row(M,x, 0 )))
        l = max( l, m)
    for y in range(1, 19):
        m =g(biggest_four_row(LR_diag_as_row(M,0, y )))
        l = max( l, m)
    return l
#INPUT: Matrix of ints, M
#OUTPUT: the largest sum of 4 consective numbers in M
#        along the right-left diagonal
def max_RL(M):
    l=g(biggest_four_row(RL_diag_as_row(M,len(M)-1, len(M)-1)))
    for i in reversed(range(0,len(M))):
        u = biggest_four_row(RL_diag_as_row(M,i,len(M)-1))
        m =g(u)
        l = max( l, m)
    for j in reversed(range(0,len(M)-1)):
        u = biggest_four_row(RL_diag_as_row(M,0,j))
        m = g(u)
        l = max( l, m)
    return l

#INPUT: Matrix of ints, M
#OUTPUT: The largest sum of 4 consecutive numbers in M
#       along the x axis
def max_horz(M):
    l=reduce(lambda x,y: x*y, biggest_four_row(M[0]))
    for y in range(1,20):
        m = reduce(lambda x,y: x*y, biggest_four_row(M[y])) 
        l = max(l,m)
    return l

#INPUT: Matrix of ints, M
#OUTPUT: The largest sum of 4 consecutive numbers in M
#       along the y axis
def max_vert(M):
    l= g( biggest_four_row( send_col_as_row(M, 0)  ))
    for y in range(1,20):
        m = g(biggest_four_row(send_col_as_row(M, y))) 
        l = max(l,m)
    return l

#INPUT: A list, z
#OUTPUT: A scalar of each element of Z multiplied together.
#DETAILS: This was used mostly to save typing of reduce and
#       and lambda.
def g(z):
    return reduce(lambda x, y: x*y, z)

#INPUT: A row of integers
#OUTPUT: A list of the largest 4 consective numbers in the row
def biggest_four_row( row ):
    if isinstance( row, list ): 
        if len(row) < 4:
            return [0]
        elif len(row) == 4:
            return row
        else:
            L = row[0:4]
            for x in range(4, len(row)):
                N = row[x:x+4]
                if g(N) > g(L):
                    L = N
            return L
    else:
        raise ValueError("Row must be a list")

#INPUT: A matrix of ints, M
#OUTPUT: A row of integers taken from a column of M
def send_col_as_row (M, col_num):
    L = []
    for row in M: 
        L.append(row[col_num] )
    return L

#INPUT: A matrix of ints, M
#OUTPUT: A row of integers take from the left-right diagonal of M
#       starting at M[i][j]
def LR_diag_as_row ( M, i, j ):
    L = []
    while i < len(M) and j < len(M):
        L.append(M[i][j])
        i=i+1
        j=j+1
    return L

#INPUT: A matrix of ints, M
#OUTPUT: A row of integers take from the right-left diagonal of M
#       starting at M[i][j]
def RL_diag_as_row (M, i, j):
    L = []
    while i<len(M) and j >= 0:
        L.append(M[i][j])
        i=i+1
        j=j-1
    return L

#INPUT: Four integers, A, B, C, D
#OUTPUT: The maximum integer
#DETAILS: This is for readability only.
def show_greatest_prod(A,B,C,D):
    print max(A, B, C, D)

#INPUT: A matrix, M
#OUTPUT: The maximum valued 4-tuple under multiplication
#       along the x, y, y=z, and y=-x axii
#DETAILS: Throws an error if M not made of ints.
def euler11(M):
    if isinstance(M,list) and isinstance(M[0], list) and isinstance(M[0][0], int):
        show_greatest_prod( max_horz(l), max_LR(l), max_RL(l), max_vert(l))
    else:
        raise ValueError("Invalid parameter. Must be a matrix of integers.")

if __name__ == "__main__":
    with open("euler11_data.txt", "r") as data:
        l = []
        for line in data:
            subl = line.strip().split(" ")
            l.append(subl)
    for x in l:
        for index, item in enumerate(x):
            x[index] = int(item)

    euler11(l)
