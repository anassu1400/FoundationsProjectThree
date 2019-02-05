# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age
        


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.president = ""
        self.members = []


    def assign_president(self, person):
        # your code goes here!
        for member in self.members:
            if member == person:
                self.president = member



    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        print("Members: ")
        age = 0.0
        m = 0.0
        for member in self.members:
            if self.president == member:
                print("- %s (%s years old, %s) - %s." % (member.name, str(member.age), "President", member.bio))
                age = age + int(member.age)
            else:
                print("- %s (%s years old) - %s." % (member.name, str(member.age), member.bio))
                age = age + int(member.age)
            m = m + 1
        average_age = age / m
        print("Average ag in this club: %.2fyr\n---------------" % (average_age))

