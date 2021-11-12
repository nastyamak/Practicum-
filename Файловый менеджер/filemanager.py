import sys
import os
import shutil

osu = input('Linux or Windows? ')
if osu == 'Linux' or 'linux':
    way = (os.getcwd()).split('/')
    way1 = way[-1] + ('/')
    vi = '/'
    print('Main folder: ' + way[-1])
elif osu == 'Windows' or 'windows':
    way = (os.getcwd()).split('/')
    way1 = way[-1] + ('\\')
    vi = '\\'
    print('Main folder: ' + way[-1])
else:
    print('Wrong input')
    sys.exit()

print("-------------------------------RULES-------------------------------\n"
      "1) To pick a command, enter it's name and params if needed\n"
      "2) You can't work outside the main folder and its contents\n"
      "3) The main folder is the one where this .py file is\n"
      "4) While using PATH, don't forget to input the name of the file/folder at the end\n"
      "     *Example for win: mkdir C:\\Users\\User\\Desktop\\Study\\newdir\n"
      "     A new dir named 'newdir' will be created in dir Study")
print("-------------------------------MENU--------------------------------\n "
      "mkdir (dir name or path)   - Create a directory\n "
      "rdir  (dir name or path)   - Delete a directory\n "
      "cd    (dir name or path)   - Move into directory\n "
      "..                         - Move out of directory\n "
      "mkfile (file name or path) - Create an empty file\n "
      "echo   (file name or path) - Append text to a .txt file or creates a .txt file\n "
      "cat    (file name or path) - View .txt file's content\n "
      "rfile  (file name or path) - Delete a file\n "
      "cp     (file name or path) - Copy a file into another directory\n "
      "mv     (file name or path) - Move a file to another directory\n "
      "rename (file name or path) - Rename a file\n "
      "end                        - Exit\n "
      "ls                         - Show contents of the current folder")


def make_dir(dir_name):
    try:
        if vi in dir_name:
            if way1 in dir_name:
                os.mkdir(dir_name)
                print('A new directory was created. Path: ' + dir_name)
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            os.mkdir(dir_name)
            print('A new directory named ' + dir_name + ' was created')
    except FileExistsError:
        print('!!!A directory with this name/path already exists. Try again')


def del_dir(dir_name):
    try:
        if vi in dir_name:
            if way1 in dir_name:
                os.rmdir(dir_name)
                print('A directory ' + dir_name + ' was deleted')
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            os.rmdir(dir_name)
            print('A directory named ' + dir_name + ' was deleted')
    except FileNotFoundError:
        print('!!!There is no directory with this name/path. Try again')
    except OSError:
        print('!!!This folder is not empty. Remove its content first to remove the folder')


def move_dir(dir_name):
    try:
        if vi in dir_name:
            if way[-1] in dir_name:
                os.chdir(dir_name)
                print("Current path: " + os.getcwd())
            else:
                print("!!!You can't work outside the main directory. Try again")
        elif '..' in dir_name:
            print("!!!You can't move back like this. Use '..' instead of 'cd ..'")
        else:
            os.chdir(dir_name)
            print("Current directory: " + dir_name + ". Current path: " + os.getcwd())
    except FileNotFoundError:
        print('!!!There is no directory with this name in the current folder. Try again')


def move_back():
    if way1 in os.getcwd():
        os.chdir("..")
        print('Moved a step back')
    else:
        print("!!!Unable to move back. You can't move out of the main folder " + way[-1])


def make_file(file_name):
    try:
        if vi in file_name:
            if way[-1] in file_name:
                new_file = open(file_name, 'x')
                new_file.close()
                print('File ' + file_name + ' was created')
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            new_file = open(file_name, 'x')
            new_file.close()
            print('File named ' + file_name + ' was created')
    except FileExistsError:
        print('!!!File with this name already exists. Try again')


def add_text(file_name):
    if '.txt' not in file_name:
        print('!!!This is not a .txt file. Try again')
    else:
        if vi in file_name:
            if way[-1] in file_name:
                new_text = open(file_name, 'w')
                new_text.write(input('Enter the text: '))
                new_text.close()
                print('Entered text was added to the file')
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            new_text = open(file_name, 'w')
            new_text.write(input('Enter the text: '))
            new_text.close()
            print('Entered text was added to the file')


def view_cont(file_name):
    if '.txt' not in file_name:
        print('!!!This is not a .txt file. Try again')
    else:
        try:
            if vi in file_name:
                if way[-1] in file_name:
                    view_file = open(file_name, 'r')
                    content = view_file.read()
                    print('Content of the file: ' + content)
                    view_file.close()
                else:
                    print("!!!You can't work outside the main directory. Try again")
            else:
                view_file = open(file_name, 'r')
                content = view_file.read()
                print('Content of the file: ' + content)
                view_file.close()
        except FileNotFoundError:
            print('!!!There is no file with this name. Try again')


