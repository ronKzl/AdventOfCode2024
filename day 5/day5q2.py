import collections
#map key : list where key is the number and list is all the numbers that must come after it
map = collections.defaultdict(list)
res = 0
res2 = 0

#O(n^2) with 2 pointers if the number Y at 1 is after number X but its not in X rules its a violation so reorder them
#can be more violations like this so restart the loop from the start maybe possible in O(n) with backtracking but this one is easier to code up
def fixWrongPrint(line,map):
    i = 0
    j = 1
    while j < len(line):
        if line[j] not in map[line[i]]:
            line[i], line[j] = line[j], line[i]
            i = 0
            j = 1
            continue
        else:
            i += 1
            j += 1    
    
    return int(line[((len(line)-1)//2)]) 

#O(n^3) overall cuz 3 nested for loops that on worst case go over n number
#space is O(n) with the map and set
with open('day5q1.txt', 'r') as file:
    isBreak = False
    for line in file:
        line = line.strip()
        if line == "":
            isBreak = True
            continue
        if not isBreak:
            start, end = line.split("|")
            map[start].append(end)
        if isBreak:
            line = line.split(",")
            visited = set()
            isWrong = False
            for number in line:
                #if we did not see any of the post numbers in visited then the ordering is currently good
                for val in map[number]:
                    if val in visited:
                        isWrong = True
                        break
                if isWrong:
                    break
                else:
                    visited.add(number) #add this number to list of visited
            if not isWrong:
                #if we did not see X that was supposed to be after Y according to rules add the middle element of line to res
                res +=  int(line[((len(line)-1)//2)]) 
            if isWrong: #if violations is deteced fix it and add to the result
                res2 += fixWrongPrint(line,map)
print(res2)
