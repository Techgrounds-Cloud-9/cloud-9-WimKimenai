# [Subject]
File permissions

## Key terminology
chmod  
chown  
chgrp

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
[Describe the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]
