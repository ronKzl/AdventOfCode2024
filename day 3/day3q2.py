# Initialize a list to store results
result = []

with open("day3q1.txt", "r") as file:
    mul_enabled = True
    for line in file:
        i = 0
        while i < len(line):
            # Check for "do()"
            if line[i:i + 4] == "do()":
                mul_enabled = True
                i += 4  # Move past this instruction

            # Check for "don't()"
            elif line[i:i + 7] == "don't()":
                mul_enabled = False
                i += 7  # Move past this instruction
            # Check for "mul"
            elif line[i:i + 4] == "mul(" and mul_enabled:
                # Extract the 9 characters after "mul"
                following = line[i + 4:i + 12]  # Adjust to capture exactly 9 characters
                result.append(following)  # Add cleaned result
                i += 3  # Move past "mul"
            else:
                i += 1  # Move to the next character
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