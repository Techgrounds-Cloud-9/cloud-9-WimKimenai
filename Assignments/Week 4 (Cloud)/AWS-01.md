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
