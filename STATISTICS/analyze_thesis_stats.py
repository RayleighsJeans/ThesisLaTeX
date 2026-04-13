#!/usr/bin/env python3
"""
Thesis Statistics Analyzer
Analyzes git history for THESIS/ and COLLOQUIUM/ directories to generate
comprehensive statistics and visualizations of work progression.
"""

import subprocess
import re
from datetime import datetime
from collections import defaultdict, Counter
import json

def run_git_command(cmd):
    """Execute git command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def parse_git_log():
    """Parse git log with numstat for THESIS and COLLOQUIUM"""
    cmd = 'git log --all --pretty=format:"%H|%ai|%an|%ae|%s" --numstat -- THESIS/ COLLOQUIUM/'
    output = run_git_command(cmd)
    
    commits = []
    current_commit = None
    
    for line in output.split('\n'):
        if '|' in line and not line.startswith('\t'):
            # Commit line
            if current_commit:
                commits.append(current_commit)
            
            parts = line.split('|')
            if len(parts) >= 5:
                current_commit = {
                    'hash': parts[0],
                    'date': datetime.strptime(parts[1].strip()[:19], '%Y-%m-%d %H:%M:%S'),
                    'author': parts[2],
                    'email': parts[3],
                    'message': parts[4],
                    'files': []
                }
        elif line.startswith('\t') or (line and current_commit):
            # File change line
            parts = line.split('\t')
            if len(parts) >= 3:
                added = parts[0].strip()
                deleted = parts[1].strip()
                filepath = parts[2].strip()
                
                # Skip binary files
                if added == '-' and deleted == '-':
                    continue
                    
                current_commit['files'].append({
                    'path': filepath,
                    'added': int(added) if added != '-' else 0,
                    'deleted': int(deleted) if deleted != '-' else 0
                })
    
    if current_commit:
        commits.append(current_commit)
    
    return commits

def analyze_commits(commits):
    """Analyze commits and generate statistics"""
    stats = {
        'total_commits': len(commits),
        'thesis_commits': 0,
        'colloquium_commits': 0,
        'total_lines_added': 0,
        'total_lines_deleted': 0,
        'total_lines_net': 0,
        'commits_by_date': defaultdict(int),
        'lines_by_date': defaultdict(lambda: {'added': 0, 'deleted': 0, 'net': 0}),
        'commits_by_month': defaultdict(int),
        'lines_by_month': defaultdict(lambda: {'added': 0, 'deleted': 0, 'net': 0}),
        'commits_by_hour': defaultdict(int),
        'commits_by_weekday': defaultdict(int),
        'file_types': defaultdict(lambda: {'commits': 0, 'added': 0, 'deleted': 0}),
        'most_edited_files': defaultdict(lambda: {'commits': 0, 'added': 0, 'deleted': 0}),
        'commit_messages': [],
        'first_commit': None,
        'last_commit': None,
        'longest_streak': 0,
        'current_streak': 0,
        'thesis_lines': {'added': 0, 'deleted': 0, 'net': 0},
        'colloquium_lines': {'added': 0, 'deleted': 0, 'net': 0},
    }
    
    if not commits:
        return stats
    
    # Sort commits by date
    commits.sort(key=lambda x: x['date'])
    stats['first_commit'] = commits[0]['date']
    stats['last_commit'] = commits[-1]['date']
    
    # Track streaks
    dates_with_commits = set()
    
    for commit in commits:
        date = commit['date']
        date_str = date.strftime('%Y-%m-%d')
        month_str = date.strftime('%Y-%m')
        hour = date.hour
        weekday = date.strftime('%A')
        
        # Count commits
        stats['commits_by_date'][date_str] += 1
        stats['commits_by_month'][month_str] += 1
        stats['commits_by_hour'][hour] += 1
        stats['commits_by_weekday'][weekday] += 1
        dates_with_commits.add(date.date())
        
        # Store commit message
        stats['commit_messages'].append({
            'date': date_str,
            'message': commit['message']
        })
        
        # Analyze files
        is_thesis = False
        is_colloquium = False
        
        for file_info in commit['files']:
            path = file_info['path']
            added = file_info['added']
            deleted = file_info['deleted']
            net = added - deleted
            
            # Track by directory
            if path.startswith('THESIS/'):
                is_thesis = True
                stats['thesis_lines']['added'] += added
                stats['thesis_lines']['deleted'] += deleted
                stats['thesis_lines']['net'] += net
            elif path.startswith('COLLOQUIUM/'):
                is_colloquium = True
                stats['colloquium_lines']['added'] += added
                stats['colloquium_lines']['deleted'] += deleted
                stats['colloquium_lines']['net'] += net
            
            # Total lines
            stats['total_lines_added'] += added
            stats['total_lines_deleted'] += deleted
            stats['total_lines_net'] += net
            
            # By date
            stats['lines_by_date'][date_str]['added'] += added
            stats['lines_by_date'][date_str]['deleted'] += deleted
            stats['lines_by_date'][date_str]['net'] += net
            
            # By month
            stats['lines_by_month'][month_str]['added'] += added
            stats['lines_by_month'][month_str]['deleted'] += deleted
            stats['lines_by_month'][month_str]['net'] += net
            
            # File type
            ext = path.split('.')[-1] if '.' in path else 'no_ext'
            stats['file_types'][ext]['commits'] += 1
            stats['file_types'][ext]['added'] += added
            stats['file_types'][ext]['deleted'] += deleted
            
            # Most edited files
            stats['most_edited_files'][path]['commits'] += 1
            stats['most_edited_files'][path]['added'] += added
            stats['most_edited_files'][path]['deleted'] += deleted
        
        if is_thesis:
            stats['thesis_commits'] += 1
        if is_colloquium:
            stats['colloquium_commits'] += 1
    
    # Calculate streaks
    sorted_dates = sorted(dates_with_commits)
    if sorted_dates:
        current_streak = 1
        max_streak = 1
        
        for i in range(1, len(sorted_dates)):
            days_diff = (sorted_dates[i] - sorted_dates[i-1]).days
            if days_diff == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
        
        stats['longest_streak'] = max_streak
        
        # Check if current streak is ongoing
        from datetime import date
        if sorted_dates[-1] == date.today() or (date.today() - sorted_dates[-1]).days == 1:
            stats['current_streak'] = current_streak
    
    return stats

def generate_markdown_report(stats):
    """Generate comprehensive markdown report"""
    
    report = f"""# Thesis Work Statistics Report

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview

