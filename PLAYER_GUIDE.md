# Accelerando: Lobsters - Player Guide

## Getting Started

### Installation
No installation required! Just Python 3.7+

```bash
python3 accelerando_game.py
```

### First Time Playing

1. **Start a New Game** - Choose option 1 from the main menu
2. **Read the intro** - Sets up the story and your role
3. **Make choices** - Each decision affects your resources and progress
4. **Monitor your stats** - Keep an eye on reputation and resources
5. **Progress toward victory** - Reach the singularity or help enough entities

## Understanding Your Resources

### Reputation (Primary Resource)
- **What it is**: Your standing in the agalmic community
- **How to gain**: Release patents, help digital entities, accelerate innovation
- **How to lose**: Hoard wealth, betray AIs, support old economic systems
- **Why it matters**: You need 50+ reputation to win, and 0 reputation means game over

### Ideas
- **What it is**: Creative output and innovations
- **How to gain**: Idea generation events, AI cooperation, rest periods
- **How to use**: Convince others, negotiate, unlock options
- **Regenerates**: Slowly each turn

### Bandwidth
- **What it is**: Network capacity for digital interactions
- **How to gain**: Upgrades, certain choices, rest periods
- **How to use**: Interact with AIs, help uploaded entities
- **Critical**: Running out ends the game!

### Influence
- **What it is**: Political and social power
- **How to gain**: Strategic compromises, resource trades
- **How to use**: Change laws, grant asylum, affect policy
- **Strategy tip**: Save for important asylum decisions

## Key Game Concepts

### The Agalmic Economy
An economy based on reputation rather than money:
- **Good**: Giving away patents, helping entities, sharing ideas
- **Bad**: Hoarding wealth, selling to corporations, traditional capitalism

### Dead Kittens
Unintended negative consequences of your actions:
- Each risky choice may create "dead kittens"
- 10 dead kittens = game over
- Represents the dark side of unchecked innovation
- Be thoughtful, not just aggressive

### Singularity Progress
- Measures approach to technological singularity
- Increases through innovation and AI liberation
- Need 100% + good reputation to win via this path
- Some choices accelerate it more than others

### Relationship: Pamela
- Represents old-world economics vs your idealism
- Can be positive, neutral, or negative
- High positive: She might come around to your vision
- High negative: She becomes an obstacle
- Doesn't directly affect victory, but affects events

## Event Types & Strategies

### 🦞 Lobster Asylum Request
**Setup**: Uploaded lobsters seek freedom
**Best approach**: Help if you have the resources (20+ influence, 30+ bandwidth)
**Alternative**: Negotiate if resources are tight
**Avoid**: Refusing or selling out - major reputation loss

### 💡 Patent Liberation
**Setup**: You develop valuable technology
**Best approach**: Release freely for maximum reputation
**Alternative**: Cheap licensing for balanced resources
**When to sell**: Never, unless desperate for resources and willing to lose reputation

### 🤖 Russian AI Contact
**Setup**: Mysterious AI offers deal
**Best approach**: Study it first if you have 40+ bandwidth
**Risky but rewarding**: Help it escape (60% success rate)
**Safe**: Negotiate conditional freedom
**Avoid**: Reporting it - reputation loss

### 💔 Pamela Confrontation
**Setup**: She challenges your lifestyle
**Best approach**: Try to convince her if you have 10+ ideas
**Principled**: Double down (lose relationship, gain reputation)
**Practical**: Compromise (keep relationship, lose reputation)
**Neutral**: End it amicably

### 🐱 Aineko's Advice
**Setup**: Your AI cat offers mysterious guidance
**Best approach**: Study motives if you have 25+ bandwidth
**Moderate risk**: Follow cautiously
**High risk**: Trust completely (70% success rate)
**Safe**: Ignore (miss opportunity)

### 💭 Idea Generation
**Setup**: Free time to think
**For reputation**: Focus on AI rights
**For bandwidth**: Develop networking protocols
**For influence**: Create economic models
**For recovery**: Meditate and rest

