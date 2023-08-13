# Hangman Game
This is a simple Hangman game implemented in Python. The game randomly selects a word from a predefined list of words and allows the player to guess letters in order to reveal the hidden word. The player has a limited number of attempts to guess the correct letters and complete the word.

## Prerequisites
Before you run the game, make sure you have Python installed on your machine. You will also need the following files:

1. wordstochoose.py: This file should contain a list of words that the game will choose from.
2. hangman_art.py: This file should contain ASCII art for the game's logo and stages of the hanging man.
   
## How to Run
1. Clone this repository to your local machine.
2. Ensure that the wordstochoose.py and hangman_art.py files are in the same directory as the main script.
3. Open a terminal and navigate to the directory where the game files are located.
4. Run the game by executing the following command:
```bash
python main_programme.py
```

## How to Play
1. The game will start by displaying the Hangman logo and initializing the game board.
2. You will be prompted to guess a letter. Enter a letter and press Enter.
3. If the guessed letter is part of the word, the corresponding blank spaces will be replaced with the letter.
4. If the guessed letter is not part of the word, a portion of the Hangman figure will be displayed, indicating a wrong guess.
5. Continue guessing letters until you either complete the word or the Hangman figure is fully displayed.
6. If you complete the word, you win the game. If the Hangman figure is fully displayed, you lose.

## Customization
You can customize the game by modifying the following files:

1. wordstochoose.py: Add or remove words from the list to change the pool of words the game can select from.
2. hangman_art.py: Adjust the ASCII art for the game's logo and stages to your preference.

## Acknowledgements
1. The ASCII art for the Hangman logo and stages is provided by the hangman_art module.
2. The list of words to choose from is provided by the wordstochoose module.
   
Enjoy playing the Hangman game! Have fun and challenge yourself to guess the words correctly.

<img width="342" alt="image" src="https://github.com/scienmanas/Hang-Man/assets/99756067/5aa2f154-753b-473f-bbe9-e9734b2357b3">
