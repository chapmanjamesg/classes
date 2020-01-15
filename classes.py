class Pizza:
    def __init__(self, style, size):
        self.style = style
        self.size = size
        self.toppings = ""


    def add_topping(self, topping):
        self.toppings = topping

    def confirm_pizza(self):
        print(f"Your {self.size} {self.style} pizza will come with {self.toppings} toppings")

#first pizza
meat_lovers = Pizza("deep dish", 16)
meat_lovers.add_topping("pepperoni")
meat_lovers.confirm_pizza()

#second pizza
cheese_lovers = Pizza("thin crust", 18)
cheese_lovers.add_topping("extra cheese")
cheese_lovers.confirm_pizza()