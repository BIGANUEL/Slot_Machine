# Slot Machine Game

This project is a simple command-line slot machine game written in Python. It allows the user to deposit money, place bets on multiple lines, and spin a virtual slot machine.

## How to Play
1. **Deposit Money**: Start by depositing an amount you want to play with.
2. **Place Bets**: Choose how many lines you want to bet on (up to 3 lines) and how much you want to bet on each line.
3. **Spin the Slot Machine**: After placing your bets, the slot machine will spin and randomly select symbols. If you win, the amount will be added to your balance.
4. **Quit or Continue**: You can choose to continue spinning until you run out of money or decide to quit.

## Game Features
- 3x3 slot machine grid
- Adjustable bet amount between $1 and $100
- Bet on 1 to 3 lines
- Randomly generated slot machine symbols with different values:
    - "A": Value of 5 (rare)
    - "B": Value of 4
    - "C": Value of 3
    - "D": Value of 2 (common)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/slot-machine-game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd slot-machine-game
    ```

3. Run the Python script:
    ```bash
    python slot_machine.py
    ```

## Example Output

```plaintext
What would you like to deposit? $100
Enter the number of lines to bet on (1-3): 3
What would you like to bet on each line? $10
You are betting $10 on 3 line(s). Total bet is $30.
A | C | D
B | A | B
D | B | C
You won $0.
You left with $70.
