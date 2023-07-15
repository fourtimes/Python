# list = [1,2,3,4,5,6,7,5,4,3,2]

# #  print the odd and even numbers
# for i in list: print("even") if (i % 2) == 0 else print("odd")

# # get the 4th value only
# for i in list:
#     if list[list.index(4)] == i:
#         print(list[list.index(4)])


# colors = ["RED", "yellow", "green"]
# print(colors.index('green')) # returns the index of the specified element in the list

# for color in colors:
#     if color == "RED":
#         print(color.upper()) # returns the uppper letter case

#         print(color.isalpha()) # returns the value in alphabetical order
#         print(color.casefold()) # returns the value from uppercase to lowercase
#         print(color.count('E')) # returns the number of letter occurrences of a substring in the given string.


l = [{'value': 'apple', 'blah': 2},
     {'value': 'banana', 'blah': 3},
     {'value': 'cars', 'blah': 4}]

# for i in a:
#     print(i['value'])
#     # b=i.values()
#     # print(b)

an = [ print(i['value']) for i in l if 'value' in i]