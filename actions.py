# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Alaa"
my_age = 23
my_bio = "Intelligent coder"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    print ("-"*30)

def options():
    # your code goes here!
    options=["Create a new club.", "Browse and join club", "View existing clubs.", "Display members of a club.","Close application."]
    print("Would you like to:")

    for i in range(5):
    	if i+1 ==5:
    		print("-1) %s" % options[i])
    	else:
    		print("%d) %s\nor," % (i+1,options[i]))
    user_choice=int(input(""))
    return user_choice
    

def create_club():
    # your code goes here!
    club_name=str(input("Pick a name for your awesome new club: "))
    club_desc=str(input("What is your club about?\n"))
    new_club=Club(club_name,club_desc)
    new_club.assign_president(myself)
    clubs.append(new_club)
    print("Enter the numbers of the people you would like to recruite to your new club (-1 to stop):")
    print("-"*50)
    for i in range(len(population)):
    	print("[%d] %s" %(i+1, population[i]))
    club_members=[]
    while True:
    	
    	club_member=int(input())
    	if club_member==-1 :
    		break
    	elif club_member<1 or club_member>len(population):
    		print("Wrong number!!")
    	elif club_member in club_members:
    		print("This member already exist in the club")
    	else:
    		club_members.append(club_member)
    		club_member=population[club_member-1]
    		new_club.recruit_member(club_member)
    print("Here is your club:")
    print(new_club.name+"\n"+new_club.description)
    new_club.print_member_list()
    average_age(new_club)


def average_age(club):
	sum=0
	for member in club.members:
		sum+=member.age
	aver=sum/float(club.numOfMem)
	print("average age in this club %.1fyr"% (aver))


def get_club(club_name):
	for club in clubs:
		if club.name==club_name:
			return club



    

def view_clubs():
    # your code goes here!
    for club in clubs:
    	print(str(club))
    	print()
    

def view_club_members():
    # your code goes here!
    view_clubs()
    member_choice=str(input("Enter the name of the club whoes members you'ld like to see: "))
    member_choice=get_club(member_choice)
    member_choice.print_member_list()
    average_age(member_choice)


    

def join_clubs():
    # your code goes here!
    view_clubs()
    club_choice=str(input("Enter the name of the club you would like to join: "))
    for club in clubs:
    	if club.name==club_choice:
    		club.recruit_member(myself)
    		print("%s just joined %s"%(myself.name,club.name))


    

def application():
    introduction()
    # your code goes here!
    while True:
    	user_choice= options()
    	if user_choice==-1:
    		break
    	elif user_choice==1:
    		create_club()
    	elif user_choice==2:
    		join_clubs()
    	elif user_choice==3:
    		view_clubs()
    	else:
    		view_club_members()
    	print("-"*50)
    
    
