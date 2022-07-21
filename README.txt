#Github
#id0102yadav@gmail.com
or
#inderdevkumar

#Commands used in git

  588  git init
  590  git status
  591  git add .
  592  git status
  593  git commit -m "1st commit"
  594  git config --global user.email  "id0102yadav@gmail.com"
  595  git config --global user.name "inderdevkumar"
  597  git branch
  599  git push origin master

#CReate repo in github gui and run below command
  611  git remote add origin https://github.com/inderdevkumar/educational_content
  612  git remote -v
  613  git branch
  615  git push origin master
  616  ls

#If u get error of ssh
  617  sudo service ssh status
  618  sudo apt-get install openssh-server
  619  sudo service ssh status
  620  git push origin master

#CReate ssh keygen pair for github and local laptop
github@ubuntu:~$ cd ~/.ssh
github@ubuntu:~/.ssh$ ssh-keygen -o -t rsa -C "email@example.com"
cat id_rsa.pub

paste this in github gui

#Give the correct repo name  
625  git remote set-url origin git@github.com:inderdevkumar/educational_content.git
  626  git push origin master
  627  history


#In case u get error while pushing to master
git push -f origin master

#IF failing with remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
CHeck in this doc:
https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github

git rm --cached path_of_large_file
