#!/usr/bin/env python3
"""
Final deployment verification script for game tooltip enhancements.
Checks all category pages for proper tooltip integration and reports status.
"""

import os
import re
import glob
import json

def verify_tooltip_integration():
    """Verify that all game category pages have tooltip integration."""
    
    results = {
        'total_pages': 0,
        'pages_with_tooltips': 0,
        'pages_without_tooltips': 0,
        'games_with_descriptions': 0,
        'games_without_descriptions': 0,
        'missing_pages': [],
        'missing_descriptions': [],
        'success': True
    }
    
    # Check if game-descriptions.js exists
    js_file = 'assets/js/game-descriptions.js'
    if not os.path.exists(js_file):
        print("❌ Critical: game-descriptions.js not found!")
        results['success'] = False
        return results
    
    # Extract game descriptions from JS file
    try:
        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        # Extract game keys from descriptions
        desc_pattern = r"'([^']+)':\s*'"
        described_games = set(re.findall(desc_pattern, js_content))
        results['games_with_descriptions'] = len(described_games)
        
    except Exception as e:
        print(f"❌ Error reading {js_file}: {e}")
        results['success'] = False
        return results
    
    # Get all game category HTML files
    game_files = glob.glob('*-games.html')
    results['total_pages'] = len(game_files)
    
    print(f"Verifying {len(game_files)} game category pages...")
    print("=" * 60)
    
    all_games_found = set()
    
    for file_path in sorted(game_files):
        category = os.path.basename(file_path).replace('.html', '').replace('-games', '')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if tooltip script is included
            has_tooltip_script = 'game-descriptions.js' in content
            
            if has_tooltip_script:
                results['pages_with_tooltips'] += 1
                status = "✅ Integrated"
            else:
                results['pages_without_tooltips'] += 1
                results['missing_pages'].append(file_path)
                status = "❌ Missing Script"
            
            # Extract games from this page
            game_pattern = r'href="/([^"]+)-unblocked\.html"'
            page_games = set(re.findall(game_pattern, content))
            all_games_found.update(page_games)
            
            # Count games with descriptions on this page
            games_with_desc = len(page_games & described_games)
            games_without_desc = len(page_games - described_games)
            
            print(f"{category.title():<15} | {status:<15} | {len(page_games):>3} games | {games_with_desc:>3} described")
            
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
            results['success'] = False
    
    # Calculate final statistics
    results['games_without_descriptions'] = len(all_games_found - described_games)
    results['missing_descriptions'] = sorted(list(all_games_found - described_games))
    
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"📊 Total category pages: {results['total_pages']}")
    print(f"✅ Pages with tooltips: {results['pages_with_tooltips']}")
    print(f"❌ Pages missing tooltips: {results['pages_without_tooltips']}")
    print(f"🎮 Total unique games: {len(all_games_found)}")
    print(f"📝 Games with descriptions: {results['games_with_descriptions']}")
    print(f"❓ Games without descriptions: {results['games_without_descriptions']}")
    
    # Success criteria
    if results['pages_without_tooltips'] == 0:
        print("\n🎉 SUCCESS: All category pages have tooltip integration!")
    else:
        print(f"\n⚠️  WARNING: {results['pages_without_tooltips']} pages need tooltip integration:")
        for page in results['missing_pages']:
            print(f"   - {page}")
    
    coverage_percentage = (results['games_with_descriptions'] / len(all_games_found)) * 100 if all_games_found else 0
    print(f"\n📈 Description coverage: {coverage_percentage:.1f}% ({results['games_with_descriptions']}/{len(all_games_found)})")
    
    if coverage_percentage >= 95:
        print("🎯 EXCELLENT: High description coverage!")
    elif coverage_percentage >= 80:
        print("👍 GOOD: Adequate description coverage")
    else:
        print("📝 Recommendation: Consider adding more game descriptions")
    
    if results['missing_descriptions'] and len(results['missing_descriptions']) <= 10:
        print(f"\nGames without descriptions:")
        for game in results['missing_descriptions'][:10]:
            print(f"   - {game}")
    
    return results

def check_file_structure():
    """Check that all necessary files are in place."""
    
    required_files = [
        'assets/js/game-descriptions.js',
        'test-tooltips.html',
        'dev-tools/CONTENT-ENHANCEMENT-REPORT.md'
    ]
    
    print("\n" + "=" * 60)
    print("FILE STRUCTURE CHECK")
    print("=" * 60)
    
    all_present = True
    for file_path in required_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✅ {file_path:<40} ({size:,} bytes)")
        else:
            print(f"❌ {file_path:<40} (MISSING)")
            all_present = False
    
    return all_present

def main():
    """Main verification function."""
    
    print("🚀 Game Tooltip Enhancement Verification")
    print("=" * 60)
    print("Checking deployment status and coverage...\n")
    
    # Verify tooltip integration
    tooltip_results = verify_tooltip_integration()
    
    # Check file structure
    file_structure_ok = check_file_structure()
    
    # Final assessment
    print("\n" + "=" * 60)
    print("FINAL ASSESSMENT")
    print("=" * 60)
    
    if (tooltip_results['success'] and 
        tooltip_results['pages_without_tooltips'] == 0 and 
        file_structure_ok):
        print("🎉 DEPLOYMENT SUCCESSFUL!")
        print("✅ All game category pages have enhanced content")
        print("✅ Tooltip system fully operational")
        print("✅ All required files present")
        print("\n💡 Next steps:")
        print("   1. Test tooltips in browser (use test-tooltips.html)")
        print("   2. Monitor page performance and user engagement")
        print("   3. Consider adding more game descriptions if needed")
    else:
        print("⚠️  DEPLOYMENT NEEDS ATTENTION")
        if not tooltip_results['success']:
            print("❌ Tooltip integration has issues")
        if tooltip_results['pages_without_tooltips'] > 0:
            print(f"❌ {tooltip_results['pages_without_tooltips']} pages missing tooltips")
        if not file_structure_ok:
            print("❌ Required files missing")
    
    return tooltip_results['success'] and file_structure_ok

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
