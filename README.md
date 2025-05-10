# AI-ProjectSnake and Ladder Game with Power-Ups

## Overview
This project is a graphical implementation of the classic Snake and Ladder board game, enhanced with power-ups, built using Python and the `'tkinter'` library. It includes features like ladders, snakes, and additional power-ups such as shields, boosts, and traps to make the gameplay more engaging. The game also incorporates **text-to-speech** functionality to provide audio feedback during play.

## Features
- Two-Player Game: Supports two players taking turns to roll a dice and move on a 10x10 grid (100 squares).
- Ladders and Snakes: Climb up ladders to advance faster or slide down snakes to lose progress.
- **Power-Ups**:
  - **Shield**: Protects a player from a snake bite once.
  - **Boost**: Grants an extra dice roll in the same turn.
  - **Trap**: Forces the opponent to skip their next turn.
- Text-to-Speech: Audio feedback for game events using the `'gTTS'` library.
- Graphical Interface: Built with 'tkinter' for the game board, player tokens, and dice visuals.
- Dice Rolling: Random dice rolls with corresponding images displayed on the screen.

## Requirements
To run this project, you'll need the following Python libraries:
- `'tkinter'` (usually included with Python)
- `'PIL'` (Pillow) for image processing
- `'gTTS'` for text-to-speech functionality
- `'playsound'` for playing audio files
- `'random'` (included with Python)
- `'os'` (included with Python)

Install the required libraries using pip:
pip install Pillow gTTS playsound

## File Structure
- `'final.py'`: The main Python script containing the game logic and GUI code.
- `'images/'`: A folder containing the following image assets:
  - 'final_cover.png': The game board background.
  - '1.png' to '6.png': Dice face images.
  - 'roll.png': The dice roll button image.
  - 'shield.png': Shield power-up icon.
  - 'boost.png': Boost power-up icon.
  - 'trap.png': Trap power-up icon.

## How to Run
1. Ensure all required libraries are installed.
2. Place the **'images/'** folder in the same directory as **'final.py'**.
3. Run the script: python final.py
4. The game window will open. Click **"Start Game"** to begin, then take turns rolling the dice by clicking the respective player's button.

## Gameplay Instructions
- The game starts with Player 1.
- Click the "Player - 1" or "Player - 2" button to roll the dice, depending on whose turn it is.
- Move your token based on the dice roll.
- Land on a ladder to climb up, a snake to slide down, or a power-up to gain an advantage:
  - Shield: Protects you from the next snake.
  - Boost: Roll the dice again immediately.
  - Trap: The other player skips their next turn.
- The first player to reach square 100 wins the game.
- Click "Click Here to End Game" to exit.

## Limitations
- The game requires an internet connection for the `'gTTS'` library to generate audio files.
- Audio files ('Text.mp3') are temporarily created and deleted during gameplay, requiring write permissions in the working directory.
- The game is designed for a screen resolution that supports a 1600x1000 window.

## Future Improvements
- Add support for offline text-to-speech.
- Include a settings menu to adjust volume or toggle audio.
- Add more power-ups or customizable game rules.
- Improve the UI with better animations and responsive design.

## Credits
_This project was developed as a fun implementation of the Snake and Ladder game with added features for an enhanced experience._