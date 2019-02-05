# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Anas"
my_age = 20
my_bio = "Person of a personal personage, known only on a person-to-person basis."
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print("-------------")
    option = input("1) Crete a new club.\nor:\n2) Browse and join a club.\nor:\n3) View existing clubs.\nor:\n4) Display members of a club.\nor\n-1) Close application.\n")
    return option


    

def create_club():
    # your code goes here!
    club_name = input("What is the name of your awesome new club: ")
    club_desc = input("What is your club about?\n")
    club = Club(club_name, club_desc)
    club.members.append(myself)
    club.assign_president(myself)
    m = []
    print("Enter the numbers of people you would like to recruit to your club(-1 to stop): \n")
    n = 1
    for i in population:
    	print("[%d] %s" % (n, i.name))
    	n = n +1
    mem = input()
    memb = int(mem)
    while mem != -1:
    	memb = memb -1
    	club.members.append(population[memb])
    	mem = input("Who else: ")
    	memb = int(mem)
    	if memb == -1:
    		break
    clubs.append(club)
    print("Here's your new club:\n %s\n%s\n" % (club.name, club.description))
    club.print_member_list()

    

def view_clubs():
    # your code goes here!
    
    for club in clubs:
    	m = 0
    	for member in club.members:
    		m = m + 1 
    	print("\tNAME: %s.\n\tDISCRIPTION: %s.\n\tMEMBERS: %d.\n" % (club.name, club.description, int(m)))

    

def view_club_members():
    # your code goes here!
    view_clubs()
    club = input("Enter the name of the club whose members you'd like to view: ")
    for c in clubs:
    	if club == c.name:
    		c.print_member_list()


    

def join_clubs():
    # your code goes here!
    view_clubs()
    club = input("Enter the name of the club you'd like to join: ")
    for c in clubs:
    	if club == c.name:
    		c.recruit_member(myself)
    		print("%s just joing the %s\n------------------" % (my_name, c.name))
    

def application():
    introduction()
    # your code goes here!
    option = 0
    while option != -1:
    	option = int(options())
    	if option == 1:
            create_club()
    	elif option == 2:
            join_clubs()
    	elif option == 3:
            view_clubs()
    	elif option == 4:
	        view_club_members()
    	else:
	    	break
    else:
        exit()

    
