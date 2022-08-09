#!/usr/bin/env bash

echo =================
echo starting
echo ================

home_path="/home/inder/my_data/educational_content/jenkins_project/ansible_to_run_jenkins"

echo i am running with user
whoami
echo Running with sudo

#sudo sed -i -e "s/hostname1/$host_name/g" $home_path/playbook_for_jenkins/$ansible_playbook.yml
sudo sed -i -e "s/hostname1/inder1/g" $home_path/playbook_for_jenkins/$ansible_playbook.yml
echo create files
sudo touch $home_path/playbook_for_jenkins/${host_name}_with_Sudo.txt
touch $home_path/playbook_for_jenkins/${host_name}_without_sudo.txt
#kumar0102


ansible-playbook $home_path/playbook_for_jenkins/$ansible_playbook.yml -i $home_path/inventory_for_jenkins/inventory4.yml

echo =================
echo The end
echo ================
