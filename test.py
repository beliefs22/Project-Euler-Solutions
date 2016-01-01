def test(grade):
    if grade > 1.0 or grade < 0:
        return 'sorry grade must be between 0 and 1.0'
    elif grade >= .9:
        return 'A'
    elif grade >= .8:
        return 'B'
    elif grade >= .7:
        return 'C'
    elif grade >= .6:
        return 'D'
    else:
        return 'F'
