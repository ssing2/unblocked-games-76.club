#!/usr/bin/env python3
"""
Script to analyze all game category pages and extract game names for description coverage.
This helps ensure we have descriptions for all games on the website.
"""

import os
import re
import glob
from collections import defaultdict

def extract_games_from_file(file_path):
    """Extract game names from a category page."""
    games = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all game links in the format: href="/game-name-unblocked.html"
        pattern = r'href="/([^"]+)-unblocked\.html"'
        matches = re.findall(pattern, content)
        
        for match in matches:
            # Clean up the game name
            game_name = match.lower().strip()
            if game_name and game_name not in games:
                games.append(game_name)
        
        return games
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def analyze_coverage():
    """Analyze game coverage across all category pages."""
    
    # Get all game category HTML files
    game_files = glob.glob('*-games.html')
    
    if not game_files:
        print("No game category files found in current directory.")
        return
    
    print(f"Analyzing {len(game_files)} game category pages...\n")
    
    all_games = set()
    category_games = defaultdict(list)
    
    for file_path in sorted(game_files):
        category = os.path.basename(file_path).replace('.html', '').replace('-games', '')
        games = extract_games_from_file(file_path)
        
        category_games[category] = games
        all_games.update(games)
        
        print(f"{category.title()} Games ({len(games)} games):")
        for game in sorted(games)[:10]:  # Show first 10 games
            print(f"  - {game}")
        if len(games) > 10:
            print(f"  ... and {len(games) - 10} more")
        print()
    
    print(f"Total unique games found: {len(all_games)}")
    print(f"Games per category average: {len(all_games) / len(game_files):.1f}")
    
    # Check which games might need descriptions
    common_games = [
        'basket-random', 'big-tower-tiny-square', 'boxing-random', 'crossy-road',
        'drift-boss', 'drive-mad', 'park-out', 'retro-bowl', 'rooftop-snipers',
        'roper', 'car-rush', 'crazy-cars', 'eggy-car', 'fire-truck', 'endless-truck',
        'basketball-legends-2020', 'basketball-line', 'basketball-stars', 'basket-champs',
        'doodle-jump', 'fireboy-and-watergirl', 'apple-shooter', 'awesome-tanks-2',
        'ballistic', 'ball-sort-puzzle', 'block-the-pig', 'checkers-legend',
        'adam-and-eve-6', 'adam-and-eve-7', 'age-of-war', 'clicker-heroes',
        'cookie-clicker-2', 'blumgi-slime', 'blumgi-rocket', 'bomb-it-6', 'bomb-it-7',
        'chicken-merge', 'dinosaurs-merge-master', 'bottle-flip', 'bouncy-woods',
        'bubble-pop-adventures', 'bus-parking-3d', 'cubefield', 'dead-again', 'e-scooter'
    ]
    
    covered_games = set(all_games) & set(common_games)
    missing_games = set(all_games) - set(common_games)
    
    print(f"\nGames with descriptions: {len(covered_games)}")
    print(f"Games potentially missing descriptions: {len(missing_games)}")
    
    if missing_games:
        print("\nGames that might need descriptions (first 20):")
        for game in sorted(list(missing_games))[:20]:
            print(f"  - {game}")
        if len(missing_games) > 20:
            print(f"  ... and {len(missing_games) - 20} more")
    
    # Generate a template for adding new descriptions
    print("\n" + "="*60)
    print("SUGGESTED ADDITIONS TO game-descriptions.js:")
    print("="*60)
    
    for game in sorted(list(missing_games))[:10]:
        game_title = game.replace('-', ' ').title()
        print(f"  '{game}': 'Experience {game_title} with [description needed]! [Add 50-150 word description here]',")
    
    return all_games, category_games

def main():
    """Main function."""
    print("Game Coverage Analysis Tool")
    print("="*40)
    
    all_games, category_games = analyze_coverage()
    
    print(f"\nAnalysis complete! Found {len(all_games)} unique games across {len(category_games)} categories.")
    print("\nThis data helps ensure comprehensive game descriptions for better SEO content quality.")

if __name__ == "__main__":
    main()
