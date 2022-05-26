class Customer:
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total
    
    greeting = "Welcome to Coffee Place!"

c_1 = Customer("Nate","Espresso", "Pastrami on rye", 220)
c_2 = Customer("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customer("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Customer("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customer("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Customer.greeting)
print(c_2.name + " " + c_2.beverage + " " +  c_2.food + " " +  str(c_2.total))
print(c_4.name + " " + c_4.beverage + " " + c_4.food + " " + str(c_4.total))