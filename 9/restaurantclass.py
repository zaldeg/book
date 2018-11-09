class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Resturant name is : ', self.rest_name.title())
        print('Cuusin type is : ', self.cuisine_type.title())

    def open_restaurant(self):
        print('Restarunt is open now')