row, col = 5, 5
start_row = row/2
start_col = col/2

grid = [[[] for x in range(row)] for y in range(col)]

trav_row = 0
trav_col = col
for num in range(col, 0, -2):
    
        grid[trav_row][trav_col - 1] = num ** 2    
        trav_row += 1
        trav_col -= 1

for line in grid:
    print line