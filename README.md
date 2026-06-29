**Password Leak Checker**

A simple Python command-line application that checks whether a password has been exposed in known data breaches using the Have I Been Pwned (HIBP) Passwords API.

The application uses the k-Anonymity model, meaning your actual password is never sent over the internet. Instead, it sends only the first five characters of the SHA-1 hash of your password and compares the remaining hash locally.

**Features**
* Check one or multiple passwords from the command line
* Uses the Have I Been Pwned Passwords API
* Passwords are never transmitted to the API
* Simple, lightweight, and beginner-friendly Python project

**How It Works**
1. Your password is hashed using SHA-1.
2. Only the first five characters of the hash are sent to the HIBP API.
3. The API returns all matching hash suffixes.
4. The program compares the remaining characters locally.
5. If a match is found, it reports how many times the password has appeared in known breaches.

This approach protects your password while still allowing you to verify whether it has been compromised.

**Requirements**
* Python 3.x
* requests

**Technologies Used**
* Python
* requests
* hashlib
* Have I Been Pwned Passwords API

**Disclaimer**

This project is intended for educational purposes and personal password checking. Always use strong, unique passwords and consider using a password manager.

**Acknowledgements**

This project uses the Have I Been Pwned Passwords API created by Troy Hunt.
