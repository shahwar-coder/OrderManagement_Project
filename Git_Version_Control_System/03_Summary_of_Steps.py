'''
GIT + GITHUB WORKFLOW (Concise Summary)

1️⃣ Setup Identity (One-time Only)
git config --global user.name "YourName"
git config --global user.email "you@example.com"

2️⃣ Initialize Git in Project Folder
git init

3️⃣ Add Files to Staging Area
git add -A   # Stage all changes

4️⃣ Create a Commit (Save Point)
git commit -m "Meaningful commit message"

5️⃣ Set Default Branch Name
git branch -M main

6️⃣ Connect Local Repo to GitHub
git remote add origin <GitHub_Repo_URL>

7️⃣ Upload Code to GitHub (First Time)
git push -u origin main

👉 After first push, only use:
git push

SUMMARY:
Workspace → git add → Staging Area → git commit → Local Repo → git push → Remote Repo (GitHub)
'''


'''
==========================================================
            GIT + GITHUB WORKFLOW (with Commands)
==========================================================

   (Your Project Files)
            │
            ▼
+---------------------------------------+
|   Workspace (Untracked changes)       |
+---------------------------------------+
               │  git add -A
               ▼
+---------------------------------------+
|   Staging Area (Tracked changes)      |
+---------------------------------------+
               │  git commit -m "msg"
               ▼
+---------------------------------------+
|   Local Repository (Commits stored)   |
+---------------------------------------+
               │  git push / first time: git push -u origin main
               ▼
+---------------------------------------+
|     Remote Repository (GitHub)        |
+---------------------------------------+


SETUP COMMANDS (done during the above flow):
-------------------------------------------
git init                          → Start Git in project folder  
git branch -M main                → Set branch name to main  
git remote add origin <URL>       → Connect to GitHub Repo  


==========================================================
FULL COMMAND ORDER (in one place)
----------------------------------------------------------
1️⃣ git init
2️⃣ git add -A
3️⃣ git commit -m "message"
4️⃣ git branch -M main
5️⃣ git remote add origin <URL>
6️⃣ git push -u origin main
➡️ After that: git push
==========================================================
'''
