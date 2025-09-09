class animal():
    def sound(self):
        return "animal sound"
    def sound(self):
        return "bow bow"
    def animal_name(self):
        return "lab"
class cat():
    def sound(self):
        return "meows"
class dog(cat,animal):
    pass
    

s1=animal()
s2=cat()
s3=dog()

print(s3.sound())
print(s3.animal_name())
