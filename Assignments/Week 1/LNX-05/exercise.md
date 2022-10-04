# [Subject]
File permissions

## Key terminology
chmod:  
The UNIX command 'chmod' is used to change the access mode of a file and assign permissions. 

chown:  
The UNIX command 'chown' is short for 'change owner' and used to take ownership of files and directories of a UNIX system. It can also be used to change group ownerships.  

chgrp:  
The UNIX command 'chgrp' is short for 'change group' and can be used to change the group ownership of a file or directory to another group.

## Exercise  
* Create a text file.
* Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?
* Make the file executable by adding the execute permission (x).
* Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?
* Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.
* Change the group ownership of the file to a different group.


### Sources
https://phoenixnap.com/kb/linux-file-permissions  

https://www.washington.edu/doit/technology-tips-chmod-overview#:~:text=To%20remove%20world%20read%20permission,chmod%20go%3D%20%5Bfilename%5D  

https://docs.oracle.com/cd/E19683-01/816-4883/6mb2joat2/index.html  

https://docs.oracle.com/cd/E19683-01/816-4883/6mb2joat3/index.html

### Overcome challenges
I first had to create a new group to change the group ownership of the file. I also didn't understand the syntax for permissions at first, so I had to study some documentation to get the basic understanding of it.

### Results
Here I created a text file:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-05/LNX-05-create-text-file.PNG)  

Here i listed the file's permissions:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-05/LNX-05-permission-list.PNG)  

Here I added the execute permission to the file:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-05/LNX-05-add-execute-perm.PNG)  

Here I removed the read and write permissions:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-05/LNX-05-remove-rw-perms.PNG)  

As you can see, now I can't read it anymore:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-05/LNX-05-perm-denied.PNG)  

Here I changed the ownership of the file, and I can't read it anymore:    
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-05/LNX-05-change-owner.PNG)  

Here I changed the group ownership to a different group:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux/LNX-05/LNX-05-chgrp.PNG)