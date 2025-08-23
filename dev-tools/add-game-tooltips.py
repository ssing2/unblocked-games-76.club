#!/usr/bin/env python3
"""
Script to add game description tooltips to all game category pages.
This will enhance content quality and reduce the risk of being flagged as low-quality pages.
"""

import os
import re
import glob

def add_tooltip_script_to_file(file_path):
    """Add the game-descriptions.js script to a game category page."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the script is already included
        if 'game-descriptions.js' in content:
            print(f"✓ {os.path.basename(file_path)} already has tooltip script")
            return True
        
        # Find the script section and add our script before the closing body tag
        script_pattern = r'(\s*<script src="assets/js/search_v1_8\.js"></script>\s*</body>)'
        replacement = r'\1\n    <script src="assets/js/game-descriptions.js"></script>\2'
        
        # More flexible pattern to handle different script arrangements
        if '<script src="assets/js/search_v1_8.js"></script>' in content:
            new_content = content.replace(
                '<script src="assets/js/search_v1_8.js"></script>',
                '<script src="assets/js/search_v1_8.js"></script>\n    <script src="assets/js/game-descriptions.js"></script>'
            )
        else:
            # Fallback: add before closing body tag
            new_content = content.replace(
                '</body>',
                '    <script src="assets/js/game-descriptions.js"></script>\n</body>'
            )
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ Added tooltip script to {os.path.basename(file_path)}")
        return True
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all game category pages."""
    
    # Get all game category HTML files
    game_files = glob.glob('*-games.html')
    
    if not game_files:
        print("No game category files found in current directory.")
        return
    
    print(f"Found {len(game_files)} game category pages:")
    for file in sorted(game_files):
        print(f"  - {file}")
    
    print("\nProcessing files...")
    
    success_count = 0
    for file_path in sorted(game_files):
        if add_tooltip_script_to_file(file_path):
            success_count += 1
    
    print(f"\nCompleted! Successfully updated {success_count}/{len(game_files)} files.")
    
    if success_count == len(game_files):
        print("✓ All game category pages now have enhanced content with game descriptions!")
    else:
        print(f"⚠ {len(game_files) - success_count} files may need manual review.")

if __name__ == "__main__":
    main()
