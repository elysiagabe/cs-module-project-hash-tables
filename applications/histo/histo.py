'''
Hints: 
- Items: .items() method on a dictionary might be useful.
- Sorting: it's possible for .sort() to sort on multiple keys at once.
- Sorting: negatives might help where reverse won't.
- Printing: you can print a variable field width in an f-string with nested braces, like so {x:{y}}
'''

# Your code here

# initialize histogram hash table
histo = {}

# Read in all the words from robin.txt
with open("robin.txt") as f:
    # make lower case & split
    words = f.read().lower()

# remove characters to ignore (added exclamation point & quesiton mark to ignore list)
ignore = '!?":;,.-+=/\|[]}{()*^&'

words_clean = ""

for char in words:
    if char not in ignore: 
        words_clean = words_clean + char

# split words into list
words = words_clean.split()

# finds longest word for formatting reasons...length of longest + 2 = 17
# longest = max(words, key=len)
# print("longest", len(longest))

# iterate over words...word will be key in dictionary...add hashmark to value for each occurence of word
for word in words: 
    if word not in histo:
        histo[word] = "#"
    else: 
        histo[word] = histo[word] + "#"

# sort dictionary...first by number of words, then alphabetically (if have same # of occurences)

for x in sorted(histo, key=lambda x: (-len(histo[x]), x[0])):
    print(f"{x:<17} {histo[x]}")

