#!/usr/bin/env bash

#Make all .sh files and .py available in our project  working directory store in a list and than push all in repo
#Once reboot is done, script should auto check for change and push the new change to repo

cd /home/inder/my_data/educational_content
git_status="$(git -c color.status=always status)"
echo Before if
if [[ `git status --porcelain` ]]; then
  # Changes
  echo =====================================
  echo
  echo $git_status
  git status
  git add .
  #read -p "Enter commit message: " commit_message
  git commit -m "$`date`"
  BRANCH=$(git describe --contains --all HEAD)
  git pull --rebase origin "$BRANCH"
  git push origin "$BRANCH"

else
  echo $git_status
  echo "No Changes Found"
fi

echo
echo ==============  pushing done =======================
