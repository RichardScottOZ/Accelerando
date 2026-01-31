# Accelerando: Lobsters - Game Design Document

## Overview
A text-based adventure/simulation game based on Charles Stross's "Accelerando" novel, focusing on the "Lobsters" chapter themes.

## Core Concept
Players take on the role of a meme-broker/venture altruist navigating the early 21st century on the brink of technological singularity. Make decisions about patents, AI rights, and technological advancement while managing your reputation in a post-scarcity information economy.

## Key Themes
1. **Technological Singularity** - Racing toward the singularity while managing consequences
2. **Agalmic Economics** - Reputation-based economy vs traditional wealth
3. **AI Rights** - Deciding the fate of uploaded consciousness and digital entities
4. **Innovation vs Consequences** - Balancing progress with ethical implications

## Game Mechanics

### Reputation System
- Primary resource: **Reputation Points (RP)**
- Earn RP by: Giving away patents, helping digital entities, disrupting old systems
- Lose RP by: Hoarding ideas, ignoring AI requests, supporting legacy economics

### Resources
- **Ideas** - Generate and give away for RP
- **Patents** - Can be kept (money) or released (RP)
- **Bandwidth** - Needed for digital entity interactions
- **Influence** - Used to affect policy and legal decisions

### Core Gameplay Loop
1. Receive requests from AIs, uploaded entities, or human factions
2. Make decisions that affect your reputation and resources
3. Navigate ethical dilemmas about consciousness and rights
4. Progress through events toward the singularity
5. Balance personal relationships (Pamela) vs idealistic goals

### Win Conditions
- Reach the Singularity with high reputation
- Successfully grant asylum to digital entities
- Transform the economic system to post-scarcity

### Lose Conditions
- Reputation drops to zero (discredited)
- Get trapped by legacy economic forces (IRS)
- Cause too many "dead kittens" (negative consequences)

## Characters/Entities
- **Player** - Manfred Macx-style meme broker
- **Pamela** - Represents old-world economics (antagonist/challenge)
- **The Lobsters** - Uploaded entities seeking asylum
- **Russian AI** - Mysterious AI making contact
- **Aineko** - Your AI cat companion (advisor/wildcard)

## Events
Players encounter various scenarios inspired by the novel:
- Patent liberation decisions
- AI asylum requests
- Economic confrontations
- Technological breakthrough opportunities
- Relationship challenges
- Ethical dilemmas about consciousness

## Technical Implementation
- **Language**: Python 3
- **Format**: Text-based CLI game
- **Save System**: JSON-based state persistence
- **Input**: Choice-based decision making
- **Output**: Narrative text with stats display

## Player Progression
As the game progresses:
- More complex ethical dilemmas
- Increasing AI sophistication
- Accelerating technological change
- Higher stakes decisions
- Approach to the Singularity event

## Future Enhancements
- Multiple chapters (following the novel's structure)
- More complex economic simulation
- Network graph of relationships
- Visual novel style interface
- Multiplayer cooperation/competition
