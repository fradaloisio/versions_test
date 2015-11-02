import urllib

versionFile = "https://raw.githubusercontent.com/fradaloisio/versions_test/master/VERSION"
lastVersion = urllib.urlopen(versionFile).read()

lastVersion = str(lastVersion.split('\"')[1])

currentFile = open("VERSION", "r")
#currentVersion = currentFile.readline()
# while "VERSION" not in currentVersion:
#     currentVersion = currentFile.readline()
#
# currentVersion = str(currentVersion.split('\"')[1])
currentVersion = str(currentFile.readline())

if currentVersion is lastVersion:
    print("Nice!")
else:
    print "Current version: " + currentVersion
    print "Last version: " + lastVersion
    print("Please, upgrade")