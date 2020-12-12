# First started by writing loop to add an subtract from max and mins
# but decided to go with emulating the conversion string to binary and
# converion to base 2

def find_row(code):
    rowLet = code[0:7]

    row = 0
    power = 0
    for letter in reversed(rowLet):
        if(letter == "B"):
            row += 2 ** power

        power += 1

    return(row)

def find_col(code):
    colLet = code[-3:]

    col = 0
    power = 0
    for letter in reversed(colLet):
        if(letter == "R"):
            col += 2 ** power

        power += 1

    return(col)

def seat_num(row, col):
    return((row * 8) + col)

def get_list_seats():
    with open("input.txt") as file:
        seats = []
        for seat in file:
            row = find_row(seat.strip())
            col = find_col(seat.strip())
            seats.append(seat_num(row, col))

    return(seats)

def find_seat(max, seats):
    missing = []

    for num in range(0, max):
        if(num - 1 in seats and num not in seats and num + 1 in seats):
            missing.append(num)

    return(missing)

seats = get_list_seats()

missing = find_seat(max(seats), seats)

print(missing)