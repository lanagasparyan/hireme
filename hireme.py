import os
from datetime import datetime, timedelta
import subprocess

# Define your "PLEASE HIRE ME" pattern
# 1 = make commits, 0 = skip
# Each inner list is a week (7 days: Sun, Mon, Tue, Wed, Thu, Fri, Sat)

pattern = [
    # Week 1 - P
    [1,1,1,1,1,0,0],
    [1,0,0,0,1,0,0],
    [1,1,1,1,1,0,0],
    [1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # L
    [1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # E
    [1,1,1,1,1,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,0,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # A
    [0,1,1,1,0,0,0],
    [1,0,0,0,1,0,0],
    [1,1,1,1,1,0,0],
    [1,0,0,0,1,0,0],
    [1,0,0,0,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # S
    [0,1,1,1,1,0,0],
    [1,0,0,0,0,0,0],
    [0,1,1,1,0,0,0],
    [0,0,0,0,1,0,0],
    [1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # E
    [1,1,1,1,1,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,0,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    [0,0,0,0,0,0,0],  # Space
    
    # H
    [1,0,0,0,1,0,0],
    [1,0,0,0,1,0,0],
    [1,1,1,1,1,0,0],
    [1,0,0,0,1,0,0],
    [1,0,0,0,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # I
    [1,1,1,1,1,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0],
    [1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # R
    [1,1,1,1,0,0,0],
    [1,0,0,0,1,0,0],
    [1,1,1,1,0,0,0],
    [1,0,1,0,0,0,0],
    [1,0,0,1,0,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # E
    [1,1,1,1,1,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,0,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    [0,0,0,0,0,0,0],  # Space
    
    # M
    [1,0,0,0,1,0,0],
    [1,1,0,1,1,0,0],
    [1,0,1,0,1,0,0],
    [1,0,0,0,1,0,0],
    [1,0,0,0,1,0,0],
    [0,0,0,0,0,0,0],  # Space
    
    # E
    [1,1,1,1,1,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,0,0,0],
    [1,0,0,0,0,0,0],
    [1,1,1,1,1,0,0],
]

# Set start date - adjust this to position your pattern correctly
# This should be a Sunday for best alignment
start_date = datetime(2024, 9, 1)  # Adjust this date as needed

# Create commits based on pattern
commit_counter = 0
for week_idx, week in enumerate(pattern):
    for day_idx, should_commit in enumerate(week):
        if should_commit == 1:
            commit_date = start_date + timedelta(weeks=week_idx, days=day_idx)
            date_str = commit_date.strftime('%Y-%m-%d 12:00:00')
            
            # Create 20 commits for this day
            for commit_num in range(20):
                # Modify file
                with open('data.txt', 'a') as f:
                    f.write(f'Commit {commit_counter} - {date_str}\n')
                
                # Stage changes
                subprocess.run(['git', 'add', '.'])
                
                # Commit with custom date
                env = os.environ.copy()
                env['GIT_AUTHOR_DATE'] = date_str
                env['GIT_COMMITTER_DATE'] = date_str
                subprocess.run(
                    ['git', 'commit', '-m', f'Update {commit_counter}'],
                    env=env
                )
                commit_counter += 1
                
                print(f"Created commit {commit_counter} for {date_str}")

print(f"\n✅ Created {commit_counter} total commits!")
print(f"📊 Pattern uses {sum(sum(week) for week in pattern)} days with 20 commits each")
print("\nNow pushing to GitHub...")

# Push to GitHub
subprocess.run(['git', 'push', 'origin', 'main'])

print("\n🎉 Done! Check your GitHub profile contribution graph!")