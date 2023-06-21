# https://www.codewars.com/kata/52761ee4cffbc69732000738

# create function that compares user input

def good_vs_evil(good, evil):
    good = good.split(' ')
    bad = evil.split(' ')

    good = list(map(int, good))
    bad = list(map(int, bad))

    good_dicts = {'hobbits': good[0],
                  'men': 2 * good[1],
                  'elves': 3 * good[2],
                  'dwarves': 3 * good[3],
                  'eagles': 4 * good[4],
                  'wizards': 10 * good[5]}

    bad_dicts = {'orcs': bad[0],
                 'men': 2 * bad[1],
                 'wargs': 2 * bad[2],
                 'goblins': 2 * bad[3],
                 'uruk hai': 3 * bad[4],
                 'trolls': 5 * bad[5],
                 'wizards': 10 * bad[6]}

    worth_good = sum(good_dicts.values())
    worth_bad = sum(bad_dicts.values())

    if worth_good > worth_bad:
        return 'good triumphs'
    elif worth_bad > worth_good:
        return 'bad triumphs'
    else:
        return 'no victor'


print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
