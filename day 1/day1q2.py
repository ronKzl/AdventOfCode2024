left_list = []

#track value in the second list
map = {}
#read the file again and populate the map
with open('day1q1.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        line.strip()
        left, right = line.split()
        left_list.append(int(left))
        if int(right) in map:
            map[int(right)] += 1
        else:
            map[int(right)] = 1

sim_score = 0
#O(n)
for id in left_list: 
    num_appearance = map[id] if id in map else 0
    sim_score += id * num_appearance
print(sim_score)