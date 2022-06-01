import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ------------------------------------------------------------------------------------------
folderToTrack = "C:\\Users\\Susan\\Desktop"
folderDestination = folderToTrack + "\\"+"cleanFolder"

if not os.path.isdir(folderDestination):
    os.mkdir(folderDestination)

Archieve = folderDestination+"\\"+"Archieve"
if not os.path.isdir(Archieve):
    os.mkdir(Archieve)

textFile = folderDestination+"\\"+"TextFiles"
if not os.path.isdir(textFile):
    os.mkdir(textFile)

Documents = folderDestination+"\\"+"Documents"
if not os.path.isdir(Documents):
    os.mkdir(Documents)

Executables = folderDestination+"\\"+"Executables"
if not os.path.isdir(Executables):
    os.mkdir(Executables)

Others = folderDestination+"\\"+"Others"
if not os.path.isdir(Others):
    os.mkdir(Others)

Media = folderDestination+"\\"+"Media"
if not os.path.isdir(Media):
    os.mkdir(Media)

Audio = Media+"\\"+"Audio"
if not os.path.isdir(Audio):
    os.mkdir(Audio)

Video = Media+"\\"+"Video"
if not os.path.isdir(Video):
    os.mkdir(Video)

Images = Media+"\\"+"Images"
if not os.path.isdir(Images):
    os.mkdir(Images)

Programming = folderDestination+"\\"+"Programming"
if not os.path.isdir(Programming):
    os.mkdir(Programming)

C = Programming+"\\"+"C"
if not os.path.isdir(C):
    os.mkdir(C)

Cpp = Programming+"\\"+"C++"
if not os.path.isdir(Cpp):
    os.mkdir(Cpp)

Java = Programming+"\\"+"Java"
if not os.path.isdir(Java):
    os.mkdir(Java)

Go = Programming+"\\"+"Go"
if not os.path.isdir(Go):
    os.mkdir(Go)

Csharp = Programming+"\\"+"C#"
if not os.path.isdir(Csharp):
    os.mkdir(Csharp)

Js = Programming+"\\"+"Javascript"
if not os.path.isdir(Js):
    os.mkdir(Js)

Json = Programming+"\\"+"Json"
if not os.path.isdir(Json):
    os.mkdir(Json)

Python = Programming+"\\"+"Python"
if not os.path.isdir(Python):
    os.mkdir(Python)

R = Programming+"\\"+"R"
if not os.path.isdir(R):
    os.mkdir(R)

Html = Programming+"\\"+"Html"
if not os.path.isdir(Html):
    os.mkdir(Html)

Css = Programming+"\\"+"Css"
if not os.path.isdir(Css):
    os.mkdir(Css)

# -------------------------------------------------------------------------------------------


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folderToTrack):
            i = 1
            if filename != "cleanFolder":
                try:
                    splitName = filename.split('.')
                    extension = str(splitName[1])
                    if extension not in extensionFolders.keys():
                        extension = "other"
                    newName = filename
                    fileExists = os.path.isfile(
                        extensionFolders[extension] + "\\" + newName)

                    while fileExists:
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
    def on_created(self, event):
        self.on_modified(event)

# --------------------------------------------------------------------------------------------------


extensionFolders = {
    "zip": Archieve,
    "rar": Archieve,
    "txt": textFile,
    "md": textFile,
    "cpp": Cpp,
    "c": C,
    "h": C,
    "py": Python,
    "java": Java,
    "html": Html,
    "css": Css,
    "js": Js,
    "r": R,
    "json": Json,
    "go": Go,
    "cs": Csharp,
    "m4a": Audio,
    "mp3": Audio,
    "wav": Audio,
    "wma": Audio,
    "mp4": Video,
    "mkv": Video,
    "avi": Video,
    "png": Images,
    "PSD": Images,
    "Ai": Images,
    "jpeg": Images,
    "gif": Images,
    "docx": Documents,
    "pdf": Documents,
    "ppt": Documents,
    "docx": Documents,
    "xlsx": Documents,
    "exe": Executables,
    "msi": Executables,
    "bat": Executables,
    "cmd": Executables,
    "lnk": Executables,
    "other": Others
}
# ----------------------------------------------------------------------------------------------------------

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
