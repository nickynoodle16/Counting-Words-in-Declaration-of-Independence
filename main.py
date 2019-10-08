# opens, closes, and reads in whole text file
with open('declaration.txt', 'r') as dataFile:
    string = dataFile.read()

word_delimiter = [' ','.','?','!',',',';',':','/','\\','_','|','(',')','[',']','{','}','~','\n','\t']

WordList = {}
word = ''
CountWords = 0

for  letter in string:
  if letter in word_delimiter: #found an end to a word
    if len(word)>0:
     # print(word)
      if word.lower() in WordList: 
       CountWords += 1
       WordList[word.lower()] += 1
      else: 
       WordList.update({word.lower(): 1})
    word = ''
  else:
    word += letter
    
totalcount = 0
    
sorted(WordList.keys())
for key in sorted(WordList.keys()):
  value = WordList[key]
  totalcount += value #increment add value. totalcount keeps a running total of words and adds and prints it out at the end to get 1337 words.
  print(key,value)
print('\nTotal is', totalcount)
