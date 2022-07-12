import math

#Basic Calculator
choice=1
while True:
    print('1. Addition\t2. Subtraction\t3. Multiplicaton\t4.Division\t5. Exponential\t6. Root\t 7. Factorial\t8. Multi Input Operation\t9. Exit')
    choice = int(input('Enter the Choice : '))

    #Add
    if choice==1 :
        num1 = float(input('Enter the First Number : '))
        num2 = float(input('Enter the Second Number : '))
        result = num1 + num2
        print('{} + {} = {}\n'.format(num1,num2,result))


    #Subtract
    elif choice==2:
        num1 = float(input('Enter the First Number : '))
        num2 = float(input('Enter the Second Number : '))
        result = num1 - num2
        print('{} - {} = {}\n'.format(num1,num2,result))


    #Multiplication
    elif choice==3:
        num1 = float(input('Enter the First Number : '))
        num2 = float(input('Enter the Second Number : '))
        result = num1 * num2
        print('{} * {} = {}\n'.format(num1,num2,result))


    #Division
    elif choice==4:
        num1 = float(input('Enter the Dividend : '))
        num2 = float(input('Enter the Divisor : '))
        result = num1 / num2
        print('{} / {} = {}\n'.format(num1,num2,result))


    #Exponential
    elif choice==5:
        num1 = float(input('Enter base number : '))
        num2 = int(input('Raise to number : '))
        result = num1**num2
        print('{}^{} = {}\n'.format(num1,num2,result))


    #Roots
    elif choice==6:
        num1 =  float(input("Enter a number : "))
        if num1<0:
            print('Error! Number Less than zero. \n')
            continue
        print('1.Square Root\t2. Cube Root\n')
        choice1 = int(input('Enter the Choice : '))

        if choice1==1:
            result = math.sqrt(num1)
            print('Square Root of {} is : {}\n'.format(num1,result))

        elif choice1==2:
            result = num1**(1/3)
            print('Cube Root of {} is : {}\n'.format(num1,result))


    #Factorial
    elif choice==7:
        num1=int(input('Enter a number : '))
        if num1<0:
            print('Erro! Number less than zero\n')
            continue
        result = math.factorial(num1)
        print('{}! = {}'.format(num1,result))


    #Multiple Number Operation
    elif choice==8:
        value = input("Perform Operation : ")
        print(value)
        result = eval(value)
        print(result)


    #Exit
    elif choice==9:
        print('\n***Calculator Shutdown***')
        break


    #For Invalid Inputs
    else:
        print('Invalid Operation\n')















