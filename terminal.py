import os


def list_dirs():
    for dir in os.scandir():
        print(dir.name)


def cd(command: str):
    if command == '..':
        os.chdir('..')
    else:
        try:
            new_dir = os.path.join(os.curdir, command)
            os.chdir(new_dir)
        except FileNotFoundError as e:
            print("Error! No such path!")


def create(new_file: str):
    file = open(new_file, mode='x')
    file.close()


def delete(command: str):
    try:
        os.remove(command)
    except FileNotFoundError as e:
        print("Error! No such file in the current directory!")


def rename(old_file: str, new_file: str):
    try:
        os.rename(old_file, new_file)
    except FileNotFoundError as e:
        print("Error! No such file in the current directory!")


def open_file(file_name: str):
    try:
        with open(file_name, 'r') as file:
            print("File was opened successfully!")
    except FileNotFoundError as e:
        print("Error! No such file in the current directory!")


def start():
    print("Welcome to the terminal!\nList of commands: ls, cd, create, delete, rename, open, end")
    while True:
        # ex: ['cd', 'some_dir'] where 2nd entity may be empty if 'ls' is given
        command = input().split()
        match command[0]:
            case "ls":
                list_dirs()
            case "cd":
                cd(command=command[1])
            case "create":
                create(command[1])
            case "delete":
                delete(command[1])
            case "rename":
                # command[1] is an old file name, command[2] is a new file name
                rename(command[1], command[2])
            case "open":
                open_file(command[1])
            case "end":
                break
            case _:
                print("Invalid command!")


if __name__ == '__main__':
    start()
