# CleanDesk

![Screenshot (717)](https://user-images.githubusercontent.com/83111399/214790042-3430b134-2a5d-47ec-ab0f-4dcaaafed02b.png)
![Screenshot (718)](https://user-images.githubusercontent.com/83111399/214790061-cf9ae7a2-2766-4fb1-9fcd-9e881e0b4074.png)

**Open cmd and go to the location where you downloaded the project**

`> cd C:\Users\JohnDoe\Desktop`

**Run**

`> pip install -r requirements.txt`

`> python myCleaner.py`

**And enter your source folder to track**

**Create files inside the source folder and will se all your files are organized inside the cleanFolder**

## To have this run itself on startup:

1. ### Initialize the source folder inside the code
2. ### Create a file and name it anything with extension .bat
3. ### Inside the file write:

    `cd projectFolderLocation `

    `python myCleaner.py`

    `exit`

    _projectFolderLocation is where the project is located in your system eg. C:\\Users\\JohnDoe\\Desktop_

4. ### Go to the following location and paste the .bat file there
    `C:\Users\JohnDoe\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## To have this run itself on a scheduled time refer to the tutorial:

[Click Here](https://youtu.be/n2Cr_YRQk7o)
