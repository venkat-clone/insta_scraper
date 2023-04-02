import os
import shutil

# Path to the directory containing the files
directory_path = '#hot/'

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Create a dictionary to store the files by extension
file_dict = {}

# Iterate through each file in the directory
for file in files:
    # Get the extension of the file
    extension = os.path.splitext(file)[1]
    
    # If the extension is not in the dictionary, add it
    if extension not in file_dict:
        file_dict[extension] = []
    
    # Add the file to the list of files for the extension
    file_dict[extension].append(file)

# Create a directory for each extension and move the files into the directories
for extension in file_dict:
    # Create a directory for the extension
    dir_name = directory_path + '/' + extension[1:]
    os.makedirs(dir_name, exist_ok=True)
    
    # Move the files into the directory
    for file in file_dict[extension]:
        src = directory_path + '/' + file
        dst = dir_name + '/' + file
        shutil.move(src, dst)
