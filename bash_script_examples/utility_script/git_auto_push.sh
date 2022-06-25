#!/usr/bin/env bash

#Make all .sh files and .py available in our project  working directory store in a list and than push all in repo
#Once reboot is done, script should auto check for change and push the new change to repo

git status
git add .
read -p "Enter commit message: " commit_message
git commit -m "$commit_message"
BRANCH=$(git describe --contains --all HEAD)
git pull --rebase origin "$BRANCH"
git push origin "$BRANCH"
