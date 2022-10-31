# [Subject]
Elastic Block Storage (EBS)

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise

### Exercise 1
* Navigate to the EC2 menu.
* Create a t2.micro Amazon Linux 2 machine with all the default settings.
* Create a new EBS volume with the following requirements:
* Volume type: General Purpose SSD (gp3)
* Size: 1 GiB
* Availability Zone: same as your EC2
* Wait for its state to be available.

### Exercise 2
* Attach your new EBS volume to your EC2 instance.
* Connect to your EC2 instance using SSH.
* Mount the EBS volume on your instance.
* Create a text file and write it to the mounted EBS volume.

### Exercise 3
* Create a snapshot of your EBS volume.
* Remove the text file from your original EBS volume.
* Create a new volume using your snapshot.
* Detach your original EBS volume.
* Attach the new volume to your EC2 and mount it.
* Find your text file on the new EBS volume.


### Sources
https://www.youtube.com/watch?v=77qLAl-lRpo  

https://aws.amazon.com/ebs/  

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html  

https://devopscube.com/mount-ebs-volume-ec2-instance/

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

### Results

### Exercise 1

![screenshot](/00_includes/AWS/Week-1/exercise-7-1.PNG)

### Exercise 2
* Attach your new EBS volume to your EC2 instance.  

![screenshot](/00_includes/AWS/Week-1/exercise-7-2.PNG)
* Connect to your EC2 instance using SSH.
![screenshot](/00_includes/AWS/Week-1/exercise-6-2.PNG)
* Mount the EBS volume on your instance.
![screenshot](/00_includes/AWS/Week-1/exercise-7-3.PNG)
![screenshot](/00_includes/AWS/Week-1/exercise-7-4.PNG)
* Create a text file and write it to the mounted EBS volume.
![screenshot](/00_includes/AWS/Week-1/exercise-7-5.PNG)

### Exercise 3
* Create a snapshot of your EBS volume.

![screenshot](/00_includes/AWS/Week-1/exercise-7-6.PNG)
![screenshot](/00_includes/AWS/Week-1/exercise-7-7.PNG)
* Remove the text file from your original EBS volume.

![screenshot](/00_includes/AWS/Week-1/exercise-7-10.PNG)
* Create a new volume using your snapshot.
![screenshot](/00_includes/AWS/Week-1/exercise-7-78.PNG)

* Detach your original EBS volume.

![screenshot](/00_includes/AWS/Week-1/exercise-7-9.PNG)
* Attach the new volume to your EC2 and mount it.
* Find your text file on the new EBS volume.
![screenshot](/00_includes/AWS/Week-1/exercise-7-12.PNG)
