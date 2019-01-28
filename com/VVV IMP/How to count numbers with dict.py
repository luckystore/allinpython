# Model 1
def countNum(word):
    wordDict =  {}
    for index in word:
        try:
            wordDict[index] += 1
        except KeyError:
            wordDict[index] = 1
    return wordDict
wordDict = '1,2,3,4,4,4,4,5,6,7,8,9,9,8,7,7,7,6,3,2,0'.split(',')
print(wordDict)
print(countNum(wordDict))

# Model 2
number = '1234567890'
wordDict = '1,2,3,4,4,4,4,5,6,7,8,9,9,8,7,7,7,6,3,2,0'
str = wordDict.casefold()

count = {}.fromkeys(number, 0)

for char in str:
    if char in count:
        count[char] += 1
print(count)

# vowels = 'aeiou'
# str = 'Hello, have you tried our tutorial section yet?'
# str = str.casefold()
#
# count = {}.fromkeys(vowels,0)
#
# for char in str:
#    if char in count:
#        count[char] += 1
# print(count)

