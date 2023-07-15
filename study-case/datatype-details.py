name = 'docker'
print(name.capitalize())       # Docker

language = 'Python'
print(language.casefold())       # python

Place = 'chennai'
print(Place.center(15))            #        chennai => Allocate 15 places and then print the place

fan = ['usha','chrompton','usha']
print(fan.count('usha'))           # 2 => to show the how many usha's there in the list

sub = ['maths','tamil','eng']
list = sub[2].encode("utf-8")
print(list)                         # b'eng' => dispalys the encoded values with the specified value

number = ['one', 'two', 'three']
print(number.index('two'))          # 1 => Displays the index of the place

letter = ['a','b','c','d']
letter.insert(3,'dmo')
print(letter)                    # ['a', 'b', 'c', 'dmo', 'd'] 


name=['ashli', 'joe', 'joseph', 'vic']
print(name.pop())                # vic => without argument, pop print the last values of the list
print(name.pop(2))              # joseph => with argument, Prints the specified value of the argument


fruits = ['apple', 'orange', 'banana']
fruits.remove('orange')
print(fruits)                    # ['apple', 'banana'] => eliminate the specified element.


keys= ['hi', 'hello', 'welcome']
keys.reverse()
print(keys)                      # ['welcome', 'hello', 'hi']

code_lang = ['python', 'nodejs', '.net', 'react', 'java']
code_lang.sort()
print(code_lang)                 # ['.net', 'java', 'nodejs', 'python', 'react'] => displays the values in ascending order

