class Pizza: 
    def __init__(self):
        self.size = ""
        self.crust = ""
        self.type = ""
        self.toppings = []
    
    def add_topping(self, topping):
        self.new_topping = topping
        print(self.toppings)

    def 