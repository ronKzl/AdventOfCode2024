#brute force
#build a matrix

count = 0
ROWS = 140
COLS = 140
matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
with open('day4q1.txt', 'r') as file:
    # Read each line in the file
    row = 0
    for line in file:
        line = line.strip()
        col = 0
        for char in line:
            matrix[row][col] = char
            col += 1
        row += 1

#loop until we find X
#check in all 8 directions for an M
#for the direction we see an M see if we can go twice in that direction with OOB
#if that so check that its followed with A and then S -> it is increment count

directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)] #up, down, left, right, up + left, up + right, down + left, down + right
#Time O(n^2) for every spot check into 8 directions for the word probably a better way with DFS/BFS that I am not seeing
for r in range(COLS):
    for c in range(ROWS):
        if matrix[r][c] == "X":
            for row, col in directions:
                if r + row >= 0 and c + col >= 0 and r + row < ROWS and c + col < COLS: #if its in bounds
                    if matrix[r + row][c+col] == "M": #if it is indeed equals M
                        if r + (3*row) >= 0 and c + (3*col) >= 0 and r + (3*row) < ROWS and c + (3*col) < COLS: #if the next 2 spots in this direction are in bounds
                            if matrix[r + (2*row)][c+ (2*col)] == "A" and matrix[r + (3*row)][c+ (3*col)] == "S": #if they equal A and S respectively
                                count += 1
print(count)