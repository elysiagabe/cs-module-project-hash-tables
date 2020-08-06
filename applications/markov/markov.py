import random

# UPER
## UNDERSTAND

## PLAN -- plan is done if we have good pseudocode
# 1. Read the file 'input.txt' and split it into words
    ### Already read in
    ### split into words

# 2. Analyze the text, building up the dataset of which words can follow a word
    ### which words can follow a word? 
        # any word that actually follows, i.e., any word at index + 1
    ### How to build dataset? 
        # Use a hash table!
            # good way to associate keys and values, relate one piece of info with other info
            # if constructing sentences, we'll be looking up often...frequent lookups
        # key: word, value: list of all the words that can follow this word

# 3. Choose a random "start word" to begin
    ### What is a "start word"?
        # word w/ capital letter or quotation mark followed by capital letter
        # first or second character is capitalized
    
    ### Make a list of start words perhaps

# 4. Loop through, print, choose a random following word, if it's a stop word --> stop
    ### What's a stop word? 
        # ends with .?! (or as second to the last character....might end with ")

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# split into words: 
words = words.split()

# TODO: analyze which words can follow other words
# Your code here

# initialize dictionary
dataset = {}

for i in range(len(words) - 1): # stop before end so we don't get error with next_word
    word = words[i]
    next_word = words[i + 1]

    if word not in dataset: 
        dataset[word] = [next_word]
    else: 
        dataset[word].append(next_word)

# make a list of start words
## If first/second character is capitalized, put into list
## loop over split words and put any start word into list (list comprehension)
## or loop over dataset keys.... could add a .keys() method to HashTable class
for key in dataset.keys():
    start_words = []
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

# choose random start word
word = random.choice(start_words)


# TODO: construct 5 random sentences
# Your code here

# loop thru dataset
stopped = False

stop_signs = "?.!"

while not stopped:
    # print start word
    print(word, end=' ')

    # if printed word is a stop word, stop
    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        stopped = True

    # choose a random following word
    following_words = dataset[word]

    word = random.choice(following_words)