# Hangman game
#

# -----------------------------------
# import a wordlist and strip to return word only

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

#make a random choice from the wordlist for the game
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

secretWord = random.choice(wordlist)
lettersGuessed = []

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
print(isWordGuessed(secretWord, lettersGuessed))   



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordGuessed = ''
    for letter in secretWord:
            if letter not in lettersGuessed:
                wordGuessed += ' _'
            else:
                wordGuessed+=str(letter)
    return wordGuessed

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lettersnotguessed = ""
    for letter in (string.ascii_lowercase):
        if letter not in lettersGuessed:
            lettersnotguessed+=letter
    return lettersnotguessed
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
 
secretWord = random.choice(wordlist)
lettersGuessed = []
numberGuesses = 8
import string

print('Welcome to hangman!')
print('I am thinking of a word that is ' + str(len(secretWord)) +' letters long.')

print('Each incorrect guess counts against you! But correct guesses are not included. Duplicate guesses will not be counted')


while isWordGuessed(secretWord, lettersGuessed) == False and numberGuesses > 0:
    print('You have '+ str(numberGuesses) + ' guesses left')
    print('Available letters: ' + (getAvailableLetters(lettersGuessed)))
    x = input("Please guess a letter:")
    if len(x)>1:
        print('Please enter only one letter at a time.')
    elif x not in (string.ascii_lowercase):
        print('That input is not allowed. Choose a letter from a-z.')
    elif x =='':
        print('You did not enter a letter.')
    elif x in lettersGuessed:
        print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))
    elif x in secretWord:
        lettersGuessed.append(x)
        print("Good guess: "+ getGuessedWord(secretWord, lettersGuessed))
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            print('Congratulations, you won!')
    elif x not in secretWord or lettersGuessed:
        print("Oops! That letter is not in my word: "+ getGuessedWord(secretWord, lettersGuessed))
        lettersGuessed.append(x)
        numberGuesses -=1
        if numberGuesses <1:
            print('Sorry, you ran out of guesses. The word was '+secretWord)
    else:
        print('Sorry, you ran out of guesses. The word was '+secretWord)



