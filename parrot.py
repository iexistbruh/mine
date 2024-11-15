class Parrot:

    #class attribute
    species="bird"

    #instance attribute
    def_init_(self,name,age):
    self.name = name
    self.age = age

#instantiate the Parrot class
blu = Parrot("Blu",10)
woo = Parrot("Woo",10)

#access the class attribute
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

#access the instace attribute
print("{} is {} years old".format(blu.age,blu.name))
print("{} is {} years old".format(woo.age,woo.name))