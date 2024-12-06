#This time A is the center and diagonaly above and below needs to be S or M 
# 0 1 2
# . A . 
# 0 1 2

#Kinda like the leetcode sudoku question where a 3 x 3 area is checked
#If 0,0 is M then its diagonal inverse 2,2 must be S 
#If 0,2 is S then its diagonal inverse must be M
#A is at (1,1) so need to check (0,0) (0,2) (2,0) (2,2) which is (-1,-1), (-1,1), (1,-1), (1,1)
#(0,0) and (2,2) are together so (-1,-1) to (1,1) must be A or M and opposite
#(0,2) and (2,0) are together so (-1,1) to (1,-1) must be A or M and opposite as well

#Otherwise strat is the same for this look for A then check that the 4 spots in bounds then check them 
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

directions = [(-1,-1), (-1,1), (1,-1), (1,1)] 
#O(n^2) again and direction check is only loops 4 times this time. This one not sure DFS/BFS will work since looking for a specific X pattern
#but maybe there is an approach that works by looking at the problem from a different approach.
for r in range(COLS):
    for c in range(ROWS):
        if matrix[r][c] == "A":
            inBounds = 0
            doesItMatch = True
            for row, col in directions:
                if r + row >= 0 and c + col >= 0 and r + row < ROWS and c + col < COLS: #if its in bounds
                    inBounds += 1
            #only if all 4 are in bounds can we check
            if inBounds == 4:
                print("here")
                if matrix[r-1][c-1] == "S" and matrix[r+1][c+1] == "M" or matrix[r-1][c-1] == "M" and matrix[r+1][c+1] == "S":
                    if matrix[r-1][c+1] == "S" and matrix[r+1][c-1] == "M" or matrix[r-1][c+1] == "M" and matrix[r+1][c-1] == "S":
                        count += 1
print(count)

