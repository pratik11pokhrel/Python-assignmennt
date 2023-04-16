# . Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values

# def check():
#     a=[]
#     for i in range(1,5):
#         b=int(input("Enter the value:  "))
#         a.append(b)
#     print(a)
    
# check()

# a=[1,2,3,4,5]
# for i in a:
#     b=2
#     b=b+i
#     print(b)
def check():
 a=[1,5,3,9]
 for i in a:
    b=1
    b1=b*i
    if b1 % 2 != 0:
        print(b,"*",i)
    b=5
    b1=b*i
    if b1 % 2 != 0:
        print(b,"*",i)
        
check()
        


        