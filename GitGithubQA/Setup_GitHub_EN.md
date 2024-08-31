
# How to Set Up a Local Git Repository and Connect to GitHub

## Step 1: Create a New GitHub Account
1. **Sign Up**: Go to [GitHub](https://github.com) and create a new account.

## Step 2: Create a New Repository on GitHub
1. **Log In**: Log in to your new GitHub account.
2. **Create a Repository**: Click on the “+” icon in the upper-right corner and select “New repository.”
3. **Name Your Repository**: Enter a repository name (e.g., `Algorithm101`) and click “Create repository.”

## Step 3: Set Up Your Local Repository
1. **Navigate to Your Project Directory**:
   ```bash
   cd /path/to/your/project
   ```
2. **Initialize a Git Repository**:
   ```bash
   git init
   ```
3. **Add Files to the Repository**:
   ```bash
   git add .
   ```
4. **Commit the Files**:
   ```bash
   git commit -m "Initial commit"
   ```

## Step 4: Generate a Personal Access Token (PAT) on GitHub
1. **Go to GitHub Settings**: Click on your profile icon in the upper-right corner, then go to **Settings > Developer settings > Personal access tokens**.
2. **Generate a New Token**:
   - Click on **Generate new token**.
   - Give your token a name (e.g., `MyToken`) and select the scopes (permissions) you need, typically `repo` for full control of private repositories.
   - Click **Generate token** and copy the token. You won’t be able to see it again!

## Step 5: Connect Your Local Repository to the Remote GitHub Repository Using the PAT
1. **Add the Remote Repository**:
   Replace `USERNAME` with your GitHub username, `REPO_NAME` with the repository name, and `PAT` with the Personal Access Token you generated.
   ```bash
   git remote add origin https://USERNAME:PAT@github.com/USERNAME/REPO_NAME.git
   ```

   Example:
   ```bash
   git remote add origin https://BarryTang22:your_personal_access_token@github.com/BarryTang22/Algorithm101.git
   ```

## Step 6: Push Your Code to GitHub
1. **Push to GitHub**:
   Push your local changes to the remote repository.
   ```bash
   git push -u origin main
   ```
   If your branch is not named `main`, replace `main` with the correct branch name.

## Common Issues and Resolutions:
- **If you get a non-fast-forward error**: Pull the latest changes from the remote before pushing.
   ```bash
   git pull origin main --allow-unrelated-histories
   ```
   Resolve any conflicts, commit, and then push.

- **If prompted for authentication**: Use your GitHub username and Personal Access Token.

## Step 7: Set Up SSH (Optional, but Recommended)
1. **Generate SSH Key**:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
   ```
2. **Add SSH Key to SSH Agent**:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_rsa
   ```
3. **Add SSH Key to GitHub**:
   Copy the SSH public key (`~/.ssh/id_rsa.pub`) and add it to your GitHub account under **Settings > SSH and GPG keys**.
4. **Switch Remote to SSH**:
   ```bash
   git remote set-url origin git@github.com:USERNAME/REPO_NAME.git
   ```

## Final Push
After setting everything up, you should be able to push your code to GitHub:
```bash
git push origin main
```
