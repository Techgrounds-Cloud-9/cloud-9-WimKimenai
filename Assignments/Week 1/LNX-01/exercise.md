# [Subject]
Connecting to Linux VM and using the whoami command.

## Key terminology
CLI:  
The command line interface is a text based user interface, which can be used to manage and navigate a system without using a graphical user interface.  

GUI:  
The graphical user interface is the opposite of a command line interface, which enables you to manage and navigate around the system using your mouse and a visual representation of the system. This makes it easier for people without command line knowledge to use a computer.  

VM:  
A virtual machine runs an operating system inside of your operating system. This can be achieved using a hypervisor. A hypervisor shares resources, memory and processing with the main host machine.    


SSH:  
The Secure Shell Protocol is a protocol used to connect to network services. It replaced the Telnet protocol and is a much safer alternative.   

## Exercise
* Make an SSH-connection to your machine. SSH requires the key file to have specific permissions, so you might need to change those.
* When the connection is successful, type whoami in the terminal. This command should show your username.

### Sources
https://askubuntu.com/questions/1111994/login-with-ssh-authorized-key-with-changed-ssh-port  
https://superuser.com/questions/1666505/how-to-set-600-permission-on-a-pem-file-in-w10

### Overcome challenges
First I couldn't figure out why the permissions were too open on the .pem key file. I then looked up what the issue was and found an article on how to change the permissions. This still didn't seem to fix it.

After that I found an article on askubuntu which mention it was also needed to include the port number in the string by using -p. After that I was able to log in to the VM.

### Results
I logged into my VM and used whoami to see what user I am currently using.  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-Connect-VM.PNG)  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-whoami.PNG)
