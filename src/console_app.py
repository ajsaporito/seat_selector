import os
from src.seat_logic import seat_list, seat_letters, rows, display_seats, mark_seat

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def main():
  choice = ""

  while choice != 'q':
    display_seats(seat_list)
    seat = input("Select a seat or 'q' to quit: ").upper()

    if (
      len(seat) == 2
      and seat[0] in seat_letters
      and seat[1].isdigit()
      and int(seat[1]) <= rows
      and seat in [item for sublist in seat_list for item in sublist]
    ):
      mark_seat(seat_list, seat, seat_letters)
      clear()
    elif seat == 'Q':
      choice = 'q'
    else:
      clear()
      print("Invalid seat. Please enter an available seat.")

if __name__ == "__main__":
  main()
