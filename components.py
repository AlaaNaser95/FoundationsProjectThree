# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name=name
        self.bio=bio
        self.age=age
    def __str__(self):
        s= "- "+ self.name+ " ("+str(self.age)+ " years old) - "+self.bio
        return s



class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name=name
        self.description=description
        self.members=[]
        self.numOfMem=0
    def __str__(self):
        return "\tNAME: "+self.name+"\n\t"+"DESCRIPTION: "+self.description+"\n\t"+"MEMBERS: "+str(self.numOfMem)+"\n"
    



    def assign_president(self, person):
        # your code goes here!
        self.president=person
        self.members.append(person)
        self.numOfMem+=1


    def recruit_member(self, person):
        # your code goes here!
        if (person not in self.members):
            self.members.append(person)
            self.numOfMem+=1


    def print_member_list(self):
        # your code goes here!
        print("Members:")
        print("- %s (%d years old, president) - %s"%(self.president.name,self.president.age,self.president.bio))
        for member in self.members:
            if member.name!=self.president.name:
                print(str(member))

            

