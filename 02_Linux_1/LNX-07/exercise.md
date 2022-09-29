# [Subject]
Bash scripting (Bourne Again Shell)

## Key terminology
Shebang:  
A 'shebang' is expressed as '#!' and is used to specify the programming language of a script in UNIX.  

Variable:  
A variable is a value that is not fixed. It can change based on conditions, information given to a program, or even over time.  

Argument:  
An argument is a parameter that we can use to tell a script what to do. It often requires user input and performs actions based on that input.

## Exercise 1
* Create a directory called ‘scripts’. Place all the scripts you make in this directory.
* Add the scripts directory to the PATH variable.
* Create a script that appends a line of text to a text file whenever it is executed.
* Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

### Sources  
Exercise 1:  
https://linuxize.com/post/how-to-add-directory-to-path-in-linux/

https://www.youtube.com/watch?v=SPwyp2NG-bE 

https://youtu.be/l9YxTXDiiFY

Exercise 2 & 3:  
https://linuxhint.com/generate-random-number-bash/#:~:text=The%20random%20number%20or%20a,RANDOM%20with%20a%20specific%20value.

### Overcome challenges
Exercise 1:  

I couldn't get httpd to install, after I learned you need to specify a specific installation I went with apache2 and then everything worked.

Exercise 2:  

I had to study bash syntax a bit better, when I first tried to execute the scripts they didn't work as intended.

### Results
**Exercise 1**  

Here I created the directory 'scripts':  
![screenshot](/00_includes/Linux/LNX-07/LNX-07-mkdir-scripts.PNG)


Here I added 'scripts' to the PATH variable:  
![screenshot](/00_includes/Linux/LNX-07/LNX-07-add-path-variable.PNG)

Here I made the script that appends a line of text to a text file, using an argument to specify what text needs to be appended:  
![screenshot](/00_includes/Linux/LNX-07/LNX-07-appendtext-script.PNG)

Here I created the httpd script:  
![screenshot](/00_includes/Linux/LNX-07/LNX-07-httpd-script.PNG)

**Exercise 2**  
Here I created a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file:  
![screenshot](/00_includes/Linux/LNX-07/LNX-07-randnumber-script.PNG)

**Exercise 3**  
Here I created a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead:  
![screenshot](/00_includes/Linux/LNX-07/LNX-07-exercise-3.PNG)

