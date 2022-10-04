# [Subject]
Cron jobs

## Key terminology
crontab:  
The crontab is a file in which you can schedule cronjobs. Cronjobs are scheduled actions that the system can automatically perform on specified time intervals, such as backups or creating log files.  

df:  
The UNIX command 'df' is short for 'disk free' and is used to display the amount of available free disk space on a drive or file system.

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
Here I created a Bash script that writes the current date and time to a file in my home directory.  
![screenshot](/00_includes/Linux/LNX-08/LNX-08-datetime-script.PNG)  

Here I registered the script in my crontab so that it runs every minute.  
![screenshot](/00_includes/Linux/LNX-08/LNX-08-crontab.PNG)  

Here I created a script that writes available disk space to a log file in ‘/var/logs’:  
![screenshot](/00_includes/Linux/LNX-08/LNX-08-diskspacescript.PNG)  

Here I put that script into my crontab so that it runs weekly:  
![screenshot](/00_includes/Linux/LNX-08/LNX-08-crontab2.PNG)  




