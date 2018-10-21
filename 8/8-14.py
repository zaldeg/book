def create_car(car, car_title, **args):
    car_info = dict()
    car_info['mark'] = car
    car_info['manufacturer'] = car_title
    for key, value in args.items():
        car_info[key] = value
    return car_info


new_car = create_car('prius', 'toyota', first_fuel= 'petrol', second_fuel='electricity', max_speed='120km')


print(new_car)