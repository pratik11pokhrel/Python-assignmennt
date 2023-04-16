# Write a lambda function that takes in two numbers, and returns the sum of the squares of the
# input numbers.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
x = lambda a, b : a ** 2 + b ** 2
print(x(num1,num2))