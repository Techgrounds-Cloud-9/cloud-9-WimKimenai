# [Subject]
Asymmetric Encryption


## Key terminology
Asymmetric encryption  
Symmetric encryption  
Key pairs  
Public key  
Private key

## Exercise

* Generate a key pair.
* Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. The recipient should be able to read the message, but it should remain a secret to everyone else.
* You are not allowed to use any private messages or other communication channels besides Slack. Analyse the difference between this method and symmetric encryption.

### Sources
https://travistidwell.com/jsencrypt/demo/ 

### Overcome challenges
I had a hard time understanding the assignment, because I believe there is some miscommunication in the exercise. The assignment says "They should be able to decrypt the message using a key you share with them.". But the only way to decrypt your message is with your private key (which you are not allowed to share in this exercise). Even if you would encrypt the private key and send it to someone, in the end they would still have your private key. So, we did things a little bit different and shared our public keys to send messages to each other.

### Results
Here I generated the key pairs:  

![screenshot](/00_includes/Week-3/key-pairs.PNG)  

I then shared my public key in a group DM on Slack with Atalla and Jayashree:  
![screenshot](/00_includes/Week-3/shared-public-keys.PNG)  

I then decrypted their messages and this is what showed up:  

Atalla:  
![screenshot](/00_includes/Week-3/atalla-message.PNG)  

Jayashree:  
![screenshot](/00_includes/Week-3/jayashree-message.PNG)  