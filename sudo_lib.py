from random import sample

def gen_blank_sudoku():
    '''Return 9x9 matrix of 0'''
    
    return [[0 for i in range(1,10)] for i in range(9)]

def gen_sudoku():
    '''Return 9x9 sudoku'''
    
    sudo = gen_blank_sudoku()
    sudoku_filler(sudo, True)
    return sudo

def gen_puzzul(level):
    '''Return a sudoku not full and its solution'''
    
    coords = [(x,y) for x in range(9) for y in range(9)]
    choosen_vars = sample(coords, k=(level+1)*10)
    sudo = gen_sudoku()
    return [[sudo[i][j] if (i,j) in choosen_vars else 0 for j in range(len(sudo))] for i in range(len(sudo))] , sudo

def _can_col(n, s, c):
    '''Test if a column contain already the number'''
    
    return not n in [s[i][c[1]] for i in range(0,9)]

def _can_row(n, s, c):
    '''Test if a row contain already the number'''
    
    return not n in s[c[0]]

def _can_square(n, s, c):
    '''Test if a 3x3 region contain already the number'''
    
    x = (c[0]//3)*3
    y = (c[1]//3)*3
    return not n in [s[i][j] for i in range(x,x+3) for j in range(y, y+3)]

def _can_num(n, s, c):
    '''Test if a number can be placed at tthe coord'''
    
    return _can_col(n, s, c) and _can_row(n, s, c) and _can_square(n, s, c)

def sudoku_filler(s, is_rand):
    '''Solve a sudoku'''
    
    if _back_s(s, 0, -1, is_rand):
        return s
    else:
        return 'no solution found'

def _back_s(s, curr_x, curr_y, is_rand):
    '''Backtracking function to solve the sudoku'''
  
    if curr_x == curr_y == 8 :
        return True

    new_x, new_y = 0,0
    if curr_y >= 8:
        new_y = 0
        new_x = curr_x + 1
    else:
        new_y = curr_y + 1
        new_x = curr_x

    if s[new_x][new_y] == 0:
        num_range = sample(range(1,10), k=9) if is_rand else range(1,10)
        for i in num_range:
            if _can_num(i, s, (new_x, new_y)):
                s[new_x][new_y] = i
                if _back_s(s, new_x, new_y, is_rand):
                    return True
            
        s[new_x][new_y] = 0
    else:
        if _back_s(s, new_x, new_y, is_rand):
            return True
    
    return False

def displayer(p):
    '''Display matrix'''
    if type(p) == list:
        for i in p:
            print(i)
    elif type(p) == tuple:
        for i in p:
            displayer(i)
            print()
    else:
        print(p)
    
if __name__ == '__main__':
    displayer(gen_puzzul(1))