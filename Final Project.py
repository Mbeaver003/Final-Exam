# Matthew Beaver
# Final Exam

#In this project, I am going to create a program that asks people whether or not they would want my website building buisness


visitor_count = 0
possible_visitor_count = 0

Q1 = input("Would you like to have a website built for you? Type Yes or No. ")

while (Q1 != "Yes","No"):

    if Q1 == "Yes":
        print("We can do that for you!")
    elif Q1 == "No":
        print("Maybe another time.")
    else:
        print("That is not an actual variable. ")
