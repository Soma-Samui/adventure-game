import time
import random

# Define list of enemies
enemies = ["wicked fairie", "pirate", "zombie", "monster"]


# Function to randomly choose an enemy
def get_random_enemy():
    enemy = random.choice(enemies)
    return enemy


enemy = get_random_enemy()

# Define the global variables
visited_cave = "NO"
weapon = "DAGGER"
skip_intro = "NO"


# Function to Print messages with 2 seconds delay
def print_pause(str):
    print(str)
    time.sleep(2)


# Function to display introductory messages
def introduction():
    global skip_intro
    if skip_intro != "YES":
        print_pause("You find yourself standing in an open field, filled with "
                    "grass and yellow wildflowers.")
        print_pause("Rumor has it that a " + enemy + " is somewhere around "
                    "here, and has been terrifying the nearby village.")
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand you hold your trusty (but not very "
                    "effective) dagger.")
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


# Function to play the game when visiting the cave
def peer_into_cave():
    print_pause("You peer cautiously into the cave.")

    global visited_cave
    global weapon

    # In case no prior visit to cave, allow collection of Sword
    if visited_cave == "NO":
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        weapon = "SWORD"
        visited_cave = "YES"
    # In case already visited the cave before
    else:
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")


# Function to play the game when visiting the house
def go_to_house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    print_pause("Would you like to (1) fight or (2) run away?")

    while True:
        choice2 = input()

        # If choice is fight, call the function to fight
        if choice2 == "1":
            fight()
            break

        # If choice is run away
        elif choice2 == "2":
            print_pause("You run back into the field. Luckily, you don't seem"
                        " to have been followed.")
            break

        # Invalid choice
        else:
            print("Sorry, I don't get you. Would you like to (1) fight or"
                  " (2) run away?")


# Function to fight against the enemy
def fight():
    # In case collected the sword from the cave
    if weapon == "SWORD":
        print_pause("As the " + enemy + " moves to attack, you unsheath"
                    " your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you"
                    " brace yourself for the attack.")
        print_pause("But the " + enemy + " takes one look at your shiny new"
                    " toy and runs away!")
        print_pause("You have rid the town of the " + enemy + ". You are "
                    "victorious!")

    # If weapon is Dagger
    elif weapon == "DAGGER":
        print_pause("You feel a bit under-prepared for this, what with only"
                    " having a tiny dagger.")
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the pirate.")
        print_pause("You have been defeated!")


# Function to play the game as per input
def play_game():
    global skip_intro
    choice1 = input()

    # Go to house
    if choice1 == "1":
        go_to_house()

    # Peer into cave
    elif choice1 == "2":
        peer_into_cave()
        # After sword is collected, no need to display entire introduction
        skip_intro = "YES"
        introduction()
        # Continue the game as per input
        play_game()

    # Invalid choice
    else:
        print_pause("Sorry, I don't get you")
        # No need to display entire introduction. Ask for input only.
        skip_intro = "YES"
        introduction()
        # Continue the game as per input
        play_game()


def play_again():

    global visited_cave
    global weapon
    global skip_intro

    print_pause("Would you like to play again?")
    choice3 = input("Y or N ")
    # Play again
    if choice3.upper() == "Y":
        print_pause("Excellent! Restarting the game...")

        # Reset the global variables
        visited_cave = "NO"
        weapon = "DAGGER"
        skip_intro = "NO"

        # Display introduction messages
        introduction()

        # Play the game as per inputs
        play_game()

        # Ask if user wants to play again
        play_again()

    # Exit the game
    elif choice3.upper() == "N":
        print_pause("Thanks for playing! See you next time.")

    # Invalid input
    else:
        print_pause("Sorry, I don't get you")
        play_again()


# Display introduction messages
introduction()

# Play the game as per inputs
play_game()

# Ask if user wants to play again
play_again()
