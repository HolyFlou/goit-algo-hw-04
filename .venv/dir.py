from colorama import Fore, Style
from pathlib import Path
def get_dir(path, level = 0):
    directory = Path(path)
    for path in directory.iterdir():
        if path.is_dir():
            print(Fore.BLUE + "\t"*level, f"{path.parts[-1]}/")
            get_dir(path, level+1)  
        else:
            print(Fore.GREEN + "\t"*level, path.parts[-1] + Style.RESET_ALL)