import getpass
import os

user = getpass.getuser()
folderToTrack = "C:\\Users\\" + user + "\\Desktop"
fileLoc = "C:\\Users\\" + user + "\\Documents\\locText.txt"


if os.path.isfile(fileLoc):
    yn = input("Do you want to use previoiusly defined folder location: ")
    if(yn == "y"):
        with open(fileLoc, 'r') as f:
            folderToTrack = f.read()
    else:
        folderToTrack = str(input("Enter a folder path: "))
        with open(fileLoc, 'w') as f:
            f.write(folderToTrack)

else:
    folderToTrack = str(input("Enter a folder path: "))
    with open(fileLoc, 'w') as f:
        f.write(folderToTrack)

folderToTrack = folderToTrack.replace("\\", "\\\\")
folderDestination = folderToTrack + "\\"+"cleanFolder"
