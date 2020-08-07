# In the program below, we have used anonymous (lambda) function inside the filter() built-in function to find all the numbers divisible by 13 in the list.

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)