def del_file(file_name):
    try:
        if vi in file_name:
            if way[-1] in file_name:
                os.remove(file_name)
                print('File ' + file_name + ' was deleted')
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            os.remove(file_name)
            print('File named ' + file_name + ' was deleted')
    except FileNotFoundError:
        print('!!!There is no file with this name in the current folder. Try again')
    except PermissionError:
        print('!!!Error')


def copy_file(file_name):
    try:
        if vi in file_name:
            if way[-1] in file_name:
                dir_name = input('Copy into: ')
                if vi in dir_name:
                    if way[-1] in dir_name:
                        shutil.copy(file_name, dir_name)
                        print('Copied')
                    else:
                        print("!!!You can't work outside the main directory. Try again")
                else:
                    shutil.copy(file_name, dir_name)
                    print('Copied')
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            dir_name = input('Copy into: ')
            if vi in dir_name:
                if way[-1] in dir_name:
                    shutil.copy(file_name, dir_name)
                    print('Copied')
                else:
                    print("!!!You can't work outside the main directory. Try again")
            else:
                shutil.copy(file_name, dir_name)
                print('Copied')
    except FileNotFoundError:
        print('!!!There is no directories with this name. Try again')
    except FileExistsError:
        print('!!!File with this name already exists. Try again')
    except OSError:
        print('!!!Error')


def move_file(file_name):
    try:
        if vi in file_name:
            if way[-1] in file_name:
                move_to = (input('Input full/short path to a new folder with the name of a new file at the end.\n'
                                 'Examples for win:\n'
                                 '  1) C:\\Users\\User\\Desktop\\Study\\1.txt\n'
                                 '  2) existingdir\\1.txt (name of a folder located in the current dir)\n'
                                 '>: '))
                os.replace(file_name, move_to)
                print('File ' + file_name + ' was moved to another directory. New path: ' + move_to)
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            move_to = (input('Input full/short path to a new folder with the name of a new file at the end.\n'
                             'Examples for win:\n'
                             '  1) C:\\Users\\User\\Desktop\\Study\\1.txt\n'
                             '  2) existingdir\\1.txt (name of a folder located in the current dir)\n'
                             '>: '))
            os.replace(file_name, move_to)
            print(
                'File named ' + file_name + ' was moved to another directory.')
    except FileNotFoundError:
        print('!!!There is no file/dir with this name. Try again')


def rename_file(file_name):
    try:
        if vi in file_name:
            if way[-1] in file_name:
                new_name = (input('*If you are not using path, the file will be moved to the current folder*\n'
                                  'New name: '))
                os.rename(file_name, new_name)
                print('File ' + file_name + ' was renamed into ' + new_name)
            else:
                print("!!!You can't work outside the main directory. Try again")
        else:
            new_name = (input('*If you are not using path, the file will be moved to the current folder*\n'
                              'New name: '))
            os.rename(file_name, new_name)
            print('File named ' + file_name + ' was renamed into ' + new_name)
    except FileNotFoundError:
        print('!!!There is no file with this name. Try again')
    except FileExistsError:
        print('!!!File with this name already exists. Try again')


while True:
    print('-------------------------------------------------------------------')
    print('Current path: ' + os.getcwd())
    command = input('>: ')
    command = command.split(' ')
    try:
        if command[0] == 'mkdir':
            make_dir(' '.join(command[1::]))
        elif command[0] == 'rdir':
            del_dir(' '.join(command[1::]))
        elif command[0] == 'cd':
            move_dir(' '.join(command[1::]))
        elif command[0] == '..':
            move_back()
        elif command[0] == 'mkfile':
            make_file(' '.join(command[1::]))
        elif command[0] == 'echo':
            add_text(' '.join(command[1::]))
        elif command[0] == 'cat':
            view_cont(' '.join(command[1::]))
        elif command[0] == 'rfile':
            del_file(' '.join(command[1::]))
        elif command[0] == 'cp':
            copy_file(' '.join(command[1::]))
        elif command[0] == 'mv':
            move_file(' '.join(command[1::]))
        elif command[0] == 'rename':
            rename_file(' '.join(command[1::]))
        elif command[0] == 'end':
            sys.exit()
        elif command[0] == 'ls':
            print('Contents of the current folder:', os.listdir())
        else:
            print('!!!Wrong entry data. Try again')
    except IndexError:
        print('!!!Incorrect input. Check if your input matched the rules')
    except FileNotFoundError:
        print('!!!Incorrect input. Check if your input matched the rules')
