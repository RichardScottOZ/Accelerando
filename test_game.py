#!/usr/bin/env python3
"""
Test script for Accelerando game mechanics
"""

from accelerando_game import GameState, AccelerandoGame
import json


def test_game_state():
    """Test GameState serialization"""
    print("Testing GameState serialization...")
    state = GameState()
    state.reputation = 75
    state.turn = 5
    
    # Test to_dict
    state_dict = state.to_dict()
    assert state_dict['reputation'] == 75
    assert state_dict['turn'] == 5
    
    # Test from_dict
    new_state = GameState.from_dict(state_dict)
    assert new_state.reputation == 75
    assert new_state.turn == 5
    
    print("✓ GameState serialization works!")


def test_win_conditions():
    """Test win condition logic"""
    print("\nTesting win conditions...")
    game = AccelerandoGame()
    
    # Test singularity victory
    game.state.singularity_progress = 100
    game.state.reputation = 60
    assert game.check_win_condition() == True
    
    # Test entity helper victory
    game2 = AccelerandoGame()
    game2.state.entities_helped = 10
    game2.state.reputation = 75
    assert game2.check_win_condition() == True
    
    # Test non-victory
    game3 = AccelerandoGame()
    game3.state.reputation = 20
    assert game3.check_win_condition() == False
    
    print("✓ Win conditions work correctly!")


def test_lose_conditions():
    """Test lose condition logic"""
    print("\nTesting lose conditions...")
    game = AccelerandoGame()
    
    # Test reputation loss
    game.state.reputation = 0
    assert game.check_lose_condition() == True
    
    # Test dead kittens loss
    game2 = AccelerandoGame()
    game2.state.dead_kittens = 10
    assert game2.check_lose_condition() == True
    
    # Test bandwidth loss
    game3 = AccelerandoGame()
    game3.state.bandwidth = 0
    assert game3.check_lose_condition() == True
    
    # Test non-loss
    game4 = AccelerandoGame()
    assert game4.check_lose_condition() == False
    
    print("✓ Lose conditions work correctly!")


def test_save_load():
    """Test save/load functionality"""
    print("\nTesting save/load...")
    import os
    
    game = AccelerandoGame()
    game.state.reputation = 88
    game.state.turn = 15
    game.state.entities_helped = 3
    
    # Save
    game.save_game()
    assert os.path.exists(game.save_file)
    
    # Load into new game
    game2 = AccelerandoGame()
    game2.load_game()
    assert game2.state.reputation == 88
    assert game2.state.turn == 15
    assert game2.state.entities_helped == 3
    
    # Cleanup
    os.remove(game.save_file)
    
    print("✓ Save/load works correctly!")


def test_game_initialization():
    """Test game initialization"""
    print("\nTesting game initialization...")
    game = AccelerandoGame()
    
    assert game.state.reputation == 50
    assert game.state.ideas == 10
    assert game.state.bandwidth == 100
    assert game.state.influence == 20
    assert game.state.turn == 0
    assert game.state.dead_kittens == 0
    assert game.state.game_over == False
    assert game.state.victory == False
    
    print("✓ Game initializes with correct defaults!")


def main():
    """Run all tests"""
    print("="*70)
    print("ACCELERANDO GAME - TEST SUITE")
    print("="*70)
    
    try:
        test_game_initialization()
        test_game_state()
        test_win_conditions()
        test_lose_conditions()
        test_save_load()
        
        print("\n" + "="*70)
        print("✓ ALL TESTS PASSED!")
        print("="*70)
        return 0
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
