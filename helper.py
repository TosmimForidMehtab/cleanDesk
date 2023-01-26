import os
from userInp import folderDestination

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

Exexutables = folderDestination+"\\"+"Exexutables"
if not os.path.isdir(Exexutables):
    os.mkdir(Exexutables)

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
    "exe": Exexutables,
    "msi": Exexutables,
    "bat": Exexutables,
    "cmd": Exexutables,
    "lnk": Exexutables,
    "other": Others
}
