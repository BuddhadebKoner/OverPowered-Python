class Student:
    def __init__(self,name):
        self.name = name
        
        
s1 = Student("Buddhadeb")
print(s1.name)
del s1.name
print(s1.name) #obbiusly it will show error, s1 obj is deleted
        
  
                    
