# Blackjack Game

A classic Blackjack game built with Python and Pygame, featuring a Matrix-style welcome screen and smooth card animations.

## Features

- Matrix digital rain effect on welcome screen
- Classic Blackjack gameplay
- Clean card display with suit colors
- Betting tracker

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation & Setup

1. **Clone or download this repository**

   ```bash
   git clone https://github.com/Themba619/blackJack
   cd blackJack
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies**
   ```bash
   pip install -r requirments.txt
   ```

## Running the Game

1. **Make sure your virtual environment is activated**

   ```bash
   venv\Scripts\activate
   ```

2. **Run the game**
   ```bash
   python main.py
   ```

## How to Play

1. **Welcome Screen**: Enjoy the Matrix effect and click "Play BlackJack" to start
2. **Betting**: Use UP/DOWN arrow keys to adjust bet amount, then click "BET"
3. **Playing**:
   - Click "HIT" to take another card
   - Click "STAND" to end your turn
   - Try to get as close to 21 without going over
4. **Winning**: Beat the dealer without busting to win chips!

## Game Controls

- **Mouse**: Click buttons to interact
- **Arrow Keys**: Adjust bet amount (UP/DOWN)
- **Close Window**: End the game

## Project Structure

```
blackJack/
├── main.py              # Main game entry point
├── requirments.txt      # Python dependencies
├── model/              # Game data models
│   ├── card.py         # Card class
│   ├── deck.py         # Deck class
│   ├── hand.py         # Hand class
│   ├── player.py       # Player class
│   └── dealer.py       # Dealer class
├── game/               # Game logic
│   └── blackjack_game.py # Main game logic
├── screens/            # UI screens
│   ├── welcome_screen.py # Matrix welcome screen
│   └── game_screen.py    # Main game interface
└── utils/              # Utility effects
    ├── matrix_effect.py  # Matrix digital rain
    └── shuffle_effect.py # Card shuffle animation
```

## Troubleshooting

- **Import errors**: Make sure virtual environment is activated and pygame is installed
- **Window not opening**: Check that you have proper graphics drivers
- **Game crashes**: Ensure Python 3.7+ is being used

## Requirements

- pygame==2.6.1

Enjoy the game!
