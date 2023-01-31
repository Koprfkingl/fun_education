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
        list_of_integer_blocks = filecontent.split('\n\n')
        print(list_of_integer_blocks)
        return list_of_integer_blocks


def evaluate_calories(top_n_calories):
    """
    split list of calories to list of list of integers
    order the list of integers
    sum the list of integers
    print top N sums
    """

    # separated blocks of strings, in memory ['5345\n4324\n'...]
    input_list_of_calories = handle_data_input(r'C:\UserData\git_ws\private_fun_education\d1t1_input.txt') 
    
    # declare list for each elf (=block)
    sum_of_elf_calories = []

    # for each single block of calories stored as '3424\n4323'
    for calorie_list in input_list_of_calories:
        # separate numbers
        list_of_separated_calories = calorie_list.split('\n')
        
        # calorie counter
        single_calorie = 0
        
        # for each single calorie saved as string, e.g. '4324'
        for calorie in list_of_separated_calories:
            # in case input is not number, ignore the error
            try:
                # make a sum of calories
                single_calorie = single_calorie + int(calorie)
            except ValueError:
                continue
        
        # as we now have sum of calories for each elf, store the value to a list
        sum_of_elf_calories.append(single_calorie)

    # sort the list descending
    sum_of_elf_calories.sort(reverse=True)
    
    # select first n calories
    user_output = sum(sum_of_elf_calories[0:top_n_calories])
    
    return user_output
    
print(evaluate_calories(3))
