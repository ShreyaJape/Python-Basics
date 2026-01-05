dummy = "hii....shreya Here!"
print(dummy)

print(type(dummy))

# Let's explore other data type quickly before focusing our attention to strings
num = 3
another_num = 3.0
print(type(num))
print(type(another_num))

val = True
print(type(val))

# Let's just print the actual values 
print(num)
print(another_num)
print(val)


# Few things to note. String has to be mentioned within '' or ""
# If your string needs ' for some reason, then you can use escape character \ like below. 
test = 'Apple\'s products are beautiful' 
print(test)
#insted of these we can use 2 double quotes
test = "Apple's product are excellent"
print(test)

# Use len() function to check length of the string (this includes the blank spaces as well)
text = "Hello World"
print(len(text))


#indexing
text = "Hello Planet"
print(text[0])
print(text[4])

text = "Welcome to Python!"

# prints string from index 2 upto 5 (i.e. from 3rd letter to 6th letter)
print(text[2:5])

# prints string upto index 2 (i.e. print index 0 and index 1 (first and second letter))
print(text[:2])

# prints string starting from index 2 onwards
print(text[2:])

#String function
text = "heLLo worLD!"

# prints string in uppercase
print(text.upper())

# prints string in lowercase
print(text.lower())

# prints first letter of each word in uppercase and rest in lowercase
print(text.title())

# Use count() to check how many times a particular character is repeated in the text
text = 'hello world'
print(text.count('l'))
