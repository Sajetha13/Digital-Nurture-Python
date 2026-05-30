import os
if os.path.exists("file.txt"):
    with open("file.txt") as f:
        content = f.read()
        print(content + "\n")
else:
    print("no file")