import random

MAX_REMOVE = 3
TRIALS = 10000


def evaluation_position(self, num_items):
    """
    Monte Carlo evaluation method for Nim
    """
    best_percentage = 0.0
    best_move = 0
    for first_move in range(1, MAX_REMOVE + 1):
        wins = 0
        for i in range(TRIALS):
            total = first_move

            # This boolean win is used to control the turn of which player, computer or the player
            win = True
            # The winner is the one breaks the loop
            # The loop is broken when the total is larger than the number of items.
            # On the other hand, the loop continues while the total is lower than the number of items.
            while total < num_items:
                total += random.randrange(1, MAX_REMOVE) + 1
                # Flip the turn
                win = not win

            # Determine who wins this game
            if win:
                wins += 1
        current_percentage = float(wins) / TRIALS

        # Update the highest winning probability to determine the winning initial move
        if current_percentage > best_percentage:
            best_percentage = current_percentage
            best_move = first_move
    return best_move


def play_game(self, start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    current_items = start_items
    print("Starting game with value", current_items)
    while True:
        comp_move = self.evaluation_position(current_items)
        current_items -= comp_move
        print("Computer choose", comp_move, ", current value is", current_items)
        if current_items <= 0:
            print("Computer wins")
            break
        player_move = int(input("Enter your current move: "))
        current_items -= player_move
        print("Player choose", comp_move, ", current value is", current_items)
        if current_items <= 0:
            print("Computer wins")
            break


play_game(21)
