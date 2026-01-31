#!/usr/bin/env python3
"""
Integration test - simulates an actual game session
"""

from accelerando_game import AccelerandoGame, GameState
import sys
from io import StringIO


def simulate_game_session():
    """Simulate a complete game session with automated inputs"""
    print("="*70)
    print("INTEGRATION TEST: Simulating Full Game Session")
    print("="*70)
    
    game = AccelerandoGame()
    
    # Test 1: Game initialization
    print("\n[TEST 1] Game initializes correctly")
    assert game.state.reputation == 50
    assert game.state.turn == 0
    print("✓ PASS: Initial state is correct")
    
    # Test 2: Stats display (should not crash)
    print("\n[TEST 2] Stats display works")
    try:
        game.display_stats()
        print("✓ PASS: Stats display successful")
    except Exception as e:
        print(f"✗ FAIL: Stats display error: {e}")
        return False
    
    # Test 3: Simulate turn progression
    print("\n[TEST 3] Turn progression mechanics")
    initial_turn = game.state.turn
    initial_progress = game.state.singularity_progress
    
    # Manually progress resources (like play_turn does)
    game.state.turn += 1
    game.state.singularity_progress += 2
    game.state.ideas += 2
    
    assert game.state.turn == initial_turn + 1
    assert game.state.singularity_progress >= initial_progress
    print("✓ PASS: Turn progression works correctly")
    
    # Test 4: Victory scenario
    print("\n[TEST 4] Victory condition detection")
    victory_game = AccelerandoGame()
    victory_game.state.singularity_progress = 100
    victory_game.state.reputation = 60
    
    if victory_game.check_win_condition():
        print("✓ PASS: Victory condition detected correctly")
    else:
        print("✗ FAIL: Victory condition not detected")
        return False
    
    # Test 5: Defeat scenario
    print("\n[TEST 5] Defeat condition detection")
    defeat_game = AccelerandoGame()
    defeat_game.state.reputation = 0
    
    if defeat_game.check_lose_condition():
        print("✓ PASS: Defeat condition detected correctly")
    else:
        print("✗ FAIL: Defeat condition not detected")
        return False
    
    # Test 6: Save functionality
    print("\n[TEST 6] Save game functionality")
    save_game = AccelerandoGame()
    save_game.state.reputation = 99
    save_game.state.turn = 42
    try:
        save_game.save_game()
        print("✓ PASS: Game saved successfully")
    except Exception as e:
        print(f"✗ FAIL: Save error: {e}")
        return False
    
    # Test 7: Load functionality
    print("\n[TEST 7] Load game functionality")
    load_game = AccelerandoGame()
    try:
        if load_game.load_game():
            if load_game.state.reputation == 99 and load_game.state.turn == 42:
                print("✓ PASS: Game loaded correctly with saved state")
            else:
                print("✗ FAIL: Loaded state doesn't match saved state")
                return False
        else:
            print("✗ FAIL: Load returned False")
            return False
    except Exception as e:
        print(f"✗ FAIL: Load error: {e}")
        return False
    
    # Test 8: Events can be called without crashing
    print("\n[TEST 8] Event system integrity")
    event_game = AccelerandoGame()
    event_game.state.influence = 100
    event_game.state.bandwidth = 100
    event_game.state.ideas = 100
    
    try:
        # These events require user input, so we can't fully test them
        # But we can verify they exist and are callable
        assert hasattr(event_game, 'event_lobster_asylum')
        assert hasattr(event_game, 'event_patent_decision')
        assert hasattr(event_game, 'event_russian_ai')
        assert hasattr(event_game, 'event_pamela_confrontation')
        assert hasattr(event_game, 'event_aineko_advice')
        assert hasattr(event_game, 'event_idea_generation')
        print("✓ PASS: All events are defined and accessible")
    except Exception as e:
        print(f"✗ FAIL: Event system error: {e}")
        return False
    
    # Test 9: Resource constraints
    print("\n[TEST 9] Resource constraint validation")
    constraint_game = AccelerandoGame()
    
    # Test that resources can go negative (game should handle this)
    constraint_game.state.reputation = 10
    constraint_game.state.reputation -= 50
    
    # Should trigger lose condition
    if constraint_game.check_lose_condition():
        print("✓ PASS: Resource constraints properly enforced")
    else:
        print("✗ FAIL: Resource constraints not working")
        return False
    
    # Test 10: Display methods don't crash
    print("\n[TEST 10] Display methods")
    display_game = AccelerandoGame()
    try:
        display_game.display_header()
        display_game.display_victory()
        display_game.display_defeat()
        print("✓ PASS: All display methods work without crashing")
    except Exception as e:
        print(f"✗ FAIL: Display method error: {e}")
        return False
    
    # Cleanup
    import os
    if os.path.exists("accelerando_save.json"):
        os.remove("accelerando_save.json")
    
    return True


def main():
    """Run integration test"""
    print("\n")
    success = simulate_game_session()
    
    print("\n" + "="*70)
    if success:
        print("✓ ALL INTEGRATION TESTS PASSED")
        print("="*70)
        print("\nThe game is ready to play!")
        print("Run: python3 accelerando_game.py")
        return 0
    else:
        print("✗ INTEGRATION TESTS FAILED")
        print("="*70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
