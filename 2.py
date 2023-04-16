#  Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.

def takes():
    b=[]
    d=0
    cube=0
    
    a=int(input("How many numbers you want to enter: "))
    # number=int(input("Enter your intended number: "))
    
    for i in range(a):
        c=int(input("Enter the number: "))
        b.append(c)
        
    for g in b:
         cube=g*g*g
         d+=cube
    return d

amazing=takes()
print(amazing) 



        
        
         
    