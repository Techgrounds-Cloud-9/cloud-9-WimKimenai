# [Subject]
Firewalls

## Key terminology
UFW (Uncomplicated firewall)  
Ports

## Exercise

* Installeer een webserver op je VM.
* Bekijk de standaardpagina die met de webserver geïnstalleerd is.
* Stel de firewall zo in dat je webverkeer blokkeert, maar wel ssh-verkeer toelaat.
* Controleer of de firewall zijn werk doet.


### Sources
https://www.cyberciti.biz/faq/ufw-allow-incoming-ssh-connections-from-a-specific-ip-address-subnet-on-ubuntu-debian/  

https://medium.com/@nutanbhogendrasharma/install-apache2-web-server-in-ubuntu-virtual-server-fda675e25db  

https://linuxhint.com/ufw_list_rules/  

https://ubuntu.com/server/docs/security-firewall  

https://www.digitalocean.com/community/questions/which-ufw-service-to-use-for-apache2

### Overcome challenges
I couldn't connect to the default HTTP port and it turns out we had to connect to the correct HTTP port listed in the first email we got with our credentials.

### Results
Here I started my apache2 webserver:  
![screenshot](/00_includes/Week-2/apache2-status.PNG)  

Here is the default apache2 webpage:  
![screenshot](/00_includes/Week-2/apache2-page.PNG)

I then denied the HTTP ports 80 and 58009, which didn't work. I then Googled how to block Apache2 using ufw and found on a website you need to use "ufw deny apache". 
![screenshot](/00_includes/Week-2/ufw-apache2.PNG)  

After running this I couldn't connect to the website anymore:  
![screenshot](/00_includes/Week-2/ufw-blocked.PNG)  
