#!/usr/bin/env python3
"""
Demo script showing Accelerando game in action
This simulates a few turns with automated choices
"""

from accelerando_game import AccelerandoGame, GameState
import random


def automated_demo():
    """Run an automated demo of the game"""
    print("="*70)
    print("ACCELERANDO: LOBSTERS - AUTOMATED DEMO")
    print("="*70)
    print("\nThis demo shows the game in action with automated choices.\n")
    
    game = AccelerandoGame()
    game.display_header()
    
    print("Starting new game with default state:")
    game.display_stats()
    
    print("\n" + "="*70)
    print("DEMO: Simulating game events...")
    print("="*70)
    
    # Demo 1: Lobster asylum (helpful response)
    print("\n[DEMO] Event: Lobster Asylum Request")
    print("Choice: Help them immediately")
    game.state.influence = 30
    game.state.bandwidth = 50
    original_rep = game.state.reputation
    game.state.influence -= 20
    game.state.bandwidth -= 30
    game.state.reputation += 25
    game.state.entities_helped += 1
    game.state.singularity_progress += 15
    print(f"Result: Reputation {original_rep} → {game.state.reputation}")
    print(f"Entities helped: {game.state.entities_helped}")
    print(f"Singularity progress: {game.state.singularity_progress}%")
    
    # Demo 2: Patent decision (release freely)
    print("\n[DEMO] Event: Patent Liberation")
    print("Choice: Release patent freely")
    original_rep = game.state.reputation
    game.state.reputation += 30
    game.state.patents_released += 1
    game.state.singularity_progress += 10
    print(f"Result: Reputation {original_rep} → {game.state.reputation}")
    print(f"Patents released: {game.state.patents_released}")
    print(f"Singularity progress: {game.state.singularity_progress}%")
    
    # Demo 3: Russian AI (cautious approach)
    print("\n[DEMO] Event: Russian AI Contact")
    print("Choice: Negotiate conditional freedom")
    original_rep = game.state.reputation
    game.state.reputation += 15
    game.state.singularity_progress += 10
    game.state.entities_helped += 1
    game.state.ideas += 5
    print(f"Result: Reputation {original_rep} → {game.state.reputation}")
    print(f"Ideas gained: 5")
    print(f"Singularity progress: {game.state.singularity_progress}%")
    
    # Demo 4: Check current state
    print("\n" + "="*70)
    print("Current Game State After Demo Events:")
    game.display_stats()
    
    # Demo 5: Check win condition
    print("Checking win conditions...")
    if game.check_win_condition():
        print("✓ Victory conditions met!")
        game.display_victory()
    elif game.check_lose_condition():
        print("✗ Defeat conditions met!")
        game.display_defeat()
    else:
        print("○ Game continues - neither victory nor defeat yet.")
        print(f"  Need: 100% singularity progress OR 10 entities helped + 75 reputation")
        print(f"  Current: {game.state.singularity_progress}% progress, {game.state.entities_helped} entities, {game.state.reputation} reputation")
    
    print("\n" + "="*70)
    print("DEMO COMPLETE")
    print("="*70)
    print("\nTo play the full game, run: python3 accelerando_game.py")
    print()


if __name__ == "__main__":
    automated_demo()
