# [Subject]
Identity and Access Management

## Key terminology
Authentication  
Authorization  
Permissions  
MFA (multi-factor authentication)  
Knowledge Factor  
Possession Factor  
Inherence Factor  
Principle of least privilege  
Privilege creep  

I will go further into these key terms under "Results".
  
## Exercise
**Study:**  
* The difference between authentication and authorization.
* The three factors of authentication and how MFA improves security.
* What the principle of least privilege is and how it improves security.


### Sources
https://www.onelogin.com/learn/authentication-vs-authorization#:~:text=Authentication%20vs.-,Authorization,authorization%20determines%20their%20access%20rights  

https://www.okta.com/identity-101/authentication-vs-authorization/  

https://rublon.com/blog/what-are-the-three-authentication-factors  

https://www.cyberark.com/what-is/least-privilege/

### Overcome challenges
I had no challenges during this assignment, because we only had to study the concepts.

### Results
* The difference between authentication and authorization:  

Authentication verifies the identity of a user or service. Authorization determines their access rights. They are both equally important in securing applications and data.  

Usernames and passwords are the most common examples of authentication. Authentication is the process of granting a user permissions.

* The three factors of authentication and how MFA improves security:  

The three factors of authentication are; the Knowledge Factor, Possession Factor and Inherence Factor.  

Knowledge Factor - something you know. For example, a password or PIN code. It generally refers to something you already know before the authentication takes place. Another good example of the knowledge factor is a security question (in case you lose or forget your passsword).  

Possesion Factor - requires you to possess (own) a hardware item. For example a SIM card, Smart Card, hardware OTP token or a FIDO2 security key. The possession factor checks if a user has a piece of hardware, which makes it a lot harder to crack than the knowledge factor - since an attacker would have to possess the item for authentication.  

Inherence Factor - often said to be the strongest authentication factor. It requires the user to confirm their identity, often using biometrics such as fingerprint scans, retina pattern scans or facial recognition.  

MFA (multi-factor authentication) greatly improves security by combining multiple factors. These days, 2FA (two-factor authentication) is commonly implemented in popular applications and digital government platforms. To further improve security, 3FA (three-factor authentication) can be used, which combines all three factors mentioned above.  

* What the principle of least privilege is and how it improves security:  

PoLP (principle of least privilege) refers to the information security concept where a user is given the minimum levels of access to meet their needs. Such as, only having the permissions neccessary to perform their job or function and nothing more than that. It's a cybersecurity best practice and a fundamental step in protecting important or confidential data.  

An example that I can think of to easily understand this concept is a bank. A person working behind the counter for customer service does not require access to the vault where all the money and gold is in, therefore they do not have access or permission to enter the area where the vault is in. This is an example of PoLP being used in physical form, but this also extends to digital applications, systems and connected devices.  

It improves security by making sure only authorized users are able to access what they need, and therefore reducing "privilege creep", which is the term used for permissions that are not being re-granted after a user doesn't need them anymore. When privilege creep occurs, users have access to higher levels of permissions than they need.

