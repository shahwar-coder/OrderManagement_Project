'''
>> git switch main      # we have to be on main if we want branch from main
>> git pull             # get latest from GitHub
>> git switch -c feature-branch-name
              # or older git:
              # git checkout -b feature-branch-name
              
# 1. See what changed (optional but useful)
>> git status

# 2. Stage changes
>> git add -A

# 3. Commit changes
>> git commit -m "Describe what you did"

# 4. If first time push:
>> git push -u origin feature-branch-name
Else:
>> git push
'''
