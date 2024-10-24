import random

# Constants
MAX_LINES = 3  # Maximum number of lines the player can bet on
MIN_BET = 1    # Minimum bet per line
MAX_BET = 100  # Maximum bet per line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Dictionary to define the count of each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictionary to assign values to symbols for calculating winnings
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function to check for winnings based on the slot spin result
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    # Iterate through each line the player bet on
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol from the first column for comparison
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # Stop if symbols in the line don't match
        else:
            # If all symbols in the line match, calculate winnings
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)  # Add the winning line (1-indexed)

    return winnings, winnings_lines

# Function to simulate the slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Create a list of all symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    # Create random columns by selecting symbols
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

# Function to display the slot machine's columns
def print_slot_machine(columns):
    # Iterate through each row to display symbols in a formatted way
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print symbol with separator
            else:
                print(column[row], end="")  # No separator for the last symbol
        print()  # Newline after each row

# Function to handle user deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

# Function to get the number of lines the user wants to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")
    return lines

# Function to get the bet amount per line from the user
def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount

# Function to execute a spin, calculate winnings, and update balance
def spin(balance):
    lines = get_number_of_lines()  # Get the number of lines the player wants to bet on

    while True:
        bet = get_bet()  # Get the bet amount per line
        total_bet = bet * lines  # Calculate the total bet
        if total_bet > balance:
            print(f"You don't have enough balance to bet. Current balance: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} line(s). Total bet is ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Generate the slot machine spin
    print_slot_machine(slots)  # Display the result
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Check for winnings
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet  # Update the balance with winnings

# Main function to run the game loop
def main():
    balance = deposit()  # Get the user's initial deposit
    while True:
        print(f'Current balance is ${balance}.')
        user_input = input("Press Enter to play (q to quit). ")
        if user_input == 'q':
            break
        balance += spin(balance)  # Update the balance after each spin
    print(f"You left with ${balance}.")

# Run the game
main()
