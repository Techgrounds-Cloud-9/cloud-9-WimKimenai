# [Subject]
Network Detection

## Key terminology
nmap  
packets

## Exercise

* Scan the network of your Linux machine using nmap. What do you find?
* Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser. (Tip: you will find that Zoom is constantly sending packets over the network. You can either turn off Zoom for a minute, or look for the packets sent by the browser between the packets sent by Zoom.)

### Sources
https://nmap.org/book/man.html  

https://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection.html

### Overcome challenges
I had to look up some documentation on how Wireshark packets are displayed before completely understanding what I was looking at.

### Results
I scanned the network of my linux machine using "sudo nmap -sP 3.73.91.175/24" and this is what I found:  

![screenshot](/00_includes/Week-2/nmap-linux.PNG)    

As you can see there are 256 IP addresses and 34 hosts are up.  

I then ran a port scan using "sudo nmap -sT 3.73.91.175/24", which runs a TCP connect port scan. 
![screenshot](/00_includes/Week-2/nmap-ports.PNG)  

Here I used Wireshark and connected to YouTube in my browser. First I made sure to close Zoom and other applications that regularly check for updates (such as Discord, Telegram and Dropbox). Then I found some packets that looked like they were connected to my browser after reconnecting to YouTube a few times in a row and looking for similar packets in the list.
![screenshot](/00_includes/Week-2/wireshark-chrome.PNG)  

Finding out the actual packets associated with my browser would require a lot of reverse engineering, and possibly doing some assembly research in IDA Pro.


