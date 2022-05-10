import shutil
import os


# preliminary check to see if the path exists within the file system
def check_path(string):
    while True:
        path = str(input(string))
        if os.path.exists(path):
            return path
        print("Error: That path does not exist")


def move_file(source_path, destination_path):
    if source_path == destination_path:
        print("File is already in this directory")
        return
    else:
        shutil.move(source_path, destination_path)
        print(f"File has been moved to {destination_path}")
        return


def add_folder(name, parent_directory):
    split_up = parent_directory.split("/")
    if split_up[-1] == name:
        print("Directory already made")
    else:
        os.mkdir(parent_directory, name)
        print("Directory has been made")


def delete_file(path):
    os.remove(path)
    print("File has been removed")


def copy_file(source_path, destination_path):
    if source_path == destination_path:
        print("File is already in this directory")
        return
    else:
        shutil.copy(source_path, destination_path)
        print(f"File has been copied to {destination_path}")
        return


def find_file(filename, path):
    files = os.listdir(path)
    if filename in files:
        print("File has been found in this directory")
    else:
        print("File was not found, try again")


def prompt_user():
    print("Welcome to the File Manager")
    print()
    print("1. Move File")
    print("2. Add Folder")
    print("3. Delete File")
    print("4. Copy File")
    print("5. Find File")
    print("x. Exit")
    print()


def user_input():
    choice = int(input("Enter your choice:"))
    if choice == 1:
        source = check_path("Enter the name of the path you want to move: ")
        destination = check_path("Enter the name of the path you want to send it to: ")
        move_file(source, destination)
    elif choice == 2:
        name = str(input("Enter the name of this new folder: "))
        parentDirectory = check_path(
            "Enter the name of the directory you want to add this to: "
        )
        add_folder(name, parentDirectory)
    elif choice == 3:
        source = check_path(
            "Enter the name of the file that you want to remove (add the path): "
        )
        delete_file(source)
    elif choice == 4:
        source = check_path("Enter the name of the path you want to move: ")
        destination = check_path("Enter the name of the path you want to copy it to: ")
        copy_file(source, destination)
    elif choice == 5:
        filename = str(input("Enter the name of the folder you want to find: "))
        path = check_path("Enter the path where it should be: ")
        find_file(filename, path)
    else:
        return -1


def main():
    while True:
        prompt_user()
        user_input()
        if user_input() == -1:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
