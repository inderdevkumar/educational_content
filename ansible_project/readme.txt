# Executing custom inventory file
ansible webserver1 -m ping -i inventory.txt

ansible webserver* -m ping -i inventory2.txt


ansible inder* -m ping -i inventory_test_files/inventory1.txt  --ask-pass 


#For playbook
ansible-playbook ansible_playbook/playbook1.yml -i inventory_test_files/inventory2.txt
