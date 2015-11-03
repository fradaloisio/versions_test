import urllib

versionFile = "https://raw.githubusercontent.com/fradaloisio/versions_test/master/VERSION"
lastVersion = str(urllib.urlopen(versionFile).read())

if lastVersion.__contains__("\""):
    lastVersion = str(lastVersion.split('\"')[1])

currentFile = open("VERSION", "r")
currentVersion = currentFile.readline()
while "VERSION" not in currentVersion:
    currentVersion = currentFile.readline()

if currentVersion.__contains__("\""):
    currentVersion = str(currentVersion.split('\"')[1])

if currentVersion == lastVersion:
    print("Nice!")
else:
    print "Current version: " + currentVersion
    print "Last version: " + lastVersion
    print("Please, upgrade")