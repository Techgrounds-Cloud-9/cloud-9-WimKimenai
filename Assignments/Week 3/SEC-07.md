# [Subject]
Passwords

## Key terminology
Hashing  
Salted

## Exercise
* Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.  

* Find out how a Rainbow Table can be used to crack hashed passwords.
Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.
03F6D7D1D9AAE7160C05F71CE485AD31
03D086C9B98F90D628F2D1BD84CFA6CA

* Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.
Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted.

### Sources
https://crackstation.net/  

https://www.techtarget.com/searchdatamanagement/definition/hashing  

https://www.darkreading.com/risk/safely-storing-user-passwords-hashing-vs-encrypting

### Overcome challenges
There were no challenges during this exercise.

### Results
Hashing is the process of transforming any given key or a string of characters into another value. This is usually represented by a shorter, fixed-length value or key that represents and makes it easier to find or employ the original string.  

When an application receives a username and password from a user, it performs the hashing operation on the password and compares the resulting hashed value with the password hash stored in the database for the particular user. If the two hashes are an exact match, the user provided a valid username and password.  

Hashing is preferred over symmetric encryption because symmetric encryption is a reversible operation. This means that the encryption key must be accessible to the application and will be used for every password verification. If the encrypted passwords are stolen, the attackers only need to find out what the symmetric key used by the application is. Once the key becomes known, through a breach or through brute force attacks on a weak key - all passwords are instantly decrypted and accessible.  

Here I cracked the first md5 hash using Crackstation:  
![screenshot](/00_includes/Week-3/cracked-md5-1.PNG)  

I wasn't able to crack the 2nd md5 hash using Crackstation. 

Here I created a new Linux user called "hashtest" and found the password hash in the shadow file:  
![screenshot](/00_includes/Week-3/shadow-file.PNG)  

Indeed, when I ran it through the Rainbow Table in Crackstation, it did not recognize the hash:  
![screenshot](/00_includes/Week-3/12345-hash.PNG) 

When I compared the hash with my team mates they were indeed a lot different, only the salted formatting stayed roughly the same.