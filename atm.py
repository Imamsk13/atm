print("welcome to STATE BANK OF INDIA")
print("0 log out ",)
print("1 view balance ")
print("2 cash withdrawl")
print("3 deposit cash")
print("4 change pin")

b= int(input("  ")) 
   
if b == 0:
        print("succesfully logged out")
elif b == 1:
        print("your current balance is xxxxx.xx")
elif b == 2:
        a= int(input("enter your ATM PIN"))
        if a in range(1111,9999):
            c= int(input("enter amount to withdraw"))
            print(" amount  withdrawn ")
        else: print("wrong pin")
elif b == 3:
        a= int(input("enter your ATM PIN"))
        if a in range(1111,9999):
            c= int(input("enter amount to deposit"))
            print(" amount  deposited ")
        else: print("wrong pin")
elif b == 4:
        a= int(input("enter your ATM PIN"))
        if a in range(1111,9999):
            c= int(input("enter your new pin"))
            if c in range(1111,9999):
                 print(" pin changed ")
            else: print("unexpected error")
        else: print("wrong pin")
else: print("unexpected error")