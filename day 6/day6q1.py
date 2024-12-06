
ROWS = 130
COLS = 130
matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
move_map = {"^" : [-1,0], ">": [0,1], "v": [1,0], "<": [0,-1]}
guard_direction = "^" #initaly up
guard_pos = None #know the initial guard position
crates = set() #know where all the crates are
visited = set()
#Time O(N*M)
with open('day6q1.txt', 'r') as file:
    # Read each line in the file
    row = 0
    for line in file:
        line = line.strip()
        col = 0
        for char in line:
            if char == "^":
                guard_pos = (row,col)
            if char == "#":
                crates.add((row,col))
            matrix[row][col] = char
            col += 1
        row += 1

def rotateGuard():
    global guard_direction
    if guard_direction == "^":
        guard_direction = ">"
    elif guard_direction == ">":
        guard_direction = "v"
    elif guard_direction == "v":
        guard_direction = "<"
    else:
        guard_direction = "^"


while guard_pos[0] >= 0 and guard_pos[1] >= 0 and guard_pos[0] < ROWS and guard_pos[1] < COLS:
    temp_guard_pos = (guard_pos[0] + move_map[guard_direction][0], guard_pos[1] + move_map[guard_direction][1])
    if temp_guard_pos in crates:
        rotateGuard()
        continue
    else:
        matrix[guard_pos[0]][guard_pos[1]] = "X"
        visited.add(temp_guard_pos) #will count all the X's
        guard_pos = temp_guard_pos       

print(len(visited))

    