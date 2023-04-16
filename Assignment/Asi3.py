# 3. Complete the Line class given below. Your class should accept two sets of coordinate points as
# tuples. Write two methods within the class, one to compute distance between two points, and
# another to compute the slope

# You have to complete the code given below:
# class Line:
#  def __init__(self,coordinateA,coordinateB):
#  pass
#  def distance(self):
#  pass
#  def slope(self):
#  pass
# Example output:
# c1 = (3, 2)
# c2 = (8, 10)
# myline = Line(c1, c2)



# import  math    # using importing math method to use square root for formula
# class Line:
#     def __init__(self,coordinateA,coordinateB):
#         self.place1=coordinateA     #Initializing 
#         self.place2=coordinateB     #Initializing
        
#     def distance(self):
#         x1,y1=self.place1
#         x2,y2=self.place2
#         distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  #Using formula to get the distance
#         print("The distance between teo points is: ",distance)
    
#     def slope(self):
#         x1,y1=self.place1      #Initializing the points x1 y1 in self.place1 respectvely
#         x2,y2=self.place2
        
#         slope=(y2-y1)/(x2-x1)
#         print("The slope of two points is: ",slope)
 
 
        
# c1=(3,2)          #As stated in the question
# c2=(8,10)  

# myline=Line(c1,c2)   #Providing Arguments
# myline.distance()         #Calling respective function
# myline.slope()


# # Output of the program

# # The distance between teo points is:  9.433981132056603
# # The slope of two points is:  1.6


import math
class Line:
    def __init__(self,CoordinateA,CoordinateB):
        self.x1=CoordinateA[0]
        self.y1=CoordinateB[0]
        self.x2=CoordinateA[1]
        self.y2=CoordinateB[1]
    
    def distance(self):
        distance = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return distance
    
    def slope(self):
         slope=(self.y2-self.y1)/(self.x2-self.x1)
         return slope

c1=(3,2)            
c2=(8,10)  

myline=Line(c1,c2)   

print("The distnace between two points is: ",myline.distance())
print("The slope between two points is:  ",myline.slope())


        
        
        




