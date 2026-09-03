a="3"
b="6"
print(a+b)
#python doesnot take a as a string not as a interger so it will print 36 instead of 9 because it will concatenate the two strings instead of adding them. To add them we need to convert them into integer using int() function.
print(int(a)+int(b))

#now first we tell the python that it's not string but an integer so we use int() function to convert it into integer and then we add them.
c="3.5"
d="6.5"
print(c+d)
#python doesnot take c as a string not as a float so it will print 3.56.5 instead of 10.0 because it will concatenate the two strings instead of addingthem. To add them we need to convert them into float using float() function.
print(float(c)+float(d))

e=7
f=6
print(e+f)
#python takes e and f as integer so it will print 13 instead of 76 because