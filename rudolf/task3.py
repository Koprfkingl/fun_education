# =============================================================================
# Author: Michal Sykora
# Date: 14.2.2023
# Trademark: ®️ RK: LOL
# =============================================================================

"""
python.klusik.cz
third task definition:
Největší ze všech
Prográmek se bude postupně ptát uživatele na různá celá čísla včetně nuly.
V momentě, co uživatel napíše 'konec', program se přestane ptát na další čísla
a vypíše 3 nejvyšší čísla ze zadaných.

Pokud uživatel zadá žádné, jedno až do tří čísel, tak to buď nevypíše nic (není
co), anebo všechna tři čísla. Pokud zadá víc než 3 čísla, vypíše to pouze
nejvyšší tři čísla.
"""


def greatest():
    # list to store user values
    # RK: Pojďme udělat docstringy a type-hinty :-)
    numbers_storage = []

    # storage of function output
    output_list = []

    # cycle until user writes 'konec'
    while True:
        user_value = input('Kindly asking you to enter a number of your choice: ')

        # no user input -> print 'nic'
        if not user_value:
            return 'nic' # RK: Kombinace angličtiny a 'nic' je funny :-D

        # RK: Když zadávám čísla a omylem zmáčknu 2× enter, napíše to "nic" a skončí.
        # Udělal bych to prostě trošku víc "jůžrfrenly," prostě zadám nic, prostě to řekne něco
        # jako "okey, tuto se nepovedlo," ale jede se dál :-)

        # end of user input
        if user_value == 'konec':
            # user entered less than 3 values -
            if len(numbers_storage) < 3: # RK: Tahle podmínka se mi moc nelíbí, pokud zadám 3 čísla, vrátil bych to taky.
                numbers_storage.sort()
                return numbers_storage
            break

        # being suspicious about user's ill minds check for providing correct
        # input is needed. classical python mentality is to ask for forgiveness
        # rather than permission, therefore if statement testing for int type
        # is not the best solution. try - except statement is recommended instead # RK LOOOL :-D
        try:
            # convert user value to integer
            user_value = int(user_value)
        except ValueError:
            print('Is it possible that you have entered a string instead of integer,'
                  'you sick minded pervert?')
            # as it is not obvious what should function return at this point
            # I am going for break clause, adjustments possible later
            # (after discussion...)

            # RK: Eyup, again like before I'd rather see "okay, no valid number, life goes on" :-)
            break

        # add given user value to list of values
        numbers_storage.append(user_value)

        # sort list of user choices, order not specified -> default used
        numbers_storage.sort() # RK: Znovu třídění, to už máš jinde :-) Neříkám, že je to špatně, ale...

    # slice the list for last three elements
    output_list = numbers_storage[-1:-4:-1] # RK: Clever!
    return output_list


# RUNTIME
# RK: Víš, co ti k tomu tady řeknu -- když to načtu jako modul, automaticky se spustí :-) Řešení znáš :-)
print(greatest())

# RK: Hej, funguje, jdu spát, vstávám v 5 :-D Zítra mrknu víc, čus :-)
