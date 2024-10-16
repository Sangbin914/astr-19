#Write a Python program that declares a class describing your favorite animal. 
#Have the data members of the class represent the following physical parameters of 
#the animal: length of the arms (float), length of the legs (float), number of eyes (int), 
#does it have a tail? (bool), is it furry? (bool). Write an initialization function 
#that sets the values of the data members when an instance of the class is created. 
#Write a member function of the class to print out and describe the data members 
#representing the physical characteristics of the animal.

class Animal:
	def __init__(self, arm, leg, eyes, tail, furry):
		self.arm = arm
		self.leg = leg
		self.eyes = eyes
		self.tail = tail
		self.furry = furry

def describe(self):
    # Print the characteristics of the animal
    description = (
        f"Favorite Animal Characteristics:\n"
        f" - Arm Length: {self.arm} meters\n"
        f" - Leg Length: {self.leg} meters\n"
        f" - Number of Eyes: {self.eyes}\n"
        f" - Has Tail: {'Yes' if self.ail else 'No'}\n"
        f" - Is Furry: {'Yes' if self.furry else 'No'}"
    )
    print(description)

def main():
	fav = Animal(20.0, 20.0, 2, True, True)
	describe(fav)

if __name__ == "__main__":
	main()