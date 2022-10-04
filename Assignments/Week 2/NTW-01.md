# [Subject]
The OSI (Open Systems Interconnection) model and the TCP/IP model.

## Key terminology
TCP  
HTTP  
FTP  
Packets  
Frames  


## Exercise  

Study the OSI & TCP/IP model and its uses.

### Sources
https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/  

https://www.geeksforgeeks.org/tcp-ip-model/

### Overcome challenges
There were no challenges in this case because there was no exercise.

### Results
I learned about the Open Systems Interconnection (OSI) model, which is a model used to enable diverse communication systems to communicate using standard protocols. It allows for different computer systems to be able to communicate with each other.  

The OSI model consists of 7 layers:  

**7 - Application Layer**  

This layer directly interacts with data from the user. For example, web browsers and email clients rely on the application layer to initiate communications. However, client software applications ae not part of the application layer. The application layer is only responsible for the protocols and data manipulation that the software relies on.  

A few examples of application layer protocols are HTTP and SMTP.

**6 - Presentation Layer**  

The presentation layer is responsible for translation, encryption and compression of data. It's also responsible for compressing data it receives from the application layer before delivering it to layer 5. It does this for optimization purposes, to improve speed and efficiency.

**5 - Session Layer**

The session layer opens and closes connections, and keeps track of connections. It also synchronizes data with checkpoints, so that a session could be resumed from where it stopped - during a connection timeout or a crash for example.

**4 - Transport Layer**

The transport layer is responsible for the end-to-end communication between two devices. It breaks it up into smaller pieces called segments before sending to layer 3. The transport layer on the receiving device then pieces all those segments together again into data the session layer can consume.  

The transport layer is also responsible for flow and error control. It determines the optimal speed of a transmission to make sure that a sender doesn't overload a receiver with data or vice versa. It also checks for errors on the receiving end by making sure the data is complete, it can request a retransmission if there are errors in the data.

**3 - Network Layer**  

The network layer provides data transfer between two different networks. If the two devices are on the same network, the network layer is not necessary. The network layer breaks up segments from the transport layer into smaller segments, called "packets". It then reassembles these packets on the receiving device. It also handles routing, which means it finds the best physical path for the data to reach its destination.

**2 - Datalink Layer**  

The datalink layer provides data transfer between two devices on the same network. It takes packets from the network layer and breaks them into smaller packets called "frames". Just like the network layer, the datalink layer also provides flow and error control.

**1 - Physical Layer**  

The physical layer includes all the physical hardware involved in the data transfer. Such as cables, switches, routers, modems, etc. This is also where the data gets converted into a bit stream (1s and 0s).

**TCP/IP model**  

TCP refers to the Transmission Control Protocol. The TCP/IP model only consists of 4 layers; the application layer, the transport layer, the internet layer and the network access layer.

