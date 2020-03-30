#!/bin/python3
################INTRO TO PYTHON##################

#This is a comment
print("This is a string")
print('Hello World')
print("""Hello this is
a multi line string""")
print("This is"+" a string")
print("\n") #new line

#Math
print("Math time")
print(50+50)	      #Add
print(50-50)	      #Sub
print(50*50)	      #Mul	
print(50/50)          #Divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50**2)	      #Exponent
print(50%6)           #Remainder
print(50//6)          #No decimal
print("\n")

#Variable & Methods
print("Fun with variable and methods:") 
quote = 'Life is a W.I.P'
print(len(quote))
print(quote.upper())
print(quote.lower())
print(quote.title())

name = "Nikhil"
age =20	     #int int(20)
gpa =6.4     #float float(6.4)
print(int(age))
print(int(20.6)) #omits the decimal

print("My name is "+name+" and I am "+str(age)+" years old.")

age +=1
print(age)
birthday=1
age += birthday
print(age)

#Functions
print("Functions")
def who_am_i():
	print("\nThis is Start of Function")
	name = "Nikhil"
	age =20	     #int int(20)
	gpa =6.4     #float float(6.4)
	#print(int(age))
	#print(int(20.6)) #omits the decimal
	print("My name is "+name+" and I am "+str(age)+" years old.")
	print("Function Ends here")
	
who_am_i()	

#with single parameters
def add_one_hundred(num):
	print(num+100)
	
add_one_hundred(100)	
	
#with multiple parameters
def add(x,y):
	print(x+y)
		
add(69,420)

#return values
def multiply(x,y):
	return x*y
	
print(multiply(7,7))

def root(x):
	return x **0.5

print(root(64))

#Boolean (True or False) 			
print("\nBoolean Expressions")
bool1 =True
bool2 =3*3 ==9
bool3 =False
bool4 = 3*3 !=9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5="True"
print(type(bool5))	

#Relational and Boolean Operators
greater_than=7>5
less_than=5<7
greater_than_equal_to =7>=7
less_than_equal_to =7<=7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)	

test_and = (7>5) and (6<7)
test_or  = (7>5) or (5<7)
test_not = not True

print(test_and)

#Conditional Statements	
print("\nConditional Statements")
print("\nFunction 1")
def soda(money):
	if money>=2:
		return "You get a soda!"
	else:
		return "Nope."

print(soda(3))
print(soda(1))	

print("\nFunction 2")
def alcohol(age,money):
	if (age >=21) and (money>=5):
		return "You can get DrUnK!"
	elif (age>=21) and (money<5):
		return "Get More moolah!"
	elif (age<21) and (money>5):
		return "Get out kid."
	else:
		return "Nope."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))		

#lists
print("\nLists Contain Brackets")
movie=["Kung Fu Panda","The Hangover","Iron Man I"]
print(movie[1])
#list slicing
print(movie[0:2])
print(movie[:1])
print(movie[1:])
print(movie[-1])	#Last item
print(len(movie))

#Adding to List
movie.append("Big Hero 6")
print(movie)

#Removing from List
movie.pop()
print(movie)
movie.pop(1) 		#Specific Delete
print(movie)

#Combining Lists
person =["Nikhil","BongoCat","Markimoo"]	#Makrimoo isnt zipped since less number of movies,only number available are zipped rest are removed
combined = zip(movie,person)
print(list(combined))

#Tuples

print("\nTuples have parentheses and cannot be changed\n")
grades = ("A","B","C")
print(grades)

#Loops
print("\nFor loops - start to finish of iterate:")
veggie=["Cucumber","Broccoli","Cabbage"]
for x in  veggie:
	print(x)
print("\nWhile loops - Execute as long as True:")
i=0;
while i<10:
	print(i)
	i+=1
