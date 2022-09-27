# [Subject]
Connecting to Linux VM and using the whoami command.

## Key terminology
CLI  
GUI  
VM  
Hypervisor  
SSH  

## Exercise
### Sources
https://askubuntu.com/questions/1111994/login-with-ssh-authorized-key-with-changed-ssh-port  
https://superuser.com/questions/1666505/how-to-set-600-permission-on-a-pem-file-in-w10

### Overcome challenges
First I couldn't figure out why the permissions were too open on the .pem key file. I then looked up what the issue was and found an article on how to change the permissions. This still didn't seem to fix it.

After that I found an article on askubuntu which mention it was also needed to include the port number in the string by using -p. After that I was able to log in to the VM.

### Results
I logged into my VM and used whoami to see what user I am currently using.  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-Connect-VM.PNG)****  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-whoami.PNG)****
