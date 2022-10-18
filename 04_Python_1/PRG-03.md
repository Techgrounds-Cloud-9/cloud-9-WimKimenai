# [Subject]
Data types and comments

## Key terminology
[Write a list of key terminology with a short description. To prevent duplication you can reference to previous excercises.]

## Exercise 

**Exercise 1:**  

* Create a new script.
* Copy the code below into your script.
a = 'int'
b = 7
c = False
d = "18.5"
* Determine the data types of all four variables (a, b, c, d) using a built in function.
* Make a new variable x and give it the value b + d.
* Print the value of x. This will raise an error. Fix it so that print(x) prints a float.
* Write a comment above every line of code that tells the reader what is going on in your script.

**Exercise 2:**  

* Create a new script.
* Use the input() function to get input from the user. 
* Store that input in a variable.
* Find out what data type the output of input() is. 
* See if it is different for different kinds of input (numbers, words, etc.).



### Sources
[List the sources you used for solving the exercise]

### Overcome challenges
[Give a short description of the challeges you encountered, and how you solved them.]

### Results
**Exercise 1:**  

![screenshot](/00_includes/Python-1/data-types/exercise-1-2.PNG)  

I did it this way because when you have large sets of data, it's easier to scale. You could do "print(type(a))", "print(type(b))" and so forth but then you have to keep adding more lines of "print" - while this way you can just add the variables to the data_list and it automatically checks for the data types.  


**Exercise 2:**  

![screenshot](/00_includes/Python-1/data-types/exercise-2.PNG)  

It always returns a string, because the input function always returns a string. You can convert it to another data type after it's stored in the variable if you wanted to.  