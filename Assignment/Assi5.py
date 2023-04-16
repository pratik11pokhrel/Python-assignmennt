# 5. Define a class InputOutString which has at least two methods: getString: to get a string from
# console input, printString: to print the string in upper case. Also please include simple test function
# to test the class methods.

class InputOutString:
    def __init__(self):
      self.a=""
    
    def getString(self):
      self.a=input("Enter a string")
      
    def printString(self):
        print(self.a.upper())
      

hello=InputOutString()
hello.getString()
hello.printString()

