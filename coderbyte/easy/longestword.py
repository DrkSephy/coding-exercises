# Challenge:

# Have the function LongestWord(sen) take the sen parameter 
# being passed and return the largest word in the string. If 
# there are two or more words that are the same length, return 
# the first word from the string with that length. Ignore 
# punctuation and assume sen will not be empty. 

def LongestWord(sen): 
    words = sen.split(' ')
    length = 0
    for word in words:
    	if len(word) > length:
    		length = len(word)
    return length

print LongestWord("David Leonard")