from pathlib import Path
import os


def readfileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")


def createfile():
    try:
        readfileandfolder()

        name = input("Please tell your file name:- ")

        if not name.endswith(".txt"):
            name += ".txt"

        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file:- ")
                fs.write(data)

            print("File created successfully")
        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occurred: {err}")


def readfile():
    try:
        readfileandfolder()

        name = input("Which file do you want to read:- ")

        if not name.endswith(".txt"):
            name += ".txt"

        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()

            print("\nFile Content:")
            print(data)
            print("\nFile read successfully")

        else:
            print("The file does not exist")

    except Exception as err:
        print(f"An error occurred: {err}")


def updatefile():
    try:
        readfileandfolder()

        name = input("Tell which file you want to update:- ")

        if not name.endswith(".txt"):
            name += ".txt"

        p = Path(name)

        if p.exists() and p.is_file():

            print("\nPress 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending content to your file")

            res = int(input("Tell your response:- "))

            if res == 1:
                name2 = input("Tell your new file name:- ")

                if not name2.endswith(".txt"):
                    name2 += ".txt"

                p2 = Path(name2)
                p.rename(p2)

                print("File renamed successfully")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter new content (old content will be deleted):- ")
                    fs.write(data)

                print("File updated successfully")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append:- ")
                    fs.write(" " + data)

                print("Content appended successfully")

            else:
                print("Invalid choice")

        else:
            print("The file does not exist")

    except Exception as err:
        print(f"An error occurred: {err}")


def deletefile():
    try:
        readfileandfolder()

        name = input("Which file do you want to delete:- ")

        if not name.endswith(".txt"):
            name += ".txt"

        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully")

        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occurred: {err}")


print("\n===== FILE HANDLING PROJECT =====")
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

try:
    check = int(input("Please tell your response:- "))

    if check == 1:
        createfile()

    elif check == 2:
        readfile()

    elif check == 3:
        updatefile()

    elif check == 4:
        deletefile()

    else:
        print("Invalid choice")

except ValueError:
    print("Please enter a valid number")