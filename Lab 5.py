import random
NUM_DICE_TO_ROLL = 5
SEED = 2183
list = []
num = 0
rolls = SEED
count = 1
def roll_dice(NUM_DICE_TO_ROLL):
    '''This function rolls 5 dice and returns the results random in a list'''
    global rolls
    for num in range(NUM_DICE_TO_ROLL):
        rolls = random.randint(1,6)
        list.append(rolls)
    print(list)
    return list
def most_repeats(SEED):
    global count
    for reps in range(NUM_DICE_TO_ROLL):
        if list == list.count(rolls):
            count = count + 1
    print(count)
most_repeats(SEED)
def main():
    random.seed(SEED)
    while True:
        answer = input(f"Do you want to roll again (Y/N)? ")
        print(f"Your roll of {roll_dice(NUM_DICE_TO_ROLL)} contains {count} of a kind.")
        if answer == 'N':
            break
if __name__ == "__main__":
    main()
