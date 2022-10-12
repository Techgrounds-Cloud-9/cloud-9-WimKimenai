# [Subject]
Symmetric Encryption

## Key terminology
Ciphers  
Symmetric encryption  
Asymmetric encryption  
Secret key  
AES-256  
Base64

## Exercise

* Find two more historic ciphers besides the Caesar cipher.
* Find two digital ciphers that are being used today.
* Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. 
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the shortcomings of this method.

### Sources
https://www.sciencedirect.com/topics/computer-science/symmetric-encryption  

https://interestingengineering.com/innovation/11-cryptographic-methods-that-marked-history-from-the-caesar-cipher-to-enigma-code-and-beyond  

https://www.beaming.co.uk/knowledge-base/techs-cryptography-use-modern-day-networking/  

https://www.devglan.com/online-tools/aes-encryption-decryption

### Overcome challenges
I had to find out what different symmetric encryption ciphers there were first.

### Results
Another two historic ciphers besides the Caesaer cipher are the Enigma machine and Alberti's disk. 

Two ciphers being used today are two-way encryption formulas such as AES-256 or Triple-Des.  

First I created a symmetrical encrypted message with a secret key:  
![screenshot](/00_includes/Week-3/encrypted-message2.PNG)  

I then encrypted the secret key using Atalla's public key:  
![screenshot](/00_includes/Week-3/encrypted-key-for-atalla.PNG)  

I then sent both my encrypted message and encrypted key to Atalla via Slack:  
![screenshot](/00_includes/Week-3/atalla-encryptedmessages.PNG)  

Atalla then was able to decrypt my secret key using his private key and decrypt my symmetric encrypted message:  
![screenshot](/00_includes/Week-3/atalla-decrypted.PNG)  

