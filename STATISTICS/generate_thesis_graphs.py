#!/usr/bin/env python3
"""
Generate visual graphs for thesis statistics
"""

import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from collections import defaultdict
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

def load_stats():
    """Load statistics from JSON file"""
    with open('thesis_stats.json', 'r') as f:
        return json.load(f)

def plot_commits_over_time(stats):
    """Plot commits over time"""
    dates = []
    commits = []
    
    for date_str, count in sorted(stats['commits_by_date'].items()):
        dates.append(datetime.strptime(date_str, '%Y-%m-%d'))
        commits.append(count)
    
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.bar(dates, commits, width=1.0, color='steelblue', alpha=0.7, edgecolor='navy')
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Commits', fontsize=12, fontweight='bold')
    ax.set_title('Commit Activity Over Time', fontsize=14, fontweight='bold')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('graphs/commits_over_time.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: graphs/commits_over_time.png")

def plot_lines_over_time(stats):
    """Plot lines added/deleted over time"""
    dates = []
    added = []
    deleted = []
    net = []
    
    for date_str in sorted(stats['lines_by_date'].keys()):
        data = stats['lines_by_date'][date_str]
        dates.append(datetime.strptime(date_str, '%Y-%m-%d'))
        added.append(data['added'])
        deleted.append(data['deleted'])
        net.append(data['net'])
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Lines added/deleted
    ax1.bar(dates, added, width=1.0, label='Added', color='green', alpha=0.6)
    ax1.bar(dates, [-d for d in deleted], width=1.0, label='Deleted', color='red', alpha=0.6)
    ax1.set_ylabel('Lines', fontsize=12, fontweight='bold')
    ax1.set_title('Lines Added and Deleted Over Time', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)
    
    # Net lines (cumulative)
    cumulative_net = np.cumsum(net)
    ax2.plot(dates, cumulative_net, linewidth=2, color='steelblue', marker='o', markersize=3)
    ax2.fill_between(dates, cumulative_net, alpha=0.3, color='steelblue')
    ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Cumulative Net Lines', fontsize=12, fontweight='bold')
    ax2.set_title('Cumulative Net Lines Over Time', fontsize=14, fontweight='bold')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graphs/lines_over_time.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: graphs/lines_over_time.png")

def plot_monthly_activity(stats):
    """Plot monthly activity"""
    months = []
    commits = []
    lines_added = []
    lines_net = []
    
    for month_str in sorted(stats['commits_by_month'].keys()):
        months.append(month_str)
        commits.append(stats['commits_by_month'][month_str])
        lines_added.append(stats['lines_by_month'][month_str]['added'])
        lines_net.append(stats['lines_by_month'][month_str]['net'])
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Commits per month
    x = np.arange(len(months))
    ax1.bar(x, commits, color='steelblue', alpha=0.7, edgecolor='navy')
    ax1.set_ylabel('Number of Commits', fontsize=12, fontweight='bold')
    ax1.set_title('Monthly Commit Activity', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(months, rotation=45, ha='right')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Lines per month
    ax2.bar(x, lines_added, color='green', alpha=0.6, label='Lines Added')
    ax2.plot(x, lines_net, color='red', linewidth=2, marker='o', label='Net Lines', markersize=6)
    ax2.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Lines', fontsize=12, fontweight='bold')
    ax2.set_title('Monthly Line Changes', fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(months, rotation=45, ha='right')
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('graphs/monthly_activity.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: graphs/monthly_activity.png")

def plot_work_patterns(stats):
    """Plot work patterns (hour and weekday)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Hour distribution
    hours = list(range(24))
    hour_commits = [stats['commits_by_hour'].get(str(h), 0) for h in hours]
    
    ax1.bar(hours, hour_commits, color='steelblue', alpha=0.7, edgecolor='navy')
    ax1.set_xlabel('Hour of Day', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Commits', fontsize=12, fontweight='bold')
    ax1.set_title('Commit Activity by Hour of Day', fontsize=14, fontweight='bold')
    ax1.set_xticks(hours)
    ax1.set_xticklabels([f'{h:02d}:00' for h in hours], rotation=45, ha='right')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Weekday distribution
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_commits = [stats['commits_by_weekday'].get(day, 0) for day in weekdays]
    
    colors = ['#1f77b4' if i < 5 else '#ff7f0e' for i in range(7)]  # Blue for weekdays, orange for weekend
    ax2.barh(weekdays, weekday_commits, color=colors, alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Number of Commits', fontsize=12, fontweight='bold')
    ax2.set_title('Commit Activity by Day of Week', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('graphs/work_patterns.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: graphs/work_patterns.png")

def plot_thesis_vs_colloquium(stats):
    """Plot THESIS vs COLLOQUIUM comparison"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # Commits comparison
    categories = ['THESIS', 'COLLOQUIUM']
    commits = [stats['thesis_commits'], stats['colloquium_commits']]
    colors = ['#2E86AB', '#A23B72']
    
    ax1.bar(categories, commits, color=colors, alpha=0.7, edgecolor='black')
    ax1.set_ylabel('Number of Commits', fontsize=12, fontweight='bold')
    ax1.set_title('Commits: THESIS vs COLLOQUIUM', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Lines added comparison
    lines_added = [stats['thesis_lines']['added'], stats['colloquium_lines']['added']]
    ax2.bar(categories, lines_added, color=colors, alpha=0.7, edgecolor='black')
    ax2.set_ylabel('Lines Added', fontsize=12, fontweight='bold')
    ax2.set_title('Lines Added: THESIS vs COLLOQUIUM', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Net lines comparison
    net_lines = [stats['thesis_lines']['net'], stats['colloquium_lines']['net']]
    ax3.bar(categories, net_lines, color=colors, alpha=0.7, edgecolor='black')
    ax3.set_ylabel('Net Lines', fontsize=12, fontweight='bold')
    ax3.set_title('Net Lines: THESIS vs COLLOQUIUM', fontsize=13, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Pie chart of total contribution
    sizes = [stats['thesis_lines']['net'], stats['colloquium_lines']['net']]
    ax4.pie(sizes, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90)
    ax4.set_title('Proportion of Net Lines', fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graphs/thesis_vs_colloquium.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: graphs/thesis_vs_colloquium.png")

def plot_file_types(stats):
    """Plot file type distribution"""
    # Get top 10 file types by commits
    sorted_types = sorted(stats['file_types'].items(), 
                         key=lambda x: x[1]['commits'], 
                         reverse=True)[:10]
    
    extensions = [f".{ext}" for ext, _ in sorted_types]
    commits = [data['commits'] for _, data in sorted_types]
    added = [data['added'] for _, data in sorted_types]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Commits by file type
    ax1.barh(extensions, commits, color='steelblue', alpha=0.7, edgecolor='navy')
    ax1.set_xlabel('Number of Commits', fontsize=12, fontweight='bold')
    ax1.set_title('Top 10 File Types by Commits', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='x')
    
    # Lines added by file type
    ax2.barh(extensions, added, color='green', alpha=0.7, edgecolor='darkgreen')
    ax2.set_xlabel('Lines Added', fontsize=12, fontweight='bold')
    ax2.set_title('Top 10 File Types by Lines Added', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('graphs/file_types.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: graphs/file_types.png")

def create_summary_dashboard(stats):
    """Create a summary dashboard with key metrics"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # Title
    fig.suptitle('Thesis Work Statistics Dashboard', fontsize=20, fontweight='bold', y=0.98)
    
    # Key metrics
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.text(0.5, 0.5, f"{stats['total_commits']}", 
             ha='center', va='center', fontsize=48, fontweight='bold', color='steelblue')
    ax1.text(0.5, 0.15, 'Total Commits', ha='center', va='center', fontsize=14)
    ax1.axis('off')
    
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.text(0.5, 0.5, f"{stats['total_lines_net']:,}", 
             ha='center', va='center', fontsize=48, fontweight='bold', color='green')
    ax2.text(0.5, 0.15, 'Net Lines', ha='center', va='center', fontsize=14)
    ax2.axis('off')
    
    ax3 = fig.add_subplot(gs[0, 2])
    duration = (datetime.fromisoformat(stats['last_commit']) - 
                datetime.fromisoformat(stats['first_commit'])).days
    ax3.text(0.5, 0.5, f"{duration}", 
             ha='center', va='center', fontsize=48, fontweight='bold', color='purple')
    ax3.text(0.5, 0.15, 'Days Duration', ha='center', va='center', fontsize=14)
    ax3.axis('off')
    
    # Commits over time (mini)
    ax4 = fig.add_subplot(gs[1, :])
    dates = [datetime.strptime(d, '%Y-%m-%d') for d in sorted(stats['commits_by_date'].keys())]
    commits = [stats['commits_by_date'][d] for d in sorted(stats['commits_by_date'].keys())]
    ax4.plot(dates, commits, linewidth=2, color='steelblue', marker='o', markersize=4)
    ax4.fill_between(dates, commits, alpha=0.3, color='steelblue')
    ax4.set_title('Commit Timeline', fontsize=14, fontweight='bold')
    ax4.set_ylabel('Commits')
    ax4.grid(True, alpha=0.3)
    
    # Work patterns
    ax5 = fig.add_subplot(gs[2, 0])
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    weekday_full = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_commits = [stats['commits_by_weekday'].get(day, 0) for day in weekday_full]
    colors = ['#1f77b4' if i < 5 else '#ff7f0e' for i in range(7)]
    ax5.bar(weekdays, weekday_commits, color=colors, alpha=0.7)
    ax5.set_title('Commits by Weekday', fontsize=12, fontweight='bold')
    ax5.set_ylabel('Commits')
    ax5.tick_params(axis='x', rotation=45)
    
    # THESIS vs COLLOQUIUM
    ax6 = fig.add_subplot(gs[2, 1])
    categories = ['THESIS', 'COLLOQ']
    values = [stats['thesis_commits'], stats['colloquium_commits']]
    ax6.bar(categories, values, color=['#2E86AB', '#A23B72'], alpha=0.7)
    ax6.set_title('Commits by Project', fontsize=12, fontweight='bold')
    ax6.set_ylabel('Commits')
    
    # Longest streak
    ax7 = fig.add_subplot(gs[2, 2])
    ax7.text(0.5, 0.5, f"{stats['longest_streak']}", 
             ha='center', va='center', fontsize=36, fontweight='bold', color='orange')
    ax7.text(0.5, 0.15, 'Longest Streak (days)', ha='center', va='center', fontsize=12)
    ax7.axis('off')
    
    plt.savefig('graphs/summary_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: graphs/summary_dashboard.png")

def main():
    import os
    
    # Create graphs directory
    os.makedirs('graphs', exist_ok=True)
    
    print("Loading statistics...")
    stats = load_stats()
    
    print("\nGenerating graphs...")
    print("-" * 60)
    
    plot_commits_over_time(stats)
    plot_lines_over_time(stats)
    plot_monthly_activity(stats)
    plot_work_patterns(stats)
    plot_thesis_vs_colloquium(stats)
    plot_file_types(stats)
    create_summary_dashboard(stats)
    
    print("-" * 60)
    print("\n✓ All graphs generated successfully in 'graphs/' directory")
    print("\nGenerated files:")
    print("  - graphs/commits_over_time.png")
    print("  - graphs/lines_over_time.png")
    print("  - graphs/monthly_activity.png")
    print("  - graphs/work_patterns.png")
    print("  - graphs/thesis_vs_colloquium.png")
    print("  - graphs/file_types.png")
    print("  - graphs/summary_dashboard.png")

if __name__ == '__main__':
    main()

# Made with Bob
