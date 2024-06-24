# Wordle Game

This project simulates Wordle by NYT. The game selects a secret word from a predefined list and provides hints via colors (green for correct letter and position, yellow for correct letter and wrong position, and gray for wrong letter) based on the player's guesses.

## How to Play

1. The program selects a secret word from a predefined list of words.
2. The player has up to 6 attempts to guess the secret word.
3. After each guess, the game provides a hint:
   - "green" indicates that a letter is correct and in the correct position.
   - "yellow" indicates that a letter is correct but in the wrong position.
   - "grey" indicates that a letter is not contained in the secret word.
4. The player wins if they guess the secret word within 6 attempts.

## Classes and Methods

### Wordle
Represents the Wordle game with the following attributes and methods:
- `__init__()`: Initializes the game with a random secret word from a predefined list and sets the initial hint and win status.
- `makeHint(guess)`: Populates the hint list with "grey", "yellow", or "green" based on the Wordle rules and the player's guess.
- `checkWin(guess)`: Sets the win status to True if the guess matches the secret word.
- `getSecret()`: Returns the secret word.
- `getHint()`: Returns the current hint.
- `getWin()`: Returns the current win status.

## How to Use

1. **Initialize the Game**:
    ```python
    wordle = Wordle()
    ```

2. **Start the Game Loop**:
    ```python
    numGuesses = 0
    print("Welcome to Wordle!")
    while(wordle.getWin() == False and numGuesses < 6):
        guess = input("Please enter a guess: ")
        numGuesses += 1
        wordle.checkWin(guess)
        if wordle.getWin() == True:
            print("Congrats, you won!")
        else:
            print("You didn't win yet, guesses remaining = " + str(6 - numGuesses))
            wordle.makeHint(guess)
            print("Hint = " + str(wordle.getHint()))
    if wordle.getWin() == False:
        print("Sorry, you lost. The secret word was: " + wordle.getSecret())
    ```
