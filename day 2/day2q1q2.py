safe = 0

def check(input):
    isAsc = int(input[1]) > int(input[0])
    isDesc = int(input[1]) < int(input[0])
    i = 1
    works = True
    i = 1
    j = 0
    while i < len(input):
        diff = abs(int(input[i-1])-int(input[i]))
        if diff > 0 and diff < 4:
            if isAsc and int(input[i]) > int(input[i-1]):
                j = i
                i += 1
                continue
            elif isDesc and int(input[i-1]) > int(input[i]):
                j = i
                i += 1
                continue
            else:
                works= False
                break
        else:
            works = False
            break      
    return works

#Time Compelxity: n * n * n so worst O(n^3)

with open('day2q2.txt', 'r') as file:
    # Read each line in the file
    for line in file: #O(n)
        line.strip()
        input = line.split()
        if check(input): #O(n)
            safe += 1
        else:
            #try to remove 1 number from input and check again
            for i in range(len(input)): #O(n)
                arr = input[:i] + input[i + 1:]
                if check(arr): #O(n)
                    safe += 1
                    break
print(safe)