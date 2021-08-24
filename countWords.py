#this sign is used to make a comment
#filename should end with .py
yourIntro = input ('Enter your introduction')
characterCount = 0
wordCount = 1
#wordCount starts with 1, because only 3 spaces

for character in yourIntro :
    characterCount = characterCount + 1
    if (character == ' ') :
        wordCount = wordCount + 1

if (wordCount > 20) :
    print('This is a big introduction')
elif (wordCount < 20 and wordCount > 10) :
    print('This is a medium introduction')
elif (wordCount < 10) :
    print('This is a small introduction')

print(wordCount)
print(characterCount)

#use python3 filename to see the output