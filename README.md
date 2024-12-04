# Calculator

## Description:
This is a text-based implementation of the classic Blackjack game in Python. The game follows standard Blackjack rules, 
allowing players to hit or stand, and includes dynamic handling of Aces, dealer logic, and win conditions. Players 
can choose to replay the game after each round.

## How to Play:
1. The goal of Blackjack is to beat the dealer by getting as close to 21 as possible without going over.
2. You and the dealer will be dealt cards from a deck with the following rules:
   - The deck is unlimited in size and contains no jokers.
   - The cards Jack, Queen, and King each count as 10 points.
   - The Ace can count as either 1 or 11, depending on what is more beneficial for your hand.
3. You will start with a certain number of chips and can place a bet at the beginning of each round.
4. You may choose to:
   - Hit: Draw another card to increase your score.
   - Stand: Keep your current score and end your turn.
5. The dealer will play after you. The dealer must draw cards until their score is 17 or higher.
6. If your total exceeds 21, you go "bust" and lose your bet.
7. The cards have an equal probability of being drawn, and they are not removed from the deck after being dealt.

-House Rules:
- If the dealer gets Blackjack (an Ace + a 10-value card), they win automatically, even if you also have a Blackjack.
- If you get Blackjack and the dealer doesn’t, you win immediately.
- If both you and the dealer get Blackjack, it’s a tie.

Good luck, and may the cards be in your favor! 🃏

## Level
- **Level**: Intermediate
- **Skills:** Python programming, functions, conditional statements, loops, random module, game logic, user input handling
- **Domain:** Gaming

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 2024-12-04

## Features
- Text-based gameplay with player and dealer logic.
- Automatic Ace value adjustment (1 or 11) based on current score.
- Comprehensive win/bust checks for player and dealer.
- Continuous gameplay with replay functionality.
- Simplified, intuitive user interaction for hitting and standing.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/blackjack-game-intermediate.git

2. Navigate to the project directory:
   ```bash
   cd blackjack-game-intermediate

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

