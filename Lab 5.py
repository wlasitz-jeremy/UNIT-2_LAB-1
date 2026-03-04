import random

NUM_DICE_TO_ROLL = 5
SEED = 2183

def roll_dice(NUM_DICE_TO_ROLL):
    """Rolls die and returns the results in a list."""
    return [random.randint(1, 6) for _ in range(NUM_DICE_TO_ROLL)]

def most_repeats(dice):
    """This function returns the highest count of any repeated value."""
    max_count = 0
    for value in set(dice):
        count = dice.count(value)
        if count > max_count:
            max_count = count
    return max_count

def main():
    random.seed(SEED)

    while True:
        dice = roll_dice(NUM_DICE_TO_ROLL)
        repeats = most_repeats(dice)
        print(f"Your roll of {dice} contains {repeats} of a kind.")
        answer = input("Do you want to roll again (Y/N)? ").strip().upper()
        if answer == 'N':
            break

if __name__ == "__main__":
    main()
