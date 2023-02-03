# ===================================================================
# author: micha sykora
# date: 1.2.2023
# trademark: ®
# ===================================================================

"""
Přečti větu zadanou z klávesnice a spočti počet slov.

Prográmek se uživatele zeptá na nějakou větu, může obsahovat čárky,
tečky, různé věci. Zpočátku tyhle znaky neřeš, prostě uživatel
zadá třeba "toto je veta a kdo je vic" -- prográmek vrátí, že to má
7 slov.

Postupně pak budeme přidávat další funkcionality
"""


def word_counter():
    """
    Calculate count of words based on count of white spaces
    => count of white spaces = count of words
    """

    # ask the user for a sentence
    the_sentence = input('Vazene uzivatelstvo, zadejte retezec znaku,'
                         've kterem si prejete spocitat obsah slov: ')

    # declare counter to keep track of word counts
    the_counter = 1

    # handle the no input situation
    if the_sentence == '':
        the_counter = 0

    # cycle through given sentence and look for whitespaces
    for character in the_sentence:

        # if whitespace is found, a word is found
        if character == ' ':
            # raise word counter by 1
            the_counter += 1

    # as user would like to know the answer, let's provide it
    return the_counter


# RUNTIME
print(word_counter())

""" 
RK COMMENT

Stejně jako u add_two_numbers, když to ukončím během zadávání, vyhodí to:

  File "<frozen codecs>", line 319, in decode
KeyboardInterrupt

Process finished with exit code -1073741510 (0xC000013A: interrupted by Ctrl+C)

Dál, pro vstup: rudolf klusal    je nejlepší

to vypíše, že 7. Ale přitom jen 4 :-)
"""