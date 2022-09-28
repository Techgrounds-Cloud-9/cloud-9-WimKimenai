# [Subject]
Processes

## Key terminology
kill  
systemctl  


## Exercise  
* Start the telnet daemon.
* Find out the PID of the telnet daemon.
* Find out how much memory telnetd is using.
* Stop or kill the telnetd process.

### Sources
https://www.linuxquestions.org/questions/linux-server-73/start-and-stop-telnet-service-on-linux-833451/  

https://www.cyberciti.biz/faq/how-do-i-turn-on-telnet-service-on-for-a-linuxfreebsd-system/  

https://linuxhint.com/linux-telnet-command/  

https://forum.lowyat.net/topic/346775

### Overcome challenges
I first had to install telnetd to turn it on.

### Results
Here I started the telnet daemon:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-06/LNX-06-turn-on-telnet.PNG)  

The PID of the telnet daemon is 6913 and it's using 844.0K of memory.  

Here I killed the telnetd process (the PID is now 7322 after accidentally restarting it):   
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-06/LNX-06-kill-telnet.PNG)