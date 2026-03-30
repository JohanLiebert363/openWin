import subprocess
from pathlib import Path

script_path = Path(__file__).resolve()
print(f"Script file path: {script_path}")


script_dir = script_path.parent
print(f"Script directory: {script_dir}")

directory = script_dir
ask  = int(input("how many times to open cmd >> "))
def find_file(directory):
        subprocess.Popen(f'start cmd /K "cd {directory}"', shell=True)
def open_cmd(ask):
    for i in range(ask):
        print(f"Opening cmd window {i} and executing 'dir /s'...")

        subprocess.Popen(f'start cmd /K "dir /s {directory}"', shell=True)
        # cd C:\Users\vpbg-ucenik08\Desktop
        # C:/Users/vpbg-ucenik08/AppData/Local/Programs/Python/Python313/python.exe print.py
def run_file(script_path):
    subprocess.Popen(f'start cmd /K "python {script_path}"', shell=True)
def main():
     print("OpenWin")
     options = [
          "1. find file",
          "2. run file",
          "3. open cmd",
          "4. run all",
     ]
     print(options)
     print("What to run (type the number) ")
     ask_command = (input("\>>> "))
     if ask_command == "1" or "1.":
          find_file(directory)
     elif ask_command == "2" or "2.":
          run_file(script_path)
     elif ask_command == "3" or "3.":
          open_cmd(ask)
     elif ask_command == "4" or "4.":
        find_file(directory)
        run_file(script_path)
        open_cmd(ask)
while True:
    main()
