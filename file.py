import shutil
import os

# preliminary check to see if the path exists within the file system
def checkPath(string):
    while True:
        path = str(input(string))
        if os.path.exists(path):
            return path
        print("Error: That path does not exist")


def moveFile(sourcePath, destinationPath):
    if sourcePath == destinationPath:
        print("File is already in this directory")
        return
    else:
        shutil.move(sourcePath, destinationPath)
        print(f"File has been moved to {destinationPath}")
        return


def addFolder(name, parentDirectory):
    splitUp = parentDirectory.split("/")
    if splitUp[-1] == name:
        print("Directory already made")
    else:
        os.mkdir(parentDirectory, name)
        print("Directory has been made")


def deleteFile(path):
    os.remove(path)
    print("File has been removed")


def copyFile(sourcePath, destinationPath):
    if sourcePath == destinationPath:
        print("File is already in this directory")
        return
    else:
        shutil.copy(sourcePath, destinationPath)
        print(f"File has been copied to {destinationPath}")
        return


def findFile(filename, path):
    files = os.listdir(path)
    if filename in files:
        print("File has been found in this directory")
    else:
        print("File was not found, try again")


def promptUser():
    print("Welcome to the File Manager")
    print()
    print("1. Move File")
    print("2. Add Folder")
    print("3. Delete File")
    print("4. Copy File")
    print("5. Find File")
    print("x. Exit")
    print()


def userInput():
    choice = int(input("Enter your choice:"))
    if choice == 1:
        source = checkPath("Enter the name of the path you want to move: ")
        destination = checkPath("Enter the name of the path you want to send it to: ")
        moveFile(source, destination)
    elif choice == 2:
        name = str(input("Enter the name of this new folder: "))
        parentDirectory = checkPath(
            "Enter the name of the directory you want to add this to: "
        )
        addFolder(name, parentDirectory)
    elif choice == 3:
        source = checkPath(
            "Enter the name of the file that you want to remove (add the path): "
        )
        deleteFile(source)
    elif choice == 4:
        source = checkPath("Enter the name of the path you want to move: ")
        destination = checkPath("Enter the name of the path you want to copy it to: ")
        copyFile(source, destination)
    elif choice == 5:
        filename = str(input("Enter the name of the folder you want to find: "))
        path = checkPath("Enter the path where it should be: ")
        findFile(filename, path)
    else:
        return -1


def main():
    while True:
        promptUser()
        userInput()
        if userInput() == -1:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
