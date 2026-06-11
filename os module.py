# os module: a built-in standard utility library that provides a portable way to interact with the underating oprating system.  in Python is a built-in standard utility library that provides a portable way to interact with the underlying operating system. It acts as a bridge between your Python script and system-level features, allowing you to manipulate files, manage folders, query environment variables, and execute terminal commands across Windows, macOS, and Linux.
#  Core Capabilities:
# 1. Directory navigation and management: You can use os to change the current working directory, create new folders, list files in a directory, and remove files or directories.
# os.getcwd() - Returns the absolute path of the current working directory.
# os.chdir(path) - Changes the current working directory context to the specified path.
# os.listdir(path) - Returns a list containing the names of the entries in the directory.
# os.mkdir(path) - Creates a single new directory; raises an error if it alrady exixts.
# os.makedirs(path) - Creates nested or multi-level directories recursively.

# File Operations: The os module provides functions to create, read, write, and delete files. You can also check if a file exists, get its size, or retrieve its metadata.
# os.rename(src, dst) - Renames a file or a folder to a new destination name.
# os.remove(path) - Deletes an individual file from the file system.
# os.rmdir(path) - Removes an empty directory; raises an error if the directory is not empty.
# os.walk(path) -  Yields a 3-tuple (dirpath, dirnames, filenames) for each directory in the directory tree rooted at the specified path.

# Environment and system control: You can access and modify environment variables, execute system commands, and manage process-related information using os.
# os.environ - A mapping object representing the string environment; you can read and modify environment variables using this dictionary-like object.
# os.system(command) - Executes the specified command in a subshell, allowing you to run terminal commands directly from your Python script.
# os.name - A string indicating the name of the operating system dependent module imported. For example, 'posix' for Unix/Linux/MacOS and 'nt' for Windows.

# Quick Code Example:

import os
# 1. get and print the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# 2. create a new folder
new_folder ="test_directory"
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"Created new folder: {new_folder}")  

# 3. list files and filders
print("Directory contents:", os.listdir("."))

# Path manipulation with os.path: The os module includes the os.path submodule, which provides functions for manipulating file paths in a platform-independent way. You can join paths, split them, get file extensions, and more.
# os.path.join(path1, path2, ...) - Connects path components intelligently using the system-correct separator.
# os.path.exists(path) - Verifies if a given file or directory path physically exists on the file system.
# os.path.abspath(path) - Resolves a relative path to an absolute format.
# os.path.basename(path) - Extracts the ultimate file or direction name from a full path.
# os.path.dirname(path) - Retrieves the directory portion of a full path, excluding the final file or folder name.
# os.path.splitext(path) - Splits the file name into a tuple (root, ext

# Best Practieces Note: For standard file system paths, consider using the modern pathlib module alongside os. While os is ideal for low-level system attributes and environment interactions, pathlib provides an intuitive, object-oriented approach for basic file path operations.

# Examples:
# Ex 1:
def current_path(label):
    print(f"Current working directory {label}")
    print(os.getcwd())
    print()
current_path("before")
os.chdir('../')
current_path("after")

# Ex 2:
import os
directory = "GeeksForGeeks"
parent_dir = "/Pycharm Projects/"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '%s' created" % directory)
directory = "Geeks"
parent_dir = "D:/Pycharm Projects/"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '%s' created" % directory)
# Ex 3:
import os
directory = "Nikhil"
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '%s' created" % directory)
directory = "c"
parent_dir = "D:/Pycharm projects/GeeksForGeeks/a/b"
mode = 0o666
path = os.path.join(parent_dir,directory)
os.makedirs(path,mode)
print("Directory '%s' created" % directory)
# Ex 4:
import os
path = "/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)