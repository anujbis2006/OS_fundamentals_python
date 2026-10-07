# Pathlib - is a  modernobject- oriented way to work with file and folder paths in python . 
# instead of manually doing string apth manippulation like os.path.join() and os.path.split() ,
#  we can use pathlib to work with paths in a more intuitive way.

# benefits of using pathlib:
# 1. It provides a more readable and intuitive syntax for working with file paths.
# 2. It is cross-platform compatible, meaning it works on different operating systems without needing
# provide clean code than os.path module.
# eacy joining of paths using the / operator instead of os.path.join() function.


from pathlib import Path
# Creating a Path object
p1 = Path('data/file.txt')
print(p1)  # Output: data/file.txt

# Window-style path absolute path (raw string)
p2 = Path(r'C:\Users\Username\Documents\file.txt')
print(p2)  # Output: C:\Users\Username\Documents\file.txt

# linux/mac-style path absolute path
p3 = Path('/home/username/documents/file.txt')
print(p3)  # Output: /home/username/documents/file.txt

# Accessing current working directory
current_dir = Path.cwd()
print(current_dir)  # Output: /Users/anujbiswas/Desktop/python_system_engineering_and_automation


# Home directory
home = Path.home()  
print(home)  # Output: /Users/anujbiswas

# joinning path
base=Path('projects')
file_path = base / 'data' / 'input.txt'
print(file_path)  # Output: projects/data/input.txt
# its '/' operator is overloaded to join paths in a more intuitive way.

# checking if a path exists
p = Path('data/file.txt')
print(p.exists()) # False

# checking if a path is a file or directory
print(p.is_file())  # Output: True or False
print(p.is_dir())   # Output: True or False

# Chechking if a path is absolute or relative
print(p.resolve()) # Output: /Users/anujbiswas/Desktop/python_system_engineering_and_automation/data/file.txt
# absolute path
print(p.absolute()) # Output: /Users/anujbiswas/Desktop/python_system_engineering_and_automation/data/file.txt

# in both of them we use mainly more is resolve beacuse its automatically generlize the 
# absolute path and also normalize it and take me to the real location.

# Some usefule methods of pathlib:
p = Path('project/data/input.txt')
print(p.name)  # Output: input.txt
print(p.stem)  # Output: input
print(p.suffix)  # Output: .txt
print(p.suffixes)  # Output: ['.txt']
print(p.parent)  # Output: project/data
print(p.parents)  # Output: <PosixPath.parents>
# its give to the immediate parent from the directory one by one
print(list(p.parents))  # Output: [PosixPath('project/data'), PosixPath('project'), PosixPath('.')]


# changing the file name an extensions
p = Path('project/data/input.txt')
new_p = p.with_name('output.txt')
print(new_p)  # Output: project/data/output.txt

# change suffix (extension)
# This only change the path but does not actuallly rename the file on the filesystem.
#  To rename the file, you would need to use the `rename()` method.
new_p = p.with_suffix('.csv')
print(new_p)  # Output: project/data/input.csv

# Listing files and folders
# list immediate contents
folder = Path('project/data')

# folder.iterdir() returns an iterator of Path objects representing the immediate contents of the folder.
for item in folder.iterdir():
    print(item)  # Output: project/data/file1.txt, project/data/file2.txt, etc.
    if item.is_file():
        print(f"{item} is a file")
    elif item.is_dir():
        print(f"{item} is a directory")

# Pattern searching using glob
# glob() method allows you to search for files and directories matching a specific pattern.
# For example, to find all text files in a directory:
folder = Path('project/data')
for txt_file in folder.glob('*.txt'):
    print(txt_file)  # Output: project/data/file1.txt, project/data/file2.txt, etc.

# if we want to search recursively in all subdirectories, we can use the rglob() method:
for txt_file in folder.rglob('*.txt'):
    print(txt_file)  # Output: project/data/file1.txt, project/data/subdir/file3.txt, etc.

# Renaming and Deleting Files
p = Path('project/data/input.txt')
p.rename("new.txt") #₹ Renames the file to new.txt in the same directory.

p = Path('project/data/new.txt')
# for delting an file we can use two methods:
# unlink() - for deleting a file
# rmdir() - for deleting empty directory
p.unlink(missing_ok = True)  # Deletes the file new.txt from the filesystem.
p.rmdir()  # Deletes the empty directory if it exists.

# if wnat to delete a non-empty directory, we can use shutil.rmtree() function from the shutil module.
p.shutil.rmtree('project/data')  # Deletes the directory and all its contents.


# Working woth relatvies vs absolute paths safely
BASE_DIR = Path(__file__).resolve()
# this will give the absolute path of the current script file.
BASE_DIR = Path(__file__).resolve().parent
# this will give the absolute path of the directory containing the current script file.

# And now we easily join this up ..
datafile = BASE_DIR / 'data' / 'input.txt'
print(datafile)  # Output: /absolute/path/to/data/input.txt
# this script can be run from anywhere his will always run 
# this is not an hardcoded path and will always work correctly regardless of the current working directory.
# This is also an professional setup 
