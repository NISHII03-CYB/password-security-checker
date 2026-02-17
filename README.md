#PASSWORD SECURITY CHECKING AND HASHING TOOL (PYTHON)



Name : Dehiwattage Kavindu Nishitha Fernando

Role : SOC Analyst (Lab Project)

Date : 16/02/2026

This project demonstrates the development of a basic password security checker using Python. The lab evaluates password strength based on common security criteria and generates a SHA-256 hash of the password. The objective was to understand password complexity requirements, hashing concepts, and how weak credentials increase the risk of brute-force and credential-based attacks.

________________________________________
Project Objective

The objective of this lab was to:

•	Understand password strength evaluation principles

•	Identify characteristics of weak vs strong passwords

•	Implement a simple password validation script

•	Demonstrate password hashing using SHA-256

•	Relate password security to SOC detection use cases
________________________________________

Environment Setup

Component	Description

Programming Language	Python

Operating System	Windows

Hashing Algorithm	SHA-256

Development Tool	Command Prompt / VS Code

________________________________________

Password Strength Criteria

The password checker evaluated passwords based on:

•	Minimum length (≥ 8 characters)

•	Presence of uppercase letters

•	Presence of lowercase letters

•	Presence of numbers

•	Presence of special characters

Each criterion contributed to an overall strength score.


________________________________________

Implementation

Python Script Used
 

________________________________________

Methodology

1.	The user inputs a password.

2.	The script checks for required character types.

3.	A score is calculated based on complexity criteria.

4.	The password is classified as:

     o	Weak

     o	Moderate

     o	Strong

5.	The password is hashed using SHA-256.

6.	The hashed value is displayed.

________________________________________

Example Output

Input:

Password123!

Output:

Password Strength: Strong

SHA-256 Hash: a3f5c8...


________________________________________

Security Concepts Demonstrated

This lab reinforced the following concepts:

•	Password complexity enforcement

•	Importance of minimum length requirements

•	Risk of predictable passwords

•	One-way hashing functions

•	Why systems store hashes instead of plaintext passwords

________________________________________

Security Relevance

Weak passwords increase risk of:

•	Brute-force attacks

•	Credential stuffing

•	Password spraying

•	Account takeover

This lab connects directly to SOC detection use cases such as:

•	Multiple failed login attempts (MITRE ATT&CK T1110 – Brute Force)

•	Credential-based attacks


________________________________________

Limitations

•	Script does not check against breached password databases

•	No salting implemented

•	Does not enforce enterprise-level password policies

________________________________________

Conclusion

This lab successfully demonstrated the implementation of a simple password strength validation tool and introduced password hashing using SHA-256. The project strengthened understanding of authentication 
security, password policy enforcement, and credential attack risks.
The knowledge gained supports both defensive security monitoring and authentication policy evaluation in SOC environments.


