import shutil         
import os

#preliminary check to see if the path exists within the file system
def checkPath(string):
    while True:
        path = str(input(string))
        if os.path.exists(path):
            return path
        print('Error: That path does not exist')

def moveFile(sourcePath, destinationPath):
    if sourcePath == destinationPath:
        print("File is already in this directory")
        return
    else:
        shutil.move(sourcePath, destinationPath)
        print(f'File has been moved to {destinationPath}')
        return

def addFile(destinationPath):
    pass

def deleteFile(destinationPath):
    os.remove(destinationPath)

def copyFile(sourcePath, destinationPath):
    pass

def promptUser():
    print('Welcome to the File Manager')
    print()
    print('1. Move File')
    print('2. Add File (Only text files)')
    print('3. Delete File')
    print('4. Copy File')
    print('5. Find File')
    print()

def userInput():
    choice = int(input("Enter your choice:"))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass 

def main():
    promptUser()
    userInput()

if __name__ == "__main__":
    main()