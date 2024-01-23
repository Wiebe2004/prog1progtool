def total_cost(amount):
    if amount < 100:
        return amount + 10
    if amount >= 200:
        return amount*0.95
    else:
        return amount

def rock_paper_scissors(player1_choice,player2_choice):
    rock = 0
    paper = 1
    scissors = 2
    if player1_choice == rock and player2_choice == paper:
        return 2
    elif player1_choice == paper and player2_choice == rock:
        return 1
      