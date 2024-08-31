
# Merging Changes from a Forked Repository

If someone forked your Git repository and made modifications, follow these steps to retrieve and merge those changes into your repository.

## 1. Add the Forked Repository as a Remote

First, add the forked repository as a new remote. Replace `username` with the GitHub username of the person who forked your repository, and `repository-name` with the name of the repository.

\`\`\`bash
git remote add forked-repo https://github.com/Yintercept94/Algorithm101.git
\`\`\`

This command adds the forked repository as a remote named `forked-repo`. You can use any name you prefer instead of `forked-repo`.

## 2. Fetch the Changes

Fetch the changes from the forked repository using:

\`\`\`bash
git fetch forked-repo
\`\`\`

This retrieves the branches and commits from the `forked-repo` remote.

## 3. Review the Changes

Review the changes made in the forked repository. For example, to see the differences between the `main` branch of your repository and the `main` branch of the forked repository, run:

\`\`\`bash
git diff main forked-repo/main
\`\`\`

This command shows the differences between the two branches.

## 4. Merge the Changes

If you’re satisfied with the changes and want to merge them into your repository, use:

\`\`\`bash
git merge forked-repo/main
\`\`\`

This merges the `main` branch from the forked repository into your current branch (typically `main`).

## 5. Push the Merged Changes (Optional)

If you want to push the merged changes back to your original repository, use:

\`\`\`bash
git push origin main
\`\`\`

This pushes the merged changes to the `main` branch of your original remote (`origin`).

## 6. Remove the Remote (Optional)

If you no longer need the `forked-repo` remote, you can remove it with:

\`\`\`bash
git remote remove forked-repo
\`\`\`

This step is optional but helps keep your remotes clean.

## Summary of Commands

1. Add the forked repository as a remote:
   \`\`\`bash
   git remote add forked-repo https://github.com/Yintercept94/Algorithm101.git
   \`\`\`

2. Fetch the changes:
   \`\`\`bash
   git fetch forked-repo
   \`\`\`

3. Review the changes:
   \`\`\`bash
   git diff main forked-repo/main
   \`\`\`

4. Merge the changes:
   \`\`\`bash
   git merge forked-repo/main
   \`\`\`

5. Push the merged changes (if needed):
   \`\`\`bash
   git push origin main
   \`\`\`

6. Remove the forked remote (optional):
   \`\`\`bash
   git remote remove forked-repo
   \`\`\`

Following these steps will allow you to successfully incorporate modifications from a forked repository into your own project.
