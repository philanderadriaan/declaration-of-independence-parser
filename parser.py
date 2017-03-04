import re

fileObject = open("declaration.txt", "r")


for aline in fileObject:
    wordList = re.findall('[a-zA-Z]*s[^a-zA-Z]', aline)
    #wordList = re.findall('[^a-zA-Z]a[a-zA-Z]*r[^a-zA-Z]', aline)
    #wordList = re.findall('[^a-zA-Z][a-zA-Z][aeiouAEIOU][aeiouAEIOU][a-zA-Z][^a-zA-Z]', aline)
    print(wordList)