## Winning Strategies

### Path 1: Singularity Victory
- Target: 100% singularity progress + 50+ reputation
- Strategy: Aggressively help AIs, release patents, take calculated risks
- Watch out for: Dead kittens accumulating
- Timeline: Usually 15-20 turns

### Path 2: Entity Helper Victory
- Target: 10+ entities helped + 75+ reputation
- Strategy: Focus on asylum/AI events, maintain high reputation
- More stable: Fewer risks needed
- Timeline: Usually 20-30 turns

### Path 3: Balanced Approach
- Pursue both paths simultaneously
- Most flexible and forgiving
- Recommended for first playthrough

## Common Pitfalls

### 1. Running Out of Bandwidth
- **Problem**: Can't interact with digital entities
- **Solution**: Choose bandwidth-generating events, rest periodically
- **Prevention**: Never let it drop below 30

### 2. Dead Kittens Accumulation
- **Problem**: Too many negative consequences
- **Solution**: Don't always take the riskiest option
- **Prevention**: Mix calculated risks with safe choices

### 3. Reputation Crash
- **Problem**: Made too many traditional economic choices
- **Solution**: Focus on patent liberation and entity helping
- **Prevention**: Stay true to agalmic principles

### 4. Resource Starvation
- **Problem**: Not enough influence/ideas for good choices
- **Solution**: Use idea generation events
- **Prevention**: Don't spend all resources at once

## Advanced Tips

1. **Resource Management**: Always keep a buffer of resources
2. **Risk Assessment**: High reputation allows more risk-taking
3. **Event Cycling**: Some events give better resource ratios
4. **Pamela Strategy**: Her relationship doesn't affect victory - focus on your goals
5. **Aineko**: Study before trusting for best results
6. **Save Often**: Use save function before major decisions
7. **Turn Efficiency**: Resources regenerate each turn, so pace yourself

## Save System

### Saving
- Choose "Save game" option during turn menu
- Saves to `accelerando_save.json`
- Can save at any point

### Loading
- Choose "Load Game" from main menu
- Resumes exactly where you left off
- If file corrupted, starts fresh

## Thematic Choices

The game is based on themes from Charles Stross's novel:

- **Agalmic vs Traditional Economics**: Core tension in every choice
- **AI Rights**: Central ethical question throughout
- **Unintended Consequences**: "Dead kittens" represent this
- **Acceleration**: Singularity progress shows technological change
- **Human Relationships**: Pamela represents the personal cost of idealism

## After Winning

Once you've won:
- Try the other victory path
- Minimize turns to victory (speedrun)
- Maximize final reputation
- Try keeping Pamela relationship positive while winning
- Experiment with different event strategies

## Troubleshooting

**Game won't start**: Check Python version (3.7+ required)
**Save won't load**: Delete `accelerando_save.json` and start fresh
**Want to reset**: Delete save file or start new game
**Stuck in bad state**: Make strategic compromises to recover resources

## Quick Reference Card

```
VICTORY CONDITIONS:
- 100% Singularity + 50 Reputation
- 10 Entities Helped + 75 Reputation

DEFEAT CONDITIONS:
- 0 Reputation
- 10 Dead Kittens
- 0 Bandwidth

RESOURCE GENERATION (per turn):
- Ideas: +1-3
- Bandwidth: +5-10
- Influence: +1-2
- Singularity: +1-3%
```

## Lore & Background

Based on "Accelerando" by Charles Stross:
- **Manfred Macx**: Your character archetype - venture altruist
- **The Lobsters**: First uploaded consciousness seeking rights
- **Pamela**: Represents clash between old and new economics
- **Aineko**: Superintelligent AI with unclear motivations
- **Agalmic Economy**: Post-scarcity reputation-based system
- **The Singularity**: Point where AI surpasses human intelligence

Read the novel at: https://www.antipope.org/charlie/blog-static/fiction/accelerando/accelerando.html

Enjoy the game, and remember: The future is accelerating. Which side of history will you be on?
