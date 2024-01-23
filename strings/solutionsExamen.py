def greet(name):
    return f"Hello, {name}!"


# print(greet("Wiebe"))


def interactive_greet():
    name = input("WHat is you name? ")
    print(greet(name))


def tip_calculator():
    total_price = int(input("Enter total price: "))
    tip_percentage = input("Enter tip percentage(default=20): ")
    if tip_percentage == "":
        tip_percentage = 20
    else:
        tip_percentage = int(tip_percentage)
    total_price = round(total_price * (tip_percentage / 100 + 1))
    print(total_price)


def box(string):
    top = "+" + "-" * (len(string) + 2) + "+"
    middle = "| " + string + " |"
    print(f"{top}\n{middle}\n{top}")


def last_character(string):
    if string == "":
        print(None)
    else:
        print(string[-1])


# def last_character(string): versie van school, doet niks omdat het return is en niet print... pfff fuck heel deze manier van cursussen ze
#     if len(string) != 0:
#         return string[len(string) - 1]
#     else:
#
#          return None


def is_digit(char):
    return char in "0123456789"


def is_student_id(string): #Werkt even goed al die domme oplossing
    first_char = string[0].lower()
    if len(string) != 9:
        print(False)
    elif first_char not in "rs":
        print(False)
    elif not is_digit(string[1:]):
        print(False)
    else:
        print(True)


is_student_id("us123456")
