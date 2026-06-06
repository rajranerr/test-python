# Shutil motule: The shutil module (short for "shell utilities") is a built-in Python standard library used for high-level file and directory operations like copying, moving, renaming, and deleting. While the os module handles basic single-file tasks, shutil abstracts complex operations (such as recursive folder copying) into simple, cross-platform functions.

# Example:

# importing shutil module 
import shutil 

source = "path/main.py"
destination ="path/main2.py"

# Copy the content of 
# source to destination 
dest = shutil.copy(source, destination) 

# Print path of newly 
# created file 
print("Destination path:", dest)