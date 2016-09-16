
# # Exercise 2.1: # Write a script with two methods.
# The first method should read in a matrix like the one here and return a list of lists.
# The first method should take the file name as a parameter.

def matrixToList(filename):
    file_object = open(filename, 'r')
    res = file_object.read().splitlines()
    for idx, item in enumerate(res):
        res[idx] = item.split()
    return res

# The second method should do the inverse, namely take, as input, a list of lists and save it in a file with same format as the initial file. 
# The second method should take two arguments, the list of lists, and a filename of where to save the output.

def listToMatrix(listOfLists, filename):
    target = open(filename, 'w')
    for item1 in listOfLists:
        for item2 in item1:
            target.write(item2 + " ")
        target.write("\n")
    target.close()

# Exercise 2.2:

# Write a script that takes an integer N, and outputs all bit-strings of length N as lists. For example: 3 -> [0,0,0], [0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]. As a sanity check, remember that there are 2^N such lists.
# Do not use the bin-function in Python. Do not use strings at all. Do not import anything. Try to solve this using only lists, integers, if-statements, loops and functions.

def getPermutationsList(size, currList):
    if len(currList[0]) == size:
        return currList
    else:
        res = []
        num = len(currList)
        for i in range(num):
            curr = currList[i]
            new = list(curr)
            new.append(0)
            new2 = list(curr)
            new2.append(1)
            res.append(new)
            res.append(new2)
        return getPermutationsList(size, res)        

def bsOfNum(num):
    res = [[0],[1]]
    if num > 1:
        res = getPermutationsList(num, res)
    return res
    
# Exercise 2.3:

# Write a script that takes this file (from this Kaggle competition), extracts the request_text field from each dictionary in the list, 
# and construct a bag of words representation of the string (string to count-list).
# There should be one row pr. text. The matrix should be N x M where N is the number of texts and M is the number of distinct words in all the texts.
# The result should be a list of lists ([[0,1,0],[1,0,0]] is a matrix with two rows and three columns).


import json
import string

# open json file
with open('pizza-train.json') as data_file:    
    data = json.load(data_file)

textList = [] #textList will contain list of the text in bag-of-words form
wordList = [] #wordList will contain all the words in request_text in the whole json file

for i in range(len(data)):
    #remove punctuation and change all to lowercase
    words = "".join(l for l in data[i]['request_text'] if l not in string.punctuation).lower().split()
    textList.append(words)
    wordList += words
#ensure only unqiue words in list by using set
wordList = list(set(wordList))

res = []
for text in textList:
    textCount = []
    for word in wordList:
        textCount.append(text.count(word))
    res.append(textCount)

print(res)



    


    
    
    


