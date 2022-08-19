#!/bin/bash
password=`cat sudopasswordfile`

sshpass -p $password ssh -o StrictHostKeyChecking=no virtual_project@192.168.0.36  <<EOF
  echo "$password" | sudo -S hostname
  test1=$(echo '$password' | sudo hostname)
  test=$(echo "foo=bar" | cut -d "=" -f1)
  
  echo TEsting for test1: \$test1
  echo TEsting for test: \$test
  echo "$password" | sudo df -hT
EOF


test=$(echo "foo=bar" | cut -d "=" -f1)

  
  echo TEsting for test: "$test"
