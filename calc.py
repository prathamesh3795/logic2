def calculate():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    c=input("enter your choice(+,-,*,/)")
    match(c):
        case "+":
            print(a+b)
        case"-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            print(a/b)
calculate()