from Calculator import Calculator
while True:
    first_number=float(input("\nenter the first number: "))
    second_number=float(input("enter the second number: "))

    y=Calculator(first_number,second_number)

    def operations():
        options = """
                Please select one of the following: 
                    =======================================
                    + for addition
                    - for subtraction 
                    * for multiplication 
                    / for division
                    % for modulus
                    tr to find the area of a triangle
                    in to convert cm_to_inches 
                    cm to convert inches_to_cm 
                    0 to exit
                    ========================================
                    """
        print(options)
    operations()
    selection= input('enter your operator: ')
    if selection=="0":
        print('Exit...')
        break
    elif selection=="+" :
        print(y.addition(first_number,second_number))
    elif selection=="-" :
        print(y.subtraction(first_number,second_number))
    elif selection=="*" :
        print(y.multiplication(first_number,second_number))
    elif selection=="/" :
        print(y.division(first_number,second_number))
    elif selection=="tr" :
        print(y.tr(first_number,second_number))
    else:
       print("Invalid Operator.")

