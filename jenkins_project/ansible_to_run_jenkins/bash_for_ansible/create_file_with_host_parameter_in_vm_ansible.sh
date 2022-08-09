#!/usr/bin/env bash

echo =================
echo starting
echo ================

home_path="/home/inder/my_data/educational_content/jenkins_project/ansible_to_run_jenkins"

echo i am running with user
whoami
echo Running with sudo

sudo -S sed -i -e "s/hostname1/$host_name/g" $home_path/playbook_for_jenkins/$ansible_playbook.yml
kumar0102


ansible-playbook $home_path/playbook_for_jenkins/$ansible_playbook.yml -i $home_path/inventory_for_jenkins/inventory4.yml

echo =================
echo The end
echo ================
