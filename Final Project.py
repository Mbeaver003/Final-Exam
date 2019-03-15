"""
Matthew Beaver
Final Exam
3/15/19
In this project, I am going to create a program that asks people whether or not they would want my website building

buisness and find out what type of website they want, who is the owners and what their price range is.

"""


# Starting here I am going to find out whether they would like to have a website built for them.  When they answer what they want they will get different answers for each different response.

Q1 = input("Would you like to have a website built for you? Type Yes or No. ")

if Q1 == "Yes":
    print("We can do that for you!")
elif Q1 == "No":
    print("Maybe another time.")
else:
    print("That is not an actual variable. ")

# Starting here, we find out what type of website they want, and how many people will have control of the website.  Then we respond with what they put in and our own message.
while Q1 == "Yes":
    Website_Type = input("What type of website would you like me to make for you?  Buisness, or Personal. ")
    num_of_people = int(input("How many people would have ownership of this website? "))
    for i in range(num_of_people):
        name = input("What is your name? ")
        print(name + " has ownership of the " + Website_Type + " website")
    break

# Here we are going to figure out their budget and depending on how much money they put in.

if Q1 == "Yes":
    budget_of_website = float(input("Now, it is time to decide your budget, you can put up to $1000.  The more money you are willing to spend, the better features are possible to get."))
    if budget_of_website < 100:
        print("Little low, you are probably not looking for much")
    elif budget_of_website > 100:
        print("Wow, you are expecting a lot, but we can do that for you!!")
    elif budget_of_website == 100:
        ("That is a very exact price.")

#This is going to print an end statement for all users.

endstatement = "We hope you are happy with our services so far."

def happiness(print_msg):
    print(print_msg)
happiness(endstatement)