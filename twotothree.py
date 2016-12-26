from subprocess import call
import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        File = os.path.join(root,name)
        if File.endswith(".py"):
            call(["2to3","-w",File])
