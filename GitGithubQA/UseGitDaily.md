
# Daily Git Workflow

This outlines the recommended daily Git workflow to ensure efficient and organized work management.

## 1. Creating a Daily Branch

At the start of each day, create a new branch named with the current date. This branch will serve as your workspace for the day.

### Command to Create a Branch

```bash
git checkout -b $(date +%Y-%m-%d)
```

- This command creates a new branch with the current date in `YYYY-MM-DD` format (e.g., `2024-09-03`) and switches to it.

## 2. Working on the Daily Branch

Throughout the day, commit your changes to the daily branch. This keeps your work isolated and allows for easy review and integration at the end of the day.

## 3. Reviewing and Merging Daily Work

At the end of the day, review your changes and merge your daily branch into the main branch or another feature branch.

### Command to Pull Latest Changes and Merge

```bash
git pull origin main --rebase
git checkout main
git merge $(date +%Y-%m-%d)
```

- Ensure your branch is up to date with the latest changes from the main branch before merging.

## 4. Renaming and Keeping the Branch

If your daily work leads to a new feature or an important isolated version, you can rename the branch to a more descriptive name.

### Command to Rename the Branch

```bash
git branch -m $(date +%Y-%m-%d) new-feature-name
```

- Replace `new-feature-name` with a meaningful name for the branch.

## 5. Deleting Daily Branches

If the daily branch is no longer needed after merging, you can delete it.

### Command to Delete the Branch

```bash
git branch -d $(date +%Y-%m-%d)
```

- This will delete the branch from your local repository if it has already been merged.

## 6. Automating the Workflow

You can create scripts to automate the daily start and end processes.

### Example Start Script

```bash
#!/bin/bash
# Create a new branch with today's date
git checkout -b $(date +%Y-%m-%d)
```

### Example End Script

```bash
#!/bin/bash
# Pull latest changes, rebase and merge
git pull origin main --rebase
git checkout main
git merge $(date +%Y-%m-%d)

# Optional: Rename the branch if needed
# git branch -m $(date +%Y-%m-%d) new-feature-name

# Optional: Delete the branch if merged
# git branch -d $(date +%Y-%m-%d)
```
