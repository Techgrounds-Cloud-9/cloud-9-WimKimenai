# [Subject]
Public Key Infrastructure


## Key terminology
SSL  
Certificates  
X.509  
PKI

## Exercise
* Create a self-signed certificate on your VM.
* Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
* Find the list of trusted certificate roots on your system (bonus points if you also find it in your VM).

### Sources
https://travistidwell.com/jsencrypt/demo/ 

https://manpages.ubuntu.com/manpages/bionic/man1/pki---self.1.html  

https://docs.strongswan.org/docs/5.9/pki/pkiSelf.html  

https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-20-04  

http://woshub.com/updating-trusted-root-certificates-in-windows-10/  

https://betterstack.com/community/questions/how-to-list-all-available-ca-ssl-certificates-on-ubuntu/

### Overcome challenges
I first had to study the basics of SSL and the SSL certificate before I really understood why you are able to self-sign a certificate.

### Results
First I had to enable SSL on my VM using the command "sudo a2enmod ssl". Then I created the X.509 self signed certificate:  
![screenshot](/00_includes/Week-3/self-signed-ssl.PNG)  

Here I analyzed the certification path of techgrounds.nl:  
![screenshot](/00_includes/Week-3/techgrounds-certificate.PNG)  
![screenshot](/00_includes/Week-3/techgrounds-certificate-details.PNG)  

I found the list of trusted certificate roots on my Windows system using "mmc.exe":  
![screenshot](/00_includes/Week-3/windows-certs.PNG)  

Then I found the certificates on my VM by navigating to "/etc/ssl/certs" and running the 'ls' command in that directory:  
![screenshot](/00_includes/Week-3/ssl-certs-linux.PNG)  
![screenshot](/00_includes/Week-3/ssl-certs-linux2.PNG)  