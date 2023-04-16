# Design a faulty calculator for the following statement:
    # 45*3=   56+9=   56/6=

op1=int(input("Enter the first number: "))
opera=input("Enter the sign: ")
op2=int(input("Enter the second number: "))
f={
    '45*':'3'
}
f2=56+9
f3=56/6


if op1==45 and opera=='*' and op2==3:
    print(0.0)
    print("You are caught cheating: ")

elif opera=='+':
    c=op1+op2
    print(c)
elif opera=='-':
    c=op1-op2
    print(c)
elif opera=='*':
    c=op1*op2
    print(c)
elif opera=='/':
    c=op1/op2
    print(c)



    

