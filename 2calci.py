while True:
    print("MY CALCULATOR")
    print("===============")
    print("1. ADDING")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("0. Exit")
    operation=int(input("PLEASE CHOOSE OPERATION:"))

    if operation==1:
        number1=int(input("Enter 1st Number:"))
        number2=int(input("Enter 2nd Number:"))
        add=number1+number2;
        print("Result:",add)
    elif operation==2:
        number1=int(input("Enter 1st Number:"))
        number2=int(input("Enter 2nd Number:"))
        sub=number1-number2;
        print("Result:",sub)
    elif operation==3:
        number1=int(input("Enter 1st Number:"))
        number2=int(input("Enter 2nd Number:"))
        mul=number1*number2;
        print("Result:",mul)
    elif operation==4:
        number1=int(input("Enter 1st Number:"))
        number2=int(input("Enter 2nd Number:"))
        div=number1/number2;
        print("Result:",div)
    elif operation==0:
        print("Exit")
        break
    else:
        print("Please choose correct operation")
    x=input("Do you want to continue yes or no")
    if x!='yes':
        print("exit")
        break