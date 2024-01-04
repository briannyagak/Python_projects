import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = '|')
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("Enter the amount you wish to Deposit. $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Enter a real number")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you wish to bet. (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a real number")
    return lines

def get_bet():
    while True:
        bet = input(f"What would you line to bet? ${MIN_BET} - ${MAX_BET}. ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a valid bet amount, ${MIN_BET} - ${MAX_BET}. ")
        else:
            print("Enter a real number")
    return bet

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"Your balance is {balance} and you've bet on {lines} lines with a bet amount of ${bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        spin = input("Press enter to spin (q to quit) ")
        if spin == 'q':
            break
        balance += game(balance)

    print(f"You left with ${balance}")


main()