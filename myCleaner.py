from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import os
from helper import *
from userInp import *


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folderToTrack):
            if filename != "cleanFolder":
                i = 1
                try:
                    splitName = filename.split('.')
                    extension = str(splitName[1])
                    if extension not in extensionFolders.keys():
                        extension = "other"
                    newName = filename
                    fileExists = os.path.isfile(
                        extensionFolders[extension] + "\\" + newName)

                    while fileExists:  # Bug 1
                        i += 1
                        newName = os.path.splitext(
                            folderToTrack+"\\"+newName)[0] + str(i) + os.path.splitext(folderToTrack+"\\"+newName)[1]
                        newName = newName.split("\\")[5]

                        fileExists = os.path.isfile(
                            extensionFolders[extension] + "\\"+newName)

                    src = folderToTrack + "\\"+filename
                    newName = extensionFolders[extension] + "\\"+newName
                    os.rename(src, newName)
                except Exception:
                    continue
                    # print(f"Error in {filename}")

    def on_created(self, event):
        time.sleep(6)
        self.on_modified(event)


if __name__ == "__main__":
    eventHandler = MyHandler()
    observer = Observer()
    observer.schedule(eventHandler, folderToTrack, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
