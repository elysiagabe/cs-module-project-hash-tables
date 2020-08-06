'''
Add up and print the sum of the all of the minimum elements of each inner array:

[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
'''

# need to loop thru outer array
# find minimum value of each inner array
# add up each of the minimum values

my_arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

sum = 0
i = 0
while i in range(len(my_arr)):
    inner_min = min(my_arr[i])
    sum += inner_min
    i += 1

print(sum)



