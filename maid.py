print("Maid 0.1_1")
import sys
import os
import time as clock

commonWords = ["he","him","she","her","program","computer","test","python","programming","window","code","class","function","android","windows","ios","iphone","mac","they","them","our","ours","his","their"]

if not len(sys.argv) > 1:
    print("File path expected. Closing.")
    exit()

makefile = open(str(sys.argv[1]), "a")
makefile.close()

class target:
    def content():
        targetfile = open(str(sys.argv[1]), "r")
        return targetfile.read()
        targetfile.close()

    def writeContent():
        inputText = input()
        if inputText == ":\\clr":
            targetfile = open(str(sys.argv[1]), "w")
            targetfile.write("")
        elif inputText == ":\\del":
            os.remove(str(sys.argv[1]))
            exit()
        elif inputText == ":\\exit":
            exit()
        else:
            targetfile = open(str(sys.argv[1]), "a+")
            targetfile.write(str(inputText)+"\n")
        targetfile.close()

while True:
    print('\033c')
    print(":\\clr = Clear file    :\\del = Delete file & exit    :\\exit = Exit (Or CTRL+C)\n")
    print(target.content())
    target.writeContent()
    clock.sleep(0.05)
exit()

