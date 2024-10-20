import tkinter as tk
from tkinter import messagebox
from src.seat_logic import seat_list, seat_letters, mark_seat

rows = 4
cols = 6

def select_seat():
  seat = seat_entry.get().upper()
  if len(seat) == 2 and seat[0] in seat_letters and seat[1].isdigit() and int(seat[1]) <= rows:
    success = mark_seat(seat_list, seat, seat_letters)
    if success:
      update_seat_display()
    else:
      messagebox.showerror("Error", f"Seat {seat} is already taken.")
  else:
    messagebox.showerror("Error", "Invalid seat selection.")

def update_seat_display():
  for row in range(rows):
    for col in range(cols):
      seat_label = seat_labels[row][col]
      seat_value = seat_list[row][col]
      seat_label.config(text=seat_value)

      if seat_value == 'X':
        seat_label.config(bg="red", fg="white")

def main():
  global seat_labels, seat_entry

  root = tk.Tk()
  root.title("Seat Selector")
  root.resizable(False, False)
  root.configure(bg='lightblue')

  seat_labels = []
  for row in range(rows):
    row_labels = []
    for col in range(cols):
      seat_value = seat_list[row][col]
      seat_label = tk.Label(root, text=seat_value, width=8, height=3, font=("Arial", 14))
      seat_label.grid(row=row, column=col, padx=5, pady=5)
      row_labels.append(seat_label)
    seat_labels.append(row_labels)

  seat_entry = tk.Entry(root, font=("Arial", 12))
  seat_entry.grid(row=rows + 1, column=0, columnspan=3)

  submit_button = tk.Button(root, text="Select Seat", font=("Arial", 12), width=10, height=2, command=select_seat)
  submit_button.grid(row=rows + 1, column=3, columnspan=3)

  root.mainloop()
