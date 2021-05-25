

#on AtBSWP's Position 164(according to Calibre's epub viewer)
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#Tests???
#y = vertical = grid
#x = horizontal = grid[1]
#Define in what loop we are
loop = 0

#for y in grid[loop]
for y in range(len(grid[loop])):

    #for x in grid size
    for x in range(len(grid)):
        
        #prints grid[x(horizontal) y(vertical)], since 'grid' list is 'reversed'
        print(grid[x][y], end="")
    loop =+ 1
    print()
