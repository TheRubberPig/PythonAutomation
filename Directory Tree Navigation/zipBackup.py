#! python3
# zipBackup.py - Copies an entire folder and its contents into a ZIP file where the file name increments each time 

import zipfile, os

def backupToZip(folder):
    #Back up entire folder to ZIP

    folder = os.path.abspath(folder)

    #Calculate version number
    number = 1
    while True:
        zipFileName = os.path.basename(folder + '_' + str(number) + '.zip')
        if not os.path.exists(zipFileName):
            break
        number += 1
    
    #Create the zip file
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')
    print('Done.')

    #Walk the directory tree and compress the files in each folder
    for folderName, subFolders, fileNames in os.walk(folder):
        print(f'Adding files in {folderName}...')
        # Add the current folder to ZIP file
        backupZip.write(folderName)

        #Add all files in this folder to the ZIP file
        for fileName in fileNames:
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                #Dont back up ZIP files
                continue
            backupZip.write(os.path.join(folderName, fileName))
        backupZip.close()
        print('Done.')
