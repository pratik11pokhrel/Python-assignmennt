#2. Write a function that asks for an integer and prints the square of it. Use a while loop with a try,
# except, else block to account for incorrect inputs.

# This should be the output of your function:
# Input an integer: “hello”
# Unrecognized number! Please try again!

# Input an integer: 2
# You entered 2, your number squared is: 4




def find():            #Defining Function & naming it find()
    while 1:           #Using while loop as stated by the question
        try:   
            a = int(input("Enter an integer: "))
            b = a ** 2
            print(b)
        except:        #Using except keyword to handle errors
            print("Unrecognized number! Please try again!")
            
            continue
        else:          #Run if no error is raised
            print("you entered",a,"your number is",b)
            break
find()                 #Calling function


#Output of the program:

# Enter an integer: hello world
# Unrecognized number! Please try again!

# Enter an integer: 4
# 16
# you entered 4 your number is 16
 
         



