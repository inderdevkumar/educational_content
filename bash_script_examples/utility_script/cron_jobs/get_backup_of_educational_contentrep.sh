#!/usr/bin/env bash

echo Deleting old Rrepo backup folder
rm -rf /home/inder/my_data/backup_educational_content_repo*

echo

echo Creating backup for educational_content repo on $(date)
gcp -rf /home/inder/my_data/educational_content /home/inder/my_data/backup_educational_content_repo_$(date +%F)
echo

echo Backup sucesfully created
