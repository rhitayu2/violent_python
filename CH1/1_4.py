import zipfile

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd = password)
        return password
    except Exception, e:
        return

def main():
    zFile = zipfile.ZipFile('trial.zip')
    passFile = open("dictionary.txt")
    for lines in passFile.readlines():
        password = lines.strip('\n')
        guess = extractFile(zFile, password)
        if guess:
            print "Password = " + password
            exit(0)
if __name__ == '__main__':
    main()
