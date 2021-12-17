import os

def convertType(size_in_bytes, size_type):
    """ Convert the size from bytes to other types like KB, MB or GB"""
    if size_type == "BYTES":
        return size_in_bytes
    elif size_type == "KB":
        return size_in_bytes / 1024
    elif size_type == "MB":
        return size_in_bytes / (1024*1024)
    elif size_type == "GB":
        return size_in_bytes / (1024*1024*1024)
    else:
        print("Please give you the correct type")

def getFileSize(file_name, size_type):
    """ Get file in size in given unit like KB, MB or GB"""
    size = os.path.getsize(file_name)
    return convertType(size, size_type)

def getFilesList(directory_name):
    files = []
    for r,d,f in os.walk(directory_name):
        for each_file in f:
            files.append(os.path.join(r,each_file))
    return files

def getFile():
    directory = input("Enter directory path for search large files (Only folder path): ")
    size_type = input("Enter type of size (BYTES,KB,MB,GB): ")
    count = int(input("Enter number of files (Only integer): "))

    sorted_files = sorted(getFilesList(directory), key=os.path.getsize, reverse=True)
    for file in sorted_files[:count]:
        size = getFileSize(file, size_type)
        print(f"File path: {file}")
        print(f"File size: {round(size, 2)} {size_type}")
        print("-" * 80)