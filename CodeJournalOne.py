#State my name / pronouns / movie / food
name = "Sangbin Lee"
pronoun = "He/him"
movie = "Forest Gump"
food = "Fried Chicken"


#prints my name
def PrintName():
	print("Hello my name is ", name)

#prints my preferred pronouns
def PrintPronouns():
	print("My preferred pronoun is ", pronoun)

#prints my favorite movie
def PrintMovie():
	print("My favorite movie is ", movie)

#prints my favorite food
def PrintFood():
	print("My favorite food is ", food)

#main function that I will execute
def main():
	PrintName()
	PrintPronouns()
	PrintMovie()
	PrintFood()

#execute main fuction as program runs
if __name__ == "__main__":
	main()

