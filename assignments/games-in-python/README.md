
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective
Build a console-based Hangman game in Python that teaches string manipulation, looping, conditionals, and handling user input. Students will implement the game loop, track guessed letters, and enforce a limited number of incorrect guesses.

## 📝 Tasks

### 🛠️ Implement the Basic Hangman Game
#### Description
Create a fully playable, console-based Hangman game using Python. Use the provided `starter-code.py` as a starting point and implement the game logic so a player can guess letters until they either win or run out of attempts.

#### Requirements
Completed program should:
- Randomly select a word from a predefined list (see `starter-code.py`).
- Accept single-letter guesses and display the current progress in `_ _ _ _` format for unguessed letters.
- Track and display the number of incorrect guesses remaining.
- End the game when the word is fully guessed or when the player exhausts all attempts.
- Display a clear win or lose message along with the correct word.

### 🛠️ Optional Enhancements (Stretch Goals)
#### Description
Add improvements to the game experience. These are optional but recommended for students who want an extra challenge.

#### Requirements
Completed program may include any of the following:
- Show a list of already-guessed letters and ignore duplicate guesses (don’t penalize repeated guesses).
- Allow guessing the whole word in a single attempt.
- Add ASCII-art hangman stages that update with incorrect guesses.
- Introduce difficulty levels (e.g., easy/medium/hard) that control the word pool or number of allowed incorrect guesses.
- Read word lists from a file or categorize words into themes (animals, programming terms, etc.).

---

### Example gameplay
```
Welcome to Hangman!
_ _ _ _ _ _
Guesses remaining: 6
Guessed letters: 
Enter a letter: a
Current word: _ a _ _ _ _
Guesses remaining: 6
Guessed letters: a
```

Use `starter-code.py` in this folder for a basic scaffold and start adding logic into the TODO sections.

