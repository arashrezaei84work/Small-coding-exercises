import random


class Hangman:
    words = ['apple', 'banana', 'football', 'camel', 'computer']
    player_list = set()

    def __init__(self, player):
        self.player = player
        self.word = random.choice(self.words)
        self.__guesses_left = 3
        self.__result = False
        self.wrong_words = []
        self.player_list.add(self.player)

    def gaps(self):
        return "_ " * len(self.word)

    def check_game(self):
        answer = input(f"{self.player} please Enter your guess {self.gaps()}: ")
        if answer.isalpha():
            if answer == self.word:
                print("Congratulations! That is correct .")
                self.__result = True
            else:
                print("Sorry, that's not the right word\nTry again.")
                self.__minus_guesses()
                print(f"your guesses left = {self.__guesses_left}")
                self.wrong_words.append(answer)
        else:
            print("Sorry, you should write an alphabetical.")

    def __minus_guesses(self):
        self.__guesses_left -= 1
        if self.__guesses_left == 1:
            print(f"This is your last chance the word has start and end of with {self.word[0]}...{self.word[-1]}")

    def guesses_status(self):
        return self.__guesses_left

    def is_game_over(self):
        return self.__result


class Player:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    try:
        name = input("Enter your name: ")
        my_player = Player(name)
        game = Hangman(my_player.name)
        action = input("what do you want to do? ")
        if action == "start":
            while True:
                order = input(f"{game.player} Would you like to play :")
                if order == "yes":
                    game.check_game()
                    if game.is_game_over():
                        print("Thanks for playing!")
                        break
                    if game.guesses_status() <= 0:
                        print("Game Over! You lost.")
                        break
                elif order == "new player":
                    name = input("Enter your name: ")
                    my_player = Player(name)
                    game = Hangman(my_player.name)
                elif order == "no":
                    break
                elif order == "show" or order == "players":
                    print(game.player_list)
                elif order == "add":
                    game.words.append(input("Enter a word: "))
                else:
                    print("Invalid")
                    break

        else:
            print("sth were wrong! ")

    finally:
        print("The program has ended")
