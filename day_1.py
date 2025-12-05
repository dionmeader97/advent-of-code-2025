starting_value = 50
password = ""

with open("day1_input.txt") as file:
    lines = file.readlines()
    current_value = starting_value
    zero_count = 0
    

    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        distance_range = range(distance)

        for distance_index in distance_range:
            if direction == "R":
                current_value += 1
                if current_value == 100:
                    current_value = 0
            elif direction == "L":
                current_value -= 1
                if current_value == -1:
                    current_value = 99

            if current_value == 0:
                zero_count += 1

password = str(zero_count)
print("The password is:", password)
