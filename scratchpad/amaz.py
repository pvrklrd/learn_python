import os
def clear_terminal():
    if os.environ == 'NT':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

nums = {1, 2, 3, 4, 5}

def get_comb_val():
    comb = 1;
    for n in nums:
      comb *= n
    return comb

def get_sum_of_set():
    sum = 0
    for n in nums:
        sum += n
    return sum

print(f'\nThere are {get_comb_val()} possible combination for the given series and the sum of the combinations is : {get_sum_of_set() * get_comb_val()}\n')