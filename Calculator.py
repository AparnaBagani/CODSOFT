print("Calculator Menu: \n" \
      "1. Addition\n" \
      "2. Subtraction \n" \
      "3. Multiplication \n" \
      "4. Division \n"  )
def Addition(num1,num2):
    return num1+num2
def Subtraction(num1,num2):
    return num1-num2
def Multiplication(num1,num2):
    return num1*num2
def Division(num1,num2):
    return num1/num2
select = int(input("Choose the operation you want to do 1,2,3,4:"))

number_1 = int(input("Enter 1st no:"))
number_2 = int(input("Enter 2nd no:"))

if select == 1:
    print(number_1,"+",number_2,"=", Addition(number_1,number_2))
elif select == 2:
    print(number_1,"-",number_2,"=", Subtraction(number_1,number_2))
elif select == 3:
    print(number_1,"*",number_2,"=", Multiplication(number_1,number_2))
elif select == 4:
    print(number_1,"/",number_2,"=", Division(number_1,number_2))
else:
    print("invalid input")