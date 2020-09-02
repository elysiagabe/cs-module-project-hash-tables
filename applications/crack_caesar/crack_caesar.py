# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# initialize letter count hash table
letter_count = {}

# open and read text
with open("ciphertext.txt") as f:
    text = f.read()

# only find counts of letters in the alphabet
for char in text:
    if char not in letter_count and char.isalpha():
        letter_count[char] = 1
    elif char in letter_count and char.isalpha():
        letter_count[char] += 1

# sort by frequency
sorted_count = dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))

# from read me...in order of frequency
sorted_alph_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# replace the numeric value with the letter by frequency (sorted_alph_list from README)
modifiedList = dict(map(lambda x, y: x + y, sorted_count, sorted_alph_list))

# decode the text
decoded = ""

for ltr in text: 
    if ltr in modifiedList:
        decoded += modifiedList[ltr]
    else: 
        decoded += ltr

print(decoded)