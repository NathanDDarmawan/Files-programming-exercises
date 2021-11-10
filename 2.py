# Write a program that given a text file will create a new text file in which
# all the lines from the original file are numbered
# from 1 to n (where n is the number of lines in the file).

filename = input("Enter a file: ")
file = open(filename, 'r', encoding='utf-8')
length = len(file.readlines())
file.seek(0)

newFile = open("listed.txt", 'x', encoding='utf-8')

line = 1
while line <= length:
    text = file.readline()
    newText = ("{}. {}".format(line, text))
    newFile.write(newText)
    line = line + 1
