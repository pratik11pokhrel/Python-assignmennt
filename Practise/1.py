# class animal:
#     def dog(self):
#         print("I am a dog ")
#         return "I am a dog"
#     def cat(self):
#         print("I am a cat ")
#         return 'i am cat'
        

# a=animal()
# b=animal()
# print(b.dog())
# print(a.cat())


# class animal:
#     def __init__ (self,name):
#         self.name=name
#         print(name)
        
        
# a=animal('tom')
# b=animal('dom')




class Dog:
    species='Dog'
    
    def dog_name(self,dog1):
        print('Your dog name is ',dog1,'and its species is',self.species)
    
puppy=Dog()
pup=Dog()
puppy.dog_name('tommy')
Dog.species='tiger'
pup.dog_name('tim')
puppy.color='red'
print(puppy.color)


        
