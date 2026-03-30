import subprocess
from pathlib import Path
import sys

script_path = Path(__file__).resolve()
directory = script_path.parent

def find_file(directory):
     

     print(directory
     )

def open_cmd(ask, directory):
    for i in range(ask):
        print(f"Opening cmd window {i+1}...")
        subprocess.Popen(f'start cmd /K "dir /s "{directory}""', shell=True)

def run_file(script_path):

    subprocess.Popen(f'start cmd /K "{sys.executable} "{script_path}""', shell=True)

def main():
    print("\n--- OpenWin ---")
    options = ["1. find file", "2. run file", "3. open cmd", "4. run all"]
    print("\n".join(options))
    
    ask_command = input("What to run (type the number) >>> ").strip()


    if ask_command in ["1", "1."]:
        find_file(directory)
        print(directory)
    elif ask_command in ["2", "2."]:
        run_file(script_path)
    elif ask_command in ["3", "3."]:
        ask = int(input("How many times to open cmd >> "))
        open_cmd(ask, directory)
    elif ask_command in ["4", "4."]:
        ask = int(input("How many times to open cmd >> "))
        find_file(directory)
        run_file(script_path)
        open_cmd(ask, directory)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    while True:
        main()
