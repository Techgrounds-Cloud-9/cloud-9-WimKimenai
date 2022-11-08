# [Subject]
Global Infrastructure

## Key terminology
* Regions
* Availability Zones
* Edge Locations


## Exercise
Study:  
* What is an AWS Availability Zone?
* What is a Region?
* What is an Edge Location?
* Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).


### Sources
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html  

https://www.youtube.com/watch?v=0hlZvybbaGk

### Overcome challenges
N/A
### Results  

AWS Availability Zones are multiple isolated locations within a Region. A Region in AWS is a geographic area.

Edge Locations are part of the CloudFront network. Which is a CDN (Content Delivery Network) used to provide users with for example video files and other important data that require the least amount of latency. To deliver content to end users with lower latency, Amazon CloudFront uses a global network of 410+ Points of Presence (400+ Edge locations and 13 regional mid-tier caches) in 90+ cities across 48 countries.

You would choose the region closest to you, or the region closest to your target audience/client. You want to have the least amount of latency between you and your AWS instance.  

* Compliance:    

If your workload contains data that is bound by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.
* Latency:   

A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.
* Cost:  

AWS services are priced differently from one Region to another. Some Regions have lower cost than others, which can result in a cost reduction for the same deployment.
* Services and features:  

Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.
