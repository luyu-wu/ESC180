def drink_coffee():
    global last_coffee_time
    global last_coffee_time2
    global too_much_coffee
    # print("Drink drink")
    if last_coffee_time2 < 120:
        too_much_coffee = True
        # print("TOO MUCH")
    last_coffee_time2, last_coffee_time = last_coffee_time, 0

def study(minutes):
    global knols
    global last_coffee_time
    global last_coffee_time2
    global current_time
    global too_much_coffee
    if too_much_coffee:
        # print("DRANK TOO MUCH COFEE")
        return
    elif last_coffee_time == 0:
        # print("Had coffee right before")
        knols += 10*minutes
    else:
        # print("Normal")
        knols += 5*minutes
    current_time += minutes
    last_coffee_time += minutes
    last_coffee_time2 += minutes


def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = 1000
    last_coffee_time2 = 1000


if __name__ == "__main__":
    initialize() # start the simulation
    study(60) # knols = 300
    print(knols)
    study(20) # knols = 400
    print(knols)
    drink_coffee() # knols = 400
    study(10) # knols = 500
    print(knols)
    drink_coffee() # knols = 500
    study(10) # knols = 600
    print(knols)
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600
    print(knols)
