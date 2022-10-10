# [Subject]
Public Key Infrastructure


## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise
* Create a self-signed certificate on your VM.
* Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
* Find the list of trusted certificate roots on your system (bonus points if you also find it in your VM).

### Sources
https://travistidwell.com/jsencrypt/demo/ 

https://manpages.ubuntu.com/manpages/bionic/man1/pki---self.1.html  

https://docs.strongswan.org/docs/5.9/pki/pkiSelf.html

### Overcome challenges
First I had to install PKI on my Linux VM.

### Results
Here I created a self-signed certificate on my VM:  



Here I analyzed the certification path of techgrounds.nl:  
![screenshot](/00_includes/Week-3/techgrounds-certificate.PNG)  
![screenshot](/00_includes/Week-3/techgrounds-certificate-details.PNG)  