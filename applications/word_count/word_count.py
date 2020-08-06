def word_count(s):
    # Your code here
    # initialize dictionary
    big_dict_energy = {}

    # lower case the input string
    s = s.lower()

    # filter out ignored chars
    ignore = '":;,.-+=/\|[]}{()*^&'

    s_clean = ""

    for char in s:
        if char not in ignore:
            s_clean = s_clean + char

    # break the string into list of words
    s = s_clean.split()
    print(s)

    # iterate over the list
    for word in s:
        # if key not in dictionary
        if word not in big_dict_energy:
            # insert the key...value of 1
            big_dict_energy[word] = 1
        # otherwise,
        else:
            # increment the value by 1
            big_dict_energy[word] += 1
    
    return big_dict_energy


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))