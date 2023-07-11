a = [1,2,3,4,5,6,7,8,6,5,4,4]
print(a)

# pop() - eliminating the last number 
a.pop()
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4]

# append() - add the one more value in the list
a.append(44)
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 44]

# copy() - copy the entire list to the another list format
a.copy()
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 44] 
        #  [1, 2, 3, 4, 5, 6, 7, 8, 6, 5, 4, 44]

# clear() - clear all the values in the list
a.clear()
print(a) # []


# extend() - add multiple elements at the same time at the end of the list.
b = ['ashli', 'vic', 'jino']

b.extend([6, "demo",9])
print(b) # ['ashli', 'vic', 'jino', 6, 'demo', 9]

