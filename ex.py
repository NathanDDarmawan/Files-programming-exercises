import re
def getHapex(file):
    myBook = open(file)
    words = re.findall('\w+', myBook.read().lower())
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    hapexList = []
    for word in counts:
        if counts[word] == 1:
            hapexList.append(word)
    return hapexList

print(getHapex("32891.txt"))
