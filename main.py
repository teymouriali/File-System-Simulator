import os
import subprocess
import shutil
from colorama import Fore


def menu():

    print(Fore.LIGHTCYAN_EX+"""
        ----------------------------------------------------------------------------  
        Choose the desired number from the menu below to do the work:
        
        0-Change the script execution path (default Script execution path)
        1-List of files and folders, script execution path
        2-List of files and folders, script execution path (tree)
        3-Create a folder in the script execution path
        4-Create a file in the script execution path
        5-Edit the text file in the script execution path (vim)
        6-Delete a file or directory in the script execution path by search
        7-Rename a file or directory in the script execution path by search
        8-Delete all files or directories in the script execution path (dangerous)
        9-Help
        10-Exit
        ----------------------------------------------------------------------------  
        """+Fore.LIGHTWHITE_EX)
    current = os.getcwd()
    print(Fore.LIGHTGREEN_EX +
          f"Script execution path {Fore.LIGHTRED_EX+current+Fore.LIGHTWHITE_EX}")

    inp = input("Waiting to receive the desired number from the menu above : ")

    if inp.isnumeric() and int(inp) == 0:
        changedirectory()
    if inp.isnumeric() and int(inp) == 1:
        listt()
    if inp.isnumeric() and int(inp) == 2:
        listtree()
    if inp.isnumeric() and int(inp) == 3:
        add_directory()
    if inp.isnumeric() and int(inp) == 4:
        add_file()
    if inp.isnumeric() and int(inp) == 5:
        edit_vim()
    if inp.isnumeric() and int(inp) == 6:
        delete_d_f()
    if inp.isnumeric() and int(inp) == 7:
        rename()
    if inp.isnumeric() and int(inp) == 8:
        deleteall()
    if inp.isnumeric() and int(inp) == 9:
        helpp()
    if inp.isnumeric() and int(inp) == 10:
        print("Good Luck")
        exit(0)
    else:
        menu()


def helpp():
    os.system("clear")
    print(Fore.LIGHTCYAN_EX+"""
-------------------------------------------------------------------------------------------------------------  
|                                                                                                           |
|This script is for file system work                                                                        |
|                                                                                                           |
|File or directory search capabilities in the selected path                                                 |
|                                                                                                           |
|Create a file or directory in the selected path                                                            |
|                                                                                                           |
|Delete the file or directory in the selected path                                                          |
|                                                                                                           |
|Delete all files or directories in the script execution path (dangerous)                                   |
|                                                                                                           |
|The ability to change the name of the file or directory in the selected path                               |    
|                                                                                                           |
|Display files and directories in the selected path                                                         |
|                                                                                                           |
|Display files and directories in a tree in the selected path                                               |
|                                                                                                           |
|Edit text files with the VIM editor                                                                        |
|                                                                                                           |
|Note:                                                                                                      |
|Commands are executed in the selected path, which by default is the directory where this script is running.|
|                                                                                                           |
|Tips:                                                                                                      |
|You can use option 0 to change the script execution path                                                   |
-------------------------------------------------------------------------------------------------------------
        """+Fore.LIGHTWHITE_EX)

    inp = input("Enter q to exit the program help :>> ")

    if inp.lower() == "q":
        os.system("clear")
        menu()

    else:
        helpp()


def changedirectory():

    inp = input(
        "Waiting for the new execution path to run the script (q for show menu) : ")

    if inp.lower() == "q":
        menu()

    inp = os.path.expanduser(inp)

    if os.path.exists(inp) or os.path.isdir(inp):
        os.chdir(inp)
        menu()

    else:
        print(Fore.LIGHTRED_EX+"There is no path to choose"+Fore.LIGHTWHITE_EX)


def listt():

    items = os.listdir()

    for r in items:
        print(r)

    menu()


def listtree():

    items = os.getcwd()

    for r, d, f in os.walk(items):

        if not os.listdir(r):
            print(r + Fore.LIGHTRED_EX +
                  " is empty"+Fore.LIGHTWHITE_EX)

        else:
            print(Fore.LIGHTGREEN_EX+r+Fore.LIGHTWHITE_EX)
            if d:
                for dr in d:
                    print(Fore.LIGHTYELLOW_EX+" - ", dr+Fore.LIGHTWHITE_EX)

            if f:
                for fr in f:
                    print(" - ", fr)

    menu()


