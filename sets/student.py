def contains_duplicates(xs):
    return len(xs) != len(set(xs)) #sets zien duplicates als 1 element.

def remove_duplicates(xs):
    found = set()
    result = []
    for x in xs:
        if x not in found:
            result.append(x)
            found.add(x)
    return result

def spellcheck(document, valid_words):
    result = set()
    for word in len(document):
        if word not in valid_words:
            result.add(word)
    return result


def spellcheck(document, valid_words):
    valid_words = set(valid_words)
    words = {word.lower() for line in document.splitlines() for word in line.split(' ')}
    return words - valid_words

def find_duplicates(xs):
    found = set()
    listed = set()
    result = []

    for x in xs:
        if x in found and x not in listed:
            listed.add(x)
            result.append(x)
        found.add(x)

    return result

def plagiarism(s1, s2):
    lines1 = set(s1.splitlines())
    lines2 = set(s2.splitlines())
    return len(lines1 & lines2)
