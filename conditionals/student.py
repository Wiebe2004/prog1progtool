from math import ceil


def total_cost(amount):
    if amount < 100:
        return amount + 10
    elif amount >= 200:
        return amount * 0.95
    else:
        return amount


def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 0
    elif (
        (player1_choice == 0 and player2_choice == 2)
        or (player1_choice == 2 and player2_choice == 1)
        or (player1_choice == 1 and player2_choice == 0)
    ):
        return 1
    elif (
        (player1_choice == 1 and player2_choice == 2)
        or (player1_choice == 0 and player2_choice == 1)
        or (player1_choice == 2 and player2_choice == 0)
    ):
        return 2


def player_movement(position, left_arrow, right_arrow, shift):
    if shift:
        step = 2
    else:
        step = 1

    if left_arrow:
        position -= step
    if right_arrow:
        position += step

    return position


def movie_ticket(duration, imax, student, ticket_count):
    if duration <= 90:
        price = 10
    elif duration <= 120:
        price = 11
    elif duration <= 150:
        price = 12
    else:
        price = 15

    if imax:
        price = ceil(price * 1.2)

    if student:
        price -= 3
    return price * ticket_count
""