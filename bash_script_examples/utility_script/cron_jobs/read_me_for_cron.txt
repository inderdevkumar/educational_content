step1: crontab -l  #To list available cron jobs
step2: crontab -e   #To make cron job
step3: CReate your cron job as below:
        * * * * * inder echo "test" > /home/inder/my_data/educational_content/bash_script_examples/utility_script/cron_jobs/test_cron.txt
	
	or
	
	* * * * * echo "test" > /home/inder/my_data/educational_content/bash_script_examples/utility_script/cron_jobs/test_cron.txt
	
	where syntax is :
        A B C D E USERNAME /root/backup.sh
  Explanation of above cron syntax:

    A: Minutes range: 0 – 59
    B: Hours range: 0 – 23
    C: Days range: 0 – 31
    D: Months range: 0 – 12
    E: Days of the week range: 0 – 7. Starting from Monday, 0 or 7 represents Sunday
    USERNAME: replace this with your username
    /path/to/command – The name of the script or command you want to schedule

To save file in nano editor:
 ctrl+O -> enter -> ctrl+x ->save ->enter

step4: IF you like to make cron job for diff user than use
       sudo crontab -u user_name -l
       sudo crontab -u user_name -e
