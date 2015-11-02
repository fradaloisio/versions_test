import urllib

versionFile = "https://raw.githubusercontent.com/fradaloisio/versions_test/master/VERSION"
lastVersion = urllib.urlopen(versionFile).read()

currentFile = open("VERSION", "r")
currentVersion = currentFile.readline()
while "VERSION" not in currentVersion:
    currentVersion = currentFile.readline()

if currentVersion is not lastVersion:
    print("Please, upgrade")
else:
    print("Nice!")
