# . Write a python program to copy the contents of one file to another. Your new file should be
# named as old file name followed by a 1. For example: if your original file is named: myfile.txt, your
# new file should be named: myfile1.txt


with open('myfile.txt',"r") as f, open('myfile1.txt',"w") as f1:
    for line in f:
        f1.write(line)