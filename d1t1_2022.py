# gracefully handle input from file
# read content of the file, split it by '\n\n'
# provide the input for further processing in function further processing
vstup = ''
print(vstup)

rozdeleno = vstup.split('\n')
print(rozdeleno)

prubezny_soucet = 0
nejvyssi_soucet = 0

for kalorie in rozdeleno:
    if kalorie == '':
        if prubezny_soucet > nejvyssi_soucet:
            nejvyssi_soucet = prubezny_soucet
        prubezny_soucet = 0
        continue
    kalorie = int(kalorie)
    prubezny_soucet = prubezny_soucet + kalorie

print(nejvyssi_soucet)
