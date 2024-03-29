def double_items(ns):
    for i in range(len(ns)):
        ns[i] *= 2


def pad_right(xs, length, padding):
    while len(xs) < length:
        xs.append(padding)


def remove_all(xs, item_to_remove):
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] == item_to_remove:
            del xs[i]

def to_roman(n):
    table = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    result = ""
    for value, representation in table:
        while value <= n:
            n -= value
            result += representation
    return result

def from_roman(string):
    table = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    result = 0
    for value, representation in table:
        while string.startswith(representation):
            result += value
            string = string[len(representation):]
    return result

def remove_runs(ns):
    result = []
    for n in ns:
        if not result or result[-1] != n: #if not result or result[-1] != n:: Controleert of de lijst result leeg is of het laatste element in result anders is dan het huidige element n. Als dit waar is, voegt het de huidige waarde n toe aan de lijst result.
            result.append(n)
    return result

def compact(xs):
    result = []
    for x in xs:
        if x is not None:
            result.append(x)
    return result


def compact_in_place(xs):
    for i in range(len(xs) - 1, -1, -1): #Moet achterwaards omdat als je vanvoor naar achter gaat de indexes veranderen van nummer en het niet meer klopt.
        if xs[i] is None:
            del xs[i]

def matching_brackets(string):
    stack = []

    for char in string:
        if char in '([{':
            stack.append(char)
        else:
            if char == ')':
                expected_bracket = '('
            elif char == '}':
                expected_bracket = '{'
            else:
                expected_bracket = '['

            if len(stack) == 0 or stack[-1] != expected_bracket:
                return False

            stack.pop()

    return len(stack) == 0


def make_teams(participants, team_size):
    team_count = max(1, len(participants) // team_size)
    teams = []
    for _ in range(team_count):
        teams.append([])
    for i in range(len(participants)):
        teams[i % team_count].append(participants[i])
    return teams

def ranking_table(ranking):
    ranks = [str(rank) for rank in range(1, len(ranking) + 1)]
    names = [str(row[0]) for row in ranking]
    times = [row[1] for row in ranking]
    longest_rank_length = max([len(rank) for rank in ranks])
    longest_name_length = max([len(name) for name in names])
    lines = [f'{rank.rjust(longest_rank_length)} {name.ljust(longest_name_length)} {time:.2f}' for rank, name, time in zip(ranks, names, times)]
    return "\n".join(lines)

def concatenate(xs, ys):
    if xs is ys:
        ys = ys[:]
    for i in ys:
        xs.append(i)
    return xs

