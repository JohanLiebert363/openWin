import subprocess
from pathlib import Path
import sys
from rich import print
from rich.prompt import Prompt
from pyfiglet import Figlet


script_path = Path(__file__).resolve()
directory = script_path.parent
f = Figlet(font='slant')            # try 'slant','banner','standard'
print(f.renderText('WinOpen'))

print("[cyan]What to run[/cyan]\n")
ask = Prompt.ask("[red]>>> [/red]")
print("[cyan]Where is it (directory)[/cyan]\n")
ask2 = Prompt.ask("[red]>>> [/red]")
def open_cmd(ask, ask2):
    pass
def main():


    options = ["[blue]1. run all[/blue]"]
    print("\n".join(options))
    
    ask_command = input("What to run (type the number) >>> ").strip()


    if ask_command in ["1", "1."]:
        open_cmd(ask, directory, script_path)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    while True:
        main()
