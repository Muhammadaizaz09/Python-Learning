name="aizaz"
friend="ali"

#charachter in double quotes are knnown as strings anything inside double quotes is known as string. and we can use single quotes also to define a string.

print(name)
print(friend)

text="my name is aizaz \" i am a student of bscs \""
print(text)

#to print anything in double quotes we use backlashbefore the qoutes
#we also have another method for it write """ to start or ''' to start then we can print it

discription= """I am a uet student and my major is "Computer Science" """
print(discription)

#Now indexing 
print(name[0]) #this will print the first character of the string name
print(name[1]) #this will print the second character of the string name
print(name[2]) #this will print the third character of the string name

#to print a long block of statement we use for loop 

for character in discription:
    print(character) #this will print each character of the string discription in a new line.


#String slicing 
pips="python is a programming language"
print(pips[0:12]) #this will print the first 12 characters of the string pips
print(pips[13:31]) #this will print characters from index 13 to 31 of the string pips
len=len(pips) #this will print the length of the string pips
print(len)

#how to covert string into upper case and lower case

print(name.upper())
#this will convert the string name into upper case and print it



#strings are immutable in python we cannot change the value of a string once it is created but we can create a new string with the same value and assign it to the same variable name.



#now replace the value of name with a new value


name="ali"
print(name.replace("ali", "basit"))

#this replaces the value of name with new value 


#center() 
str1="WELCOME TO PYTHON PROGRAMMING LANGUAGE"
print(str1.center(80))  
#this will center the string str1 in a width of 80 characters and print it.











