
# Connecting Local Git to GitHub Repo with SSH

This guide will walk you through the steps to connect your local Git repository to a GitHub repository using SSH.

## 1. Check for Existing SSH Keys
First, check if you already have an SSH key:

```bash
ls -al ~/.ssh
```

This command lists the files in the `.ssh` directory. Look for files named `id_ed25519` (private key) and `id_ed25519.pub` (public key).

## 2. Generate a New SSH Key (if you don't have one)
If you don’t see `id_ed25519` and `id_ed25519.pub`, generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

During the process, you’ll be prompted to "Enter a file in which to save the key." Press `Enter` to accept the default file location. Next, you’ll be prompted to enter a passphrase. It’s a good idea to use a passphrase for added security, but you can leave it empty if you prefer.

## 3. Add Your SSH Key to the ssh-agent
Start the `ssh-agent` in the background:

```bash
eval "$(ssh-agent -s)"
```

Then add your SSH private key to the ssh-agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

## 4. Add Your SSH Key to Your GitHub Account
Copy the SSH key to your clipboard:

```bash
cat ~/.ssh/id_ed25519.pub
```

Now, go to [GitHub SSH settings](https://github.com/settings/keys):

1. Click on **New SSH key**.
2. Give it a title (e.g., "My Laptop SSH Key").
3. Paste your SSH key into the "Key" field.
4. Click **Add SSH key**.

## 5. Manually Add the GitHub SSH Key
Sometimes, you may need to manually add GitHub's SSH key to your `known_hosts` file:

```bash
ssh-keyscan -t ed25519 github.com >> ~/.ssh/known_hosts
```

This command fetches the SSH key from GitHub's server and appends it to your `known_hosts` file.

## 6. Test the SSH Connection
To verify that everything is working correctly:

```bash
ssh -T git@github.com
```

If everything is set up properly, you should see a message like:

```bash
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

## 7. Connect Your Local Repository to GitHub
If you haven’t already initialized a Git repository, do so:

```bash
git init
```

Then, add the remote repository:

```bash
git remote add origin git@github.com:username/repo-name.git
```

Replace `username` with your GitHub username and `repo-name` with the name of your GitHub repository.

## 8. Push to GitHub
Now you can push your local changes to the GitHub repository:

```bash
git push -u origin main
```

If your default branch is not `main`, replace `main` with your branch name.

You're now connected to your GitHub repository via SSH!
