import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def print_directory_structure(path, level=0):
    try:
        dir_path = Path(path)
        if not dir_path.exists() or not dir_path.is_dir():
            print(f"Error: '{path}' is not a valid directory.")
            return

        for item in dir_path.iterdir():
            indent = '    ' * level  
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}")
                print_directory_structure(item, level + 1) 
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python 03.py /path/to/directory")
        return

    directory_path = sys.argv[1]
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
