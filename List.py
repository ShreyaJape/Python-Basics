#List is immutable
# #denoted by square bracket

greeting = ['hii', 'hello', 'hey', 'yup', 'nope', 'ohk']
print(greeting) 
print(type(greeting))

#----------------Accessing list items-------------------
# Access first element
print(greeting[0])

# Access first and second element
print(greeting[0:2])

# Access 2nd to 5th element 
# 2nd element = 1st index, 5th element = 4th index
print(greeting[1:5]) 

# Access last element (sometimes you don't know how long a list is, so a quick shortcut is)
print(greeting[-1])   # -1 represents last
print(greeting[-2])   # -2 represents second last
print(greeting[-3:-1]) # print from thirdlast  to last (excluding last)
print(greeting[-3:]) # print from thirdlast  to last (including last)

#--------------list Function-----------------
greeting.append("wlc")      #appends the element at the last position
print(greeting)

# To insert an element somewhere in the middle, say 3rd index
greeting.insert(3, 'ME')           # i.e. insert requires position and value
print(greeting)

# You can append another variable as well
c = 'pls'
greeting.append(c)
print(greeting)

# You can append a list within a list
new = ['yes', 'hello']   # Defining a new list
greeting.append(new)      # Appending new list to the old list
print(greeting)           # Note that the list itself got inserted into the list. That list constitutes one element and not two. 

# To add individual list items to the original list, use the function extend
greeting.extend(new)
print(greeting)

# To remove last entry of list, use pop()
greeting.pop()
print(greeting)

# To remove specific item, use remove()
greeting.remove('hello')
print(greeting)    # ba is removed

flowers = ['lily','aster','sunflower','rose','tulip','lotus']
print(flowers)

flowers.sort()
print(flowers)

flowers.reverse()
print(flowers)

# Similary, sort works on the list with only numbers as well
nums = [12, 4, 2, 11, 1, 100]
print(nums)
nums.sort()
print(nums)

# to check length of list, use len()
countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
print(len(countries))

nums = [8, 4, 2, 1, 16]     # Returns the highest number, when list is of numbers
print(max(nums))    #output 16
print(min(nums))      #output1
print(sum(nums))   #output 31

print(max(countries))   # Returns the one with highest alphabet, when list is made of strings
print(min(countries))

countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
for i in countries:
    print(i)

# Note that : is required at the end of for line. Also, the next code block needs to have 4 indentation (i.e. blank space). 
# Check the difference between these two examples
for x in countries:
  print(x)
print('Now I am outside the for loop')
print('-------------')
for x in countries:
  print(x)
  print('Now I am inside the for loop')   #these sentense will print after every country name

for item in countries:
  print(item, len(item))          # printing each item and its length

for item in countries:
  print(item, item.upper(), len(item))          # Let's capitalize as well

# Use enumerate() function to get index of element.
for id, item in enumerate(countries):   # enumerate returns index along with the actual item, hence we need to catch it explicitly. 
  print(id, item) 

# let's try to create a list using for loop and append()
cubes = []    # first define a blank list
for i in range(5):       # you can explore what range(5) gives. In short, it returns numbers upto 5. 
  cubes.append(i ** 3)
print(cubes)

# To deconstruct what is exactly happening in the above code, you can use print() like this
cubes = []    
for i in range(5):       
  print("i = ", i)
  cubes.append(i ** 3)
  print("Number appended (i ** 3) = ", i ** 3)
  print("Current status of cubes list = ", cubes)
print()
print('Outside for loop')
print(cubes)

#----------------Nested List
fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[0], type(fruits[0]))
print(fruits[1], type(fruits[1]))
print(fruits[0][0])       #mango
print(fruits[1][0])       #sitafal







