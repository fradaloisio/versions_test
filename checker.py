import urllib

def cleanVersion(self):
    if self.__contains__("\""):
        return self.split('\"')[1]
    else:
        return self

versionFile = "https://raw.githubusercontent.com/fradaloisio/versions_test/master/VERSION"
lastVersion = cleanVersion(urllib.urlopen(versionFile).read())

currentFile = open("VERSION", "r")
currentVersion = cleanVersion(currentFile.readline())
currentFile.close()

if currentVersion == lastVersion:
    print("Nice!")
else:
    print "Current version: " + currentVersion
    print "Last version: " + lastVersion
    print("Please, upgrade")