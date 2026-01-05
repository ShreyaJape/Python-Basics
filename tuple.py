#Tuple is a collection which is ordered and unchangeable (i.e. immutable)
#Duplicates are allowed
#Written in round bracket ()

courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses))     # Note that we get class 'tuple' as output. 

# To access data, just like list, simply pass index within []
print(courses[1])    # Index 1 = Position 2

#tuples has only two functions defined specifically for them
# 1. count() - returns number of occurances of value
# Here 'ba' is used only once, hence output is 1
print(courses.count('ba'))
print(courses.count('baa'))    # 'baa' not part of courses. Output = 0

# 2. index() - returns the first index of value
# bsc is defined at third position (second index)
print(courses.index('bsc'))

# Let's re-define courses, and allow duplicate
courses = ('ba', 'bcom', 'bsc', 'bsc', 'ba')
print(courses)
print(courses.count('bsc'))            # 'bsc' is used twice hence 2
print(courses.index('bsc'))            # index returns the index of first occurance (so even if bsc is defined at index 2 and index 3, output will be 2)

# As we saw in the list, whenever there is collection of data, for loop becomes important. 
# Let's see simple example of for loop
for item in courses:     
  print(item)

#to check length of tuple we use len function
print(len(courses))