# ===================================================================
# author: micha sykora
# date: 1.2.2023
# trademark: ®
# ===================================================================

# because nobody will ever review this code and task is in CZ lang.
# I will comment everything also in CZ; vars remain in ENG lang.

# TASK DESCRIPTION:
"""
Jednoduchý progámek na součet dvou čísel.

Napiš jednoduchý prográmek, který se uživatele zeptá na dvě celá čísla.
Prográmek vypíše součet tutěch čísel.
"""

def superAdder():
    """Ask user for two numbers; add them together"""
    try:
        a = int(input('Drahe uzivatelstvo, zadejte prvni scitanec: '))
        b = int(input('Drahe uzivatelstvo, zadejte druhy scitance: '))
    except ValueError:
        print('''
        Drahe uzivatelstvo, Vase selhani pri pokusu o zadani 
        cisla je do nebe volajici. Prokazte lidstvu laskavost,
        zasebevrazdete se a ostatky poskytnete ke zkoumani, dekuji.''')
        return

    return a + b

print(superAdder())

""" RK COMMENT
Pokud zapnu program a ukončím ho při zadávání (v pycharmu zastavit, ctrl+c v konzoli atd), vyhodí to následující:

Traceback (most recent call last):

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen codecs>", line 319, in decode
KeyboardInterrupt

Process finished with exit code -1073741510 (0xC000013A: interrupted by Ctrl+C)
"""
