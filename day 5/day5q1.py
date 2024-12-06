import collections
#map key : list where key is the number and list is all the numbers that must come after it
map = collections.defaultdict(list)
res = 0
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
                        isWrong = True #order is violated since we have X such that in its rules we found a Y that came before it instead of after
                        break
                if isWrong:
                    break
                else:
                    visited.add(number) #add this number to list of visited
            if not isWrong:
                #if we did not see X that was supposed to be after Y according to rules add the middle element of line to res
                res +=  int(line[((len(line)-1)//2)]) 
print(res)
