filename = input("Enter a file: ")
file = open(filename, 'r', encoding='utf-8')
text = file.read().split()
titles = ['Mr.', 'Jr.', 'Ms.', 'Mrs.', 'Dr.', ]
split_text = ''
for word in text:
    if '?' not in word and '!' not in word:
        split_text += (word + " ")
        if '.' in word.strip('.') and word not in titles:
            pass
        elif '.' in word[-1] and word not in titles:
            split_text += "\n"
    else:
        split_text += (word + "\n")

newFile = open("sentence splitter.txt", 'x', encoding='utf-8')
newFile.write(split_text)
