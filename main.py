import random


class Dice:
    def __init__(self):
        self.choice()

    @staticmethod
    # this function will allow us to play a random generated game with the computer.
    def random_play():
        while True:
            # will get a value between 1 and 6
            player = random.randint(1, 6)
            computer = random.randint(1, 6)
            print(f"you rolled a {player} and the computer rolled a {computer}")
            if player == computer:
                print("You lucky bustard.")
            else:
                print("i guess you aren't as lucky as you seem.")
            user = input("do you wish to play again: ")
            # the user[0] will get the first character from the user input and convert to lower.
            if user[0].lower() == "n":
                return False

    @staticmethod
    # this function will allow us to play by guessing what the computer will choose.
    def user_play():
        while True:
            # int converts the user input to an integer.
            user = int(input("choose a value between 1 and 6\n"))
            if user > 6:
                print("the value entered is not usable")
            else:
                computer = random.randint(1, 6)
                print(f"the computer rolled a {computer}")
                if user == computer:
                    print("How did you guess that. ")
                else:
                    print("not so lucky it seems")
                choice = input("do you wish to play again ")
                if choice[0].lower() == 'n':
                    return False

    def choice(self):
        print("hello player.This is a dice game.\n How do you wish to play: \n")
        player_choice = input("1) Random Generated \n 2)Guess game\n ")
        if player_choice == "1" or player_choice == "Random Generated":
            self.random_play()
        elif player_choice == "2" or player_choice == "Guess game":
            self.user_play()
        else:
            print("what you have written makes no sense.")


if __name__ == '__main__':
    dice = Dice()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
