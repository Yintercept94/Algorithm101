
# 如何设置本地 Git 仓库并连接到 GitHub

## 第一步：创建一个新的 GitHub 账号
1. **注册**：访问 [GitHub](https://github.com) 并创建一个新账号。

## 第二步：在 GitHub 上创建一个新的仓库
1. **登录**：登录到你的新 GitHub 账号。
2. **创建一个仓库**：点击右上角的“+”图标，然后选择“New repository”（新建仓库）。
3. **命名你的仓库**：输入仓库名称（例如 `Algorithm101`），然后点击“Create repository”（创建仓库）。

## 第三步：设置你的本地仓库
1. **导航到你的项目目录**：
   ```bash
   cd /path/to/your/project
   ```
2. **初始化 Git 仓库**：
   ```bash
   git init
   ```
3. **将文件添加到仓库**：
   ```bash
   git add .
   ```
4. **提交文件**：
   ```bash
   git commit -m "Initial commit"
   ```

## 第四步：在 GitHub 上生成个人访问令牌（PAT）
1. **进入 GitHub 设置**：点击右上角的头像，然后进入 **Settings > Developer settings > Personal access tokens**（设置 > 开发者设置 > 个人访问令牌）。
2. **生成一个新令牌**：
   - 点击 **Generate new token**（生成新令牌）。
   - 给你的令牌命名（例如 `MyToken`），并选择你需要的权限范围，通常是 `repo`，用于完全控制私有仓库。
   - 点击 **Generate token**（生成令牌），然后复制令牌。你将无法再次查看它！

## 第五步：使用 PAT 连接本地仓库到远程 GitHub 仓库
1. **添加远程仓库**：
   用你的 GitHub 用户名替换 `USERNAME`，用仓库名称替换 `REPO_NAME`，并用你生成的个人访问令牌替换 `PAT`。
   ```bash
   git remote add origin https://USERNAME:PAT@github.com/USERNAME/REPO_NAME.git
   ```

   例如：
   ```bash
   git remote add origin https://BarryTang22:your_personal_access_token@github.com/BarryTang22/Algorithm101.git
   ```

## 第六步：将代码推送到 GitHub
1. **推送到 GitHub**：
   将你的本地更改推送到远程仓库。
   ```bash
   git push -u origin main
   ```
   如果你的分支名称不是 `main`，请用正确的分支名称替换 `main`。

## 常见问题及解决方案：
- **如果出现非快速前进错误**：在推送之前从远程拉取最新的更改。
   ```bash
   git pull origin main --allow-unrelated-histories
   ```
   解决所有冲突，提交，然后推送。

- **如果提示身份验证**：使用你的 GitHub 用户名和个人访问令牌。

## 第七步：设置 SSH（可选，但推荐）
1. **生成 SSH 密钥**：
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
   ```
2. **将 SSH 密钥添加到 SSH Agent**：
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_rsa
   ```
3. **将 SSH 密钥添加到 GitHub**：
   复制 SSH 公钥 (`~/.ssh/id_rsa.pub`)，然后在 **Settings > SSH and GPG keys**（设置 > SSH 和 GPG 密钥）中添加到你的 GitHub 账号。
4. **将远程地址切换为 SSH**：
   ```bash
   git remote set-url origin git@github.com:USERNAME/REPO_NAME.git
   ```

## 最后推送
设置完成后，你应该能够将代码推送到 GitHub：
```bash
git push origin main
```
