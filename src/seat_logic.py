seat_letters = ['A', 'B', 'C', 'D', 'E', 'F']
rows = 4
cols = 6
seat_list = [[f'{seat_letters[col]}{row + 1}' for col in range(cols)] for row in range(rows)]

def display_seats(seat_list):
  for row in seat_list:
    print(" ".join(row))

def mark_seat(seat_list, seat, seat_letters):
  row = int(seat[1:]) - 1
  col = seat_letters.index(seat[0])
  if seat_list[row][col] == 'X':
    return False
  seat_list[row][col] = 'X'
  return True
