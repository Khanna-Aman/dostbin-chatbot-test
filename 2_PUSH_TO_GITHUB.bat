@echo off
echo ========================================
echo STEP 2: Push to GitHub
echo ========================================
echo.
echo IMPORTANT: Before running this, make sure you:
echo 1. Created a GitHub repository named "dostbin-chatbot"
echo 2. Have your GitHub Personal Access Token ready
echo.
pause
echo.

set /p GITHUB_USERNAME="Enter your GitHub username: "
echo.

git add .
git commit -m "Initial commit: Dostbin AI Chatbot"
git remote add origin https://github.com/%GITHUB_USERNAME%/dostbin-chatbot.git
git branch -M main
git push -u origin main

echo.
echo ========================================
echo Upload Complete!
echo ========================================
echo.
echo Go to: https://github.com/%GITHUB_USERNAME%/dostbin-chatbot
echo to verify all files are uploaded.
echo.
pause

