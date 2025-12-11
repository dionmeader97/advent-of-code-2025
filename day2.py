invalid_ids = []

with open("day2_input.txt") as f:
    line = f.readline().strip()
    ranges = [tuple(map(int, part.split("-"))) for part in line.split(",")]

    for a, b in ranges:
        length_a = len(str(a))
        length_b = len(str(b))

        for l in range(length_a, length_b + 1):
            if l % 2 != 0:
                continue

            half = l // 2
            s_start = 10 ** (half - 1)
            s_end = 10 ** half  

            for s in range(s_start, s_end):
                n = int(str(s) * 2)
                if a <= n <= b:
                    invalid_ids.append(n)

print("The sum of all invalid IDs is:", sum(invalid_ids))

