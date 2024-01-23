def ingredients():
    ingredients = {
        "chocolate": "250g",
        "eggs": "5",
        "sugar": "125g",
        "flour": "75g",
        "butter": "175g",
    }
    return ingredients


def desktop(catalog, components):
    price = 0
    for component in components:
        price += catalog[component]
    return price


def rankings(participants):
    ranking = {}
    arrival = 0
    for person in participants:
        arrival += 1
        ranking[person] = arrival
    return ranking


def sell(stock, model):
    stock[model] -= 1  # Verwijder een enkeling van het model uit de stock
    if (
        stock[model] == 0
    ):  # Heb je door het verwijderen van er enkel model er nog maar 1 over haal dan de naam uit de opslag.
        del stock[model]
    return stock


def orbit_chain(orbits, start):
    current = start
    result = [start]
    while current in orbits:
        current = orbits[current]
        result.append(current)
    return result


def combine(d1, d2):
    result = {}
    for key, value in d1.items():
        if value in d2:
            result[key] = d2[value]
    return result


def counts(xs):
    result = {}
    for item in xs:
        result[item] = result.get(item, 0) + 1
    return result


def election_winner(votes):
    vote_counts = {}
    winner = None
    winner_vote_count = 0
    for vote in votes:
        updated_count = vote_counts.get(vote, 0) + 1
        vote_counts[vote] = updated_count
        if updated_count > winner_vote_count:
            winner = vote
            winner_vote_count = updated_count
    return winner


def group_by_first_letter(strings):
    result = {}
    for string in strings:
        key = string[0].upper()
        result.setdefault(key, []).append(string)
    return result


def inverse_lookup(dictionary, value):
    result = []
    for item in dictionary:
        if dictionary[item] == value:
            result.append(item)
    return result


def cake(stock, recipe_ingredients):
    amounts = []
    for ingredient, amount in recipe_ingredients.items():
        amounts.append(stock.get(ingredient, 0) // amount)
    return min(amounts)


def sell2(stock, model, size):
    if model not in stock:
        return False
    available_sizes = stock[model]
    if size not in available_sizes:
        return False
    available_sizes[size] -= 1
    if available_sizes[size] == 0:
        del available_sizes[size]
    if len(available_sizes) == 0:
        del stock[model]
    return True


def matches_pattern(pattern, string):
    if len(pattern) != len(string):
        return False
    bindings = {}
    for pc, sc in zip(pattern, string):
        if pc in bindings:
            if bindings[pc] != sc:
                return False
        elif sc in bindings.values():
            return False
        else:
            bindings[pc] = sc
    return True
