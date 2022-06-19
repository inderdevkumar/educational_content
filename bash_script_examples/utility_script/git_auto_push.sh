#!/usr/bin/env bash


git branch
git checkout master
git pull
git rebase master
git add .
git status
git commit --amend -m "my new commit `date` "
git push origin master