def add_directory():

    inp = input(
        "Enter the name of the directory to create (q for show menu) : ").strip()

    if inp.lower() == "q":
        menu()

    try:
        os.mkdir(inp)
        print("Directory created :)")
        add_directory()

    except FileExistsError:

        if inp == "/":
            print(Fore.LIGHTRED_EX+"Directory name cannot be / "+Fore.LIGHTWHITE_EX)
            add_directory()

        else:
            print(Fore.LIGHTRED_EX +
                  f"Directory {inp} is exist"+Fore.LIGHTWHITE_EX)

            add_directory()


def add_file():

    inp = input(
        "Enter the name of the file to create (q for show menu) : ").strip()

    if inp.lower() == "q":
        menu()

    if os.path.isdir(inp):
        print(f"{inp} is a directory")
        add_file()

    elif os.path.exists(inp):
        print(f"File {inp} is exist")
        add_file()

    else:

        try:

            with open(inp, mode="w"):
                print("The file was created :)")

        except:
            return 0

    add_file()


def delete_d_f():

    inp = input(
        "Enter the name of the file or directory to delete (q for show menu) : ")

    if inp.lower() == "q":
        menu()

    if not (os.path.isdir(inp)) and not (os.path.exists(inp)):
        print(Fore.LIGHTRED_EX + "File or directory not exist"+Fore.LIGHTWHITE_EX)
        delete_d_f()

    if os.path.isdir(inp):
        inp2 = input(
            "To delete a safe selected directory (all its subsets are also deleted)(y/n) :")

        if inp2.lower().strip() == "y":
            shutil.rmtree(inp)
            print("Directory deleted successfully")
            delete_d_f()

    if os.path.exists(inp):
        os.remove(inp)
        print("File deleted successfully")
        delete_d_f()

    delete_d_f()


def rename():

    inp = input(
        "Enter the name of the file or directory to rename (q for show menu) : ")

    if inp.lower() == "q":
        menu()

    if os.path.isdir(inp) or os.path.exists(inp):
        inp2 = input(
            "Enter the NEW name of the file or directory selected (q for show menu) : ")

        if not (os.path.isdir(inp2)) and not (os.path.exists(inp2)):

            if inp2.lower() == "q":
                menu()

            if os.path.isdir(inp):
                os.rename(inp, inp2)
                print("The directory was successfully renamed")
                rename()

            if os.path.exists(inp):
                os.rename(inp, inp2)
                print("The file was successfully renamed")
                rename()
        else:
            print(Fore.LIGHTRED_EX +
                  "NEW name of the file or directory selected EXIST"+Fore.LIGHTWHITE_EX)
            rename()

    else:
        print(Fore.LIGHTRED_EX +
              "The directory or file name entered does not exist"+Fore.LIGHTWHITE_EX)
        rename()


def deleteall():

    inp = input(
        "Are you sure to delete all files and directories of the selected path? ? (y/n) ").strip()

    if inp.lower() == "y":

        try:

            for i in os.listdir(os.getcwd()):
                itemp = os.path.join(os.getcwd(), i)

                if os.path.isfile(itemp) or os.path.islink(itemp):
                    os.remove(itemp)

                elif os.path.isdir(itemp):
                    shutil.rmtree(itemp)
            print("All files and directories of the selected path are deleted :(")

        except:
            return 0

    else:
        print(Fore.LIGHTRED_EX + "Opt out of deletion :)"+Fore.LIGHTWHITE_EX)

    menu()


def edit_vim():

    inp = input(
        "Enter the name of the text file to edit (q for show menu) : ").strip()

    if inp.lower() == "q":
        menu()

    if os.path.isdir(inp):
        print("The entered name is the name of the directory")
        edit_vim()

    elif os.path.exists(inp):
        subprocess.run(["vim",  inp])

    else:
        print(Fore.LIGHTRED_EX +
              "The imported text file is not available"+Fore.LIGHTWHITE_EX)

        menu()


if __name__ == "__main__":
    os.system("clear")
    menu()
