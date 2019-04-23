def finish_game(score):
    tickets = 10 * socre
    if score >= 10:
        tickets += 50
    elif score >= 7:
        tickets += 20
    return tickets


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return print(cost)

rental_car_cost(2)
#80
rental_car_cost(3)
#100


def trip_cost(city,days):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)