### Timeline
- **First Commit**: {stats['first_commit'].strftime('%Y-%m-%d %H:%M:%S') if stats['first_commit'] else 'N/A'}
- **Last Commit**: {stats['last_commit'].strftime('%Y-%m-%d %H:%M:%S') if stats['last_commit'] else 'N/A'}
- **Duration**: {(stats['last_commit'] - stats['first_commit']).days if stats['first_commit'] and stats['last_commit'] else 0} days

### Commit Statistics
- **Total Commits**: {stats['total_commits']:,}
- **THESIS Commits**: {stats['thesis_commits']:,}
- **COLLOQUIUM Commits**: {stats['colloquium_commits']:,}
- **Longest Streak**: {stats['longest_streak']} days
- **Current Streak**: {stats['current_streak']} days

### Line Statistics

#### Overall
- **Lines Added**: {stats['total_lines_added']:,}
- **Lines Deleted**: {stats['total_lines_deleted']:,}
- **Net Lines**: {stats['total_lines_net']:,}

#### THESIS
- **Lines Added**: {stats['thesis_lines']['added']:,}
- **Lines Deleted**: {stats['thesis_lines']['deleted']:,}
- **Net Lines**: {stats['thesis_lines']['net']:,}

#### COLLOQUIUM
- **Lines Added**: {stats['colloquium_lines']['added']:,}
- **Lines Deleted**: {stats['colloquium_lines']['deleted']:,}
- **Net Lines**: {stats['colloquium_lines']['net']:,}

## Work Patterns

