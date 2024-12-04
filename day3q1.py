# Initialize a list to store results
result = []

with open("day3q1.txt", "r") as file:
    for line in file:
        index = 0
        while (index := line.find("mul(", index)) != -1:
            # Move past the "mul" occurrence
            index += len("mul(")
            
            # Get the next 8 characters after "mul()" cuz xxx,yyy)
            following = line[index:index + 8]
            result.append(following)
multiplier = 0
for entry in result:
    #try and read to see if its valid so first 1-3 spots may be a number then a , then another 1-3 number and then must end with )
    #we can then mult the numbers and add to result
    num1 = ""
    num2 = ""
    sawColon = False
    sawClosing = False
    wayToBig = False
    count = 0
    for char in entry:
        if char.isnumeric():
            if sawColon:
                num2 += char
                count += 1
                if count > 6:
                    wayToBig = True
                    break
            else:
                num1 += char
                count += 1
                if count > 3:
                    wayToBig = True
                    break
        elif char == ",":
            sawColon = True
        elif char == ")":
            sawClosing = True
            break
    if sawColon and sawClosing and num1 and num2 and not wayToBig: #proper format achieved
        multiplier = multiplier + (int(num1) * int(num2))    
print(multiplier)