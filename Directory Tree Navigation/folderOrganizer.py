import os, shutil, time
import pyinputplus as pyip
from pathlib import Path

# Ask the user for a folder to organize the files in
while True:
    print('Please enter a full folder path to organize: ')
    pathToOrganize = pyip.inputFilepath()
    p = Path(pathToOrganize)
    # Check if the folder is valid using
    if Path.is_dir(p):
        #Exit loop if it is
        break
    # Provide feedback to the user that its not a valid path
    print('Please enter a valid folder path!')

#Change the CWD to the requested folder
os.chdir(pathToOrganize)
mainPath = Path.cwd()
fileList = list(mainPath.glob('*'))

# Go through all the files and make a new folder for each file type
for file in fileList:
    # Skip any Folders/Directories
    if Path.is_dir(Path(file.name)):
        continue

    # Check if a folder of the prefix type exists
    fullNewPath = mainPath / Path(f'{file.suffix} Files')
    if Path.is_dir(fullNewPath):
        #Move file if directory already exists
        shutil.move(file.name, fullNewPath)
    else:
        #Make the directory then move the file to the new directory
        os.mkdir(fullNewPath)
        shutil.move(file.name, fullNewPath)
    
    #Tell the user what was moved and sleep to let the move fully take place before the next file is processed
    print(f'Moved the file {file.name} to {fullNewPath.name}')
    time.sleep(2)