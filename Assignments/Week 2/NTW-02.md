# [Subject]
Network devices and networking hardware.

## Key terminology
DHCP  
ipconfig command  


## Exercise  
* Benoem en beschrijf de functies van veel voorkomend netwerkapparatuur
* De meeste routers hebben een overzicht van alle verbonden apparaten, vind deze lijst. 
* Welke andere informatie heeft de router over aangesloten apparatuur?
* Waar staat je DHCP server op jouw netwerk? Wat zijn de configuraties hiervan?

### Sources
https://www.techjockey.com/blog/what-are-computer-network-devices#:~:text=The%20purpose%20of%20networking%20devices,network%20resources%20between%20different%20systems.

### Overcome challenges
I had some trouble figuring out where to find the configuration for the DHCP server.

### Results
Network devices  

Repeater: extends the length of the signal and allows it to transmit over the same network. It copies the signal bit by bit and re-generates at its original strength by operating at the physical layer.  

Network hub: multiport repeater that connects multiple wires from different branches. It is used to transfer important data and communicate among diverse network hosts.  

Bridge: a device that joins any two networks or host segments together. Its primary function in a networking architecture is to store and relay frames among the various connected segments. They transfer frames using the MAC or the Media Access Control. It can also prevent data crossing if the MAC addresses are wrong. Besides, it also links different physical LANs together to form a bigger logical LAN.  

Network Switch: A switch is a multi-port device that enhances network efficiency. It provides limited routing information about nodes in the internal network and allows systems to connect. They can read the hardware address of incoming data packets and transmit them to the applicable destination. A multilayer switch is a high-performance device that supports routing protocols like routers.  

Modem: devices that transform digital signals into the form of analog signals that are of various frequencies. Then it sends the analog signals to receivers.  

Gateway: the gateway is a passage that interlinks two networks together. It works as the messenger agent that takes data from one system, interprets it, and transfers it to another system. Gateways are also called protocol converters, and they can operate at various network layers.  

Access points: First, as a regular wired network for wireless devices. Second, like a router for transferring data between different access points. The access point has various ports to expand the network’s size, firewall capabilities, and DHCP service. As a result, there are access points that act as a switch, DHCP server, router, and firewall.  

Here I found my router's client list:  
![screenshot](/00_includes/Week-2/Clientlist.PNG)  

Other information the router has on it's clients are; what kind of permissions they have and what ports should be forwarded. There is also a firewall built in to control in and outgoing connections. It can also log data connection and see when and how much data the device is using.  

This is the DHCP server on my network:  
![screenshot](/00_includes/Week-2/DHCPserver.PNG)  
