import re

filename = input("Enter a file: ")
file = open(filename, 'r', encoding='utf-8')
words = re.findall('\w+', file.read().lower())
length = len(words)
i = 0
total = 0
while i < length:
    total += len(words[i])
    i += 1
avg = int(total/length)
print("average word length:", avg)
