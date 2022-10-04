# [Subject]
Users and groups

## Key terminology
useradd:  
The UNIX command 'useradd' is used to create new users on a UNIX operating system.   

usermod:  
The UNIX command 'usermod' can be used to modify the properties of a user on a UNIX operating system, such as the password or changing the home directory of the user. 

cat:  
The UNIX command 'cat' is short for 'concatenate' and can be used to create single or multiple files, view the contents of a file, merge files and redirect the output in the command line interface or files.

## Exercise  
* Create a new user in your VM. 
The new user should be part of an admin group.
The new user should have a password.
The new user should be able to use ‘sudo’  

* Locate the files that store users, passwords, and groups. See if you can find your newly created user’s data in there.

### Sources
https://www.freecodecamp.org/news/linux-how-to-add-users-and-create-users-with-useradd/

### Overcome challenges
For this exercise I didn't experience any challenges because we already did this exercise during the assessment week.

### Results  
Here I created a new user in my VM that's part of an admin group, has a password an is able to use 'sudo':  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-add-user.PNG)  

Here I located the file that stores users, passwords and groups. As you can see, my new user "Wim2" is in there as well:  
![alt text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-user-list.PNG)
