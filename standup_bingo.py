#!/usr/bin/env python3
"""
Standup Bingo Generator - Because "blocked by dependencies" deserves a prize.
"""

import random
import sys
from typing import List

# The sacred texts of standup clichés
PHRASES = [
    "Blocked by dependencies",
    "Syncing with the team",
    "It's in code review",
    "Working as expected",
    "Need to refactor",
    "Looking into it",
    "Almost done",
    "Technical debt",
    "Edge case handling",
    "Waiting on QA",
    "Following up",
    "Investigating",
    "Will update later",
    "Scope changed",
    "Legacy code",
    "Environment issues",
    "Documentation",
    "Meeting overload",
    "Priorities shifted",
    "Learning the codebase",
    "Async communication",
    "Backend/frontend mismatch",
    "Third-party API",
    "Browser compatibility",
    "It worked on my machine"
]

def generate_card(size: int = 5) -> List[List[str]]:
    """
    Create a bingo card of corporate platitudes.
    Free space: "Yesterday I... Today I will..."
    """
    if size < 3:
        size = 3  # Even tiny standups need structure
    
    # Shuffle the sacred phrases
    shuffled = random.sample(PHRASES, size*size - 1)
    
    card = []
    idx = 0
    for i in range(size):
        row = []
        for j in range(size):
            if i == size//2 and j == size//2:
                row.append("FREE: Yesterday/Today")  # The eternal standup formula
            else:
                row.append(shuffled[idx])
                idx += 1
        card.append(row)
    
    return card

def print_card(card: List[List[str]]) -> None:
    """Print with the elegance of a Jira ticket."""
    size = len(card)
    col_width = max(len(phrase) for row in card for phrase in row) + 2
    
    print("\n" + "=" * (col_width * size + 1))
    print(f"STANDUP BINGO ({size}x{size}) - First to 5 excuses wins!")
    print("=" * (col_width * size + 1))
    
    for row in card:
        print("|" + "|".join(phrase.center(col_width) for phrase in row) + "|")
        print("-" * (col_width * size + 1))
    
    print("\nRules: Mark a square when someone says the phrase. BINGO = productivity!")

def main() -> None:
    """The main event - more exciting than most standups."""
    try:
        size = int(sys.argv[1]) if len(sys.argv) > 1 else 5
        if size > 8:
            print("Warning: Card larger than our sprint planning attention span")
            size = 8
    except ValueError:
        size = 5
    
    card = generate_card(size)
    print_card(card)

if __name__ == "__main__":
    main()
