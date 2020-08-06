def no_dups(s):
    # Your code here
    my_dict = {}
    output_string = ""
    word_list = s.split()

    if len(word_list) < 1:
        return output_string

    for word in word_list:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    for key in my_dict:
        if len(output_string) == 0:
            output_string += key
        else: 
            output_string += f" {key}"

    return output_string
    

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))