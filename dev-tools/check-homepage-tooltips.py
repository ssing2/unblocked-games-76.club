#!/usr/bin/env python3
"""
Homepage Game Tooltip Coverage Verification Script.
Checks which games on index.html have tooltip descriptions and which are missing.
"""

import os
import re

def extract_homepage_games():
    """Extract all games from index.html."""
    
    if not os.path.exists('index.html'):
        print("❌ index.html not found!")
        return []
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all game links
        pattern = r'href="([^"]+)-unblocked\.html"'
        matches = re.findall(pattern, content)
        
        # Clean up game names
        games = []
        for match in matches:
            game_name = match.lower().strip()
            if game_name and game_name not in games:
                games.append(game_name)
        
        return games
        
    except Exception as e:
        print(f"❌ Error reading index.html: {e}")
        return []

def extract_described_games():
    """Extract games that have descriptions in game-descriptions.js."""
    
    js_file = 'assets/js/game-descriptions.js'
    if not os.path.exists(js_file):
        print(f"❌ {js_file} not found!")
        return set()
    
    try:
        with open(js_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract game keys from descriptions
        pattern = r"'([^']+)':\s*'"
        matches = re.findall(pattern, content)
        
        return set(matches)
        
    except Exception as e:
        print(f"❌ Error reading {js_file}: {e}")
        return set()

def main():
    """Main verification function."""
    
    print("🏠 Homepage Game Tooltip Coverage Check")
    print("=" * 50)
    
    # Extract games from homepage
    homepage_games = extract_homepage_games()
    
    if not homepage_games:
        print("❌ No games found on homepage!")
        return
    
    print(f"📊 Found {len(homepage_games)} games on homepage")
    
    # Extract described games
    described_games = extract_described_games()
    
    if not described_games:
        print("❌ No game descriptions found!")
        return
    
    print(f"📝 Found {len(described_games)} games with descriptions")
    
    # Calculate coverage
    homepage_set = set(homepage_games)
    covered_games = homepage_set & described_games
    missing_games = homepage_set - described_games
    
    coverage_percentage = (len(covered_games) / len(homepage_games)) * 100
    
    print("\n" + "=" * 50)
    print("COVERAGE ANALYSIS")
    print("=" * 50)
    
    print(f"✅ Games with tooltips: {len(covered_games)}")
    print(f"❌ Games missing tooltips: {len(missing_games)}")
    print(f"📈 Coverage percentage: {coverage_percentage:.1f}%")
    
    if missing_games:
        print(f"\n🔍 Games missing descriptions:")
        for i, game in enumerate(sorted(missing_games), 1):
            print(f"  {i:2d}. {game}")
            
        print(f"\n📝 Suggested additions to game-descriptions.js:")
        for game in sorted(list(missing_games))[:5]:
            game_title = game.replace('-', ' ').title()
            print(f"  '{game}': 'Experience {game_title} with [add description here]! [50-150 words explaining gameplay and features]',")
    
    if coverage_percentage >= 95:
        print("\n🎉 EXCELLENT: High tooltip coverage!")
    elif coverage_percentage >= 80:
        print("\n👍 GOOD: Adequate tooltip coverage")
    else:
        print("\n⚠️  NEEDS IMPROVEMENT: Low tooltip coverage")
    
    print(f"\n📋 Games with tooltips:")
    for i, game in enumerate(sorted(covered_games), 1):
        print(f"  {i:2d}. {game}")
    
    return coverage_percentage >= 90

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
