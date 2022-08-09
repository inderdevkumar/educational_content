#!/usr/bin/env bash

echo =================
echo starting
echo ================

home_path="/home/inder/my_data/educational_content/jenkins_project/ansible_to_run_jenkins"

echo hostn_name
#read host_name

echo playbook
#read ansible_playbook
echo hostname is : $host_name
echo playbook is: $ansible_playbook.yml
sudo -S mkdir /tmp/for_sed
kumar0102
sudo sed -i -e "s/hostname1/$host_name/g" $home_path/playbook_for_jenkins/$ansible_playbook.yml

#> /tmp/create_file_playbook

#mv /tmp/create_file_playbook $home_path/playbook_for_jenkins/$ansible_playbook.yml

ansible-playbook $home_path/playbook_for_jenkins/$ansible_playbook.yml -i $home_path/inventory_for_jenkins/inventory4.yml

echo =================
echo The end
echo ================
