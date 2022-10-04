# [Subject]
Network protocols

## Key terminology
TCP  
UDP  
HTTPS  
SSH

## Exercise

* Identify several other protocols and their associated OSI layer. Name at least one for each layer.
* Figure out who determines what protocols we use and what is needed to introduce your own protocol.
* Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.

### Sources
https://en.wikipedia.org/wiki/List_of_network_protocols_(OSI_model)  

https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet/  

https://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection.html#:~:text=To%20only%20display%20packets%20containing,in%20the%20display%20filter%20toolbar.  

https://stackoverflow.com/questions/18249847/how-to-build-a-protocol-on-top-of-tcp  

https://www.geeksforgeeks.org/elements-of-network-protocol/

### Overcome challenges
I didn't experience any challenges with this assignment. Before I started I was carefully reading up on the material.

### Results
There are way too many protocols to go into, so I will list some of the most commonly used ones in my exercise. 

Physical layer:  
Ethernet and infrared  

Datalink layer:  
Ethernet and VLAN  

Network layer:  
IP, NAT and ICMP.   

Transport layer:  
DCCP, NetBIOS, SCTP.   

Session layer:  
NetBIOS, SMPP, H.245  

Presentation layer:  
TLS and SSL.  

Application layer:  
DHCP, HTTP/HTTPS, SMTP, FTP, SSH, IMAP, DNS.  

The World Wide Web Consortium (W3C) and the Internet Engineering Task Force determines what protocols we use. Many of the internet standards we know, like HTML, XHTML, CSS, XML, and many more, have been proposed, discussed, defined, and formalized by the W3C. The World Wide Web Consortium was founded in October 1994 at MIT in collaboration with CERN by the "father" of the web, Tim Berners Lee. W3C's mission is to take the web to its full potential, creating protocols and standards that support technologies with specifications, guidelines, applications, and support programs. 

To introduce your own protocol, you can write a specification that defines the data you send through the TCP socket. The elements needed for a network communication protocol are: message encoding, message formatting and encapsulation, message size, message timing, and message delivery options.


Here I searched for the TCP protocol in Wireshark:  
![screenshot](/00_includes/Week-2/TCP-wireshark.PNG)