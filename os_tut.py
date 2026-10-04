# Python os Module — Complete Practical Guide
# os = Operating System
# Python ko operating system ke saath interact karne deta hai:
# files/folders create/delete karna
# current directory dekhna/change karna
# environment variables read karna
# file paths handle karna
# system information lena
# processes/commands ke saath basic interaction

import os
import shutil
import tempfile

# 1. CURRENT WORKING DIRECTORY 
# python abhi kis folder ke context mein kaam kar rha hai

original_dir = os.getcwd()
demo_dir = tempfile.mkdtemp(prefix="os-fundamentals-")
os.chdir(demo_dir)
os.makedirs("data", exist_ok=True)
open("data/file1.txt", "w", encoding="utf-8").write("sample file\n")
open("data/delete_me.txt", "w", encoding="utf-8").write("temporary file\n")
open("data/users.csv", "w", encoding="utf-8").write("name\nAsha\n")
open("data/report.pdf", "w", encoding="utf-8").write("sample report\n")

print(os.getcwd())
# Output: a temporary practice directory

# 2. CHANGE CURRENT WORKING DIRECTORY
# os.chdir() function ka use karke current working directory change kar sakte hai

os.chdir(demo_dir)
print(os.getcwd())

# now check which deirectory we are now by 
print(os.getcwd())# using 

# now official code will be -
print(os.getcwd()) # current working directory
os.chdir(demo_dir) # change current working directory
print(os.getcwd()) # check current working directory after changing it

# 3 . LISTING FILES AND DIRECTORIES
print(os.listdir()) # list all files and directories in current working directory
# output : ['file1.txt', 'file2.txt', 'folder1', 'folder2']

# for getting specific directory or folder
print(os.listdir('data')) # list all files and directories in specific directory

# where it is use -
# suppose fodler has 1000 csv files and 
# you want to read all of them, 
# then you can use os.listdir() 
# to get all the files in that 
# folder and then loop through them to read each file.

files = os.listdir('data') # list all files and directories in specific directory
for file in files:
    print(file) # print each file name


# 4. check if a file or directory exists
print(os.path.exists('data')) # check if 'data' directory exists
# output : True

# In backend use - 
if os.path.exists('config.json'):
    print('config file exists')
else:
    print('config file does not exist')



# 5. File ha ya folder ?? 
os.path.isfile('main.py') # check if 'data' is a file
output :True # if its a file 

os.path.isdir('data') #check if data is a directory
output : True # if its a directory

# Example - 
for item in os.listdir():
    if os.path.isfile(item):
        print(f'{item} is a file')
    elif os.path.isdir(item):
        print(f'{item} is a directory')

# output:
# FILE1.txt is a file
# FILE2.txt is a file
# FOLDER1 is a directory


# 6. Create Folder
os.mkdir('data/new_folder') # create a new folder named 'new_folder' inside 'data' directory
# creates: data/new_folder
# if file already exists then it will throw FileExistsError

# so 
if not os.path.exists('data'):
    os.mkdir('data')  # create a new folder named 'data' if it does not exist

# 7. Create nested Folders
os.makedirs('data/folder1/folder2') # create nested folders 'folder1'
# creates : data/
#               folder1/
#                       folder2

# differnce between os.mkdir() and os.makedirs() 
# is that os.mkdir() can only create a single directory, while 
# os.makedirs() can create multiple nested directories at once.

# we use makedirs() like - 
os.makedirs('data/folder1/folder2/folder3',exist_ok = True) # create nested folders 'folder1'
# exist_ok = True means if the folder already exists then it will not throw an error


# 8. Delete Empty Folder
os.rmdir('data/new_folder') # delete the empty folder 'new_folder' inside '
# if 
# data/
#     new_folder/

# then it will delete new_folder

# os.rmdir('data')  # fails while data still contains files
# if i write this only and data has files inside it then it will throw an error.

# Ye folder aur uske andar ka sab kuch delete kar dega.
# Keep this example commented so a lesson never deletes a real directory.
# shutil.rmtree("data")


#  9. Delete File
os.remove('data/delete_me.txt') # delete a temporary file inside 'data'
# Example - 
if os.path.exists('data/delete_me.txt'):
    os.remove('data/delete_me.txt') # avoid deleting a required lesson file

# 10. Rename File or folder
os.rename('data/file1.txt','data/file2.txt') # rename file1.txt to file2.txt

# 10. File size pta krna ke liye 
size  = os.path.getsize('data/file2.txt') # get the size of the renamed file
print(size) # print the size of the file in bytes

# output: depends on the sample text; size is measured in bytes

# we can covnert it in KB, MB, GB by dividing it with 1024, 1024*1024, 1024*1024*1024 respectively.
# size_kb = size / 1024
# size_mb = size / (1024 * 1024)
# size_gb = size / (1024 * 1024 * 1024)
# print(f'Size of the file in KB: {size_kb} KB')
# print(f'Size of the file in MB: {size_mb} MB')
# print(f'Size of the file in GB: {size_gb} GB')

# 12. file extension pta krna ke liye
file = 'data.pdf'
name , extension = os.path.splitext(file) # split the file name and extension
print(name) # print the file name without extension
print(extension) # print the file extension

# output: data
#         .pdf

# extremly useful when processing files.
# Example - 
for file in os.listdir('data'):
    name , ext = os.path.splitext(file)
    if ext == '.txt':
        print(f'{file} is a text file')
    elif ext == '.csv':
        print(f'{file} is a csv file')
    elif ext == '.pdf':
        print(f'{file} is a pdf file')
    else:
        print(f'{file} is an unknown file type')


# 13. File name and directory name pta krna ke liye
path  = 'data/file2.txt'
os.path.basename(path) # get the file name from the path
# output : 'file2.txt'

os.path.dirname(path) # get the directory name from the path
# output : 'data/file1.txt' file kis directory mein hai

#  14. joining file path (important)
path = 'data/' + 'users.csv' # this is not a good way to join file path because it will not work on all operating systems
# instead use os.path.join() function to join file path
path = os.path.join('data','users.csv') # this will join the file path in a way that it will work on all operating systems

# output: data/users.csv 
# this is due because window and mac differ
# in linux/Mac : /
# in windows : \

# Example - 
DATA_DIR = 'data'
file_path = os.path.join(DATA_DIR,'users.csv') # cleaner version of joining file path


# 15. Absolute path and relative path 
path  = 'data/users.csv'
print(os.path.abspath(path)) # get the absolute path of the file 'users.csv' inside 'data' directory
# output : /Users/anuj/Desktop/project/py/data/users.csv

# Difference between absolute path and relative path is that absolute path is the full path of the file or directory from the root directory, while relative path is the path of the file or directory from the current working directory.
# realtive path = data/users.csv
# absolute path = /Users/anuj/Desktop/project/py/data/users.csv


# 16. Normalize a path
path = 'data/../data/users.csv'
print(os.path.normpath(path))  # data/users.csv

# Restore the learner's original directory and remove only our demo workspace.
os.chdir(original_dir)
shutil.rmtree(demo_dir)











