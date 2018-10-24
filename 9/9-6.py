class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.rest_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Resturant name is : ', self.rest_name.title())
        print('Cuusin type is : ', self.cuisine_type.title())

    def open_restaurant(self):
        print('Restarunt is open now')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['strawberry', 'chocolate', 'vanilla']

    def get_flavours(self):
        print('Flavours is : ', *self.flavours, sep=',')


stand = IceCreamStand('larek', 'ice cream')
stand.get_flavours()
stand.describe_restaurant()