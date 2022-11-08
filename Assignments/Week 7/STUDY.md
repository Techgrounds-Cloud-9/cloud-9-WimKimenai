# [Subject]
[Give a short summary of the subject matter.]

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise
### Sources
[List the sources you used for solving the exercise]

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

### Results

### DynamoDB & Lambda

First I created a DynamoDB to store user information. 
![screenshot](/00_includes/AWS/Week-3/DynamoDB-1.PNG)

As you can see, the table is now activated.
![screenshot](/00_includes/AWS/Week-3/DynamoDB-2.PNG)


Then I set up policies for Lambda so it's able to read and write to the DynamoDB "Users"
![screenshot](/00_includes/AWS/Week-3/Lambda-1.PNG)

Then I added a script that's able to pull the information from the DynamoDB.
![screenshot](/00_includes/AWS/Week-3/Lambda-2.PNG)

As you can see, the Lambda script works and pulls the information out under the "Item" section.
![screenshot](/00_includes/AWS/Week-3/Lambda-3.PNG)