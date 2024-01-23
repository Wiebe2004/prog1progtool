from math import floor, ceil

def five():
    return 5
def triple(x):
    return 3*x
def average(x,y):
    return (x+y)/2
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2-y1) **2) ** 0.5
def buses_needed(people_count, bus_capacity):
    amount = ceil(people_count/bus_capacity)
    return amount
def pizza(n_people, slices_per_pizza):
    amount = ceil(n_people/slices_per_pizza)
    return amount
def cake(eggs):
    return eggs // 5
def candy_per_child(candy_count, child_count):
    return candy_count//child_count
def cake2(eggs, flour):
    return min(eggs // 5, flour // 250)
def cake3(eggs, flour, butter, sugar):
    return min(eggs//5,flour//250,butter//200,sugar//250)
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    return min(eggs//eggs_per_cake, flour//flour_per_cake, butter//butter_per_cake, sugar//sugar_per_cake)
def hours(duration):
    return duration//3600
def minutes(duration):
    h = hours(duration)
    duration -= (3600 * h)
    return duration//60
def seconds(duration):
    h = hours(duration)
    duration -= (3600 * h)
    m = minutes(duration)
    duration -=(m * 60)
    return duration
def coins(amount):
    five_coin = amount // 5
    amount -= five_coin * 5

    two_coin = amount // 2
    amount -= two_coin * 2

    one_coin = amount
    total_coins = five_coin + two_coin + one_coin

    return total_coins

def leftover_candy(candy_count, child_count):
    return candy_count%child_count

def internet_costs(duration_in_seconds, cost_per_block):
    oneblock = duration_in_seconds // 360
    rest_block = duration_in_seconds % 360
    if rest_block > 0:
        return (oneblock + 1) * cost_per_block
    else:
        return oneblock * cost_per_block
def middle(a, b, c):
    return sorted([a, b, c])[1]
def last_digit(n):
    return n % 10
def drop_last_digit(n):
    return n // 10
def next_player(player, player_count):
    if player + 1 < player_count:
        return player + 1
    else:
        return 0
def next_player2(player, player_count):
    if player + 1 <= player_count:
        return player + 1
    else:
        return 1
