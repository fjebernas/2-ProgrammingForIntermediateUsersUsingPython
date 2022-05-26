
class ClubMembers:
    def __init__(self,name,birthday,age,food,goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.food = food
        self.goal = goal

    def DisplayMemberDetails(self):
        print("Name: " + self.name)
        print("Birthday: " + self.birthday)
        print("Age: " + str(self.age))
        print("Favorite food: " + self.food)
        print("Goal: " + self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, food, goal, position):
        super().__init__(name, birthday, age, food, goal)
        self.position = position

    def DisplayOfficerDetails(self):
        super().DisplayMemberDetails()
        print("Position: " + self.position)

m_1 = ClubMembers("Tom","January 16",14,"Ice cream","To be happy")
o_4 = ClubOfficers("Vera","June 22",16,"Beef stroganoff","To be the world's greatest chef","Treasurer")

m_1.DisplayMemberDetails()
o_4.DisplayOfficerDetails()
