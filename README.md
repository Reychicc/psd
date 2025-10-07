# PSD Attacker
(**LLM Bot of an attacker simulated based on the data entries provided by the Polymorphic Service Deliver (PSD) Moving Target Defense (MTD) Research Project (Pending approval) **)

## Goal
- To create a replica of a hacker who is trying to get into the PSD MTD Test Server
- Replicate similar actions and ideas to get into the server based on the ~0.25M attack attempts
- Able to output varrying attack and attack patterns to test server defense in a controlled internal enviroment

## Application
- Run a server internally and have the LLM attack the PSD MTD to continuously test it for alternative attacks
- Have it work for linux based systems to allow PSD MTD tools
- Attacking based on a few noted attack types
    - SQL Injections
    - Command-Prompt Injections
    - File Inclusion
    - Log4Shell
    - File Traversal/Navigation
    - URL Injection
    - Web Scrapping
    - Cross-Site_Scripting (XXS)

## Tools
### LLM - Llama 3.1
### Server - Polymorphic Service Delivery(PSD) MTD Linux Server
### Data - PSD MTD Research Data (210k attacks)
### Data Format - JSON
