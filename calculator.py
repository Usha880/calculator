# PYTHON PROGRAM TO PERFORM SIMPLE CALCULATOR WITH BASIC ARITHMETIC OPERATIONS
print("SIMPLE CALCULATOR USING ARITHMETIC OPERATIONS")
number_1=int(input("enter a number1:"))
number_2=int(input("enter a number2:"))
operator=input("enter a operator of your choice:")

#perform addition
if operator == '+' :
    print("perform addition")
    result=number_1+number_2
    print(f"Addition of given numbers is  :{result}")
    

#perform subtraction    
elif operator == '-' :
    print("perform subtraction")
    result=number_1-number_2
    print(f"Subtraction of given numbers is:{result}")
    

#perform multiplication
elif operator == '*':
    print("perform multiplication")
    result=number_1*number_2
    print(f"Multiplication of given numbers is :{result}")
     

#perform division
elif operator=='/':
    print("perform Division")
    result=number_1/number_2
    print(f"Division of given numbers is :{result}")
else:
    print("Invalid choice")