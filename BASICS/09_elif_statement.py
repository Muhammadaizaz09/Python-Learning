
num=int(input("Enter a number "))
if(num<0):
    print("the number is negative")

elif(num==0):
    print("the number is zero")

elif(num%2==0):
    print("the number is a even number ")    

else :
    print("the number is a postive number ")

#this is a simple elif statment program 

#the next program

marks=float(input("enter your marks "))
if(marks>=90):
    print("your grade is A")

elif(marks>=80):
     print("your grade is b")   

elif(marks>=70):
     print("your grade is c")  

elif(marks>=60):
     print("your grade is d")  

else:
    print("your grade is F")


# A simple login program with elif conditions.



username=str(input("Enter your username :"))
password=str(input("enter your pass :"))
if username == "Aizazkhan09"  and password == "005522":
    print("login succesfull")
elif username !="Aizazkhan09" or password != "005522":
    print(" PLease Enter the correct username and password") 
elif username != "AizazKhan09" and password == "005522" :
    print(" Please Enter the correct username ")   
elif username =="Aizazkhan09" and password !="005522":
    print(" please Enter the correct password")    
else:
    print("login unsuccefull")


#simple ATM program    
balance= 50000

print(" 1.check balance \n 2.withdraw money,\n 3.deposit money")
choice= int(input("please select one :"))
if choice == 1 :
    print("your balance is :",balance)

elif choice ==2 :
    amount=int(input("enter the amount for withdrawl :"))
    if amount> balance :
        print("insufficent amount")
    else :
        balance = balance - amount 
        print("withdrawl successful")
        print("remaining amount :", balance)
            

elif choice == 3 :
    amount=int(input("Enter the amount to deposit: "))
    balance= balance + amount
    print("deposit successful")
    print("new balance ", balance)

else :
    print("invalid choice ")
    


