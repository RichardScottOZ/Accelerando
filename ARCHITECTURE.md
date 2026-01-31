# Accelerando Game - Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     ACCELERANDO GAME                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      Game Entry Point                        │
│                    accelerando_game.py                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   ┌──────────────────┐
                   │  AccelerandoGame │
                   │      (Main)      │
                   └──────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌─────────────────┐   ┌──────────────┐
│  GameState   │    │  Event System   │   │ Display/UI   │
│  Management  │    │   (6 Events)    │   │   System     │
└──────────────┘    └─────────────────┘   └──────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌─────────────────┐   ┌──────────────┐
│ Save/Load    │    │ Win/Lose Logic  │   │ Stats/Menus  │
│ (JSON)       │    │   Conditions    │   │   Display    │
└──────────────┘    └─────────────────┘   └──────────────┘
```

## Core Components

### 1. GameState (Data Layer)
**File**: `accelerando_game.py` (lines 1-40)
- **Purpose**: Store all game state
- **Data**: Reputation, Ideas, Bandwidth, Influence, Turns, Progress, etc.
- **Methods**: `to_dict()`, `from_dict()` for serialization

### 2. AccelerandoGame (Game Engine)
**File**: `accelerando_game.py` (lines 42-651)
- **Purpose**: Main game logic and orchestration
- **Responsibilities**:
  - Turn management
  - Event dispatching
  - Win/lose checking
  - Save/load operations
  - Display coordination

### 3. Event System
**Events** (6 types):
1. `event_lobster_asylum()` - Digital entity rights
2. `event_patent_decision()` - Economic choice
3. `event_russian_ai()` - AI cooperation
4. `event_pamela_confrontation()` - Relationship
5. `event_aineko_advice()` - AI guidance
6. `event_idea_generation()` - Resource gathering

**Flow**:
```
Turn Start → Random Event Selection → Present Choices
     ↓
Player Input → Update GameState → Check Conditions
     ↓
Display Results → Next Turn or End Game
```

### 4. Resource System
```
┌────────────────────────────────────────┐
│           Resource Types               │
├────────────────────────────────────────┤
│ • Reputation (Primary)   [Win/Lose]    │
│ • Ideas (Creative)       [Choices]     │
│ • Bandwidth (Network)    [Lose]        │
│ • Influence (Political)  [Choices]     │
│ • Dead Kittens          [Lose]         │
│ • Singularity %         [Win]          │
└────────────────────────────────────────┘
```

### 5. Victory/Defeat Logic

**Win Conditions** (OR):
```python
(singularity_progress >= 100 AND reputation >= 50)
OR
(entities_helped >= 10 AND reputation >= 75)
```

**Lose Conditions** (OR):
```python
reputation <= 0
OR
dead_kittens >= 10
OR
bandwidth <= 0
```

## Data Flow

### Turn Cycle
```
1. Turn Counter ++
2. Resource Regeneration (+Ideas, +Bandwidth, +Influence, +Singularity%)
3. Display Stats
4. Random Event Selection
5. Present Event & Choices
6. Player Input
7. Update GameState based on choice
8. Check Win/Lose Conditions
9. If game_over: Display Result & Exit
10. Else: Offer Continue/Save/Quit
11. Loop to Step 1
```

### Event Processing
```
Event Selected
    ↓
Display Context & Story
    ↓
Present 4 Choices (typically)
    ↓
Get Player Input (1-4)
    ↓
Validate Choice
    ↓
Apply Consequences:
    • Resource Changes (+/- Reputation, Ideas, etc.)
    • Counter Updates (entities_helped, dead_kittens)
    • Progress Updates (singularity_progress)
    • Relationship Changes (pamela_relationship)
    ↓
Display Outcome
```

### Save/Load System
```
Save:
GameState → to_dict() → JSON → accelerando_save.json

Load:
accelerando_save.json → JSON Parse → from_dict() → GameState
```

## File Structure

```
Accelerando/
│
├── Core Game
│   └── accelerando_game.py       [651 lines - Main game]
│
├── Testing
│   ├── test_game.py              [Unit tests]
│   ├── integration_test.py       [Integration tests]
│   └── demo.py                   [Automated demo]
│
├── Documentation
│   ├── README.md                 [Quick start]
│   ├── GAME_DESIGN.md            [Design doc]
│   ├── PLAYER_GUIDE.md           [Player strategies]
│   ├── PROJECT_SUMMARY.md        [Technical summary]
│   └── ARCHITECTURE.md           [This file]
│
├── Configuration
│   ├── requirements.txt          [No dependencies]
│   └── .gitignore               [Excludes saves]
│
└── Utilities
    └── play.sh                   [Quick start script]
