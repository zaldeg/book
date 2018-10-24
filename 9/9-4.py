class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Resturant name is : ', self.rest_name.title())
        print('Cuusin type is : ', self.cuisine_type.title())

    def open_restaurant(self):
        print('Restarunt is open now')

    def set_number_served(self, ppl_served):
        self.number_served = ppl_served

    def increment_number_served(self, increment):
        self.number_served += increment


rest = Restaurant('olimpia', 'pizzas')

print(rest.number_served)
rest.number_served = 1
print(rest.number_served)
rest.set_number_served(100)
print(rest.number_served)
rest.increment_number_served(356)
print(rest.number_served)