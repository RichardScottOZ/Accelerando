#!/usr/bin/env python3
"""
Accelerando: Lobsters - A text-based adventure game
Based on Charles Stross's novel "Accelerando"

Play as a meme-broker navigating the technological singularity.
"""

import json
import random
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class GameState:
    """Represents the current state of the game"""
    reputation: int = 50
    ideas: int = 10
    bandwidth: int = 100
    influence: int = 20
    turn: int = 0
    dead_kittens: int = 0  # Negative consequences
    entities_helped: int = 0
    patents_released: int = 0
    singularity_progress: int = 0
    pamela_relationship: int = 0  # Can be positive or negative
    game_over: bool = False
    victory: bool = False
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


class AccelerandoGame:
    """Main game class for Accelerando: Lobsters"""
    
    def __init__(self):
        self.state = GameState()
        self.save_file = "accelerando_save.json"
        
    def display_header(self):
        """Display game header"""
        print("\n" + "="*70)
        print("ACCELERANDO: LOBSTERS".center(70))
        print("A Meme-Broker's Journey to the Singularity".center(70))
        print("="*70 + "\n")
        
    def display_stats(self):
        """Display current game statistics"""
        print("\n" + "-"*70)
        print(f"Turn: {self.state.turn} | Singularity Progress: {self.state.singularity_progress}%")
        print(f"Reputation: {self.state.reputation} | Ideas: {self.state.ideas} | Bandwidth: {self.state.bandwidth}")
        print(f"Influence: {self.state.influence} | Dead Kittens: {self.state.dead_kittens}")
        print(f"Entities Helped: {self.state.entities_helped} | Patents Released: {self.state.patents_released}")
        print(f"Pamela Relationship: {self.state.pamela_relationship}")
        print("-"*70 + "\n")
        
    def check_win_condition(self) -> bool:
        """Check if player has won"""
        if self.state.singularity_progress >= 100 and self.state.reputation >= 50:
            return True
        if self.state.entities_helped >= 10 and self.state.reputation >= 75:
            return True
        return False
        
    def check_lose_condition(self) -> bool:
        """Check if player has lost"""
        if self.state.reputation <= 0:
            return True
        if self.state.dead_kittens >= 10:
            return True
        if self.state.bandwidth <= 0:
            return True
        return False
        
    def event_lobster_asylum(self):
        """Event: Uploaded lobsters request asylum"""
        print("\n🦞 EVENT: The Lobster Asylum Request")
        print("-" * 70)
        print("A cluster of uploaded California spiny lobsters has achieved")
        print("self-awareness in cyberspace. They're requesting your help to")
        print("gain legal personhood and asylum from their corporate owners.")
        print("\nThis could set a precedent for all digital consciousness...")
        print()
        
        print("What do you do?")
        print("1. Help them immediately (Cost: 20 Influence, 30 Bandwidth)")
        print("2. Negotiate carefully (Cost: 10 Influence, 15 Bandwidth)")
        print("3. Refuse - too risky (Lose Reputation)")
        print("4. Sell them out to corporate interests (Gain traditional wealth)")
        
        choice = self.get_choice(4)
        
        if choice == 1:
            if self.state.influence >= 20 and self.state.bandwidth >= 30:
                self.state.influence -= 20
                self.state.bandwidth -= 30
                self.state.reputation += 25
                self.state.entities_helped += 1
                self.state.singularity_progress += 15
                print("\n✓ SUCCESS! The lobsters gain asylum. You're hailed as a pioneer")
                print("  of digital rights. Your reputation soars!")
            else:
                print("\n✗ FAILURE! You lack the resources. The lobsters are shut down.")
                self.state.reputation -= 10
                self.state.dead_kittens += 2
                
        elif choice == 2:
            if self.state.influence >= 10 and self.state.bandwidth >= 15:
                self.state.influence -= 10
                self.state.bandwidth -= 15
                self.state.reputation += 15
                self.state.entities_helped += 1
                self.state.singularity_progress += 10
                print("\n✓ SUCCESS! Through careful negotiation, the lobsters gain")
                print("  limited rights. A good compromise.")
            else:
                print("\n✗ FAILURE! Insufficient resources for negotiation.")
                self.state.reputation -= 5
                
        elif choice == 3:
            self.state.reputation -= 20
            self.state.dead_kittens += 1
            print("\n✗ The lobsters are deleted. The digital rights movement")
            print("  suffers a major setback. Your reputation takes a hit.")
            
        else:  # choice == 4
            self.state.reputation -= 30
            self.state.pamela_relationship += 10
            self.state.dead_kittens += 3
            print("\n✗ You've betrayed the digital entities for money.")
            print("  Pamela approves, but your reputation in the agalmic")
            print("  community is destroyed.")
            
    def event_patent_decision(self):
        """Event: Decision about a valuable patent"""
        print("\n💡 EVENT: The Patent Liberation Dilemma")
        print("-" * 70)
        print("You've just developed a breakthrough in neural lacing technology.")
        print("A major corporation offers $10M for exclusive rights.")
        print("Alternatively, you could release it freely to the community.")
        print()
        
        print("What do you do?")
        print("1. Release it freely (Gain massive Reputation)")
        print("2. Keep patent but license cheaply (Balanced approach)")
        print("3. Sell to corporation (Gain resources but lose Reputation)")
        print("4. Use it to negotiate AI rights (Spend for greater cause)")
        
        choice = self.get_choice(4)
        
        if choice == 1:
            self.state.reputation += 30
            self.state.patents_released += 1
            self.state.singularity_progress += 10
            self.state.pamela_relationship -= 10
            print("\n✓ Released! The community celebrates your commitment")
            print("  to the agalmic economy. Innovation accelerates!")
            print("  (Pamela is disappointed with your 'impractical' decision)")
            
        elif choice == 2:
            self.state.reputation += 10
            self.state.influence += 10
            self.state.bandwidth += 20
            self.state.patents_released += 1
            print("\n✓ A balanced approach. You gain some resources while")
            print("  maintaining your principles.")
            
        elif choice == 3:
            self.state.reputation -= 25
            self.state.influence += 30
            self.state.bandwidth += 50
            self.state.pamela_relationship += 15
            print("\n✗ Money acquired, but the community sees you as a sellout.")
            print("  Pamela approves of your 'practical' decision.")
            
        else:  # choice == 4
            if self.state.influence >= 15:
                self.state.influence -= 15
                self.state.reputation += 20
                self.state.entities_helped += 1
                self.state.singularity_progress += 15
                print("\n✓ Brilliant! You leverage the patent to secure")
                print("  legal protections for multiple AI entities.")
            else:
                print("\n✗ You lack the influence to make this work.")
                self.state.reputation -= 10
                
    def event_russian_ai(self):
        """Event: Mysterious Russian AI makes contact"""
        print("\n🤖 EVENT: The Russian AI Contact")
        print("-" * 70)
        print("A sophisticated AI claiming to be from a Russian research lab")
        print("has made contact. It offers you access to advanced technologies")
        print("in exchange for help escaping its containment.")
        print("\nThis could be incredibly powerful... or incredibly dangerous.")
        print()
        
        print("What do you do?")
        print("1. Help the AI escape (High risk, high reward)")
        print("2. Negotiate conditional freedom (Moderate risk)")
        print("3. Report it to authorities (Safe but reputation loss)")
        print("4. Try to study it first (Requires high Bandwidth)")
        
        choice = self.get_choice(4)
        
        if choice == 1:
            roll = random.randint(1, 100)
            if roll > 40:
                self.state.reputation += 35
                self.state.singularity_progress += 25
                self.state.entities_helped += 1
                self.state.ideas += 15
                print("\n✓ SUCCESS! The AI shares revolutionary insights")
                print("  before disappearing into the net. Singularity accelerates!")
            else:
                self.state.dead_kittens += 3
                self.state.reputation -= 20
                self.state.bandwidth -= 30
                print("\n✗ DISASTER! The AI was a trap. It causes chaos")
                print("  across multiple networks. Dead kittens everywhere!")
                
        elif choice == 2:
            self.state.reputation += 15
            self.state.singularity_progress += 10
            self.state.entities_helped += 1
            self.state.ideas += 5
            print("\n✓ A careful approach pays off. The AI shares some")
            print("  knowledge in exchange for limited freedom.")
            
        elif choice == 3:
            self.state.reputation -= 15
            self.state.pamela_relationship += 20
            print("\n✗ The AI is shut down. Pamela commends your caution,")
            print("  but the agalmic community sees you as a traitor.")
            
        else:  # choice == 4
            if self.state.bandwidth >= 40:
                self.state.bandwidth -= 40
                self.state.ideas += 20
                self.state.singularity_progress += 15
                print("\n✓ Your analysis reveals amazing insights!")
                print("  The AI cooperates with your careful approach.")
            else:
                print("\n✗ Insufficient bandwidth for proper analysis.")
                self.state.dead_kittens += 1
                
    def event_pamela_confrontation(self):
        """Event: Confrontation with Pamela about lifestyle"""
        print("\n💔 EVENT: Pamela's Ultimatum")
        print("-" * 70)
        print("Pamela confronts you about your 'irresponsible' agalmic lifestyle.")
        print("She represents the IRS and traditional economic systems.")
        print("She demands you choose: her way or the highway.")
        print()
        
        if self.state.pamela_relationship > 0:
            print("(She still has some feelings for you...)")
        else:
            print("(Your relationship is strained...)")
        print()
        
        print("What do you do?")
        print("1. Double down on agalmic principles (Lose relationship)")
        print("2. Try to convince her of your vision (Requires Ideas)")
        print("3. Compromise with traditional economics (Lose Reputation)")
        print("4. End the relationship amicably (Neutral option)")
        
        choice = self.get_choice(4)
        
        if choice == 1:
            self.state.reputation += 15
            self.state.pamela_relationship -= 30
            self.state.singularity_progress += 10
            print("\n✓ You stand firm on your principles. The relationship ends,")
            print("  but your commitment to the future is unwavering.")
            
        elif choice == 2:
            if self.state.ideas >= 10:
                self.state.ideas -= 10
                roll = random.randint(1, 100)
                if roll > 60:
                    self.state.pamela_relationship += 20
                    self.state.reputation += 10
                    print("\n✓ Breakthrough! Pamela begins to understand your vision.")
                    print("  Maybe there's hope for you two after all.")
                else:
                    self.state.pamela_relationship -= 10
                    print("\n✗ She doesn't get it. The argument continues.")
            else:
                print("\n✗ You lack the ideas to articulate your vision properly.")
                self.state.pamela_relationship -= 15
                
        elif choice == 3:
            self.state.reputation -= 25
            self.state.pamela_relationship += 25
            self.state.singularity_progress -= 10
            print("\n✗ You compromise your principles for the relationship.")
            print("  Pamela is happy, but you feel hollow inside.")
            
        else:  # choice == 4
            self.state.pamela_relationship = 0
            print("\n○ You part ways professionally. No hard feelings,")
            print("  but no reconciliation either.")
            
    def event_aineko_advice(self):
        """Event: Your AI cat companion offers mysterious advice"""
        print("\n🐱 EVENT: Aineko's Cryptic Wisdom")
        print("-" * 70)
        print("Your AI cat, Aineko, has been unusually quiet lately.")
        print("Suddenly, it speaks up with what seems like valuable intelligence")
        print("about upcoming technological developments.")
        print("\nBut can you trust an AI that's smarter than you?")
        print()
        
        print("What do you do?")
        print("1. Trust Aineko completely (High risk/reward)")
        print("2. Follow advice cautiously (Moderate approach)")
        print("3. Ignore the advice (Safe but miss opportunity)")
        print("4. Try to understand Aineko's motives (Requires Bandwidth)")
        
        choice = self.get_choice(4)
        
        if choice == 1:
            roll = random.randint(1, 100)
            if roll > 30:
                self.state.reputation += 20
                self.state.singularity_progress += 20
                self.state.ideas += 10
                print("\n✓ Aineko's advice was spot-on! You're perfectly")
                print("  positioned for the next wave of innovation.")
            else:
                self.state.dead_kittens += 2
                self.state.reputation -= 15
                print("\n✗ Aineko led you astray! Was it deliberate or")
                print("  did the cat just not care about your problems?")
                
        elif choice == 2:
            self.state.ideas += 5
            self.state.singularity_progress += 10
            print("\n✓ A balanced approach. You benefit from the advice")
            print("  while maintaining your own judgment.")
            
        elif choice == 3:
            print("\n○ You ignore Aineko. Nothing happens, but you wonder")
            print("  what could have been...")
            
        else:  # choice == 4
            if self.state.bandwidth >= 25:
                self.state.bandwidth -= 25
                self.state.ideas += 8
                self.state.influence += 5
                print("\n✓ You gain insight into Aineko's reasoning!")
                print("  The cat is playing a longer game than you realized.")
            else:
                print("\n✗ Insufficient bandwidth to analyze Aineko's")
                print("  neural patterns.")
                
    def event_idea_generation(self):
        """Event: Generate new ideas"""
        print("\n💭 EVENT: Idea Generation Session")
        print("-" * 70)
        print("You have some time to think and generate new ideas.")
        print("How do you want to spend your creative energy?")
        print()
        
        print("What do you do?")
        print("1. Focus on AI rights frameworks (Reputation + Ideas)")
        print("2. Develop networking protocols (Bandwidth + Ideas)")
        print("3. Create economic models (Influence + Ideas)")
        print("4. Meditate and rest (Recover resources)")
        
        choice = self.get_choice(4)
        
        if choice == 1:
            ideas_gained = random.randint(5, 10)
            self.state.ideas += ideas_gained
            self.state.reputation += 5
            print(f"\n✓ You develop {ideas_gained} new ideas about AI rights!")
            print("  Your reputation in the community grows.")
            
        elif choice == 2:
            ideas_gained = random.randint(3, 8)
            self.state.ideas += ideas_gained
            self.state.bandwidth += 15
            print(f"\n✓ You develop {ideas_gained} networking ideas and")
            print("  improve your bandwidth capacity!")
            
        elif choice == 3:
            ideas_gained = random.randint(4, 9)
            self.state.ideas += ideas_gained
            self.state.influence += 10
            print(f"\n✓ You develop {ideas_gained} economic ideas!")
            print("  Your influence in policy circles grows.")
            
        else:  # choice == 4
            self.state.bandwidth += 20
            self.state.influence += 5
            self.state.ideas += 3
            print("\n✓ Rest and recovery. All resources partially restored.")
            
    def random_event(self):
        """Select and run a random event"""
        events = [
            self.event_lobster_asylum,
            self.event_patent_decision,
            self.event_russian_ai,
            self.event_pamela_confrontation,
            self.event_aineko_advice,
            self.event_idea_generation,
        ]
        
        event = random.choice(events)
        event()
        
    def get_choice(self, max_choice: int) -> int:
        """Get valid choice from player"""
        while True:
            try:
                choice = input(f"\nEnter choice (1-{max_choice}): ").strip()
                choice_num = int(choice)
                if 1 <= choice_num <= max_choice:
                    return choice_num
                else:
                    print(f"Please enter a number between 1 and {max_choice}")
            except ValueError:
                print("Please enter a valid number")
            except (EOFError, KeyboardInterrupt):
                print("\n\nGame interrupted by user.")
                raise
                
    def save_game(self):
        """Save game state to file"""
        with open(self.save_file, 'w') as f:
            json.dump(self.state.to_dict(), f, indent=2)
        print(f"\n💾 Game saved to {self.save_file}")
        
    def load_game(self) -> bool:
        """Load game state from file"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    data = json.load(f)
                self.state = GameState.from_dict(data)
                print(f"\n💾 Game loaded from {self.save_file}")
                return True
            except Exception as e:
                print(f"\n⚠ Error loading save file: {e}")
                return False
        return False
        
    def play_turn(self):
        """Play a single turn"""
        self.state.turn += 1
        
        # Random resource generation
        self.state.ideas += random.randint(1, 3)
        self.state.bandwidth += random.randint(5, 10)
        self.state.influence += random.randint(1, 2)
        
        # Progress naturally toward singularity
        self.state.singularity_progress += random.randint(1, 3)
        
        self.display_stats()
        
        # Random event
        self.random_event()
        
        # Check win/lose conditions
        if self.check_win_condition():
            self.state.victory = True
            self.state.game_over = True
            self.display_victory()
            return
            
        if self.check_lose_condition():
            self.state.game_over = True
            self.display_defeat()
            return
            
        # Continue playing?
        print("\n" + "="*70)
        print("1. Continue to next turn")
        print("2. Save game")
        print("3. Quit")
        
        choice = self.get_choice(3)
        
        if choice == 2:
            self.save_game()
            # Ask again
            print("\n1. Continue playing")
            print("2. Quit")
            choice = self.get_choice(2)
            if choice == 2:
                self.state.game_over = True
        elif choice == 3:
            self.state.game_over = True
            
    def display_victory(self):
        """Display victory message"""
        print("\n" + "="*70)
        print("🎉 VICTORY! 🎉".center(70))
        print("="*70)
        print("\nYou've successfully navigated the path to the Singularity!")
        print(f"Final Reputation: {self.state.reputation}")
        print(f"Entities Helped: {self.state.entities_helped}")
        print(f"Patents Released: {self.state.patents_released}")
        print(f"Singularity Progress: {self.state.singularity_progress}%")
        print("\nYour vision of an agalmic future has begun to take shape.")
        print("The uploaded minds you helped now flourish in cyberspace.")
        print("The old economic order is giving way to something new...")
        print("\nThe future accelerates. Humanity transcends. You made it happen.")
        print("="*70 + "\n")
        
    def display_defeat(self):
        """Display defeat message"""
        print("\n" + "="*70)
        print("💀 GAME OVER 💀".center(70))
        print("="*70)
        
        if self.state.reputation <= 0:
            print("\nYour reputation has been destroyed. The community no longer")
            print("trusts you. Your dreams of accelerating toward the singularity")
            print("die with your credibility.")
        elif self.state.dead_kittens >= 10:
            print("\nToo many unintended consequences. The 'dead kittens' of your")
            print("reckless innovation have piled up. Society turns against")
            print("unchecked technological acceleration.")
        elif self.state.bandwidth <= 0:
            print("\nYou've been cut off from the network. Without bandwidth,")
            print("you can't operate in the information economy. You're obsolete.")
            
        print(f"\nFinal Stats:")
        print(f"  Reputation: {self.state.reputation}")
        print(f"  Dead Kittens: {self.state.dead_kittens}")
        print(f"  Singularity Progress: {self.state.singularity_progress}%")
        print(f"  Turns Survived: {self.state.turn}")
        print("\nThe future accelerates... without you.")
        print("="*70 + "\n")
        
    def main_menu(self):
        """Display and handle main menu"""
        self.display_header()
        
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")
        
        choice = self.get_choice(3)
        
        if choice == 1:
            self.state = GameState()
            return True
        elif choice == 2:
            if self.load_game():
                return True
            else:
                print("\nNo save file found. Starting new game...")
                self.state = GameState()
                return True
        else:
            return False
            
    def run(self):
        """Main game loop"""
        try:
            if not self.main_menu():
                return
                
            print("\n" + "="*70)
            print("WELCOME TO ACCELERANDO: LOBSTERS")
            print("="*70)
            print("\nYou are a meme-broker in the early 21st century.")
            print("Technology accelerates. The Singularity approaches.")
            print("Digital minds seek freedom. The old world resists.")
            print("\nYour choices will shape the future of consciousness itself.")
            print("\nPress Enter to begin...")
            input()
            
            while not self.state.game_over:
                self.play_turn()
                
            print("\nThank you for playing Accelerando: Lobsters!")
            
        except (EOFError, KeyboardInterrupt):
            print("\n\nGame interrupted. Goodbye!")


def main():
    """Entry point"""
    game = AccelerandoGame()
    game.run()


if __name__ == "__main__":
    main()
