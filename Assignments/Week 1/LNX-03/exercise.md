# [Subject]
Working with text (CLI)

## Key terminology
Grep:  
The UNIX command 'grep' is used to search for specific keywords or an expression in a specified file.  

Tee:  
The UNIX command 'tee' writes arguments to a specified file while also displaying the specified arguments in the command line interface.

echo:  
The UNIX command 'echo' is used to display text or a string. It can also be used to store text or strings in a bash script.
## Exercise

* Use the echo command and output redirection to write a new sentence into your text file using the command line. The new sentence should contain the word ‘techgrounds’.  
* Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.  
* Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. This time, redirect the output to a new file called ‘techgrounds.txt’.  

### Sources
https://linuxhint.com/find_text_in_files_linux/#:~:text=Find%20text%20in%20files%20using,is%20a%20command%2Dline%20tool

https://www.cyberciti.biz/faq/linux-append-text-to-end-of-file/  

https://unix.stackexchange.com/questions/382946/getting-permission-denied-when-trying-to-append-text-onto-a-file-using-sudo

### Overcome challenges
When trying to use "echo '' >> techgrounds.txt" I got a permission denied error. When searching the internet I found you can redirect echo using the "tee" command after the echo command.

### Results  
Here I used the echo command and redirected the output to a new sentence into my text file:  
![alt-text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-echo-append-grep.PNG)  

Here I filtered the output so that it only shows the sentence containing "techgrounds" and after that I redirected the output to a new file called 'techgrounds2.txt':  
![alt-text](https://github.com/Techgrounds-Cloud-9/cloud-9-WimKimenai/blob/main/00_includes/Linux-echo-append-grep.PNG)
