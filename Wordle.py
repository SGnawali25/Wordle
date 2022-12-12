import random

def read():
    old = open('words.txt','r')
    old_line = old.readline()
    data_list = old_line.split()
    return data_list

word_list = read()

class Wordle:
    word_bank = word_list

    num_wins = 0
    num_loses = 0

    def __init__(self, num_guesses):
        self.num_guesses = num_guesses
        self.word = random.choice(Wordle.word_bank)
        self.guesses = []

    def __str__(self):
        if len(self.guesses) == 0:
            return ('{} guesses remaining'.format(self.num_guesses))
        final = ''
        word = self.word.upper()

        for guess_ind in range(len(self.guesses)):
            guess = self.guesses[guess_ind].upper()
            for item in range(len(guess)):
                if guess[item] == word[item]:
                    final += guess[item] + '(g) '
                elif guess[item] in word:
                    final += guess[item] + '(y) '
                else:
                    final += guess[item] + '(r) '
            if guess_ind != len(self.guesses) - 1:
                final += '\n'
        return ('{} \n{} guesses remaining'.format(final, self.num_guesses))

    def make_guess(self, guess):
        if len(guess) != 5:
            print('Guess must be exactly 5 letters. Try again')
            return False
        if len(set(guess)) != 5:
            print('Guess must contain unique letters only. Try again')
            return False
        self.num_guesses -= 1
        self.guesses.append(guess)
        word = self.word.upper()
        if guess.upper() == word:
            print('You win!')
            Wordle.num_wins += 1
            return True
        elif self.num_guesses == 0:
            print('You lose!')
            Wordle.num_loses += 1
            return True
        return False



def run_program():
    play_again = 'y'
    while play_again == 'y':
        wordle_game = Wordle(6)
        print(wordle_game)
        game_over = False
        while not game_over:
            guess = input('What is your guess? ')
            game_over = wordle_game.make_guess(guess)
            print(wordle_game)
        print("Wins: {}, Losses: {}".format(Wordle.num_wins, Wordle.num_loses))
        print()
        play_again = input("Play again(y/n)? ")
        print()
    print("All done!")


if __name__ == "__main__":
    run_program()