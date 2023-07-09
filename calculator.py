print("Welcome to the calculator")
print("Enter two numbers")
num1= input("Number1: ")
num2= input("Number2: ")
print("NUMBER 1 :"+num1)
print("NUMBER 2 :"+num2)
print("What operation you want to perform?")
print("-------MENU-------")
print("1.Additon(+)")
print("2.Substract(-)")
print("3.Multiplication(*)")
print("4.division(/)")
print("Enter your choice:")
choice = input()
if int(choice) == 1:
    print("You want the addition of "+num1+" & "+num2)
elif int(choice)==2:
    print("You want the Subsrtaction of "+num1+" & "+num2)
elif int(choice)==3:
    print("You want the Multiplication of "+num1+" & "+num2)
elif int(choice)==4:
    print("You want the Division of "+num1+" & "+num2)
else :
    print("invalid selection")
if int(choice) == 1:
    result=int(num1)+int(num2)
    print("The Sum of " +num1+ " & " +num2+ " is : "+str(result))
elif int(choice) == 2:
    result=int(num1)-int(num2)
    print("The subsrtaction of " +num1+ " & " +num2+ " is : "+str(result))
elif int(choice) == 3:
    result=int(num1)*int(num2)
    print("The multiplication of " +num1+ " & " +num2+ " is : "+str(result))
elif int(choice) == 4:
    result=int(num1)/int(num2)
    print("The division of " +num1+ " & " +num2+ " is : "+str(result))
print("THANK YOU !!!!")

