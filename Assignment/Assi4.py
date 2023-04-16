# 4. Complete the class given below:
# class Cylinder:

#  def __init__(self,height=1,radius=1):
#  pass

#  def volume(self):
#  pass

#  def surface_area(self):
#  pass

import math
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        

    def volume(self):
        volume=math.pi*self.radius**2*self.height
        return volume
        
    def surface_area(self):
        surface = 2 * math.pi *self.radius*self.height + (2 *math.pi * self.radius **2)
        return surface
 
h=20
r=10       

answer=Cylinder(h,r)
print("The volume of the cylinder is: ",answer.volume())
print("The surface area of the cylinder is : ",answer.surface_area())



