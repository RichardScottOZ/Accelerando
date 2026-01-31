#!/bin/bash
# Quick start script for Accelerando game

echo "=================================================="
echo "  ACCELERANDO: LOBSTERS - Quick Start"
echo "=================================================="
echo ""

# Check Python version
python3 --version > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error: Python 3 not found. Please install Python 3.7 or higher."
    exit 1
fi

echo "Python found. Starting game..."
echo ""

# Run the game
python3 accelerando_game.py
