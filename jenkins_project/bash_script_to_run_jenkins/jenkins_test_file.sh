#!/usr/bin/env bash
echo
echo =================================
echo My first Jenkin Job
echo
echo =================================
echo Todays date time
date
echo
echo =================================
echo Reading Hostname
hostname
echo
echo =================================
echo Check Hard disk Space left
df -h | grep "Files*\|/dev/sda2"
echo
echo =================================
echo check FRom when the system is on
uptime
echo
echo =================================
echo IP of system and User name
ifconfig | grep "inet 19" | awk  '{print $2}'

echo Username is: `whoami`
echo
echo =================================


