# [Subject]
Subnetting

## Key terminology
Subnet mask  
Subnet  
Binary  
NAT  
CIDR  


## Exercise
* Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.
1 private subnet dat internet toegang heeft via een NAT gateway. Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).
1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).
* Plaats de architectuur die je hebt gemaakt inclusief een korte uitleg in de Github repository die je met de learning coach hebt gedeeld.



### Sources
https://awstip.com/aws-vpc-creation-f3e456b3f395  

https://www.calculator.net/ip-subnet-calculator.html  

https://www.youtube.com/watch?v=oZGZRtaGyG8  

https://ipcisco.com/lesson/ip-subnetting-and-subnetting-examples/  

https://www.youtube.com/watch?v=ecCuyq-Wprc

### Overcome challenges
I had trouble understanding how the dividing of host ID's actually worked. Then I watched the last video linked in my sources and came to a better understanding and I was able to put the knowledge to use.

### Results
Using subnetting you can divide networks into different sections.

Here is the network architecture I made:  
![screenshot](/00_includes/Week-2/subnetting-v1.PNG)    

As you can see, I used the /26 CIDR to divide the network into 4 subnets. In this case we only needed the first 3, so I took the network ID and host ID ranges from the 4 subnets.