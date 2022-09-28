# [Subject]
Cron jobs

## Key terminology
crontab  
df

## Exercise

* Create a Bash script that writes the current date and time to a file in your home directory.
* Register the script in your crontab so that it runs every minute.
* Create a script that writes available disk space to a log file in ‘/var/logs’. Use a cron job so that it runs weekly.

### Sources
https://stackoverflow.com/questions/8395358/creating-a-file-in-a-specific-directory-using-bash

https://www.howtogeek.com/409611/how-to-view-free-disk-space-and-disk-usage-from-the-linux-terminal/#:~:text=Bash%20contains%20two%20useful%20commands,terminal%20window%20to%20get%20started

### Overcome challenges
First I couldn't get the cronjobs to work. After researching I found out it was because I had to make a crontab using sudo, so the root executes the scripts instead of the user. This way it worked.  

### Results
[Describe the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]