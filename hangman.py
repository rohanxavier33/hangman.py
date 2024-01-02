from random_word import RandomWords
from os import system, name

state = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
    O   |
        |
        |
       ===""",
    """
    +---+
    O   |
    |   |
        |
       ===""",
    """
   +---+
    O   |
   /|   |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
   /    |
       ===""",
    """
    +---+
    O   |
   /|\  |
   / \  |
       ===""",
]


def cpuOrHuman():
    while True:
        try:
            humanOr = int(
                input(
                    "Type 1 if you want to provide the word. Type 2 if you want to play with a randomized word. "
                )
            )
            if humanOr == 1 or humanOr == 2:
                return humanOr
            else:
                raise ValueError
        except ValueError:
            print("Please type either '1' or '2'")
            True


def getHumanWord():
    while True:
        word = input("Type your word here: ")
        if word.isalpha == True:
            clear()
            False
            return word
        else:
            True


def randomWord():
    words = RandomWords()
    # Return a single random word
    while True:
        words = RandomWords()
        word = words.get_random_word()
        if len(word) < 3 or len(word) > 16:
            True
        else:
            False
            return word


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
    print("Terminal cleared.")


def displayBoard(missedLetters, correctLetters, secretWord):
    print(state[len(missedLetters)])
    print()

    print("Missed letters: ", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1 :]
    for letter in blanks:
        print(letter, end=" ")
    print()


def getGuess(alreadyGuessed):
    while True:
        guess = (input("Guess a letter. ")).lower()
        if len(guess) != 1 or guess.isalpha() == False:
            print("Please input a single letter")
            True
        else:
            False
            return guess


def main():
    while True:
        humanOr = cpuOrHuman()
        if humanOr == 1:
            secretWord = getHumanWord()
            break
        elif humanOr == 2:
            secretWord = randomWord()
            break
        else:
            True
    print("H A N G M A N")
    missedLetters = ""
    correctLetters = ""
    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        # Let the player enter a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won.
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                return 0
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost.
            if len(missedLetters) == len(state) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print(
                    "You have run out of guesses!\nAfter "
                    + str(len(missedLetters))
                    + " missed guesses and "
                    + str(len(correctLetters))
                    + ' correct guesses,the word was "'
                    + secretWord
                    + '"'
                )
                return 0

main()
