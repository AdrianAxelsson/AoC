with open("input.lst") as f:
    input = f.read().splitlines()
seats = []
for line in input:
    seat_row = {
    "min": 0,
    "max": 127
    }
    seat_col = {
        "min": 0,
        "max": 7
    }

    i = 0
    for char in line:
        if i < 7:
            if char == "F":
                seat_row["max"] = (seat_row["max"] + seat_row["min"] - 1) / 2
            elif char == "B":
                seat_row["min"] = (seat_row["max"] + seat_row["min"] + 1) / 2
        else:
            if char == "L":
                seat_col["max"] = (seat_col["max"] + seat_col["min"] - 1) / 2
            elif char == "R":
                seat_col["min"] = (seat_col["max"] + seat_col["min"] + 1) / 2
        i += 1
    seat = int(seat_row["max"] * 8 + seat_col["max"])
    seats.append(seat)

seats.sort()
print(seats[-1])
