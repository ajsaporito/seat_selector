import sys
import os
from src.console_app import main as console_main
from src.tkinter_app import main as tkinter_main

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    mode = sys.argv[1].lower()
    if mode == "gui":
      tkinter_main()
    elif mode == "console":
      console_main() 
    else:
      print("Invalid argument. Use 'console' to run the console version or 'gui' to run the GUI version.")
  else:
    print("Please specify 'console' or 'gui'.")
