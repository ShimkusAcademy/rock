# Import the random module to make magical choices
import random

# Function to get the wizard's choice
def get_wizard_choice():
    while True:
        # Ask the wizard to cast a spell (choose a magical item).
        wizard_choice = input("Choose your magical item (Wand, Spellbook, or Potion): ").strip().lower()

        # Check if the choice is one of the magical items.
        if wizard_choice in ["wand", "spellbook", "potion"]:
            # If it's a magical item, return the choice.
            return wizard_choice
        else:
            # If it's not a magical item, ask the wizard to try again.
            print("Invalid choice. Try again!")

# Function to get the enchanted object's choice
def get_enchanted_object_choice():
    # Create a list of enchanted objects (Wand, Spellbook, and Potion).
    # The enchanted object will make a random choice.
    enchanted_objects = ["wand", "spellbook", "potion"]
    return random.choice(enchanted_objects)

# Function to determine the winner of the magical duel
def determine_winner(wizard_choice, enchanted_object_choice):
    # Check if the wizard's choice and the enchanted object's choice are the same.
    if wizard_choice == enchanted_object_choice:
        # If they are the same, it's a tie in the magical duel!
        return "It's a tie in the magical duel!"
    # Check if the wizard wins with their choice (Wand beats Spellbook, Spellbook beats Potion, Potion beats Wand).
    elif (
        (wizard_choice == "wand" and enchanted_object_choice == "spellbook")
        or (wizard_choice == "spellbook" and enchanted_object_choice == "potion")
        or (wizard_choice == "potion" and enchanted_object_choice == "wand")
    ):
        # If the wizard wins, they are the victor of the magical duel!
        return "You are the victor of the magical duel!"
    else:
        # If the wizard didn't win, the enchanted object prevails.
        return "The enchanted object prevails in the magical duel!"

# The main magical duel
def main():
    # Welcome the wizard to the magical duel.
    print("Welcome to the Wizarding World Duel!")

    while True:  # This loop keeps the magical duel going until the wizard decides to end it.
        # Get the wizard's choice of magical item using the get_wizard_choice function.
        wizard_choice = get_wizard_choice()
        # Get the enchanted object's choice using the get_enchanted_object_choice function.
        enchanted_object_choice = get_enchanted_object_choice()

        # Reveal what the wizard chose and what the enchanted object selected.
        print(f"You chose your {wizard_choice}.")
        print(f"The enchanted object chose a {enchanted_object_choice}.")

        # Determine and announce the outcome of the magical duel using the determine_winner function.
        result = determine_winner(wizard_choice, enchanted_object_choice)
        print(result)

        # Ask if the wizard wants to engage in another magical duel.
        duel_again = input("Do you want to duel again? (yes/no): ").strip().lower()
        if duel_again != "yes":
            # If the wizard decides not to duel again, conclude the magical duel.
            break

    # Thank the wizard for participating in the magical duel.
    print("Thank you for participating in the Wizarding World Duel!")

# Start the magical duel using the main function!
main()
