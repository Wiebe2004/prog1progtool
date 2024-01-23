def multiple_choice(right_answer, given_answer):
    if right_answer == given_answer:
        return 1
    elif given_answer is None:
        return 0
    else:
        return -0.2


def product(a, b, c):
    if a is None:
        a = 1
    if b is None:
        b = 1
    if c is None:
        c = 1
    return a * b * c

def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    taken = 0
    skipped = 0
    grade = 0
    if grade1 is None:
        skipped += 1
    else:
        taken += 1
        grade += grade1
    if grade2 is None:
        skipped += 1
    else:
        taken += 1
        grade += grade2
    if grade3 is None:
        skipped += 1
    else:
        taken += 1
        grade += grade3
    if grade4 is None:
        skipped += 1
    else:
        taken += 1
        grade += grade4
    if grade5 is None:
        skipped += 1
    else:
        taken += 1
        grade += grade5
    if skipped > 1:
        return False
    if grade / taken < 12:
        return False
    else:
        return True
