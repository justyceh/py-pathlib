from pathlib import Path
import shutil
import os

username = "Justy"
p = Path(f'/Users/{username}/Downloads')


# This function takes a path to a directory and lists all the sub directories
def listSubdir(currentpath):
    for subdir in currentpath.iterdir():
        if subdir.is_dir():
            print(subdir)
        elif subdir.is_file():
            print(subdir.suffix)

# Organizes files in your downloads folder
def organizeDownloads(currentpath):
    imgExtensions = {'.png', '.jpg', '.JPG', '.PNG', '.avif', '.webp', '.svg', '.jpeg'}
    pdfExtensions = {'.pdf'}
    videoExtensions = {'.mp4', '.mp3', '.mov'}
    textExtensions = {'.txt', '.md', '.docx', '.pptx', '.json'}
    spreadsheetExtensions = {'.csv', '.xlsx'}

    images_folder = currentpath.joinpath("Images")
    images_folder.mkdir(exist_ok=True)

    pdfs_folder = currentpath.joinpath("PDFS")
    pdfs_folder.mkdir(exist_ok=True)

    
    videos_folder = currentpath.joinpath("Videos")
    videos_folder.mkdir(exist_ok=True)

    text_folder = currentpath.joinpath("Text")
    text_folder.mkdir(exist_ok=True)

    other_folder = currentpath.joinpath("Other")
    other_folder.mkdir(exist_ok=True)

    spreadsheet_folder = currentpath.joinpath("Spreadsheets")
    spreadsheet_folder.mkdir(exist_ok=True)



    for file in currentpath.iterdir():
        if file.is_dir():
            print(file)
        elif file.is_file():
            if file.suffix.lower() in imgExtensions:
                print("Image", file.name)
                destination_folder = images_folder
            elif file.suffix in pdfExtensions:
                print("PDF")
                destination_folder = pdfs_folder
            elif file.suffix in videoExtensions:
                print("Video")
                destination_folder = videos_folder
            elif file.suffix in textExtensions:
                print("text")
                destination_folder = text_folder
            elif file.suffix in spreadsheetExtensions:
                print("Spreadsheet")
                destination_folder = spreadsheet_folder
            else:
                print("Other")
                destination_folder = other_folder
            destination = destination_folder.joinpath(file.name)
            file.rename(destination)

newpath = Path(f'/Users/{username}/Downloads/mytext.txt')

def readFile(path):
    print(path.read_text())
    return path.read_text()

def writeFile(path, text):
    path.write_text(text)

readFile(newpath)

writeFile(newpath, "moneyyyyyyyyyy")

readFile(newpath)