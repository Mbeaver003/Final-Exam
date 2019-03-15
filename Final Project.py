# Matthew Beaver
# Final Exam


#In this project, I am going to create a program that asks people whether or not they would want my website building buisness


Q1 = input("Would you like to have a website built for you? Type Yes or No. ")

if Q1 == "Yes":
    print("We can do that for you!")
elif Q1 == "No":
    print("Maybe another time.")
else:
    print("That is not an actual variable. ")


#In this while statement I am going to figure out some details of what type of website they want.
while Q1 == "Yes":
    Website_Type = input("What type of website would you like me to make for you?  Buisness, or Personal. ")
    num_of_people = int(input("How many people would have ownership of this website? "))
    for i in range(num_of_people):
        name = input("What is your name? ")
        print(name + " has ownership of the " + Website_Type + " website")
    break