### Commits by Hour of Day
"""
    
    # Hour distribution
    for hour in sorted(stats['commits_by_hour'].keys()):
        count = stats['commits_by_hour'][hour]
        bar = '█' * (count // 5) if count > 0 else ''
        report += f"\n{hour:02d}:00 | {bar} {count}"
    
    report += "\n\n### Commits by Day of Week\n"
    
    # Weekday distribution
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    max_weekday_commits = max(stats['commits_by_weekday'].values()) if stats['commits_by_weekday'] else 1
    
    for day in weekday_order:
        count = stats['commits_by_weekday'].get(day, 0)
        bar = '█' * int((count / max_weekday_commits) * 50) if count > 0 else ''
        report += f"\n{day:10s} | {bar} {count}"
    
    report += "\n\n## File Type Analysis\n\n"
    report += "| Extension | Commits | Lines Added | Lines Deleted | Net Lines |\n"
    report += "|-----------|---------|-------------|---------------|----------|\n"
    
    # Sort by commits
    sorted_types = sorted(stats['file_types'].items(), key=lambda x: x[1]['commits'], reverse=True)[:15]
    for ext, data in sorted_types:
        net = data['added'] - data['deleted']
        report += f"| .{ext} | {data['commits']:,} | {data['added']:,} | {data['deleted']:,} | {net:,} |\n"
    
    report += "\n## Most Edited Files\n\n"
    report += "| File | Commits | Lines Added | Lines Deleted | Net Lines |\n"
    report += "|------|---------|-------------|---------------|----------|\n"
    
    # Sort by total changes
    sorted_files = sorted(stats['most_edited_files'].items(), 
                         key=lambda x: x[1]['added'] + x[1]['deleted'], 
                         reverse=True)[:20]
    for filepath, data in sorted_files:
        net = data['added'] - data['deleted']
        # Truncate long paths
        display_path = filepath if len(filepath) < 50 else '...' + filepath[-47:]
        report += f"| `{display_path}` | {data['commits']} | {data['added']:,} | {data['deleted']:,} | {net:,} |\n"
    
    report += "\n## Monthly Activity\n\n"
    report += "| Month | Commits | Lines Added | Lines Deleted | Net Lines |\n"
    report += "|-------|---------|-------------|---------------|----------|\n"
    
    for month in sorted(stats['lines_by_month'].keys()):
        commits = stats['commits_by_month'][month]
        lines = stats['lines_by_month'][month]
        report += f"| {month} | {commits:,} | {lines['added']:,} | {lines['deleted']:,} | {lines['net']:,} |\n"
    
    report += "\n## Recent Commit Messages (Last 20)\n\n"
    
    for msg_info in stats['commit_messages'][-20:]:
        report += f"- **{msg_info['date']}**: {msg_info['message']}\n"
    
    report += "\n---\n\n"
    report += "*This report was automatically generated from git history analysis.*\n"
    
    return report

def main():
    print("Analyzing thesis git history...")
    print("This may take a moment...")
    
    commits = parse_git_log()
    print(f"Found {len(commits)} commits")
    
    print("Generating statistics...")
    stats = analyze_commits(commits)
    
    print("Creating markdown report...")
    report = generate_markdown_report(stats)
    
    # Write report
    with open('THESIS_STATISTICS.md', 'w') as f:
        f.write(report)
    
    print("\n✓ Report generated: THESIS_STATISTICS.md")
    
    # Also save raw stats as JSON for potential further analysis
    # Convert datetime objects to strings for JSON serialization
    stats_json = stats.copy()
    if stats_json['first_commit']:
        stats_json['first_commit'] = stats_json['first_commit'].isoformat()
    if stats_json['last_commit']:
        stats_json['last_commit'] = stats_json['last_commit'].isoformat()
    
    # Convert defaultdicts to regular dicts
    stats_json['commits_by_date'] = dict(stats_json['commits_by_date'])
    stats_json['lines_by_date'] = {k: dict(v) for k, v in stats_json['lines_by_date'].items()}
    stats_json['commits_by_month'] = dict(stats_json['commits_by_month'])
    stats_json['lines_by_month'] = {k: dict(v) for k, v in stats_json['lines_by_month'].items()}
    stats_json['commits_by_hour'] = dict(stats_json['commits_by_hour'])
    stats_json['commits_by_weekday'] = dict(stats_json['commits_by_weekday'])
    stats_json['file_types'] = {k: dict(v) for k, v in stats_json['file_types'].items()}
    stats_json['most_edited_files'] = {k: dict(v) for k, v in stats_json['most_edited_files'].items()}
    
    with open('thesis_stats.json', 'w') as f:
        json.dump(stats_json, f, indent=2)
    
    print("✓ Raw data saved: thesis_stats.json")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total Commits: {stats['total_commits']:,}")
    print(f"Total Lines Added: {stats['total_lines_added']:,}")
    print(f"Total Lines Deleted: {stats['total_lines_deleted']:,}")
    print(f"Net Lines: {stats['total_lines_net']:,}")
    print(f"Longest Streak: {stats['longest_streak']} days")
    print("="*60)

if __name__ == '__main__':
    main()

# Made with Bob
