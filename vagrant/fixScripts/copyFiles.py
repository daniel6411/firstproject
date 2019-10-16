import sys

import os


def copyFile(fileToCopy):
    basePath = os.getcwd()
    os.system("scp " + basePath + fileToCopy + ' server1:/home/vagrant/')


if __name__ == '__main__':
    fileSize = 0
    count = 1
    numberOfFiles = len(sys.argv)
    numberOfFiles -= 1
    for _ in range(numberOfFiles):
        fileToCopy = sys.argv[count]
        copyFile(fileToCopy)
        if fileSize == 0:
            fileSize = os.path.getsize(fileToCopy)
        else:
            fileSize += os.path.getsize(fileToCopy)
    print(fileSize)

