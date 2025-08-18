import random
import numpy as np

def monty_hall_simulation(num_doors=3, num_trials=100000):
    """
    Simulates the Monty Hall problem to compare probabilities of winning by switching or staying.
    
    Args:
        num_doors (int): Number of doors in the game (default: 3).
        num_trials (int): Number of simulations to run (default: 100,000).
    
    Returns:
        tuple: (switch_win_probability, stay_win_probability)
    """
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # Initialize doors (0 to num_doors-1)
        all_doors = list(range(num_doors))
        # Randomly place the car behind one door
        car = random.choice(all_doors)
        # Player randomly picks a door
        player_choice = random.choice(all_doors)
        # Host reveals num_doors-2 doors that don't have the car and aren't player's choice
        host_options = [door for door in all_doors if door != car and door != player_choice]
        doors_revealed = random.sample(host_options, num_doors - 2)
        # Player switches to the remaining unopened door
        switch_options = [door for door in all_doors if door != player_choice and door not in doors_revealed]
        assert len(switch_options) == 1, "Error: Exactly one door should remain for switching."
        player_switch_choice = switch_options[0]
        # Count wins
        stay_wins += (player_choice == car)
        switch_wins += (player_switch_choice == car)

    return switch_wins / num_trials, stay_wins / num_trials

# Run simulation
switch_prob, stay_prob = monty_hall_simulation(num_doors=3, num_trials=100000)
print(f"Probability of winning when switching: {switch_prob:.4f} (Expected: ~0.6667)")
print(f"Probability of winning when player stays: {stay_prob:.4f} (Expected: ~0.3333)")