import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_folder_structure(path):
    
    for el in path.iterdir():
        indent=0
        if el.is_dir():
            print(f"{' ' * indent}{Fore.BLUE}{el.name}{Style.RESET_ALL}/")
            print_folder_structure(el, indent + 4)
        else:
            print(f"{' ' * indent}{Fore.GREEN}{el.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print("Необхідно вказати шлях до директорії")
        sys.exit(1)
    path = Path(sys.argv[1])

    if not path.exists():
        print("Такого шляху не існує")
        sys.exit(1)

    if not path.is_dir():
        print(f"{path} не є директорією")
        sys.exit(1)

    print_folder_structure(path)

if __name__ == "__main__":
    main()
