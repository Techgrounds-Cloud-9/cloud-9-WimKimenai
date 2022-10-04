# [Subject]
IP Addressing

## Key terminology
DHCP  
Public and private IP addresses  


## Exercise

* Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.
* Zijn de adressen hetzelfde of niet? Leg uit waarom.
Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.
* Zijn de adressen hetzelfde of niet? Leg uit waarom.
Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?
* Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?

### Sources
https://www.linksys.com/support-article?articleNum=132159

### Overcome challenges
I didn't have any challenges for this exercise, because I already had some experience with networking.

### Results

Public IP address desktop:  
![screenshot](/00_includes/Week-2/public-ip-desktop.PNG)    

Public IP address phone:  
![screenshot](/00_includes/Week-2/public-ip-phone.PNG)

The public IP addresses on my desktop and my mobile phone are the same, because they are connecting to the internet from the same modem.

This is the private IP assigned to my desktop:  
![screenshot](/00_includes/Week-2/private-ip-desktop.PNG)    


This is the private IP assigned to my phone:  
![screenshot](/00_includes/Week-2/private-ip-phone.PNG)    

They are not the same because each device connected to the router/modem has it's own private IP address within the network. My phone is also connected to another router, but in the case it would be connected to the same router as my desktop it would still have a different private IP due to the reason I mentioned in the beginning.

If I would change the private IP of my desktop to the one of my phone, we would get an IP conflict. This means one of the two devices would not be able to communicate with the router.

When you change the IP address from a device to an IP address outside of your network you will receive an error.