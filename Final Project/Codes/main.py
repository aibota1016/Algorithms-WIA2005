
import docx2txt as docx2txt

import obo
from stringsplitter import negativeword, positiveword

import numpy as np
import matplotlib.pyplot as plt




text = docx2txt.process("Article/Malaysia/5)Malaysia Economiy Article.docx")
# print(text)
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)
# print(sorteddict)
negcount=0
poscount=0
for s in sorteddict:
    if s[1] in negativeword:
        negcount+=1
    if s[1] in positiveword:
        poscount+=1
    else:continue
#     # print(str(s))
# print(negcount)
# print(poscount)


# creating the dataset
data = {'Words Count': len(wordlist), 'Positive Words Count': poscount, 'Negative Words Count': negcount}
x = list(data.keys())
y = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(x, y, color='maroon',
        width=0.4)

# plt.xlabel("Courses offered")
# plt.ylabel("No. of students enrolled")
# plt.title("Students enrolled in different courses")
plt.show()


print(f'Positive Words Count : {poscount}\nNegative Words Count: {negcount}\nResult:')

if poscount>negcount:
    print("Positive Sentiment")
else:print("Negative Sentiment")