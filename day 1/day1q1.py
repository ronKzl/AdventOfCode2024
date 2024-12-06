left_list = []
right_list = []
#read the file and put the first val into left second into right
with open('day1q1.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        line.strip()
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

#O(nlogn)
left_list.sort()
right_list.sort()

diff = 0
#O(n)
for i in range(len(right_list)):
    diff += abs(left_list[i]-right_list[i])
print(diff)