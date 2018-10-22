class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Resturant name is : ', self.rest_name.title())
        print('Cuusin type is : ', self.cuisine_type.title())

    def open_restaurant(self):
        print('Restarunt is open now')


rest = Restaurant('olimpia', 'pizzas')
rest1 = Restaurant('italiano', 'italian food')
rest2 = Restaurant('medved', 'russian dishes')

rest.describe_restaurant()
rest1.describe_restaurant()
rest2.describe_restaurant()