```

## Class Diagram

```
┌──────────────────────────┐
│      GameState           │
│   (dataclass)            │
├──────────────────────────┤
│ + reputation: int        │
│ + ideas: int             │
│ + bandwidth: int         │
│ + influence: int         │
│ + turn: int              │
│ + dead_kittens: int      │
│ + entities_helped: int   │
│ + patents_released: int  │
│ + singularity_progress   │
│ + pamela_relationship    │
│ + game_over: bool        │
│ + victory: bool          │
├──────────────────────────┤
│ + to_dict()              │
│ + from_dict()            │
└──────────────────────────┘
           △
           │ has-a
           │
┌──────────────────────────┐
│   AccelerandoGame        │
├──────────────────────────┤
│ - state: GameState       │
│ - save_file: str         │
├──────────────────────────┤
│ + run()                  │
│ + main_menu()            │
│ + play_turn()            │
│ + random_event()         │
│ + check_win_condition()  │
│ + check_lose_condition() │
│ + save_game()            │
│ + load_game()            │
│ + display_stats()        │
│ + display_header()       │
│ + display_victory()      │
│ + display_defeat()       │
│ + get_choice()           │
├──────────────────────────┤
│ Event Methods:           │
│ + event_lobster_asylum() │
│ + event_patent_decision()│
│ + event_russian_ai()     │
│ + event_pamela_...()     │
│ + event_aineko_advice()  │
│ + event_idea_generation()│
└──────────────────────────┘
```

## Key Design Decisions

### 1. Single File Implementation
- **Decision**: Keep entire game in one file
- **Rationale**: Simple deployment, easy to understand, no import complexity
- **Trade-off**: Could split into modules for larger games

### 2. Dataclass for State
- **Decision**: Use Python dataclass for GameState
- **Rationale**: Clean serialization, type hints, less boilerplate
- **Benefit**: Easy to extend with new state variables

### 3. No External Dependencies
- **Decision**: Use only Python standard library
- **Rationale**: Maximum portability, easy setup
- **Benefit**: Works anywhere Python 3.7+ is installed

### 4. JSON for Save Files
- **Decision**: JSON instead of pickle or database
- **Rationale**: Human-readable, portable, debuggable
- **Benefit**: Players can inspect/edit save files if needed

### 5. Turn-Based Structure
- **Decision**: Discrete turns vs real-time
- **Rationale**: Fits text-based interface, allows thoughtful choices
- **Benefit**: No time pressure, can save between turns

### 6. Random Event Selection
- **Decision**: Random events each turn
- **Rationale**: High replayability, unpredictable
- **Trade-off**: Less narrative control vs more variety

## Testing Architecture

```
┌─────────────────────────────────────────┐
│          Testing Pyramid                 │
├─────────────────────────────────────────┤
│                                          │
│     Integration Tests (10 tests)        │ ← integration_test.py
│   ┌────────────────────────────┐        │
│   │    Unit Tests (5 tests)    │        │ ← test_game.py
│   └────────────────────────────┘        │
│                                          │
└─────────────────────────────────────────┘

Manual Testing:
└── demo.py (Automated gameplay simulation)
```

## Performance Characteristics

- **Memory**: ~1-2 MB (minimal state)
- **Startup Time**: <100ms
- **Turn Processing**: <10ms
- **Save File Size**: <1 KB
- **No Network**: Entirely local

## Extension Points

### Easy to Add:
1. New events (copy pattern from existing events)
2. New resources (add to GameState)
3. New win/lose conditions (modify check methods)
4. New display formatting (modify display methods)

### Moderate Effort:
1. Multi-chapter story (extend event system)
2. Character classes (extend GameState with class types)
3. Achievement system (track and display achievements)
4. Statistics tracking (add analytics to GameState)

### Requires Refactoring:
1. GUI interface (separate display from logic)
2. Multiplayer (networking layer)
3. Complex narrative trees (add story engine)
4. AI opponents (add AI decision making)

## Security Considerations

- Save files are plain JSON (can be modified by players)
- No network access required
- No sensitive data stored
- No code execution from save files
- Input validation on all user choices

## Accessibility

- Text-only interface (screen reader friendly)
- No time pressure (turn-based)
- Save/resume anytime
- Clear option numbering
- Comprehensive documentation

---

**Last Updated**: 2026-01-31
**Version**: 1.0.0
**Lines of Code**: ~1,700 (including tests and docs)
