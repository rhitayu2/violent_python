#implementing multiple threads to work
#at the same time totry multiple passwords
#at once
import zipfile
from threading import Thread
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print "Found password"
    except Exception as e:
        pass
def main():
    zFile = zipfile.ZipFile('trial.zip')
    passFile = open('dictionary.txt')
    for lines in passFile.readlines():
        password = lines.strip('\n')
        t = Thread(target = extractFile, args = (zFile,password))
        #applying threads to work on the ZipFile
        t.start();
if __name__ == '__main__':
    main()
