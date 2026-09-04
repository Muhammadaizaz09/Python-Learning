balance = 50000
pin = int(input("Enter your pin: "))

if pin == 1234:
  print("1. Current account, 2. Saving account")
  choice = int(input("Please select account type: "))
  withdraw = int(input("Enter the amount to withdraw: "))

  if withdraw > balance:
    print("Low balance")
  elif choice == 1:
    if withdraw < 500:
      print("Cannot withdraw less than 500")
    elif withdraw > 30000:
      print("Cannot withdraw more than 30000")
    else:
      balance -= withdraw
      print("Withdraw successful")
      print("Remaining amount", balance)
  elif choice == 2:
    if withdraw < 500:
      print("Cannot withdraw less than 500")
    elif withdraw > 20000:
      print("Cannot withdraw more than 20000")
    else:
      balance -= withdraw
      print("Withdraw successful")
      print("Remaining balance:", balance)
  else:
    print("Invalid account type")
else:
  print("Incorrect pin")
     

 
    
