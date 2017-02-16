def add(x,y):
    """this function adds two numbers"""
    return float(x)+float(y)
def subtract(x,y):
    """This function subtracts teo numbers"""
    return float(x)-float(y)
def multiply (x,y):
    """This function multiply two numbers"""
    return float(x)*float(y)
def divide(x,y):
    """This function divide two numbers"""  
    return float(x)/float(y)
print("############################################")
print("************SIMPLE CALCULATOR******************")
print("...........SELECT YOUR OPERATION...............")

print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. QUIT\n\n")



choice = input("Enter choice 1/2/3/4/5\n")
num1 = input("Enter first number:   ")
num2 = input("Enter second number:  ")

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
    
elif choice =='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
        
elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))
            
elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
    
elif choice =='5':
    print("Quit")
    running = False
                


    
              
    
          



    
