# [Subject]
Detection, response and analysis

## Key terminology
IDS (Intrusion detection systems)  
IPS (Intrusion prevention systems)  
RPO (Recovery Point Objective) - how much data is lost on incident  
RTO (Recovery Time Objective) - how long it takes to be back online  
Cost

## Exercise

* A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
* An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?


### Sources
https://www.vmware.com/topics/glossary/content/intrusion-prevention-system.html  

https://www.barracuda.com/glossary/intrusion-detection-system  

https://www.unitrends.com/blog/rpo-rto  

https://www.geeksforgeeks.org/aws-disaster-recovery-strategies/

### Overcome challenges
I had to formulate the RTO and RPO in a graph before completely understanding the concepts.

### Results
Because there are not a lot of details provided, I will go with the general description of what I think the results should be.  

The RPO of the database is the amount of data that's lost between the current time and the time of the most recent available backup. We can't know exactly how much data is lost, that would depend on the amount of data they add during that time and how large that data is. The maximum amount of lost data would be 24 hours of created data.

The RTO is 8 minutes, because it takes 8 minutes to power on the backup and pull the newest version from GitHub. This is the only information we have, and it might take more time depending on other factors that are not provided.
