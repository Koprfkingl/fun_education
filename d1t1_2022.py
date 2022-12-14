# gracefully handle input from file
# read content of the file, split it by '\n\n'
# provide the input for further processing in function further processing
def handle_data_input(file):
    """
    accept the data file provided by advent of code,
    parse it to list of blocks of strings
    """
    with open(file) as f:
        filecontent = f.read()
        # print(filecontent)
        list_of_integer_blocks = filecontent.split('\n\n')
        # print(list_of_integer_blocks)
        return list_of_integer_blocks


def evaluate_calories(top_n_calories):
    """
    split list of calories to list of list of integers
    order the list of integers
    sum the list of integers
    print top N sums
    """
    input_list_of_calories = handle_data_input(r'C:\Users\sykor\PycharmProjects\fun_education\d1t1_input.txt')

    list_of_lists_of_calories = int(input_list_of_calories.split('\n'))


'''
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
'''
